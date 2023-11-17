import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Opsomming_wrongarticles() -> list[textalinea]:
    """
    Some hypothetical situation where enumerations of the same type
    do not get the same cascade level. There is no matching PDF.

    # Parameters: None (everything is hardcoded)
    # Return: list[textalinea] the hardcoded textalineas-array.
    """

    alineas = []

    thisalinea = textalinea()
    thisalinea.textlevel = 0
    thisalinea.texttitle = "Articles with incorrect cascade levels"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "That is not really an issue here."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 1"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "That is not really an issue here."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 1")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "The title with the wrong level"
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 2
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "That is not really an issue here."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("That is not really an issue here.")
    thisalinea.textcontent.append("That is not really an issue here.")
    thisalinea.textcontent.append("That is not really an issue here.")
    alineas.append(thisalinea)

    return alineas

def hardcodedalineas_Opsomming_wrongarticles_corrected() -> list[textalinea]:
    """
    Some hypothetical situation where enumerations of the same type
    do not get the same cascade level. There is no matching PDF.

    # Parameters: None (everything is hardcoded)
    # Return: list[textalinea] the hardcoded textalineas-array.
    """

    alineas = []

    thisalinea = textalinea()
    thisalinea.textlevel = 0
    thisalinea.texttitle = "Articles with incorrect cascade levels"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "That is not really an issue here."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 1"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "That is not really an issue here."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 1 The title with the wrong level"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 2
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "That is not really an issue here."
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("That is not really an issue here.")
    thisalinea.textcontent.append("That is not really an issue here.")
    thisalinea.textcontent.append("That is not really an issue here.")
    alineas.append(thisalinea)

    return alineas
