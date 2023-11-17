import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Romans() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document Romans
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
    thisalinea.texttitle = "Romans"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "h) hier beginnen we met een opsomming met h. i) en dan met romeinse cijfers ii) en dan nogmaals romeins. j) en dan ten slotte weer een letter. h) dit moet opnieuw dus weer een opsomming voorstellen i) en dit moet dan dus ook een gewone letter zijn. j) en dan de hele rotriedel nog een keer. H. En deze tekst over een h moet dan dus weer helemaal anders zijn I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers II. tsja en dan weet je helemaal niet meer wat je wilt typen J. geen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1 Kleine letters"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "h) hier beginnen we met een opsomming met h. i) en dan met romeinse cijfers ii) en dan nogmaals romeins. j) en dan ten slotte weer een letter. h) dit moet opnieuw dus weer een opsomming voorstellen i) en dit moet dan dus ook een gewone letter zijn. j) en dan de hele rotriedel nog een keer. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1 romeinse cijfers"
    thisalinea.titlefontsize = "14.346200000000067"
    thisalinea.nativeID = 2
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "h) hier beginnen we met een opsomming met h. i) en dan met romeinse cijfers ii) en dan nogmaals romeins. j) en dan ten slotte weer een letter. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "h) hier beginnen we met een opsomming met h. "
    thisalinea.titlefontsize = "9.962600000000066"
    thisalinea.nativeID = 3
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "h) hier beginnen we met een opsomming met h. i) en dan met romeinse cijfers ii) en dan nogmaals romeins. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("h) hier beginnen we met een opsomming met h.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "i) en dan met romeinse cijfers "
    thisalinea.titlefontsize = "9.962600000000066"
    thisalinea.nativeID = 4
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "i) en dan met romeinse cijfers "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i) en dan met romeinse cijfers")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "ii) en dan nogmaals romeins. "
    thisalinea.titlefontsize = "9.962599999999952"
    thisalinea.nativeID = 5
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "ii) en dan nogmaals romeins. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ii) en dan nogmaals romeins.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "j) en dan ten slotte weer een letter. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 6
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "j) en dan ten slotte weer een letter. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("j) en dan ten slotte weer een letter.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2 gewone letters"
    thisalinea.titlefontsize = "14.34620000000001"
    thisalinea.nativeID = 7
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "h) dit moet opnieuw dus weer een opsomming voorstellen i) en dit moet dan dus ook een gewone letter zijn. j) en dan de hele rotriedel nog een keer. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "h) dit moet opnieuw dus weer een opsomming voorstellen "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 8
    thisalinea.parentID = 7
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "h) dit moet opnieuw dus weer een opsomming voorstellen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("h) dit moet opnieuw dus weer een opsomming voorstellen")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i) en dit moet dan dus ook een gewone letter zijn. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 9
    thisalinea.parentID = 7
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "i) en dit moet dan dus ook een gewone letter zijn. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i) en dit moet dan dus ook een gewone letter zijn.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "j) en dan de hele rotriedel nog een keer. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 10
    thisalinea.parentID = 7
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "j) en dan de hele rotriedel nog een keer. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("j) en dan de hele rotriedel nog een keer.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2 Hoofdletters"
    thisalinea.titlefontsize = "24.78710000000001"
    thisalinea.nativeID = 11
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "H. En deze tekst over een h moet dan dus weer helemaal anders zijn I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers II. tsja en dan weet je helemaal niet meer wat je wilt typen J. geen idee wat we hier dan weer moeten typen H. hier wordt ik het wel echt een beetje zat I. dus type ik maar wat over Mr. Bean. J. en dan over zijn vertrouwde teddybeer. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.1 romeinse cijfers"
    thisalinea.titlefontsize = "14.346200000000067"
    thisalinea.nativeID = 12
    thisalinea.parentID = 11
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "H. En deze tekst over een h moet dan dus weer helemaal anders zijn I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers II. tsja en dan weet je helemaal niet meer wat je wilt typen J. geen idee wat we hier dan weer moeten typen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "H. En deze tekst over een h moet dan dus weer helemaal anders zijn "
    thisalinea.titlefontsize = "9.962600000000066"
    thisalinea.nativeID = 13
    thisalinea.parentID = 12
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "H. En deze tekst over een h moet dan dus weer helemaal anders zijn I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers II. tsja en dan weet je helemaal niet meer wat je wilt typen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("H. En deze tekst over een h moet dan dus weer helemaal anders zijn")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers "
    thisalinea.titlefontsize = "9.962600000000066"
    thisalinea.nativeID = 14
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("I. en dan doen we nog weer een hoop gedoe met met romeinse cijfers")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "II. tsja en dan weet je helemaal niet meer wat je wilt typen "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 15
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "II. tsja en dan weet je helemaal niet meer wat je wilt typen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("II. tsja en dan weet je helemaal niet meer wat je wilt typen")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "J. geen idee wat we hier dan weer moeten typen "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 16
    thisalinea.parentID = 12
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "J. geen idee wat we hier dan weer moeten typen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("J. geen idee wat we hier dan weer moeten typen")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.2 gewone letters"
    thisalinea.titlefontsize = "14.34620000000001"
    thisalinea.nativeID = 17
    thisalinea.parentID = 11
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "H. hier wordt ik het wel echt een beetje zat I. dus type ik maar wat over Mr. Bean. J. en dan over zijn vertrouwde teddybeer. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "H. hier wordt ik het wel echt een beetje zat "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 18
    thisalinea.parentID = 17
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "H. hier wordt ik het wel echt een beetje zat "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("H. hier wordt ik het wel echt een beetje zat")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "I. dus type ik maar wat over Mr. Bean. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 19
    thisalinea.parentID = 17
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "I. dus type ik maar wat over Mr. Bean. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("I. dus type ik maar wat over Mr. Bean.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "J. en dan over zijn vertrouwde teddybeer. "
    thisalinea.titlefontsize = "9.962600000000009"
    thisalinea.nativeID = 20
    thisalinea.parentID = 17
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "J. en dan over zijn vertrouwde teddybeer. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("J. en dan over zijn vertrouwde teddybeer.")
    alineas.append(thisalinea)

    return alineas
