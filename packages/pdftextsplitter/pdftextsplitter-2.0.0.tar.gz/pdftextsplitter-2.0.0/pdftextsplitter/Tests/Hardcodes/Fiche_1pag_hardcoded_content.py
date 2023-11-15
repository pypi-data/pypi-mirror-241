import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Fiche_1pag() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document Fiche_1pag
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
    thisalinea.texttitle = "Fiche_1pag"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Fiche 1: Wijziging verordeningen betreffende instant payments in euro Verordening van het Europees Parlement en de Raad tot wijziging van Verordeningen (EU) nr. 260/2012 en (EU) 2021/1230 wat betreft instantovermakingen in euro 26 oktober 2022 COM (2022) 546 https://eur-lex.europa.eu/legal- content/NL/TXT/?uri=CELEX%3A52022PC0546&qid=1669146250363 SWD (2022) 546 en SEC(2022)546 Raad Economische en Financiële Zaken Ministerie van Financiën Artikel 114 Verdrag betreffende de werking van de Europese Unie (VWEU) Gekwalificeerde meerderheid Medebeslissing In september 2020 publiceerde de Europese Commissie (hierna: Commissie) haar “Retail Payments Strategy1”. Deze strategie beoogt het bevorderen van het Europese retailbetalingsverkeer door, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Fiche 1: Wijziging verordeningen betreffende instant payments in euro")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. Algemene gegevens"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Verordening van het Europees Parlement en de Raad tot wijziging van Verordeningen (EU) nr. 260/2012 en (EU) 2021/1230 wat betreft instantovermakingen in euro 26 oktober 2022 COM (2022) 546 https://eur-lex.europa.eu/legal- content/NL/TXT/?uri=CELEX%3A52022PC0546&qid=1669146250363 SWD (2022) 546 en SEC(2022)546 Raad Economische en Financiële Zaken Ministerie van Financiën Artikel 114 Verdrag betreffende de werking van de Europese Unie (VWEU) Gekwalificeerde meerderheid Medebeslissing "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "a) Titel voorstel"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 2
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Verordening van het Europees Parlement en de Raad tot wijziging van Verordeningen (EU) nr. 260/2012 en (EU) 2021/1230 wat betreft instantovermakingen in euro "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Verordening van het Europees Parlement en de Raad tot wijziging van Verordeningen (EU) nr.")
    thisalinea.textcontent.append("260/2012 en (EU) 2021/1230 wat betreft instantovermakingen in euro")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "b) Datum ontvangst Commissiedocument"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 3
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "26 oktober 2022 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("26 oktober 2022")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "c) Nr. Commissiedocument"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 4
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "COM (2022) 546 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("COM (2022) 546")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "d) EUR-Lex"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 5
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "https://eur-lex.europa.eu/legal- content/NL/TXT/?uri=CELEX%3A52022PC0546&qid=1669146250363 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("https://eur-lex.europa.eu/legal-")
    thisalinea.textcontent.append("content/NL/TXT/?uri=CELEX%3A52022PC0546&qid=1669146250363")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "e) Nr. impact assessment Commissie en Opinie Raad voor Regelgevingstoetsing"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 6
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "SWD (2022) 546 en SEC(2022)546 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("SWD (2022) 546 en SEC(2022)546")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "f) Behandelingstraject Raad"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 7
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Raad Economische en Financiële Zaken "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Raad Economische en Financiële Zaken")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "g) Eerstverantwoordelijk ministerie"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 8
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "Ministerie van Financiën "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Ministerie van Financiën")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "h) Rechtsbasis"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 9
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Artikel 114 Verdrag betreffende de werking van de Europese Unie (VWEU) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Artikel 114 Verdrag betreffende de werking van de Europese Unie (VWEU)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "i) Besluitvormingsprocedure Raad"
    thisalinea.titlefontsize = "8.999328999999989"
    thisalinea.nativeID = 10
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "Gekwalificeerde meerderheid "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Gekwalificeerde meerderheid")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "j) Rol Europees Parlement"
    thisalinea.titlefontsize = "8.999329000000017"
    thisalinea.nativeID = 11
    thisalinea.parentID = 1
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "Medebeslissing "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Medebeslissing")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. Essentie voorstel"
    thisalinea.titlefontsize = "8.999329000000017"
    thisalinea.nativeID = 12
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "In september 2020 publiceerde de Europese Commissie (hierna: Commissie) haar “Retail Payments Strategy1”. Deze strategie beoogt het bevorderen van het Europese retailbetalingsverkeer door, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "a) Inhoud voorstel"
    thisalinea.titlefontsize = "8.999329000000017"
    thisalinea.nativeID = 13
    thisalinea.parentID = 12
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "In september 2020 publiceerde de Europese Commissie (hierna: Commissie) haar “Retail Payments Strategy1”. Deze strategie beoogt het bevorderen van het Europese retailbetalingsverkeer door, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In september 2020 publiceerde de Europese Commissie (hierna: Commissie) haar “Retail Payments")
    thisalinea.textcontent.append("Strategy1”. Deze strategie beoogt het bevorderen van het Europese retailbetalingsverkeer door,")
    alineas.append(thisalinea)

    return alineas
