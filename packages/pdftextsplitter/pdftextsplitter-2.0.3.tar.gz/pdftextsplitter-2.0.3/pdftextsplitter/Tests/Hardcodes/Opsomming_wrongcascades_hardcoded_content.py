import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Opsomming_wrongcascades() -> list[textalinea]:
    """
    Some hypothetical situation where enumerations of the same type
    do not get the same cascade level. There is no matching PDF.

    # Parameters: None (everything is hardcoded)
    # Return: list[textalinea] the hardcoded textalineas-array.
    """

    alineas = []

    thisalinea = textalinea()
    thisalinea.textlevel = 0
    thisalinea.texttitle = "Opsomming_wrongcascades"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. 1. kijken welke titel. gh frh fh dh eh dj ks cj oe ek ej dj ddh "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1 Opsommingen"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("with Mr. Morris immediately; that he is to take possession before Michaelmas, and")
    thisalinea.textcontent.append("some of his servants are to be in the house by the end of next week. Not all that Mrs.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "a) even een titeltje zonder dots"
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 2
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "a) even een titeltje zonder dots"
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("a) even een titeltje zonder dots")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "b) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 3
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "b) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("b) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "c) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 4
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "c) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("c) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "d) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 5
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "d) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("d) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "e) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 6
    thisalinea.parentID = 5
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "e) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("e) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 7
    thisalinea.texttitle = "f) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 7
    thisalinea.parentID = 6
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "f) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("f) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 8
    thisalinea.texttitle = "g) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 8
    thisalinea.parentID = 7
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "g) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("g) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 9
    thisalinea.texttitle = "h) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 9
    thisalinea.parentID = 8
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "h) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("h) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 10
    thisalinea.texttitle = "i) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 10
    thisalinea.parentID = 9
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "i) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i) en dan even een stukje met de dots...")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 11
    thisalinea.texttitle = "j) en dan even een stukje met de dots..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 11
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "j) en dan even een stukje met de dots..."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("j) en dan even een stukje met de dots...")
    alineas.append(thisalinea)


    return alineas
