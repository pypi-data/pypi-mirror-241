import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Leeswijzer() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document Leeswijzer
    It is generated with the printcode()-functions of textsplitter & textalinea
    and it is supposed to be used only after a complete document analysis
    the outcome of this analysis (this script) can then be efficiently used
    for running regression-tests in the future.

    # Parameters: None (everything is hardcoded)
    # Return: list[textalinea] the hardcoded textalineas-array.
    """

    alineas = []

    thisalinea = textalinea()
    thisalinea.textlevel = 0
    thisalinea.texttitle = "Leeswijzer"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "They attacked him in various ways–with barefaced questions, ingenious suppositions, and distant surmises; but he eluded the skill of them all, and they were at last obliged to accept the second-hand intelligence of their neighbour, Lady Lucas. Her report was Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed Why, my dear, you must know, Mrs. Long says that "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Dit wordt een documenttitel"
    thisalinea.titlefontsize = "28.0"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "They attacked him in various ways–with barefaced questions, ingenious suppositions, and distant surmises; but he eluded the skill of them all, and they were at last obliged to accept the second-hand intelligence of their neighbour, Lady Lucas. Her report was "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("They attacked him in various ways–with barefaced questions, ingenious suppositions,")
    thisalinea.textcontent.append("and distant surmises; but he eluded the skill of them all, and they were at last obliged")
    thisalinea.textcontent.append("to accept the second-hand intelligence of their neighbour, Lady Lucas. Her report was")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Dit moet een hoofdstuk voorstellen"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 2
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Dit wordt straks een sectie"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Dit zou uiteindelijk een subsectie moeten zijn"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 4
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "En tot slot een subsubsectie"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 5
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed En uiteindelijk een vetgedrukte normale tekst. Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("En uiteindelijk een vetgedrukte normale tekst.")
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("with Mr. Morris immediately; that he is to take possession before Michaelmas, and")
    thisalinea.textcontent.append("some of his servants are to be in the house by the end of next week. Not all that Mrs.")
    thisalinea.textcontent.append("Bennet, however, with the assistance of her five daughters, could ask on the subject,")
    thisalinea.textcontent.append("was sufficient to draw from her husband any satisfactory description of Mr. Bingley.")
    thisalinea.textcontent.append("")
    alineas.append(thisalinea)

    return alineas
