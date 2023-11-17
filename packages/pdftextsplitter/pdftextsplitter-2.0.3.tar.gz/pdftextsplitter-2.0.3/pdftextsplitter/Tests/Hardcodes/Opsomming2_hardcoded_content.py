import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Opsomming2() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document Opsomming2
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
    thisalinea.texttitle = "Opsomming2"
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
    thisalinea.texttitle = "1 Opsommingen en hoofdstuktitels door elkaar"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. 1. kijken welke titel. gh frh fh dh eh dj ks cj oe ek ej dj ddh "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("with Mr. Morris immediately; that he is to take possession before Michaelmas, and")
    thisalinea.textcontent.append("some of his servants are to be in the house by the end of next week. Not all that Mrs.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1. kijken welke titel. gh frh fh dh eh dj ks cj oe ek ej ..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 2
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. kijken welke titel. gh frh fh dh eh dj ks cj oe ek ej dj ddh dj. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. kijken welke titel. gh frh fh dh eh dj ks cj oe ek ej dj ddh dj.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2. ks djd djs dnd sd kd kd dfj fk dj dk kde kdfj wkdrj ..."
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 3
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. ks djd djs dnd sd kd kd dfj fk dj dk kde kdfj wkdrj kfrnfr ekff ekffj. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. ks djd djs dnd sd kd kd dfj fk dj dk kde kdfj wkdrj kfrnfr ekff ekffj.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1 En nu gaan we nog even een experimentje doen met romeise cijfers:"
    thisalinea.titlefontsize = "14.34620000000001"
    thisalinea.nativeID = 4
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. i. even kijken of dit lukt (subtype of part 2). j. en dan deze ook bekijken. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("with Mr. Morris immediately; that he is to take possession before Michaelmas, and")
    thisalinea.textcontent.append("some of his servants are to be in the house by the end of next week. Not all that Mrs.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "i. even kijken of dit lukt (subtype of part 2). "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 5
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "i. even kijken of dit lukt (subtype of part 2). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i. even kijken of dit lukt (subtype of part 2).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "j. en dan deze ook bekijken. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 6
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "j. en dan deze ook bekijken. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("j. en dan deze ook bekijken.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2 En herhalen met grote Romeinse cijfers"
    thisalinea.titlefontsize = "14.34620000000001"
    thisalinea.nativeID = 7
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week. Not all that Mrs. I. Dit moet dus ook een letter worden. J. Net als deze. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young")
    thisalinea.textcontent.append("man of large fortune from the north of England; that he came down on Monday in a")
    thisalinea.textcontent.append("chaise and four to see the place, and was so much delighted with it, that he agreed")
    thisalinea.textcontent.append("with Mr. Morris immediately; that he is to take possession before Michaelmas, and")
    thisalinea.textcontent.append("some of his servants are to be in the house by the end of next week. Not all that Mrs.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "I. Dit moet dus ook een letter worden. "
    thisalinea.titlefontsize = "9.96259999999998"
    thisalinea.nativeID = 8
    thisalinea.parentID = 7
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "I. Dit moet dus ook een letter worden. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("I. Dit moet dus ook een letter worden.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "J. Net als deze. "
    thisalinea.titlefontsize = "9.962599999999995"
    thisalinea.nativeID = 9
    thisalinea.parentID = 7
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "J. Net als deze. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("J. Net als deze.")
    alineas.append(thisalinea)

    return alineas
