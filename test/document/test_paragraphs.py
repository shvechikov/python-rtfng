import re

from rtfng.utils import RTFTestCase
from rtfng.Elements import Document
from rtfng.PropertySets import ParagraphPropertySet, TabPropertySet

from rtfng.document.base import TAB, LINE
from rtfng.document.section import Section
from rtfng.document.character import TEXT
from rtfng.document.paragraph import Paragraph

class ParagraphTestCase(RTFTestCase):

    def make_paraHeading():
        doc, section, styles = RTFTestCase.initializeDoc()
        p1 = Paragraph(styles.ParagraphStyles.Heading1)
        p1.append('Heading 1')
        section.append(p1)
        return doc
    make_paraHeading = staticmethod(make_paraHeading)

    def test_paraHeading(self):
        self.doTest()

    def make_paraNormal():
        doc, section, styles = RTFTestCase.initializeDoc()
        p1 = Paragraph(styles.ParagraphStyles.Heading1)
        p1.append('Heading 1')
        section.append(p1)
        p2 = Paragraph(styles.ParagraphStyles.Normal)
        p2.append(
            'In this case we have used two styles. The first paragraph is '
            'marked with the Heading1 style, and this one is marked with the '
            'Normal style.')
        section.append(p2)
        return doc
    make_paraNormal = staticmethod(make_paraNormal)

    def test_paraNormal(self):
        self.doTest()

    def make_paraDefaultPreviousStyle():
        doc, section, styles = RTFTestCase.initializeDoc()
        p1 = Paragraph(styles.ParagraphStyles.Heading1)
        p1.append('Heading 1')
        section.append(p1)
        p2 = Paragraph(styles.ParagraphStyles.Normal)
        p2.append(
            'In this case we have used two styles. The first paragraph is '
            'marked with the Heading1 style, and this one is marked with the '
            'Normal style.')
        section.append(p2)
        p3 = Paragraph()
        p3.append(
            'Notice that after changing the style of the paragraph to Normal '
            '(in the previous paragraph), all subsequent paragraphs have '
            'that style automatically. This saves typing and is actually the '
            'default native behaviour for RTF documents.')
        section.append(p3)
        return doc
    make_paraDefaultPreviousStyle = staticmethod(make_paraDefaultPreviousStyle)

    def test_paraDefaultPreviousStyle(self):
        self.doTest()

    def make_paraTabs():
        doc, section, styles = RTFTestCase.initializeDoc()
        p = Paragraph()
        p.append(
            'The paragraph itself can also be overridden in lots of ways: '
            'tabs, borders, alignment, etc., can all be modified either in '
            'the style or as an override during the creation of the '
            'paragraph. This is demonstrated below with custom tab widths '
            'and embedded carriage returns (i.e., new line markers that do '
            'not cause a paragraph break).')
        section.append(p)
        tabs = [
            TabPropertySet(width=TabPropertySet.DEFAULT_WIDTH),
            TabPropertySet(width=TabPropertySet.DEFAULT_WIDTH * 2),
            TabPropertySet(width=TabPropertySet.DEFAULT_WIDTH)]
        para_props = ParagraphPropertySet(tabs=tabs)
        p = Paragraph(styles.ParagraphStyles.Normal, para_props)
        p.append(
            'Phrase at Left Tab', TAB, 'Middle Phrase One', TAB, 'Right Phrase',
            LINE, 'Second Left Phrase', TAB, 'Middle Phrase Two', TAB,
            'Another Right Phrase')
        section.append(p)
        return doc
    make_paraTabs = staticmethod(make_paraTabs)

    def test_paraTabs(self):
        self.doTest()

    def make_paraTabLeaders():
        doc, section, styles = RTFTestCase.initializeDoc()
        section.append(
            'The alignment of tabs and style can also be controlled. The '
            'following demonstrates how to use flush right tabs and the '
            'supported leaders.')
        def _makePara(name):
            tabs = TabPropertySet(
                section.TwipsToRightMargin(),
                alignment=TabPropertySet.RIGHT,
                leader=getattr(TabPropertySet, name.upper().replace(' ', '_')))
            para_props = ParagraphPropertySet(tabs=[tabs])
            return Paragraph(styles.ParagraphStyles.Normal, para_props)
        for name in ['Dots', 'Hyphens', 'Underline', 'Thick Line',
                     'Equal Sign']:
            p = _makePara(name)
            p.append('Before %s' % name, TAB, 'After %s' % name)
            section.append(p)
        return doc
    make_paraTabLeaders = staticmethod(make_paraTabLeaders)

    def test_paraTabLeaders(self):
        self.doTest()

    def make_paraIndents():
        doc, section, styles = RTFTestCase.initializeDoc()
        section.append(
            'The paragraphs below demonstrate the flexibility , the following is all at the '
            'same indent level and the one after it has the first line at a '
            'different indent to the rest. The third has the first line '
            'going in the other direction and is also separated by a page '
            'break. Note that the FirstLineIndent is defined as being the '
            'difference from the LeftIndent.')
        creditURL = 'http://www.shakespeare-online.com/plots/1kh4ps.html'
        section.append('(Paragraph text from %s.)' % creditURL)

        sampleParagraph = """The play opens one year after the death of Richard
            II, and King Henry is making plans for a crusade to the
            Holy Land to cleanse himself of the guilt he feels over the
            usurpation of Richard's crown. But the crusade must be postponed
            when Henry learns that Welsh rebels, led by Owen Glendower, have
            defeated and captured Mortimer. Although the brave Henry Percy,
            nicknamed Hotspur, has quashed much of the uprising, there is still
            much trouble in Scotland. King Henry has a deep admiration for
            Hotspur and he longs for his own son, Prince Hal, to
            display some of Hotspur's noble qualities. Hal is more comfortable
            in a tavern than on the battlefield, and he spends his days
            carousing with riff-raff in London. But King Henry also has his
            problems with the headstrong Hotspur, who refuses to turn over his
            prisoners to the state as he has been so ordered.
            Westmoreland tells King Henry that Hotspur has many of
            the traits of his uncle, Thomas Percy, the Earl of Worcester, and
            defying authority runs in the family."""
        sampleParagraph = re.sub('\s+', ' ', sampleParagraph)
        para_props = ParagraphPropertySet()
        para_props.SetLeftIndent(TabPropertySet.DEFAULT_WIDTH *  3)
        p = Paragraph(styles.ParagraphStyles.Normal, para_props)
        p.append(sampleParagraph)
        section.append(p)

        para_props = ParagraphPropertySet()
        para_props.SetFirstLineIndent(TabPropertySet.DEFAULT_WIDTH * -2)
        para_props.SetLeftIndent(TabPropertySet.DEFAULT_WIDTH *  3)
        p = Paragraph(styles.ParagraphStyles.Normal, para_props)
        p.append(sampleParagraph)
        section.append(p)

        para_props = ParagraphPropertySet()
        para_props.SetFirstLineIndent(TabPropertySet.DEFAULT_WIDTH)
        para_props.SetLeftIndent(TabPropertySet.DEFAULT_WIDTH)
        p = Paragraph(styles.ParagraphStyles.Normal, para_props)
        p.append(sampleParagraph)
        section.append(p)
        return doc
    make_paraIndents = staticmethod(make_paraIndents)

    def test_paraIndents(self):
        self.doTest()

