#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""A library for reading and converting SVG.

This is a converter from SVG to RLG (ReportLab Graphics) drawings.
It converts mainly basic shapes, paths and simple text. The intended
usage is either as module within other projects:

    from svglib.svglib import svg2rlg
    drawing = svg2rlg("foo.svg")

or from the command-line where it is usable as an SVG to PDF converting
tool named sv2pdf (which should also handle SVG files compressed with
gzip and extension .svgz).
"""

import copy
import gzip
import itertools
import logging
import os
import re
import base64
import tempfile
import shlex
import shutil
import subprocess
import sys
from collections import defaultdict, namedtuple

from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth
from reportlab.pdfbase.ttfonts import TTFError, TTFont
from reportlab.pdfgen.canvas import FILL_EVEN_ODD, FILL_NON_ZERO
from reportlab.pdfgen.pdfimages import PDFImage
from reportlab.graphics.shapes import (
    _CLOSEPATH, Circle, Drawing, Ellipse, Group, Image, Line, Path, PolyLine,
    Polygon, Rect, SolidShape, String,
)
from reportlab.lib import colors
from reportlab.lib.units import pica, toLength
from reportlab.lib.utils import haveImages
from lxml import etree
import cssselect2
import tinycss2

from .utils import (
    bezier_arc_from_end_points, convert_quadratic_to_cubic_path,
    normalise_svg_path,
)

__version__ = '0.9.2'
__license__ = 'LGPL 3'
__author__ = 'Dinu Gherman'
__date__ = '2019-07-12'

XML_NS = 'http://www.w3.org/XML/1998/namespace'

# A sentinel to identify a situation where a node reference a fragment not yet defined.
DELAYED = object()

STANDARD_FONT_NAMES = (
    'Times-Roman', 'Times-Italic', 'Times-Bold', 'Times-BoldItalic',
    'Helvetica', 'Helvetica-Oblique', 'Helvetica-Bold', 'Helvetica-BoldOblique',
    'Courier', 'Courier-Oblique', 'Courier-Bold', 'Courier-BoldOblique',
    'Symbol', 'ZapfDingbats',
)
DEFAULT_FONT_NAME = "Helvetica"
_registered_fonts = {}

logger = logging.getLogger(__name__)

Box = namedtuple('Box', ['x', 'y', 'width', 'height'])

split_whitespace = re.compile(r'[^ \t\r\n\f]+').findall


def find_font(font_name):
    """Return the font and a Boolean indicating if the match is exact."""
    if font_name in STANDARD_FONT_NAMES:
        return font_name, True
    elif font_name in _registered_fonts:
        return font_name, _registered_fonts[font_name]

    NOT_FOUND = (None, False)
    try:
        # Try first to register the font if it exists as ttf,
        # based on ReportLab font search.
        registerFont(TTFont(font_name, '%s.ttf' % font_name))
        _registered_fonts[font_name] = True
        return font_name, True
    except TTFError:
        # Try searching with Fontconfig
        try:
            pipe = subprocess.Popen(
                ['fc-match', '-s', '--format=%{file}\\n', font_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            output = pipe.communicate()[0].decode(sys.getfilesystemencoding())
            font_path = output.split('\n')[0]
        except OSError:
            return NOT_FOUND
        try:
            registerFont(TTFont(font_name, font_path))
        except TTFError:
            return NOT_FOUND
        # Fontconfig may return a default font totally unrelated with font_name
        exact = font_name.lower() in os.path.basename(font_path).lower()
        _registered_fonts[font_name] = exact
        return font_name, exact


class NoStrokePath(Path):
    """
    This path object never gets a stroke width whatever the properties it's
    getting assigned.
    """
    def __init__(self, *args, **kwargs):
        copy_from = kwargs.pop('copy_from', None)
        Path.__init__(self, *args, **kwargs)  # we're old-style class on PY2
        if copy_from:
            self.__dict__.update(copy.deepcopy(copy_from.__dict__))

    def getProperties(self, *args, **kwargs):
        # __getattribute__ wouldn't suit, as RL is directly accessing self.__dict__
        props = Path.getProperties(self, *args, **kwargs)
        if 'strokeWidth' in props:
            props['strokeWidth'] = 0
        if 'strokeColor' in props:
            props['strokeColor'] = None
        return props


class ClippingPath(Path):
    def __init__(self, *args, **kwargs):
        copy_from = kwargs.pop('copy_from', None)
        Path.__init__(self, *args, **kwargs)
        if copy_from:
            self.__dict__.update(copy.deepcopy(copy_from.__dict__))
        self.isClipPath = 1

    def getProperties(self, *args, **kwargs):
        props = Path.getProperties(self, *args, **kwargs)
        if 'fillColor' in props:
            props['fillColor'] = None
        return props


class CSSMatcher(cssselect2.Matcher):
    def __init__(self, style_content):
        super(CSSMatcher, self).__init__()
        self.rules = tinycss2.parse_stylesheet(
            style_content, skip_comments=True, skip_whitespace=True
        )
        for rule in self.rules:
            if not rule.prelude:
                continue
            selectors = cssselect2.compile_selector_list(rule.prelude)
            selector_string = tinycss2.serialize(rule.prelude)
            content_dict = dict(
                (attr.split(':')[0].strip(), attr.split(':')[1].strip())
                for attr in tinycss2.serialize(rule.content).split(';')
                if ':' in attr
            )
            payload = (selector_string, content_dict)
            for selector in selectors:
                self.add_selector(selector, payload)


# Attribute converters (from SVG to RLG)

class AttributeConverter(object):
    "An abstract class to locate and convert attributes in a DOM instance."

    def __init__(self):
        self.css_rules = None
        self.main_box = None

    def set_box(self, main_box):
        self.main_box = main_box

    def parseMultiAttributes(self, line):
        """Try parsing compound attribute string.

        Return a dictionary with single attributes in 'line'.
        """

        attrs = line.split(';')
        attrs = [a.strip() for a in attrs]
        attrs = filter(lambda a:len(a)>0, attrs)

        new_attrs = {}
        for a in attrs:
            k, v = a.split(':')
            k, v = [s.strip() for s in (k, v)]
            new_attrs[k] = v

        return new_attrs

    def findAttr(self, svgNode, name):
        """Search an attribute with some name in some node or above.

        First the node is searched, then its style attribute, then
        the search continues in the node's parent node. If no such
        attribute is found, '' is returned.
        """

        # This needs also to lookup values like "url(#SomeName)"...

        if self.css_rules is not None and not svgNode.attrib.get('__rules_applied', False):
            if isinstance(svgNode, NodeTracker):
                svgNode.apply_rules(self.css_rules)
            else:
                ElementWrapper(svgNode).apply_rules(self.css_rules)
        attr_value = svgNode.attrib.get(name, '').strip()

        if attr_value and attr_value != "inherit":
            return attr_value
        elif svgNode.attrib.get("style"):
            dict = self.parseMultiAttributes(svgNode.attrib.get("style"))
            if name in dict:
                return dict[name]
        if svgNode.getparent() is not None:
            return self.findAttr(svgNode.getparent(), name)
        return ''

    def getAllAttributes(self, svgNode):
        "Return a dictionary of all attributes of svgNode or those inherited by it."

        dict = {}

        if node_name(svgNode.getparent()) == 'g':
            dict.update(self.getAllAttributes(svgNode.getparent()))

        style = svgNode.attrib.get("style")
        if style:
            d = self.parseMultiAttributes(style)
            dict.update(d)

        for key, value in svgNode.attrib.items():
            if key != "style":
                dict[key] = value

        return dict

    def id(self, svgAttr):
        "Return attribute as is."
        return svgAttr

    def convertTransform(self, svgAttr):
        """Parse transform attribute string.

        E.g. "scale(2) translate(10,20)"
             -> [("scale", 2), ("translate", (10,20))]
        """

        line = svgAttr.strip()

        ops = line[:]
        brackets = []
        indices = []
        for i, lin in enumerate(line):
            if lin in "()":
                brackets.append(i)
        for i in range(0, len(brackets), 2):
            bi, bj = brackets[i], brackets[i+1]
            subline = line[bi+1:bj]
            subline = subline.strip()
            subline = subline.replace(',', ' ')
            subline = re.sub("[ ]+", ',', subline)
            try:
                if ',' in subline:
                    indices.append(tuple(float(num) for num in subline.split(',')))
                else:
                    indices.append(float(subline))
            except ValueError:
                continue
            ops = ops[:bi] + ' '*(bj-bi+1) + ops[bj+1:]
        ops = ops.replace(',', ' ').split()

        if len(ops) != len(indices):
            logger.warning("Unable to parse transform expression '%s'" % svgAttr)
            return []

        result = []
        for i, op in enumerate(ops):
            result.append((op, indices[i]))

        return result


class Svg2RlgAttributeConverter(AttributeConverter):
    "A concrete SVG to RLG attribute converter."

    def __init__(self, color_converter=None):
        super(Svg2RlgAttributeConverter, self).__init__()
        self.color_converter = color_converter or self.identity_color_converter

    @staticmethod
    def identity_color_converter(c):
        return c

    @staticmethod
    def split_attr_list(attr):
        return shlex.split(attr.strip().replace(',', ' '))

    def convertLength(self, svgAttr, em_base=12, attr_name=None, default=0.0):
        "Convert length to points."

        text = svgAttr
        if not text:
            return default
        if ' ' in text.replace(',', ' ').strip():
            logger.debug("Only getting first value of %s" % text)
            text = text.replace(',', ' ').split()[0]

        if text.endswith('%'):
            if self.main_box is None:
                logger.error("Unable to resolve percentage unit without a main box")
                return float(text[:-1])
            if attr_name is None:
                logger.error("Unable to resolve percentage unit without knowing the node name")
                return float(text[:-1])
            if attr_name in ('x', 'cx', 'x1', 'x2', 'width'):
                full = self.main_box.width
            elif attr_name in ('y', 'cy', 'y1', 'y2', 'height'):
                full = self.main_box.height
            else:
                logger.error("Unable to detect if node '%s' is width or height" % attr_name)
                return float(text[:-1])
            return float(text[:-1]) / 100 * full
        elif text.endswith("pc"):
            return float(text[:-2]) * pica
        elif text.endswith("pt"):
            return float(text[:-2]) * 1.25
        elif text.endswith("em"):
            return float(text[:-2]) * em_base
        elif text.endswith("px"):
            return float(text[:-2])

        if "ex" in text:
            logger.warning("Ignoring unit ex")
            text = text.replace("ex", '')

        text = text.strip()
        length = toLength(text)  # this does the default measurements such as mm and cm

        return length

    def convertLengthList(self, svgAttr):
        """Convert a list of lengths."""
        return [self.convertLength(a) for a in self.split_attr_list(svgAttr)]

    def convertOpacity(self, svgAttr):
        return float(svgAttr)

    def convertFillRule(self, svgAttr):
        return {
            'nonzero': FILL_NON_ZERO,
            'evenodd': FILL_EVEN_ODD,
        }.get(svgAttr, '')

    def convertColor(self, svgAttr):
        "Convert string to a RL color object."

        # This needs also to lookup values like "url(#SomeName)"...

        text = svgAttr
        if not text or text == "none":
            return None

        if text == "currentColor":
            return "currentColor"
        elif len(text) == 7 and text[0] == '#':
            return self.color_converter(colors.HexColor(text))
        elif len(text) == 4 and text[0] == '#':
            return self.color_converter(colors.HexColor('#' + 2*text[1] + 2*text[2] + 2*text[3]))
        elif text.startswith('rgb') and '%' not in text:
            t = text[3:].strip('()')
            tup = [h[2:] for h in [hex(int(num)) for num in t.split(',')]]
            tup = [(2 - len(h)) * '0' + h for h in tup]
            col = "#%s%s%s" % tuple(tup)
            return self.color_converter(colors.HexColor(col))
        elif text.startswith('rgb') and '%' in text:
            t = text[3:].replace('%', '').strip('()')
            tup = (float(val)/100.0 for val in t.split(','))
            return self.color_converter(colors.Color(*tup))
        else:
            # Test if text is a predefined color constant
            try:
                color = getattr(colors, text)
            except AttributeError:
                logger.warning("Can't handle color: %s" % text)
            else:
                return self.color_converter(color)

        return None

    def convertLineJoin(self, svgAttr):
        return {"miter":0, "round":1, "bevel":2}[svgAttr]

    def convertLineCap(self, svgAttr):
        return {"butt":0, "round":1, "square":2}[svgAttr]

    def convertDashArray(self, svgAttr):
        strokeDashArray = self.convertLengthList(svgAttr)
        return strokeDashArray

    def convertDashOffset(self, svgAttr):
        strokeDashOffset = self.convertLength(svgAttr)
        return strokeDashOffset

    def convertFontFamily(self, svgAttr):
        if not svgAttr:
            return ''
        # very hackish
        font_mapping = {
            "sans-serif": "Helvetica",
            "serif": "Times-Roman",
            "times": "Times-Roman",
            "monospace": "Courier",
        }
        font_names = [
            font_mapping.get(font_name.lower(), font_name)
            for font_name in self.split_attr_list(svgAttr)
        ]
        non_exact_matches = []
        for font_name in font_names:
            font_name, exact = find_font(font_name)
            if exact:
                return font_name
            elif font_name:
                non_exact_matches.append(font_name)
        if non_exact_matches:
            return non_exact_matches[0]
        else:
            logger.warning("Unable to find a suitable font for 'font-family:%s'" % svgAttr)
            return DEFAULT_FONT_NAME


class ElementWrapper(object):
    """
    lxml element wrapper to partially match the API from cssselect2.ElementWrapper
    so as element can be passed to rules.match().
    """
    in_html_document = False

    def __init__(self, obj):
        self.object = obj

    @property
    def id(self):
        return self.object.attrib.get('id')

    @property
    def etree_element(self):
        return self.object

    @property
    def parent(self):
        par = self.object.getparent()
        return ElementWrapper(par) if par is not None else None

    @property
    def classes(self):
        cl = self.object.attrib.get('class')
        return split_whitespace(cl) if cl is not None else []

    @property
    def local_name(self):
        return node_name(self.object)

    @property
    def namespace_url(self):
        if '}' in self.object.tag:
            self.object.tag.split('}')[0][1:]

    def iter_ancestors(self):
        element = self
        while element.parent is not None:
            element = element.parent
            yield element

    def apply_rules(self, rules):
        matches = rules.match(self)
        for match in matches:
            attr_dict = match[3][1]
            for attr, val in attr_dict.items():
                if not attr in self.object.attrib:
                    try:
                        self.object.attrib[attr] = val
                    except ValueError:
                        pass
        # Set marker on the node to not apply rules more than once
        self.object.set('__rules_applied', '1')


class NodeTracker(ElementWrapper):
    """An object wrapper keeping track of arguments to certain method calls.

    Instances wrap an object and store all arguments to one special
    method, getAttribute(name), in a list of unique elements, usedAttrs.
    """

    def __init__(self, obj):
        super(NodeTracker, self).__init__(obj)
        self.usedAttrs = []

    def __repr__(self):
        return '<NodeTracker for node %s>' % self.object

    def getAttribute(self, name):
        # add argument to the history, if not already present
        if name not in self.usedAttrs:
            self.usedAttrs.append(name)
        # forward call to wrapped object
        return self.object.attrib.get(name, '')

    def __getattr__(self, name):
        # forward attribute access to wrapped object
        return getattr(self.object, name)


class CircularRefError(Exception):
    pass


class ExternalSVG:
    def __init__(self, path, renderer):
        self.root_node = load_svg_file(path)
        self.renderer = SvgRenderer(path, parent_svgs=renderer._parent_chain + [renderer.source_path])
        self.rendered = False

    def get_fragment(self, fragment):
        if not self.rendered:
            self.renderer.render(self.root_node)
            self.rendered = True
        return self.renderer.definitions.get(fragment)


### the main meat ###

class SvgRenderer:
    """Renderer that renders an SVG file on a ReportLab Drawing instance.

    This is the base class for walking over an SVG DOM document and
    transforming it into a ReportLab Drawing instance.
    """

    def __init__(self, path, color_converter=None, parent_svgs=None):
        self.source_path = path
        self._parent_chain = parent_svgs or []  #  To detect circular refs.
        self.attrConverter = Svg2RlgAttributeConverter(color_converter=color_converter)
        self.shape_converter = Svg2RlgShapeConverter(path, self.attrConverter)
        self.handled_shapes = self.shape_converter.get_handled_shapes()
        self.definitions = {}
        self.waiting_use_nodes = defaultdict(list)
        self._external_svgs = {}

    def render(self, svg_node):
        node = NodeTracker(svg_node)
        view_box = self.get_box(node, default_box=True)
        # Knowing the main box is useful for percentage units
        self.attrConverter.set_box(view_box)

        main_group = self.renderSvg(node, outermost=True)
        for xlink in self.waiting_use_nodes.keys():
            logger.debug("Ignoring unavailable object width ID '%s'." % xlink)

        main_group.translate(0 - view_box.x, -view_box.height - view_box.y)

        width, height = self.shape_converter.convert_length_attrs(
            svg_node, "width", "height", defaults=(view_box.width, view_box.height)
        )
        drawing = Drawing(width, height)
        drawing.add(main_group)
        return drawing

    def renderNode(self, node, parent=None):
        n = NodeTracker(node)
        nid = n.getAttribute("id")
        ignored = False
        item = None
        name = node_name(node)

        clipping = self.get_clippath(n)
        if name == "svg":
            item = self.renderSvg(n)
            parent.add(item)
        elif name == "defs":
            item = self.renderG(n)
        elif name == 'a':
            item = self.renderA(n)
            parent.add(item)
        elif name == 'g':
            display = n.getAttribute("display")
            item = self.renderG(n, clipping=clipping)
            if display != "none":
                parent.add(item)
        elif name == "style":
            self.renderStyle(n)
        elif name == "symbol":
            item = self.renderSymbol(n)
            parent.add(item)
        elif name == "use":
            item = self.renderUse(n, clipping=clipping)
            parent.add(item)
        elif name == "clipPath":
            item = self.renderG(n)
        elif name in self.handled_shapes:
            if name == 'image':
                # We resolve the image target at renderer level because it can point
                # to another SVG file or node which has to be rendered too.
                target = self.xlink_href_target(n)
                if target is None:
                    return
                elif isinstance(target, tuple):
                    # This is SVG content needed to be rendered
                    gr = Group()
                    renderer, node = target
                    renderer.renderNode(node, parent=gr)
                    self.apply_node_attr_to_group(n, gr)
                    parent.add(gr)
                    return
                else:
                    # Attaching target to node, so we can get it back in convertImage
                    n._resolved_target = target

            item = self.shape_converter.convertShape(name, n, clipping)
            display = n.getAttribute("display")
            if item and display != "none":
                parent.add(item)
        else:
            ignored = True
            logger.debug("Ignoring node: %s" % name)

        if not ignored:
            if nid and item:
                self.definitions[nid] = node
            if nid in self.waiting_use_nodes.keys():
                to_render = self.waiting_use_nodes.pop(nid)
                for use_node, group in to_render:
                    self.renderUse(use_node, group=group)
            self.print_unused_attributes(node, n)

    def get_clippath(self, node):
        """
        Return the clipping Path object referenced by the node 'clip-path'
        attribute, if any.
        """
        def get_shape_from_group(group):
            for elem in group.contents:
                if isinstance(elem, Group):
                    return get_shape_from_group(elem)
                elif isinstance(elem, SolidShape):
                    return elem

        def get_shape_from_node(node):
            for child in node.getchildren():
                if node_name(child) == 'path':
                    group = self.shape_converter.convertShape('path', NodeTracker(child))
                    return group.contents[-1]
                elif node_name(child) == 'use':
                    grp = self.renderUse(NodeTracker(child))
                    return get_shape_from_group(grp)
                elif node_name(child) == 'rect':
                    return self.shape_converter.convertRect(NodeTracker(child))
                else:
                    return get_shape_from_node(child)

        clip_path = node.getAttribute('clip-path')
        if not clip_path:
            return
        m = re.match(r'url\(#([^\)]*)\)', clip_path)
        if not m:
            return
        ref = m.groups()[0]
        if not ref in self.definitions:
            return

        shape = get_shape_from_node(self.definitions[ref])
        if isinstance(shape, Rect):
            # It is possible to use a rect as a clipping path in an svg, so we
            # need to convert it to a path for rlg.
            x1, y1, x2, y2 = shape.getBounds()
            cp = ClippingPath()
            cp.moveTo(x1, y1)
            cp.lineTo(x2, y1)
            cp.lineTo(x2, y2)
            cp.lineTo(x1, y2)
            cp.closePath()
            # Copy the styles from the rect to the clipping path.
            copy_shape_properties(shape, cp)
            return cp
        elif isinstance(shape, Path):
            return ClippingPath(copy_from=shape)
        elif shape:
            logging.error("Unsupported shape type %s for clipping" % shape.__class__.__name__)

    def print_unused_attributes(self, node, n):
        if logger.level > logging.DEBUG:
            return
        all_attrs = self.attrConverter.getAllAttributes(node).keys()
        unused_attrs = [attr for attr in all_attrs if attr not in n.usedAttrs]
        if unused_attrs:
            logger.debug("Unused attrs: %s %s" % (node_name(n), unused_attrs))

    def apply_node_attr_to_group(self, node, group):
        getAttr = node.getAttribute
        transform, x, y = map(getAttr, ("transform", "x", "y"))
        if x or y:
            transform += " translate(%s, %s)" % (x or '0', y or '0')
        if transform:
            self.shape_converter.applyTransformOnGroup(transform, group)

    def xlink_href_target(self, node, group=None):
        """
        Return either:
            - a tuple (renderer, node) when the the xlink:href attribute targets
              a vector file or node
            - the path to an image file for any raster image targets
            - None if any problem occurs
        """
        xlink_href = node.attrib.get('{http://www.w3.org/1999/xlink}href')
        if not xlink_href:
            return None

        # First handle any raster embedded image data
        match = re.match(r"^data:image/(jpeg|png);base64", xlink_href)
        if match:
            img_format = match.groups()[0]
            image_data = base64.decodestring(xlink_href[(match.span(0)[1] + 1):].encode('ascii'))
            file_indicator, path = tempfile.mkstemp(suffix='.%s' % img_format)
            with open(path, 'wb') as fh:
                fh.write(image_data)
            # Close temporary file (as opened by tempfile.mkstemp)
            os.close(file_indicator)
            # this needs to be removed later, not here...
            # if exists(path): os.remove(path)
            return path

        # From here, we can assume this is a path.
        if '#' in xlink_href:
            iri, fragment = xlink_href.split('#', 1)
        else:
            iri, fragment = xlink_href, None

        if iri:
            # Only local relative paths are supported yet
            if not isinstance(self.source_path, str):
                logger.error(
                    "Unable to resolve image path '%s' as the SVG source is not a file system path." % iri
                )
                return None
            path = os.path.normpath(os.path.join(os.path.dirname(self.source_path), iri))
            if not os.access(path, os.R_OK):
                return None
            if path == self.source_path:
                # Self-referencing, ignore the IRI part
                iri = None

        if iri:
            if path.endswith('.svg'):
                if path in self._parent_chain:
                    logger.error("Circular reference detected in file.")
                    raise CircularRefError()
                if path not in self._external_svgs:
                    self._external_svgs[path] = ExternalSVG(path, self)
                ext_svg = self._external_svgs[path]
                if ext_svg.root_node is not None:
                    if fragment:
                        ext_frag = ext_svg.get_fragment(fragment)
                        if ext_frag is not None:
                            return ext_svg.renderer, ext_frag
                    else:
                        return ext_svg.renderer, ext_svg.root_node
            else:
                # A raster image path
                try:
                    # This will catch invalid images
                    PDFImage(path, 0, 0)
                except IOError:
                    logger.error("Unable to read the image %s. Skipping..." % path)
                    return None
                return path

        elif fragment:
            # A pointer to an internal definition
            if fragment in self.definitions:
                return self, self.definitions[fragment]
            else:
                # The missing definition should appear later in the file
                self.waiting_use_nodes[fragment].append((node, group))
                return DELAYED

    def renderTitle_(self, node):
        # Main SVG title attr. could be used in the PDF document info field.
        pass

    def renderDesc_(self, node):
        # Main SVG desc. attr. could be used in the PDF document info field.
        pass

    def get_box(self, svg_node, default_box=False):
        view_box = svg_node.getAttribute("viewBox")
        if view_box:
            view_box = self.attrConverter.convertLengthList(view_box)
            return Box(*view_box)
        if default_box:
            width, height = map(svg_node.getAttribute, ("width", "height"))
            width, height = map(self.attrConverter.convertLength, (width, height))
            return Box(0, 0, width, height)

    def renderSvg(self, node, outermost=False):
        _saved_preserve_space = self.shape_converter.preserve_space
        self.shape_converter.preserve_space = node.getAttribute("{%s}space" % XML_NS) == 'preserve'

        group = Group()
        for child in node.getchildren():
            self.renderNode(child, group)
        self.shape_converter.preserve_space = _saved_preserve_space

        # Translating
        if not outermost:
            x, y = self.shape_converter.convert_length_attrs(node, "x", "y")
            if x or y:
                group.translate(x or 0, y or 0)

        # Scaling
        view_box = self.get_box(node)
        if not view_box and outermost:
            # Apply only the 'reverse' y-scaling (PDF 0,0 is bottom left)
            group.scale(1, -1)
        elif view_box:
            x_scale, y_scale = 1, 1
            width, height = self.shape_converter.convert_length_attrs(
                node, "width", "height", defaults=(None,) * 2
            )
            if height is not None and view_box.height != height:
                y_scale = height / view_box.height
            if width is not None and view_box.width != width:
                x_scale = width / view_box.width
            group.scale(x_scale, y_scale * (-1 if outermost else 1))

        return group

    def renderG(self, node, clipping=None, display=1):
        getAttr = node.getAttribute
        id, transform = map(getAttr, ("id", "transform"))
        gr = Group()
        if clipping:
            gr.add(clipping)
        for child in node.getchildren():
            item = self.renderNode(child, parent=gr)
            if item and display:
                gr.add(item)

        if transform:
            self.shape_converter.applyTransformOnGroup(transform, gr)

        return gr

    def renderStyle(self, node):
        self.attrConverter.css_rules = CSSMatcher(node.text)

    def renderSymbol(self, node):
        return self.renderG(node, display=0)

    def renderA(self, node):
        # currently nothing but a group...
        # there is no linking info stored in shapes, maybe a group should?
        return self.renderG(node)

    def renderUse(self, node, group=None, clipping=None):
        if group is None:
            group = Group()

        try:
            item = self.xlink_href_target(node, group=group)
        except CircularRefError:
            node.parent.object.remove(node.object)
            return group
        if item is None:
            return
        elif isinstance(item, str):
            logger.error("<use> nodes cannot reference bitmap image files")
            return
        elif item is DELAYED:
            return group
        else:
            item = item[1]  # [0] is the renderer, not used here.

        if clipping:
            group.add(clipping)
        if len(node.getchildren()) == 0:
            # Append a copy of the referenced node as the <use> child (if not already done)
            node.append(copy.deepcopy(item))
        self.renderNode(node.getchildren()[-1], parent=group)
        self.apply_node_attr_to_group(node, group)
        return group


class SvgShapeConverter:
    """An abstract SVG shape converter.

    Implement subclasses with methods named 'convertX(node)', where
    'X' should be the capitalised name of an SVG node element for
    shapes, like 'Rect', 'Circle', 'Line', etc.

    Each of these methods should return a shape object appropriate
    for the target format.
    """
    def __init__(self, path, attrConverter=None):
        self.attrConverter = attrConverter or Svg2RlgAttributeConverter()
        self.svg_source_file = path
        self.preserve_space = False

    @classmethod
    def get_handled_shapes(cls):
        """Dynamically determine a list of handled shape elements based on
           convert<shape> method existence.
        """
        return [key[7:].lower() for key in dir(cls) if key.startswith('convert')]


class Svg2RlgShapeConverter(SvgShapeConverter):
    """Converter from SVG shapes to RLG (ReportLab Graphics) shapes."""

    def convertShape(self, name, node, clipping=None):
        method_name = "convert%s" % name.capitalize()
        shape = getattr(self, method_name)(node)
        if not shape:
            return
        if name not in ('path', 'polyline', 'text'):
            # Only apply style where the convert method did not apply it.
            self.applyStyleOnShape(shape, node)
        transform = node.getAttribute("transform")
        if not (transform or clipping):
            return shape
        else:
            group = Group()
            if transform:
                self.applyTransformOnGroup(transform, group)
            if clipping:
                group.add(clipping)
            group.add(shape)
            return group

    def convert_length_attrs(self, node, *attrs, **kwargs):
        # When dropping Python 2, we can replace **kwargs by em_base=None in the
        # function signature.
        em_base = kwargs.pop('em_base', None)
        # Support node both as NodeTracker or lxml node
        getAttr = node.getAttribute if hasattr(node, 'getAttribute') else lambda attr: node.attrib.get(attr, '')
        convLength = self.attrConverter.convertLength
        defaults = kwargs.get('defaults', (0.0,) * len(attrs))
        return [
            convLength(getAttr(attr), attr_name=attr, em_base=em_base, default=default)
            for attr, default in zip(attrs, defaults)
        ]

    def convertLine(self, node):
        x1, y1, x2, y2 = self.convert_length_attrs(node, 'x1', 'y1', 'x2', 'y2')
        return Line(x1, y1, x2, y2)

    def convertRect(self, node):
        x, y, width, height, rx, ry = self.convert_length_attrs(
            node, 'x', 'y', 'width', 'height', 'rx', 'ry'
        )
        return Rect(x, y, width, height, rx=rx, ry=ry)

    def convertCircle(self, node):
        # not rendered if r == 0, error if r < 0.
        cx, cy, r = self.convert_length_attrs(node, 'cx', 'cy', 'r')
        return Circle(cx, cy, r)

    def convertEllipse(self, node):
        cx, cy, rx, ry = self.convert_length_attrs(node, 'cx', 'cy', 'rx', 'ry')
        width, height = rx, ry
        return Ellipse(cx, cy, width, height)

    def convertPolyline(self, node):
        points = node.getAttribute("points")
        points = points.replace(',', ' ')
        points = points.split()
        points = list(map(self.attrConverter.convertLength, points))
        if len(points) % 2 != 0 or len(points) == 0:
            # Odd number of coordinates or no coordinates, invalid polyline
            return None

        polyline = PolyLine(points)
        self.applyStyleOnShape(polyline, node)
        has_fill = self.attrConverter.findAttr(node, 'fill') not in ('', 'none')

        if has_fill:
            # ReportLab doesn't fill polylines, so we are creating a polygon
            # polygon copy of the polyline, but without stroke.
            group = Group()
            polygon = Polygon(points)
            self.applyStyleOnShape(polygon, node)
            polygon.strokeColor = None
            group.add(polygon)
            group.add(polyline)
            return group

        return polyline

    def convertPolygon(self, node):
        points = node.getAttribute("points")
        points = points.replace(',', ' ')
        points = points.split()
        points = list(map(self.attrConverter.convertLength, points))
        if len(points) % 2 != 0 or len(points) == 0:
            # Odd number of coordinates or no coordinates, invalid polygon
            return None
        shape = Polygon(points)

        return shape

    def clean_text(self, text, preserve_space):
        """Text cleaning as per https://www.w3.org/TR/SVG/text.html#WhiteSpace
        """
        if text is None:
            return
        if preserve_space:
            text = text.replace('\r\n', ' ').replace('\n', ' ').replace('\t', ' ')
        else:
            text = text.replace('\r\n', '').replace('\n', '').replace('\t', ' ')
            text = text.strip()
            while ('  ' in text):
                text = text.replace('  ', ' ')
        return text

    def convertText(self, node):
        attrConv = self.attrConverter
        xml_space = node.getAttribute("{%s}space" % XML_NS)
        if xml_space:
            preserve_space = xml_space == 'preserve'
        else:
            preserve_space = self.preserve_space

        gr = Group()

        frag_lengths = []

        dx0, dy0 = 0, 0
        x1, y1 = 0, 0
        ff = attrConv.findAttr(node, "font-family") or DEFAULT_FONT_NAME
        ff = attrConv.convertFontFamily(ff)
        fs = attrConv.findAttr(node, "font-size") or "12"
        fs = attrConv.convertLength(fs)
        x, y = self.convert_length_attrs(node, 'x', 'y', em_base=fs)
        for c in itertools.chain([node], node.getchildren()):
            has_x, has_y = False, False
            dx, dy = 0, 0
            baseLineShift = 0
            if node_name(c) == 'text':
                text = self.clean_text(c.text, preserve_space)
                if not text:
                    continue
            elif node_name(c) == 'tspan':
                text = self.clean_text(c.text, preserve_space)
                if not text:
                    continue
                x1, y1, dx, dy = self.convert_length_attrs(c, 'x', 'y', 'dx', 'dy', em_base=fs)
                has_x, has_y = (c.attrib.get('x', '') != '', c.attrib.get('y', '') != '')
                dx0 = dx0 + dx
                dy0 = dy0 + dy
                baseLineShift = c.attrib.get("baseline-shift", '0')
                if baseLineShift in ("sub", "super", "baseline"):
                    baseLineShift = {"sub":-fs/2, "super":fs/2, "baseline":0}[baseLineShift]
                else:
                    baseLineShift = attrConv.convertLength(baseLineShift, em_base=fs)
            else:
                continue

            frag_lengths.append(stringWidth(text, ff, fs))
            new_x = (x1 + dx) if has_x else (x + dx0 + sum(frag_lengths[:-1]))
            new_y = (y1 + dy) if has_y else (y + dy0)
            shape = String(new_x, -(new_y - baseLineShift), text)
            self.applyStyleOnShape(shape, node)
            if node_name(c) == 'tspan':
                self.applyStyleOnShape(shape, c)

            gr.add(shape)

        gr.scale(1, -1)

        return gr

    def convertPath(self, node):
        d = node.getAttribute('d')
        if not d:
            return None
        normPath = normalise_svg_path(d)
        path = Path()
        points = path.points
        # Track subpaths needing to be closed later
        unclosed_subpath_pointers = []
        subpath_start = []
        lastop = ''

        for i in range(0, len(normPath), 2):
            op, nums = normPath[i:i+2]

            if op in ('m', 'M') and i > 0 and path.operators[-1] != _CLOSEPATH:
                unclosed_subpath_pointers.append(len(path.operators))

            # moveto absolute
            if op == 'M':
                path.moveTo(*nums)
                subpath_start = points[-2:]
            # lineto absolute
            elif op == 'L':
                path.lineTo(*nums)

            # moveto relative
            elif op == 'm':
                if len(points) >= 2:
                    if lastop in ('Z', 'z'):
                        starting_point = subpath_start
                    else:
                        starting_point = points[-2:]
                    xn, yn = starting_point[0] + nums[0], starting_point[1] + nums[1]
                    path.moveTo(xn, yn)
                else:
                    path.moveTo(*nums)
                subpath_start = points[-2:]
            # lineto relative
            elif op == 'l':
                xn, yn = points[-2] + nums[0], points[-1] + nums[1]
                path.lineTo(xn, yn)

            # horizontal/vertical line absolute
            elif op == 'H':
                path.lineTo(nums[0], points[-1])
            elif op == 'V':
                path.lineTo(points[-2], nums[0])

            # horizontal/vertical line relative
            elif op == 'h':
                path.lineTo(points[-2] + nums[0], points[-1])
            elif op == 'v':
                path.lineTo(points[-2], points[-1] + nums[0])

            # cubic bezier, absolute
            elif op == 'C':
                path.curveTo(*nums)
            elif op == 'S':
                x2, y2, xn, yn = nums
                if len(points) < 4 or lastop not in {'c', 'C', 's', 'S'}:
                    xp, yp, x0, y0 = points[-2:] * 2
                else:
                    xp, yp, x0, y0 = points[-4:]
                xi, yi = x0 + (x0 - xp), y0 + (y0 - yp)
                path.curveTo(xi, yi, x2, y2, xn, yn)

            # cubic bezier, relative
            elif op == 'c':
                xp, yp = points[-2:]
                x1, y1, x2, y2, xn, yn = nums
                path.curveTo(xp + x1, yp + y1, xp + x2, yp + y2, xp + xn, yp + yn)
            elif op == 's':
                x2, y2, xn, yn = nums
                if len(points) < 4 or lastop not in {'c', 'C', 's', 'S'}:
                    xp, yp, x0, y0 = points[-2:] * 2
                else:
                    xp, yp, x0, y0 = points[-4:]
                xi, yi = x0 + (x0 - xp), y0 + (y0 - yp)
                path.curveTo(xi, yi, x0 + x2, y0 + y2, x0 + xn, y0 + yn)

            # quadratic bezier, absolute
            elif op == 'Q':
                x0, y0 = points[-2:]
                x1, y1, xn, yn = nums
                (x0, y0), (x1, y1), (x2, y2), (xn, yn) = \
                    convert_quadratic_to_cubic_path((x0, y0), (x1, y1), (xn, yn))
                path.curveTo(x1, y1, x2, y2, xn, yn)
            elif op == 'T':
                if len(points) < 4:
                    xp, yp, x0, y0 = points[-2:] * 2
                else:
                    xp, yp, x0, y0 = points[-4:]
                xi, yi = x0 + (x0 - xp), y0 + (y0 - yp)
                xn, yn = nums
                (x0, y0), (x1, y1), (x2, y2), (xn, yn) = \
                    convert_quadratic_to_cubic_path((x0, y0), (xi, yi), (xn, yn))
                path.curveTo(x1, y1, x2, y2, xn, yn)

            # quadratic bezier, relative
            elif op == 'q':
                x0, y0 = points[-2:]
                x1, y1, xn, yn = nums
                x1, y1, xn, yn = x0 + x1, y0 + y1, x0 + xn, y0 + yn
                (x0, y0), (x1, y1), (x2, y2), (xn, yn) = \
                    convert_quadratic_to_cubic_path((x0, y0), (x1, y1), (xn, yn))
                path.curveTo(x1, y1, x2, y2, xn, yn)
            elif op == 't':
                if len(points) < 4:
                    xp, yp, x0, y0 = points[-2:] * 2
                else:
                    xp, yp, x0, y0 = points[-4:]
                x0, y0 = points[-2:]
                xn, yn = nums
                xn, yn = x0 + xn, y0 + yn
                xi, yi = x0 + (x0 - xp), y0 + (y0 - yp)
                (x0, y0), (x1, y1), (x2, y2), (xn, yn) = \
                    convert_quadratic_to_cubic_path((x0, y0), (xi, yi), (xn, yn))
                path.curveTo(x1, y1, x2, y2, xn, yn)

            # elliptical arc
            elif op in ('A', 'a'):
                rx, ry, phi, fA, fS, x2, y2 = nums
                x1, y1 = points[-2:]
                if op == 'a':
                    x2 += x1
                    y2 += y1
                if abs(rx) <= 1e-10 or abs(ry) <= 1e-10:
                    path.lineTo(x2, y2)
                else:
                    bp = bezier_arc_from_end_points(x1, y1, rx, ry, phi, fA, fS, x2, y2)
                    for _, _, x1, y1, x2, y2, xn, yn in bp:
                        path.curveTo(x1, y1, x2, y2, xn, yn)

            # close path
            elif op in ('Z', 'z'):
                path.closePath()

            else:
                logger.debug("Suspicious path operator: %s" % op)
            lastop = op

        gr = Group()
        self.applyStyleOnShape(path, node)

        if path.operators[-1] != _CLOSEPATH:
            unclosed_subpath_pointers.append(len(path.operators))

        if unclosed_subpath_pointers and path.fillColor is not None:
            # ReportLab doesn't fill unclosed paths, so we are creating a copy
            # of the path with all subpaths closed, but without stroke.
            # https://bitbucket.org/rptlab/reportlab/issues/99/
            closed_path = NoStrokePath(copy_from=path)
            for pointer in reversed(unclosed_subpath_pointers):
                closed_path.operators.insert(pointer, _CLOSEPATH)
            gr.add(closed_path)
            path.fillColor = None

        gr.add(path)
        return gr

    def convertImage(self, node):
        if not haveImages:
            logger.warning(
                "Unable to handle embedded images. Maybe the pillow library is missing?"
            )
            return None

        x, y, width, height = self.convert_length_attrs(node, 'x', 'y', 'width', 'height')
        image = node._resolved_target
        image = Image(int(x), int(y + height), int(width), int(height), image)

        group = Group(image)
        group.translate(0, (y + height) * 2)
        group.scale(1, -1)
        return group

    def applyTransformOnGroup(self, transform, group):
        """Apply an SVG transformation to a RL Group shape.

        The transformation is the value of an SVG transform attribute
        like transform="scale(1, -1) translate(10, 30)".

        rotate(<angle> [<cx> <cy>]) is equivalent to:
          translate(<cx> <cy>) rotate(<angle>) translate(-<cx> -<cy>)
        """

        tr = self.attrConverter.convertTransform(transform)
        for op, values in tr:
            if op == "scale":
                if not isinstance(values, tuple):
                    values = (values, values)
                group.scale(*values)
            elif op == "translate":
                if isinstance(values, (int, float)):
                    # From the SVG spec: If <ty> is not provided, it is assumed to be zero.
                    values = values, 0
                group.translate(*values)
            elif op == "rotate":
                if not isinstance(values, tuple) or len(values) == 1:
                    group.rotate(values)
                elif len(values) == 3:
                    angle, cx, cy = values
                    group.translate(cx, cy)
                    group.rotate(angle)
                    group.translate(-cx, -cy)
            elif op == "skewX":
                group.skew(values, 0)
            elif op == "skewY":
                group.skew(0, values)
            elif op == "matrix":
                group.transform = values
            else:
                logger.debug("Ignoring transform: %s %s" % (op, values))

    def applyStyleOnShape(self, shape, node, only_explicit=False):
        """
        Apply styles from an SVG element to an RLG shape.
        If only_explicit is True, only attributes really present are applied.
        """

        # RLG-specific: all RLG shapes
        "Apply style attributes of a sequence of nodes to an RL shape."

        # tuple format: (svgAttr, rlgAttr, converter, default)
        mappingN = (
            ("fill", "fillColor", "convertColor", "black"),
            ("fill-opacity", "fillOpacity", "convertOpacity", 1),
            ("fill-rule", "_fillRule", "convertFillRule", "nonzero"),
            ("stroke", "strokeColor", "convertColor", "none"),
            ("stroke-width", "strokeWidth", "convertLength", "1"),
            ("stroke-opacity", "strokeOpacity", "convertOpacity", 1),
            ("stroke-linejoin", "strokeLineJoin", "convertLineJoin", "0"),
            ("stroke-linecap", "strokeLineCap", "convertLineCap", "0"),
            ("stroke-dasharray", "strokeDashArray", "convertDashArray", "none"),
        )
        mappingF = (
            ("font-family", "fontName", "convertFontFamily", DEFAULT_FONT_NAME),
            ("font-size", "fontSize", "convertLength", "12"),
            ("text-anchor", "textAnchor", "id", "start"),
        )

        if shape.__class__ == Group:
            # Recursively apply style on Group subelements
            for subshape in shape.contents:
                self.applyStyleOnShape(subshape, node, only_explicit=only_explicit)
            return

        ac = self.attrConverter
        for mapping in (mappingN, mappingF):
            if shape.__class__ != String and mapping == mappingF:
                continue
            for (svgAttrName, rlgAttr, func, default) in mapping:
                svgAttrValue = ac.findAttr(node, svgAttrName)
                if svgAttrValue == '':
                    if only_explicit:
                        continue
                    else:
                        svgAttrValue = default
                if svgAttrValue == "currentColor":
                    svgAttrValue = ac.findAttr(node.getparent(), "color") or default
                try:
                    meth = getattr(ac, func)
                    setattr(shape, rlgAttr, meth(svgAttrValue))
                except (AttributeError, KeyError, ValueError):
                    pass
        if getattr(shape, 'fillOpacity', None) is not None and shape.fillColor:
            shape.fillColor.alpha = shape.fillOpacity


def svg2rlg(path, **kwargs):
    "Convert an SVG file to an RLG Drawing object."

    # unzip .svgz file into .svg
    unzipped = False
    if isinstance(path, str) and os.path.splitext(path)[1].lower() == ".svgz":
        with gzip.open(path, 'rb') as f_in, open(path[:-1], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        path = path[:-1]
        unzipped = True

    svg_root = load_svg_file(path)
    if svg_root is None:
        return

    # convert to a RLG drawing
    svgRenderer = SvgRenderer(path, **kwargs)
    drawing = svgRenderer.render(svg_root)

    # remove unzipped .svgz file (.svg)
    if unzipped:
        os.remove(path)

    return drawing


def load_svg_file(path):
    parser = etree.XMLParser(remove_comments=True, recover=True)
    try:
        doc = etree.parse(path, parser=parser)
        svg_root = doc.getroot()
    except Exception as exc:
        logger.error("Failed to load input file! (%s)" % exc)
    else:
        return svg_root


def node_name(node):
    """Return lxml node name without the namespace prefix."""

    try:
        return node.tag.split('}')[-1]
    except AttributeError:
        pass


def copy_shape_properties(source_shape, dest_shape):
    for prop, val in source_shape.getProperties().items():
        try:
            setattr(dest_shape, prop, val)
        except AttributeError:
            pass


def monkeypatch_reportlab():
    """
    https://bitbucket.org/rptlab/reportlab/issues/95/
    ReportLab always use 'Even-Odd' filling mode for paths, this patch forces
    RL to honor the path fill rule mode (possibly 'Non-Zero Winding') instead.
    """
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.graphics import shapes

    original_renderPath = shapes._renderPath
    def patchedRenderPath(path, drawFuncs, **kwargs):
        # Patched method to transfer fillRule from Path to PDFPathObject
        # Get back from bound method to instance
        try:
            drawFuncs[0].__self__.fillMode = path._fillRule
        except AttributeError:
            pass
        return original_renderPath(path, drawFuncs, **kwargs)
    shapes._renderPath = patchedRenderPath

    original_drawPath = Canvas.drawPath
    def patchedDrawPath(self, path, **kwargs):
        current = self._fillMode
        if hasattr(path, 'fillMode'):
            self._fillMode = path.fillMode
        else:
            self._fillMode = FILL_NON_ZERO
        original_drawPath(self, path, **kwargs)
        self._fillMode = current
    Canvas.drawPath = patchedDrawPath

monkeypatch_reportlab()