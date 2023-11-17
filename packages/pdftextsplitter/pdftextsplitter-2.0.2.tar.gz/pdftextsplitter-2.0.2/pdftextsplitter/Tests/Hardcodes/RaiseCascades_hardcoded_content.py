import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_RaiseCascades() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document RaiseCascades
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
    thisalinea.texttitle = "RaiseCascades"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. 1. We moeten toch iets zeggen. Why, my dear, you must know, Mrs. Long says that Netherfield "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1 Opsommingen en hoofdstuktitels in cascade"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. 1. We moeten toch iets zeggen. Why, my dear, you must know, Mrs. Long says that Netherfield "
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
    thisalinea.texttitle = "1. We moeten toch iets zeggen. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 2
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. We moeten toch iets zeggen. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. We moeten toch iets zeggen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. en dan nog wat. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 3
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. en dan nog wat. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. en dan nog wat.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.0.1 dit zou dus een laag tussenkopje moeten zijn"
    thisalinea.titlefontsize = "11.95519999999999"
    thisalinea.nativeID = 4
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("with Mr. Morris immediately; that he is to take possession before Michaelmas, and")
    thisalinea.textcontent.append("some of his servants are to be in the house by the end of next week. Not all that Mrs.")
    alineas.append(thisalinea)

    return alineas
