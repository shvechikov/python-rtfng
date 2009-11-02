#!/usr/bin/env python
from rtfng.utils import RTFTestCase
from rtfng.Elements import Document
from rtfng.PropertySets import TextPropertySet

from rtfng.document.character import TEXT, Text
from rtfng.document.section import Section
from rtfng.document.paragraph import Paragraph

class CharacterTestCase(RTFTestCase):

    def make_charStyleOverride():
        doc, section, styles = RTFTestCase.initializeDoc()
        p = Paragraph()
        p.append('This is a standard paragraph with the default style.')
        p = Paragraph()
        p.append('It is also possible to manully override a style. ',
                  'This is a change of just the font ',
                  TEXT('size', size=48),
                  ' an this is for just the font ',
                  TEXT('typeface', font=styles.Fonts.Impact) ,
                  '.')
        section.append(p)
        return doc
    make_charStyleOverride = staticmethod(make_charStyleOverride)

    def test_charStyleOverride(self):
        self.doTest()

    def make_charColours():
        doc, section, styles = RTFTestCase.initializeDoc()
        section.append('This example test changing the colour of fonts.')
        # Text properties can be specified in two ways, either a text object
        # can have its text properties specified via the TextPropertySet
        # object, or by passing the colour parameter as a style.
        red = TextPropertySet(colour=styles.Colours.Red)
        green = TextPropertySet(colour=styles.Colours.Green)
        blue = TextPropertySet(colour=styles.Colours.Blue)
        yellow = TextPropertySet(colour=styles.Colours.Yellow)
        p = Paragraph()
        p.append('This next word should be in ')
        p.append(Text('red', red))
        p.append(', while the following should be in their respective ')
        p.append('colours: ', Text('blue ', blue), Text('green ', green))
        p.append('and ', TEXT('yellow', colour=styles.Colours.Yellow), '.')
        # When specifying colours it is important to use the colours from the
        # style sheet supplied with the document and not the StandardColours
        # object each document get its own copy of the stylesheet so that
        # changes can be made on a document by document basis without mucking
        # up other documents that might be based on the same basic stylesheet.
        section.append(p)
        return doc
    make_charColours = staticmethod(make_charColours)

    def test_charColours(self):
        self.doTest()

    def make_charUnicode():
        doc, section, styles = RTFTestCase.initializeDoc()
        section.append('This tests unicode.')
        
        p = Paragraph()
        p.append(u'32\u00B0 Fahrenheit is 0\u00B0 Celsuis')
        section.append(p)
        
        p = Paragraph()
        p.append(u'Henry \u2163 is Henry IV in unicode.')
        section.append(p)
        

        return doc
    make_charUnicode = staticmethod(make_charUnicode)

    def test_charUnicode(self):
        self.doTest()


