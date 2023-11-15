"""
XML Elements and ElementTree Implementation
"""
from io import BytesIO
from typing import Callable, Optional, BinaryIO, Set

from .element import *
from .element import _Special
from .parser import Parser, BaseParser, write_parser
from .escape import escape_cdata, escape_attrib

#** Variables **#
__all__ = ['tostring', 'fromstring', 'ElementTree']

#** Functions **#

def tostring(element: Element, *args, **kwargs) -> bytes:
    """
    convert element to string w/ the given arguments

    :param element: element to convert to string
    :param args:    positional args to pass to serializer
    :param kwargs:  keyword args to pass to serializer
    :return:        serialized bytes of element and children
    """
    data = BytesIO()
    ElementTree(element).write(data, *args, **kwargs)
    return data.getvalue()

def fromstring(text, parser: Optional[BaseParser] = None,
    fix_broken: bool = True, **kwargs) -> Element:
    """
    convert raw xml bytes into valid element tree

    :param text:       xml text content to deserialize
    :param parser:     parser instance to process xml string
    :param fix_broken: ignore or attempt to repair broken xml
    :param kwargs:     kwargs to pass to parser implementation
    :return:           html element tree
    """
    parser = parser or Parser(fix_broken=fix_broken, **kwargs)
    write_parser(parser, text)
    return parser.close()

def quote(text: str) -> str:
    """quote escape"""
    return '"' + escape_attrib(text) + '"'

def serialize_any(
    write:                Callable[[str], None], 
    element:              Element, 
    short_empty_elements: bool, 
    skip_end_tags:        Set[str],
    skip_shorten:         Set[str],
):
    """serialize xml/html using write function"""
    # check if element should skip-end
    skip_end   = skip_end_tags and element.tag in skip_end_tags
    skip_short = skip_shorten and element.tag in skip_shorten
    # serialize special elements differently
    if isinstance(element, _Special):
        func = lambda b: b
        if isinstance(element, Comment):
            start, end, func = '<!-- ', '-->', escape_cdata
        elif isinstance(element, Declaration):
            start, end, func = '<!', '>', escape_cdata
        elif isinstance(element, ProcessingInstruction):
            start, end = '<? ', ' ?>'
        else:
            raise RuntimeError('unsupported element', element)
        write(start + func(element.text or '') + end)
        write(escape_cdata(element.tail or ''))
        return
    # serialize normal elements accordingly
    write('<' + element.tag)
    for name, value in element.attrib.items():
        write(' ' + name)
        if value and value != 'true':
            write('=')
            write(quote(value))
    # close w/ short form if enabled
    if short_empty_elements and not skip_end and not skip_short \
        and not len(element) and not element.text:
        write('/>')
        write(escape_cdata(element.tail or ''))
        return
    # close normally w/ children or otherwise disabled
    write('>')
    write(escape_cdata(element.text or ''))
    for child in element:
        serialize_any(
            write, child, short_empty_elements, skip_end_tags, skip_shorten)
    if not skip_end:
        write('</' + element.tag + '>')
    write(escape_cdata(element.tail or ''))

def serialize_xml(write, element, short_empty_elements=False):
    """serialize xml and write into file"""
    serialize_any(write, element, short_empty_elements, set(), set())

def serialize_html(write, element, short_empty_elements=False):
    """serialize html and write into file"""
    from .html.parser import HTML_FULL, HTML_EMPTY
    serialize_any(write, element, short_empty_elements, HTML_EMPTY, HTML_FULL)

#** Classes **#

class ElementTree:

    def __init__(self, element=None, source=None):
        self.root: Optional[Element] = element
        if source:
            self.parse(source)

    def getroot(self) -> Element:
        if self.root is None:
            raise ValueError('No XML Root Element')
        return self.root

    def parse(self, source: BinaryIO, parser: Optional[BaseParser] = None):
        self.root = fromstring(source, parser)
        return self.getroot()

    def iter(self, tag=None):
        return self.getroot().iter(tag)

    def find(self, path: str):
        return self.getroot().find(path)

    def findall(self, path: str):
        return self.getroot().findall(path)
    
    def finditer(self, path: str):
        return self.getroot().finditer(path)

    def findtext(self, path: str):
        return self.getroot().findtext(path)

    def write(self, f: BinaryIO,
        encoding:             Optional[str] = None,
        xml_declaration:      Optional[str] = None,
        default_namespace:    Optional[str] = None,
        method:               Optional[str] = None,
        short_empty_elements: bool = True
    ):
        """

        """
        encoding  = encoding or 'utf-8'
        write     = lambda s: f.write(s.encode(encoding))
        serialize = serialize_xml
        if not method or method == 'xml':
            if xml_declaration:
                write(xml_declaration)
            else:
                write(f"<?xml version='1.0' encoding='{encoding}'?>\n")
        elif method == 'html':
            serialize = serialize_html
        return serialize(write, self.getroot(), short_empty_elements)
