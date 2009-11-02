from rtfng.utils import RTFTestCase
from rtfng.Elements import Document

from rtfng.document.base import RawCode
from rtfng.document.paragraph import Paragraph
from rtfng.document.section import Section
from rtfng.object.picture import Image

class PictureTestCase(RTFTestCase):
    
    def make_pictures():
        doc, section, styles = RTFTestCase.initializeDoc()

        # text can be added directly to the section a paragraph object is create as needed
        section.append( 'Image Example 1' )

        section.append( 'You can add images in one of two ways, either converting the '
                        'image each and every time like;' )

        image = Image( 'examples/image.jpg' )
        section.append( Paragraph( image ) )

        section.append( 'Or you can use the image object to convert the image and then '
                        'save it to a raw code element that can be included later.' )

        # Test RawCode -- split into separate test?
        rawCodeDecl = image.ToRawCode('TEST_IMAGE')
        assert rawCodeDecl.startswith('TEST_IMAGE = RawCode( """')
        assert rawCodeDecl.endswith('""" )')
        
        rawCode = RawCode(image.Data)
        section.append(rawCode)
        section.append('The above picture was displayed from a RawCode object without a Paragraph wrapper.')

        section.append( 'Here are some png files' )
        for f in [ 'examples/img1.png',
                   'examples/img2.png',
                   'examples/img3.png',
                   'examples/img4.png' ] :
            section.append( Paragraph( Image( f ) ) )

        return doc
    make_pictures = staticmethod(make_pictures)

    def test_pictures(self):
        self.doTest()



