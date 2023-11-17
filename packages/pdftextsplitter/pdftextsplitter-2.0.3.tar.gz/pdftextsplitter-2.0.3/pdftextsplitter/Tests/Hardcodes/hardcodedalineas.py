import sys
sys.path.insert(1, '../../')

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_SplitDoc(option: str) -> list[textalinea]:
    """
    Function to load hard-coded textalinea-elements
    that you want to find in the SplitDoc-result.

    # Parameters:
    option: str: tells you which library for reading PDF's you ask the content for: pdfminer or pymupdf.
    # Return: list[textalinea]: those textalinea elements:
    """
    
    # --------------------------------------------------------
    
    if (option=="pymupdf"):

        alineas = []

        thisalinea = textalinea()
        thisalinea.textlevel = 0
        thisalinea.texttitle = "SplitDoc"
        thisalinea.titlefontsize = "1000.0"
        thisalinea.nativeID = 0
        thisalinea.parentID = -1
        thisalinea.alineatype = texttype.TITLE
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "1 Let’s kick-of test-driven development 2 1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.3 Methods again . . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "First basic test Document"
        thisalinea.titlefontsize = "17.21540069580078"
        thisalinea.nativeID = 1
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "Unit Data en Innovatie"
        thisalinea.titlefontsize = "11.9552001953125"
        thisalinea.nativeID = 2
        thisalinea.parentID = 1
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "of March 2023"
        thisalinea.titlefontsize = "11.9552001953125"
        thisalinea.nativeID = 3
        thisalinea.parentID = 1
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Contents"
        thisalinea.titlefontsize = "24.787099838256836"
        thisalinea.nativeID = 4
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "1 Let’s kick-of test-driven development 2 1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.3 Methods again . . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("1 Let’s kick-of test-driven development")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.3 Methods again")
        thisalinea.textcontent.append(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.4 One more section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("3")
        thisalinea.textcontent.append("2 A new chapter starts now")
        thisalinea.textcontent.append("4")
        thisalinea.textcontent.append("2.1 A new section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("4")
        thisalinea.textcontent.append("2.1.1 Nice subsection . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("4")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "1 Let’s kick-of test-driven development"
        thisalinea.titlefontsize = "24.787099838256836"
        thisalinea.nativeID = 5
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 2
        thisalinea.summary = "We start with some general text about the chapter. with a line-break embedded in it. This is a small test for text extraction. And here is some more text. With a line break and other stuf. Lets add some whitespaces: And some text. With some text... "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("We start with some general text about the chapter.")
        thisalinea.textcontent.append("with a line-break embedded in it.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.1 Introduction"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 6
        thisalinea.parentID = 5
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "This is a small test for text extraction. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("This is a small test for text extraction.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.2 Methods"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 7
        thisalinea.parentID = 5
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "And here is some more text. With a line break and other stuf. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("And here is some more text.")
        thisalinea.textcontent.append("With a line break and other stuf.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.3 Methods again"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 8
        thisalinea.parentID = 5
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 2
        thisalinea.summary = "Lets add some whitespaces: And some text. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Lets add some whitespaces:")
        thisalinea.textcontent.append("And some text.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.4 One more section"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 9
        thisalinea.parentID = 5
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 3
        thisalinea.summary = "With some text... "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("With some text...")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "2 A new chapter starts now"
        thisalinea.titlefontsize = "24.787099838256836"
        thisalinea.nativeID = 10
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 3
        thisalinea.summary = "Now comes some extra text. With a line break. Lets give a splendid additional story. with a beautiful subsection embedded in it. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Now comes some extra text.")
        thisalinea.textcontent.append("With a line break.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "2.1 A new section"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 11
        thisalinea.parentID = 10
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Lets give a splendid additional story. with a beautiful subsection embedded in it. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Lets give a splendid additional story.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "2.1.1 Nice subsection"
        thisalinea.titlefontsize = "11.9552001953125"
        thisalinea.nativeID = 12
        thisalinea.parentID = 11
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "with a beautiful subsection embedded in it. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("with a beautiful subsection embedded in it.")
        alineas.append(thisalinea)

        return alineas

    else:

        alineas = []

        thisalinea = textalinea()
        thisalinea.textlevel = 0
        thisalinea.texttitle = "SplitDoc"
        thisalinea.titlefontsize = "1000.0"
        thisalinea.nativeID = 0
        thisalinea.parentID = -1
        thisalinea.alineatype = texttype.TITLE
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "2 1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.3 Methods again . . . . . . . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "First basic test Document"
        thisalinea.titlefontsize = "17.215400000000045"
        thisalinea.nativeID = 1
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "Unit Data en Innovatie 20th of March 2023"
        thisalinea.titlefontsize = "11.95519999999999"
        thisalinea.nativeID = 2
        thisalinea.parentID = 1
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Contents"
        thisalinea.titlefontsize = "24.78710000000001"
        thisalinea.nativeID = 3
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "2 1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.3 Methods again . . . . . . . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1 Let’s kick-of test-driven development"
        thisalinea.titlefontsize = "9.962600000000066"
        thisalinea.nativeID = 4
        thisalinea.parentID = 3
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "2 1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.3 Methods again . . . . . . . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2")
        thisalinea.textcontent.append("1.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2")
        thisalinea.textcontent.append("1.3 Methods again . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2")
        thisalinea.textcontent.append("1.4 One more section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "2 A new chapter starts now"
        thisalinea.titlefontsize = "9.962600000000009"
        thisalinea.nativeID = 5
        thisalinea.parentID = 3
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "4 2.1 A new section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.1.1 Nice subsection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("4")
        thisalinea.textcontent.append("2.1 A new section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4")
        thisalinea.textcontent.append("2.1.1 Nice subsection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "1 Let’s kick-of test-driven development"
        thisalinea.titlefontsize = "24.78710000000001"
        thisalinea.nativeID = 6
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 2
        thisalinea.summary = "We start with some general text about the chapter. with a line-break embedded in it. This is a small test for text extraction. And here is some more text. With a line break and other stuf. Lets add some whitespaces: And some text. With some text... "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("We start with some general text about the chapter.")
        thisalinea.textcontent.append("with a line-break embedded in it.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.1 Introduction"
        thisalinea.titlefontsize = "14.34620000000001"
        thisalinea.nativeID = 7
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "This is a small test for text extraction. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("This is a small test for text extraction.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.2 Methods"
        thisalinea.titlefontsize = "14.34620000000001"
        thisalinea.nativeID = 8
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "And here is some more text. With a line break and other stuf. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("And here is some more text.")
        thisalinea.textcontent.append("With a line break and other stuf.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.3 Methods again"
        thisalinea.titlefontsize = "14.34620000000001"
        thisalinea.nativeID = 9
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 2
        thisalinea.summary = "Lets add some whitespaces: And some text. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Lets add some whitespaces:")
        thisalinea.textcontent.append("And some text.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.4 One more section"
        thisalinea.titlefontsize = "14.346200000000067"
        thisalinea.nativeID = 10
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 3
        thisalinea.summary = "With some text... "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("With some text...")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "2 A new chapter starts now"
        thisalinea.titlefontsize = "24.78710000000001"
        thisalinea.nativeID = 11
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 3
        thisalinea.summary = "Now comes some extra text. With a line break. Lets give a splendid additional story. with a beautiful subsection embedded in it. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Now comes some extra text.")
        thisalinea.textcontent.append("With a line break.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "2.1 A new section"
        thisalinea.titlefontsize = "14.34620000000001"
        thisalinea.nativeID = 12
        thisalinea.parentID = 11
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Lets give a splendid additional story. with a beautiful subsection embedded in it. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Lets give a splendid additional story.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "2.1.1 Nice subsection"
        thisalinea.titlefontsize = "11.95519999999999"
        thisalinea.nativeID = 13
        thisalinea.parentID = 12
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "with a beautiful subsection embedded in it. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("with a beautiful subsection embedded in it.")
        alineas.append(thisalinea)

        return alineas

def hardcodedalineas_TestTex(option: str) -> list[textalinea]:
    """
    Function to load hard-coded textalinea-elements
    that you want to find in the TestTex-result.

    # Parameters:
    option: str: tells you which library for reading PDF's you ask the content for: pdfminer or pymupdf.
    # Return: list[textalinea]: those textalinea elements:
    """

    # --------------------------------------------------------
    
    if (option=="pymupdf"):

        alineas = []

        thisalinea = textalinea()
        thisalinea.textlevel = 0
        thisalinea.texttitle = "TestTex"
        thisalinea.titlefontsize = "1000.0"
        thisalinea.nativeID = 0
        thisalinea.parentID = -1
        thisalinea.alineatype = texttype.TITLE
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "1 Eerste hoofdstuk 2 1.1 Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2.1 Zelfs met een subsectie erin!!! . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Test title"
        thisalinea.titlefontsize = "17.21540069580078"
        thisalinea.nativeID = 1
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "Remco van Groesen Ministerie van Infrastructuur en Waterstaat March 23, 2023"
        thisalinea.titlefontsize = "11.9552001953125"
        thisalinea.nativeID = 2
        thisalinea.parentID = 1
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Contents"
        thisalinea.titlefontsize = "24.787099838256836"
        thisalinea.nativeID = 3
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "1 Eerste hoofdstuk 2 1.1 Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2.1 Zelfs met een subsectie erin!!! . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("1")
        thisalinea.textcontent.append("Eerste hoofdstuk")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.1")
        thisalinea.textcontent.append("Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.2")
        thisalinea.textcontent.append("En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.2.1")
        thisalinea.textcontent.append("Zelfs met een subsectie erin!!! . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("Tweede hoofdstuk")
        thisalinea.textcontent.append("3")
        thisalinea.textcontent.append("2.1")
        thisalinea.textcontent.append("Dit is alles wat in het tweede hoofdstuk staat . . . . . . . . . . . . . . . . . . . . . .")
        thisalinea.textcontent.append("3")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Chapter 1 Eerste hoofdstuk"
        thisalinea.titlefontsize = "20.662500381469727"
        thisalinea.nativeID = 4
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 2
        thisalinea.summary = "Hier staat een inleidende tekst. Hier staat over het algemeen een hele hoop tekst Wow, nog een sectie???? Dit had ik niet verwacht. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Hier staat een inleidende tekst.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.1 Eerste sectie in het eerste hoofdstuk."
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 5
        thisalinea.parentID = 4
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Hier staat over het algemeen een hele hoop tekst "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Hier staat over het algemeen een hele hoop tekst")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.2 En nog een sectie"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 6
        thisalinea.parentID = 4
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "Wow, nog een sectie???? Dit had ik niet verwacht. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Wow, nog een sectie????")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "1.2.1 Zelfs met een subsectie erin!!!"
        thisalinea.titlefontsize = "11.9552001953125"
        thisalinea.nativeID = 7
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Dit had ik niet verwacht. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Dit had ik niet verwacht.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Chapter 2 Tweede hoofdstuk"
        thisalinea.titlefontsize = "20.662500381469727"
        thisalinea.nativeID = 8
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 3
        thisalinea.summary = "Het tweede hoofdstuk gaat een stuk korter zijn dan de eerste Dit is alles wat in het tweede hoofdstuk staat. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Het tweede hoofdstuk gaat een stuk korter zijn dan de eerste")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "2.1 Dit is alles wat in het tweede hoofdstuk staat"
        thisalinea.titlefontsize = "14.346199989318848"
        thisalinea.nativeID = 9
        thisalinea.parentID = 8
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Dit is alles wat in het tweede hoofdstuk staat. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Dit is alles wat in het tweede hoofdstuk staat.")
        alineas.append(thisalinea)

        return alineas

    else:

        alineas = []

        thisalinea = textalinea()
        thisalinea.textlevel = 0
        thisalinea.texttitle = "TestTex"
        thisalinea.titlefontsize = "1000.0"
        thisalinea.nativeID = 0
        thisalinea.parentID = -1
        thisalinea.alineatype = texttype.TITLE
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "2 1.1 Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2.1 Zelfs met een subsectie erin!!! . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Test title"
        thisalinea.titlefontsize = "17.21539999999993"
        thisalinea.nativeID = 1
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "Remco van Groesen Ministerie van Infrastructuur en Waterstaat March 23, 2023"
        thisalinea.titlefontsize = "11.95519999999999"
        thisalinea.nativeID = 2
        thisalinea.parentID = 1
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = ""
        thisalinea.sum_CanbeEmpty = True
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Contents"
        thisalinea.titlefontsize = "24.78710000000001"
        thisalinea.nativeID = 3
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "2 1.1 Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2.1 Zelfs met een subsectie erin!!! . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1 Eerste hoofdstuk"
        thisalinea.titlefontsize = "9.962600000000066"
        thisalinea.nativeID = 4
        thisalinea.parentID = 3
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "2 1.1 Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2.1 Zelfs met een subsectie erin!!! . . . . . . . . . . . . . . "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("2")
        thisalinea.textcontent.append("1.1 Eerste sectie in het eerste hoofdstuk. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2")
        thisalinea.textcontent.append("1.2 En nog een sectie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2")
        thisalinea.textcontent.append("1.2.1 Zelfs met een subsectie erin!!! . . . . . . . . . . . . . . . . . . . . . . . . . . . 2")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "2 Tweede hoofdstuk"
        thisalinea.titlefontsize = "9.962600000000066"
        thisalinea.nativeID = 5
        thisalinea.parentID = 3
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "3 2.1 Dit is alles wat in het tweede hoofdstuk staat . . . . . . . . . . . . . . . . . . . . . . 3 "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("3")
        thisalinea.textcontent.append("2.1 Dit is alles wat in het tweede hoofdstuk staat . . . . . . . . . . . . . . . . . . . . . . 3")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Chapter 1 Eerste hoofdstuk"
        thisalinea.titlefontsize = "20.662500000000023"
        thisalinea.nativeID = 6
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 2
        thisalinea.summary = "Hier staat een inleidende tekst. Hier staat over het algemeen een hele hoop tekst Wow, nog een sectie???? Dit had ik niet verwacht. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Hier staat een inleidende tekst.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.1 Eerste sectie in het eerste hoofdstuk."
        thisalinea.titlefontsize = "14.346200000000067"
        thisalinea.nativeID = 7
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Hier staat over het algemeen een hele hoop tekst "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Hier staat over het algemeen een hele hoop tekst")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "1.2 En nog een sectie"
        thisalinea.titlefontsize = "14.34620000000001"
        thisalinea.nativeID = 8
        thisalinea.parentID = 6
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 1
        thisalinea.summary = "Wow, nog een sectie???? Dit had ik niet verwacht. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Wow, nog een sectie????")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 3
        thisalinea.texttitle = "1.2.1 Zelfs met een subsectie erin!!!"
        thisalinea.titlefontsize = "11.95519999999999"
        thisalinea.nativeID = 9
        thisalinea.parentID = 8
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Dit had ik niet verwacht. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Dit had ik niet verwacht.")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 1
        thisalinea.texttitle = "Chapter 2 Tweede hoofdstuk"
        thisalinea.titlefontsize = "20.662500000000023"
        thisalinea.nativeID = 10
        thisalinea.parentID = 0
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 3
        thisalinea.summary = "Het tweede hoofdstuk gaat een stuk korter zijn dan de eerste Dit is alles wat in het tweede hoofdstuk staat. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Het tweede hoofdstuk gaat een stuk korter zijn dan de eerste")
        alineas.append(thisalinea)

        thisalinea = textalinea()
        thisalinea.textlevel = 2
        thisalinea.texttitle = "2.1 Dit is alles wat in het tweede hoofdstuk staat"
        thisalinea.titlefontsize = "14.346200000000067"
        thisalinea.nativeID = 11
        thisalinea.parentID = 10
        thisalinea.alineatype = texttype.HEADLINES
        thisalinea.enumtype = enum_type.UNKNOWN
        thisalinea.horizontal_ordering = 0
        thisalinea.summary = "Dit is alles wat in het tweede hoofdstuk staat. "
        thisalinea.sum_CanbeEmpty = False
        thisalinea.textcontent.clear()
        thisalinea.textcontent.append("Dit is alles wat in het tweede hoofdstuk staat.")
        alineas.append(thisalinea)

        return alineas
