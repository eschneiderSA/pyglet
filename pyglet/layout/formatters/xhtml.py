#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

from pyglet.layout.formatters.xml import XMLFormatter
from pyglet.layout.css import Stylesheet

# Default stylesheet for HTML 4 
# http://www.w3.org/TR/CSS21/sample.html
default_stylesheet = Stylesheet('''
html, address,
blockquote,
body, dd, div,
dl, dt, fieldset, form,
frame, frameset,
h1, h2, h3, h4,
h5, h6, noframes,
ol, p, ul, center,
dir, hr, menu, pre   { display: block }
html            { font-family: serif }
li              { display: list-item }
head            { display: none }
table           { display: table }
tr              { display: table-row }
thead           { display: table-header-group }
tbody           { display: table-row-group }
tfoot           { display: table-footer-group }
col             { display: table-column }
colgroup        { display: table-column-group }
td, th          { display: table-cell }
caption         { display: table-caption }
th              { font-weight: bolder; text-align: center }
caption         { text-align: center }
body            { margin: 8px }
h1              { font-size: 2em; margin: .67em 0 }
h2              { font-size: 1.5em; margin: .75em 0 }
h3              { font-size: 1.17em; margin: .83em 0 }
h4, p,
blockquote, ul,
fieldset, form,
ol, dl, dir,
menu            { margin: 1.12em 0 }
h5              { font-size: .83em; margin: 1.5em 0 }
h6              { font-size: .75em; margin: 1.67em 0 }
h1, h2, h3, h4,
h5, h6, b,
strong          { font-weight: bolder }
blockquote      { margin-left: 40px; margin-right: 40px }
i, cite, em,
var, address    { font-style: italic }
pre, tt, code,
kbd, samp       { font-family: monospace }
pre             { white-space: pre }
button, textarea,
input, select   { display: inline-block }
big             { font-size: 1.17em }
small, sub, sup { font-size: .83em }
sub             { vertical-align: sub }
sup             { vertical-align: super }
table           { border-spacing: 2px; }
thead, tbody,
tfoot           { vertical-align: middle }
td, th          { vertical-align: inherit }
s, strike, del  { text-decoration: line-through }
hr              { border: 1px inset }
ol, ul, dir,
menu, dd        { margin-left: 40px }
ol              { list-style-type: decimal }
ol ul, ul ol,
ul ul, ol ol    { margin-top: 0; margin-bottom: 0 }
u, ins          { text-decoration: underline }
br:before       { content: "\A" }
:before, :after { white-space: pre-line }
center          { text-align: center }
:link, :visited { text-decoration: underline }
:focus          { outline: thin dotted invert }

/* Begin bidirectionality settings (do not change) */
BDO[dir="ltr"]  { direction: ltr; unicode-bidi: bidi-override }
BDO[dir="rtl"]  { direction: rtl; unicode-bidi: bidi-override }

*[dir="ltr"]    { direction: ltr; unicode-bidi: embed }
*[dir="rtl"]    { direction: rtl; unicode-bidi: embed }
''')

class XHTMLFormatter(XMLFormatter):
    def __init__(self, render_device):
        super(XHTMLFormatter, self).__init__(render_device)
        self.add_stylesheet(default_stylesheet)
        self.in_head = False

    def startElement(self, name, attrs):
        if name == 'head':
            self.process_content_buffer()
            self.in_head = True
        elif self.in_head and name == 'style':
            self._content_buffer = ''
        
        if not self.in_head:
            super(XHTMLFormatter, self).startElement(name, attrs)

    def endElement(self, name):
        if name == 'head':
            self.in_head = False
            self._content_buffer = ''
        elif self.in_head and name == 'style':
            stylesheet = Stylesheet(self._content_buffer)
            self.add_stylesheet(stylesheet)
            self._content_buffer = ''
        elif not self.in_head:
            super(XHTMLFormatter, self).endElement(name)
