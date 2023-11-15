import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_AI_Impact() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document AI_Impact
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
    thisalinea.texttitle = "AI_Impact"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "artificial intelligence (AI)1 kan worden ingezet om handelingen sneller of veiliger uit te voeren, zoals het inspecteren van asfaltkwaliteit of overtredingen op zee handhaven. AI biedt kansen, maar het brengt ook gevaren met zich mee. De cio-raad van IenW heeft in november 2020 akkoord gegeven om aan de slag te gaan met een concept AI Impact Assessment (AIIA), zodat er meer aandacht komt voor verantwoorde AI. Het IDlab ILT, het RWS Datalab en Concerndirectie Informatiebeleid van IenW (CDIB) hebben dit opgepakt en gezamenlijk deze nieuwe versie van het AIIA ontwikkeld. Het AIIA is vastgesteld door de Bestuursraad van IenW op "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "AI Impact Assessment Het hulpmiddel voor een betrouwbaar AI-project"
    thisalinea.titlefontsize = "36.0"
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
    thisalinea.texttitle = "In samenwerking door collega’s van het ministerie Infrastructuur en Waterstaat (IenW) bij Concerndirectie Informatiebeleid (CDIB), Inspectie Leefomgeving en Transport (ILT IDlab en afdeling analyse) en Rijkswaterstaat (RWS Datalab)"
    thisalinea.titlefontsize = "8.999999999999993"
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
    thisalinea.texttitle = "Inhoudsopgave"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Toelichting"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 4
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Leeswijzer Vragenlijst"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 5
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Inleidende vragen"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 6
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Doel van het systeem Rol binnen de organisatie"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 7
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Fundamentele rechten & fairness"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 8
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Grondrechten Bias Stakeholderparticipatie"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 9
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Technische robuustheid"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 10
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Accuraatheid Betrouwbaarheid Technische implementatie Reproduceerbaarheid Uitlegbaarheid"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 11
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Data governance"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 12
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Kwaliteit en integriteit van data Privacy en gegevensbescherming"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 13
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Risicobeheer"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 14
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Risicobeheersing Alternatieve werkwijze Hackaanvallen en corruptie"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 15
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Verantwoordingsplicht"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 16
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Communicatie Controleerbaarheid Archivering Klimaatadaptie"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 17
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Bijlagen"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 18
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Begrippenlijst Wie is wie Wie doet wat"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 19
    thisalinea.parentID = 18
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Toelichting"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 20
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "artificial intelligence (AI)1 kan worden ingezet om handelingen sneller of veiliger uit te voeren, zoals het inspecteren van asfaltkwaliteit of overtredingen op zee handhaven. AI biedt kansen, maar het brengt ook gevaren met zich mee. De cio-raad van IenW heeft in november 2020 akkoord gegeven om aan de slag te gaan met een concept AI Impact Assessment (AIIA), zodat er meer aandacht komt voor verantwoorde AI. Het IDlab ILT, het RWS Datalab en Concerndirectie Informatiebeleid van IenW (CDIB) hebben dit opgepakt en gezamenlijk deze nieuwe versie van het AIIA ontwikkeld. Het AIIA is vastgesteld door de Bestuursraad van IenW op "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("artificial intelligence (AI)1 kan worden ingezet om handelingen sneller of veiliger uit te voeren, zoals het")
    thisalinea.textcontent.append("inspecteren van asfaltkwaliteit of overtredingen op zee handhaven. AI biedt kansen, maar het brengt ook")
    thisalinea.textcontent.append("gevaren met zich mee. De cio-raad van IenW heeft in november 2020 akkoord gegeven om aan de slag te")
    thisalinea.textcontent.append("gaan met een concept AI Impact Assessment (AIIA), zodat er meer aandacht komt voor verantwoorde AI. Het")
    thisalinea.textcontent.append("IDlab ILT, het RWS Datalab en Concerndirectie Informatiebeleid van IenW (CDIB) hebben dit opgepakt en")
    thisalinea.textcontent.append("gezamenlijk deze nieuwe versie van het AIIA ontwikkeld. Het AIIA is vastgesteld door de Bestuursraad van")
    thisalinea.textcontent.append("IenW op 4 juli 2022.")
    thisalinea.textcontent.append("Het AI Impact Assessment (AIIA) wordt gebruikt voor het discussiëren over AI-systemen. Hierbij wordt")
    thisalinea.textcontent.append("gekeken naar obstakels in de data, het systeem, de algoritmiek en wordt rekening gehouden met geldende")
    thisalinea.textcontent.append("wet- en regelgeving. Het AIIA dient als instrument voor het gesprek en het vastleggen van het denkproces")
    thisalinea.textcontent.append("zodat onder andere de verantwoording, kwaliteit en reproduceerbaarheid worden vergroot. Het")
    thisalinea.textcontent.append("verwachte resultaat van het AIIA is een helder ingevuld document waarin duidelijk zichtbaar is welke")
    thisalinea.textcontent.append("afwegingen gemaakt zijn bij het inzetten van AI in een project.")
    thisalinea.textcontent.append("Primair is de opdrachtgever verantwoordelijk voor het (laten) uitvoeren van het AIIA. Er moet een")
    thisalinea.textcontent.append("AIIA worden opgesteld voor elk ai-systeem. Het invullen van het AIIA gebeurt nadrukkelijk proportioneel,")
    thisalinea.textcontent.append("passend bij de impact en het risicoprofiel van de toepassing. De verantwoordelijkheid voor wat propor-")
    thisalinea.textcontent.append("tioneel is, ligt bij de projectleiders en de opdrachtgever.")
    thisalinea.textcontent.append("AI kan ook worden gebruikt in onderzoek. Daarbij geldt dat het van belang is om onder andere te kijken")
    thisalinea.textcontent.append("naar zaken als false positives en false negatives en de verantwoording over en uitlegbaarheid van de")
    thisalinea.textcontent.append("resultaten. Ook kan AI worden gebruikt om hypotheses te genereren, die dan met AI of andere technieken")
    thisalinea.textcontent.append("verder worden uitgewerkt. Kortom ook voor onderzoekers geldt: denk goed na over AI en gebruik daar deze")
    thisalinea.textcontent.append("AIIA voor. Uiteraard vallen niet van toepassing zijnde vragen af, bijvoorbeeld als het systeem niet in beheer")
    thisalinea.textcontent.append("wordt genomen.")
    thisalinea.textcontent.append("De proportioneel ingevulde AIIA moet af zijn voor het in gebruik nemen van een AI-systeem. Het is")
    thisalinea.textcontent.append("belangrijk dat het AIIA daarna regelmatig wordt bijgesteld, bijvoorbeeld als het doel van het AI-systeem")
    thisalinea.textcontent.append("wordt gewijzigd of er veranderingen aan het AI-systeem plaatsvinden. Daarnaast kunnen zich in de loop van")
    thisalinea.textcontent.append("de tijd nieuwe risico’s voordoen. Controleer dit als projectleider/opdrachtgever periodiek.")
    thisalinea.textcontent.append("Om een AI-project goed en verantwoord uit te voeren, is er meer nodig dan een AI Impact Assessment.")
    thisalinea.textcontent.append("Denk aan het organiseren van een moreel beraad, het zorg dragen voor een zorgvuldige inbeheername en")
    thisalinea.textcontent.append("het informeren van de omgeving. Zie hiervoor de meest recente handreiking ‘AI voor opdrachtgevers’ (op te")
    thisalinea.textcontent.append("vragen bij de Concerndirectie Informatiebeleid).")
    thisalinea.textcontent.append("Past het AIIA niet bij een AI-project of systeem waaraan je denkt? Of heb je andere opmerkingen of vragen")
    thisalinea.textcontent.append("over het AIIA? Neem contact op met de CIO-office bij Concerndirectie Informatiebeleid.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Leeswijzer"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 21
    thisalinea.parentID = 20
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Voor het invullen van het AIIA is het volgende van belang: - Het AIIA dient als instrument voor gesprek en controle. - Wijzigt het doel van het ai-systeem, dan moet het AIIA bijgesteld worden. - dikgedrukte woorden zijn aanklikbare begrippen, gedefinieerd in bijlage Begrippenlijst. - Het AIIA moet af zijn voor het in gebruik nemen van een AI-systeem. - Het AIIA is verplicht, maar de mate waarin het wordt ingevuld ligt bij de expertise van de projectleider. - Enkel ‘ja’ of ‘nee’ volstaat niet als antwoord op de vragen. - Vragen zijn gecodeerd en genummerd, de eerste letter verwijst naar "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Voor het invullen van het AIIA is het volgende van belang:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- Het AIIA dient als instrument voor gesprek en controle. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 22
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- Het AIIA dient als instrument voor gesprek en controle. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Het AIIA dient als instrument voor gesprek en controle.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- Wijzigt het doel van het ai-systeem, dan moet het AIIA bijgesteld worden. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 23
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- Wijzigt het doel van het ai-systeem, dan moet het AIIA bijgesteld worden. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Wijzigt het doel van het ai-systeem, dan moet het AIIA bijgesteld worden.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- dikgedrukte woorden zijn aanklikbare begrippen, gedefinieerd in bijlage Begrippenlijst. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 24
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "- dikgedrukte woorden zijn aanklikbare begrippen, gedefinieerd in bijlage Begrippenlijst. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- dikgedrukte woorden zijn aanklikbare begrippen, gedefinieerd in bijlage Begrippenlijst.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- Het AIIA moet af zijn voor het in gebruik nemen van een AI-systeem. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 25
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "- Het AIIA moet af zijn voor het in gebruik nemen van een AI-systeem. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Het AIIA moet af zijn voor het in gebruik nemen van een AI-systeem.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- Het AIIA is verplicht, maar de mate waarin het wordt ingevuld ligt bij de ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 26
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "- Het AIIA is verplicht, maar de mate waarin het wordt ingevuld ligt bij de expertise van de projectleider. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Het AIIA is verplicht, maar de mate waarin het wordt ingevuld ligt bij de expertise van de projectleider.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- Enkel ‘ja’ of ‘nee’ volstaat niet als antwoord op de vragen. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 27
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "- Enkel ‘ja’ of ‘nee’ volstaat niet als antwoord op de vragen. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Enkel ‘ja’ of ‘nee’ volstaat niet als antwoord op de vragen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "- Vragen zijn gecodeerd en genummerd, de eerste letter verwijst naar het hoofdstuk (bv. T ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 28
    thisalinea.parentID = 21
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "- Vragen zijn gecodeerd en genummerd, de eerste letter verwijst naar het hoofdstuk (bv. T voor Technische robuustheid), de letter ‘o’ wordt hieraan toegevoegd als het een groene  hulpvraag betreft. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Vragen zijn gecodeerd en genummerd, de eerste letter verwijst naar het hoofdstuk (bv. T voor Technische")
    thisalinea.textcontent.append("robuustheid), de letter ‘o’ wordt hieraan toegevoegd als het een groene  hulpvraag betreft.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Vragenlijst"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 29
    thisalinea.parentID = 20
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Het volledige AIIA omvat zo’n 100 vragen. Het AIIA is verplicht bij het maken of inkopen van AI-systemen, maar het invullen gebeurt nadrukkelijk proportioneel, door de opdrachtgever en projectleider zelf te bepalen. Dit noemen we: verplicht, maar soepel. Dit betekent vooral dat je met gezond verstand moet nadenken over hoeveel impact jouw ai-systeem heeft. Bij alle vormen van artificial intelligence zijn de blauwe  overkoepelende vragen verplicht, deze helpen bij het faciliteren van de discussie over de wenselijkheid van het AI-systeem. De groene  hulpvragen helpen om hier een concrete invulling aan te geven. Niet alle groene vragen zijn bij "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Het volledige AIIA omvat zo’n 100 vragen. Het AIIA is verplicht bij het maken of inkopen van AI-systemen,")
    thisalinea.textcontent.append("maar het invullen gebeurt nadrukkelijk proportioneel, door de opdrachtgever en projectleider zelf te")
    thisalinea.textcontent.append("bepalen. Dit noemen we: verplicht, maar soepel. Dit betekent vooral dat je met gezond verstand moet")
    thisalinea.textcontent.append("nadenken over hoeveel impact jouw ai-systeem heeft. Bij alle vormen van artificial intelligence zijn")
    thisalinea.textcontent.append("de blauwe  overkoepelende vragen verplicht, deze helpen bij het faciliteren van de discussie over de")
    thisalinea.textcontent.append("wenselijkheid van het AI-systeem. De groene  hulpvragen helpen om hier een concrete invulling aan te")
    thisalinea.textcontent.append("geven. Niet alle groene vragen zijn bij iedere casus relevant, deze zijn dan ook niet verplicht (soepel). De")
    thisalinea.textcontent.append("opdrachtgever en projectleider kunnen op basis van een eigen risico-inschatting besluiten om deze")
    thisalinea.textcontent.append("vragen wel in te vullen. Houd er rekening mee dat de Auditdienst Rijk en de Algemene Rekenkamer het")
    thisalinea.textcontent.append("systeem kunnen controleren op correctheid en veiligheid. Ook betekent een volledig ingevuld AIIA niet")
    thisalinea.textcontent.append("per definitie dat de AI veilig is. Wanneer de AI Act in werking treedt (COM/2021/206 final), moeten ook de")
    thisalinea.textcontent.append("vragen met een rode ster  verplicht worden ingevuld voor ai met hoog risico. Het is wenselijk om dat")
    thisalinea.textcontent.append("nu ook al te doen. Voor iedere vraag geldt dat het antwoord moet worden toegelicht. Enkel een ‘ja’ of ‘nee’")
    thisalinea.textcontent.append("volstaat dus nooit als antwoord.")
    thisalinea.textcontent.append("In bijlage ‘Wie doet wat’ tref je een overzicht dat kan helpen bij het bepalen wie welke vraag moet invullen.")
    thisalinea.textcontent.append("Sommige vragen kunnen bijvoorbeeld beter door een data scientist worden ingevuld, en andere vragen")
    thisalinea.textcontent.append("door een jurist.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Inleidende vragen"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 30
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "De inleidende vragen gaan over de algemene aspecten van het ai-systeem dat je gaat ontwikkelen. Deze vragen gaan over het doel van het systeem, en de rol die het systeem binnen de organisatie gaat hebben. Denk aan vragen over de gebruikte technieken, of wie er verantwoordelijk gaat zijn. Deze vragen zijn basis vragen om weer te geven wat je voor welk doel aan het doen bent. Het antwoord op deze vragen heeft relevantie voor de rest van het AIIA. i 1. Geef een korte beschrijving van het beoogde ai-systeem (titel, algemene omschrijving, probleemstelling, en het domein) i 2. Waarom is "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("De inleidende vragen gaan over de algemene aspecten van het ai-systeem dat je gaat ontwikkelen.")
    thisalinea.textcontent.append("Deze vragen gaan over het doel van het systeem, en de rol die het systeem binnen de organisatie gaat")
    thisalinea.textcontent.append("hebben. Denk aan vragen over de gebruikte technieken, of wie er verantwoordelijk gaat zijn.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Doel van het systeem"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 31
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Deze vragen zijn basis vragen om weer te geven wat je voor welk doel aan het doen bent. Het antwoord op deze vragen heeft relevantie voor de rest van het AIIA. i 1. Geef een korte beschrijving van het beoogde ai-systeem (titel, algemene omschrijving, probleemstelling, en het domein) i 2. Waarom is er voor de huidige techniek gekozen? (hierbij is het van belang dat alle afwegingen van robuustheid tot mensenrechten, impact op gebruiker en eindgebruiker, verantwoordingsplicht etc. zijn meegenomen in het antwoord) i 3. Wat is het doel en beoogde resultaat van het AI-systeem? i 4. Welk doel wordt er "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Deze vragen zijn basis vragen om weer te geven wat je voor welk doel aan het doen bent. Het antwoord op")
    thisalinea.textcontent.append("deze vragen heeft relevantie voor de rest van het AIIA.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 1. Geef een korte beschrijving van het beoogde ai-systeem (titel, algemene omschrijving, ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 32
    thisalinea.parentID = 31
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "i 1. Geef een korte beschrijving van het beoogde ai-systeem (titel, algemene omschrijving, probleemstelling, en het domein) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 1. Geef een korte beschrijving van het beoogde ai-systeem (titel, algemene omschrijving,")
    thisalinea.textcontent.append("probleemstelling, en het domein)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 2. Waarom is er voor de huidige techniek gekozen? (hierbij is het van belang ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 33
    thisalinea.parentID = 31
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "i 2. Waarom is er voor de huidige techniek gekozen? (hierbij is het van belang dat alle afwegingen van robuustheid tot mensenrechten, impact op gebruiker en eindgebruiker, verantwoordingsplicht etc. zijn meegenomen in het antwoord) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 2. Waarom is er voor de huidige techniek gekozen? (hierbij is het van belang dat alle")
    thisalinea.textcontent.append("afwegingen van robuustheid tot mensenrechten, impact op gebruiker en eindgebruiker,")
    thisalinea.textcontent.append("verantwoordingsplicht etc. zijn meegenomen in het antwoord)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 3. Wat is het doel en beoogde resultaat van het AI-systeem? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 34
    thisalinea.parentID = 31
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "i 3. Wat is het doel en beoogde resultaat van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 3. Wat is het doel en beoogde resultaat van het AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 4. Welk doel wordt er aan het AI-systeem gekoppeld volgens het rapport Aandacht voor ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 35
    thisalinea.parentID = 31
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "i 4. Welk doel wordt er aan het AI-systeem gekoppeld volgens het rapport Aandacht voor Algoritmes van de Algemene Rekenkamer2? doel 1, doel 2 of doel 3? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 4. Welk doel wordt er aan het AI-systeem gekoppeld volgens het rapport Aandacht voor")
    thisalinea.textcontent.append("Algoritmes van de Algemene Rekenkamer2? doel 1, doel 2 of doel 3?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Rol binnen de organisatie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 36
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Deze vragen leveren vaak discussie op. Naast vragen over de bouw en details van een AI-systeem, moet er goed nagedacht worden over de impact van het AI-systeem in zijn geheel. Dit zijn fundamentele vragen. Zorg daarom dat je ze goed uitdenkt. Probeer dit goed te nuanceren. Stel dat het AI-systeem een positieve impact heeft op duizenden burgers, maar een negatieve impact op tien burgers, dan is het systeem niet meteen onbruikbaar, maar moeten er wel goede maatwerkoplossingen komen voor de tien burgers waarop negatieve impact is. Bij deze vragen stel je ook de rolverdeling binnen het ontwikkelen en gebruiken van "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Deze vragen leveren vaak discussie op. Naast vragen over de bouw en details van een AI-systeem, moet er")
    thisalinea.textcontent.append("goed nagedacht worden over de impact van het AI-systeem in zijn geheel. Dit zijn fundamentele vragen.")
    thisalinea.textcontent.append("Zorg daarom dat je ze goed uitdenkt. Probeer dit goed te nuanceren. Stel dat het AI-systeem een positieve")
    thisalinea.textcontent.append("impact heeft op duizenden burgers, maar een negatieve impact op tien burgers, dan is het systeem niet")
    thisalinea.textcontent.append("meteen onbruikbaar, maar moeten er wel goede maatwerkoplossingen komen voor de tien burgers waarop")
    thisalinea.textcontent.append("negatieve impact is.")
    thisalinea.textcontent.append("Bij deze vragen stel je ook de rolverdeling binnen het ontwikkelen en gebruiken van je systeem vast.")
    thisalinea.textcontent.append("Deze rollen staan gedefinieerd in de begrippenlijst. Houd deze definities aan.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 5. Waar in de organisatie is beoogd het AI-systeem te gebruiken en welke beoogde ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 37
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "i 5. Waar in de organisatie is beoogd het AI-systeem te gebruiken en welke beoogde impact is er voor de organisatie? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 5. Waar in de organisatie is beoogd het AI-systeem te gebruiken en welke beoogde impact is er")
    thisalinea.textcontent.append("voor de organisatie?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 6. Beschrijf de rolverdeling binnen het opzetten van het AI-systeem (zoals de ontwikkelaar, ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 38
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "i 6. Beschrijf de rolverdeling binnen het opzetten van het AI-systeem (zoals de ontwikkelaar, opdrachtgever, projectleider, beheerorganisaties en eindverantwoordelijke). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 6. Beschrijf de rolverdeling binnen het opzetten van het AI-systeem (zoals de ontwikkelaar,")
    thisalinea.textcontent.append("opdrachtgever, projectleider, beheerorganisaties en eindverantwoordelijke).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "i 7. Wie is de gebruiker van het AI-systeem, wie zijn de eindgebruikers die met ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 39
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "i 7. Wie is de gebruiker van het AI-systeem, wie zijn de eindgebruikers die met het systeem werken en welke betrokkenen ondervinden impact van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("i 7. Wie is de gebruiker van het AI-systeem, wie zijn de eindgebruikers die met het systeem")
    thisalinea.textcontent.append("werken en welke betrokkenen ondervinden impact van het AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Fundamentele rechten & fairness"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 40
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Zoals veel technologieën kunnen AI-systemen grondrechten zowel bevorderen als benadelen. Gelet op het grote belang van de bescherming van grondrechten, en de bijzondere risico’s die kunnen bestaan voor de aantasting van die grondrechten door inzet van AI-systemen, is het van belang om aan dit onderwerp afzonderlijk aandacht te besteden. Dit hoofdstuk hangt nauw samen met het hoofdstuk data governance, waarin privacy wordt behandeld. Het recht op privacy is een grondrecht, maar door het karakter van het onderwerp privacy is het onderverdeeld in een eigen hoofdstuk. Mensen die belang hebben bij de werking van het ai-systeem moeten goed behandeld worden. Dat "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Zoals veel technologieën kunnen AI-systemen grondrechten zowel bevorderen als benadelen. Gelet op")
    thisalinea.textcontent.append("het grote belang van de bescherming van grondrechten, en de bijzondere risico’s die kunnen bestaan voor")
    thisalinea.textcontent.append("de aantasting van die grondrechten door inzet van AI-systemen, is het van belang om aan dit onderwerp")
    thisalinea.textcontent.append("afzonderlijk aandacht te besteden. Dit hoofdstuk hangt nauw samen met het hoofdstuk data governance,")
    thisalinea.textcontent.append("waarin privacy wordt behandeld. Het recht op privacy is een grondrecht, maar door het karakter van het")
    thisalinea.textcontent.append("onderwerp privacy is het onderverdeeld in een eigen hoofdstuk.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Grondrechten"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 41
    thisalinea.parentID = 40
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Mensen die belang hebben bij de werking van het ai-systeem moeten goed behandeld worden. Dat bete- kent dat de (fundamentele) rechten van alle betrokkenen gewaarborgd moeten worden. Voor een goede invulling van dit onderwerp verwijzen wij je naar de Impact Assessment Mensenrechten en Algoritmes.3 De vragen die in deze AIIA gesteld worden zijn dan ook niet voldoende voor het afbakenen van dit onderwerp. Bij het beantwoorden van de vragen zijn de grondrechten van de mens van toepassing, deze staan vastgelegd in de Grondwet en het Europese Verdrag voor de Rechten van de Mens. f 1. Wat is de mogelijke impact "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Mensen die belang hebben bij de werking van het ai-systeem moeten goed behandeld worden. Dat bete-")
    thisalinea.textcontent.append("kent dat de (fundamentele) rechten van alle betrokkenen gewaarborgd moeten worden. Voor een goede")
    thisalinea.textcontent.append("invulling van dit onderwerp verwijzen wij je naar de Impact Assessment Mensenrechten en Algoritmes.3 De")
    thisalinea.textcontent.append("vragen die in deze AIIA gesteld worden zijn dan ook niet voldoende voor het afbakenen van dit onderwerp.")
    thisalinea.textcontent.append("Bij het beantwoorden van de vragen zijn de grondrechten van de mens van toepassing, deze staan")
    thisalinea.textcontent.append("vastgelegd in de Grondwet en het Europese Verdrag voor de Rechten van de Mens.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "f 1. Wat is de mogelijke impact op de grondrechten van burgers door het gebruik ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 42
    thisalinea.parentID = 41
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "f 1. Wat is de mogelijke impact op de grondrechten van burgers door het gebruik van het ai-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("f 1. Wat is de mogelijke impact op de grondrechten van burgers door het gebruik van het ai-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "f 2. Is het proportioneel en subsidiair om dit systeem in te zetten om de ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 43
    thisalinea.parentID = 41
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "f 2. Is het proportioneel en subsidiair om dit systeem in te zetten om de gestelde doelen te realiseren? Oftewel: is de impact in verhouding met de beoogde doelen en zijn er geen andere minder ingrijpende manieren om deze doelen te behalen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("f 2. Is het proportioneel en subsidiair om dit systeem in te zetten om de gestelde doelen te")
    thisalinea.textcontent.append("realiseren? Oftewel: is de impact in verhouding met de beoogde doelen en zijn er geen andere")
    thisalinea.textcontent.append("minder ingrijpende manieren om deze doelen te behalen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "f 3. Wat is de wettelijke grondslag van de inzet van het AI-systeem en van ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 44
    thisalinea.parentID = 41
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "f 3. Wat is de wettelijke grondslag van de inzet van het AI-systeem en van de beoogde besluiten die genomen worden op basis van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("f 3. Wat is de wettelijke grondslag van de inzet van het AI-systeem en van de beoogde besluiten die")
    thisalinea.textcontent.append("genomen worden op basis van het AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 1. Welke grondrechtelijke bepalingen zijn mogelijk van toepassing? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 45
    thisalinea.parentID = 41
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "fo 1. Welke grondrechtelijke bepalingen zijn mogelijk van toepassing? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 1. Welke grondrechtelijke bepalingen zijn mogelijk van toepassing?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 2. Op welk van deze grondrechtelijke bepalingen kan mogelijk een inbreuk worden gemaakt ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 46
    thisalinea.parentID = 41
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "fo 2. Op welk van deze grondrechtelijke bepalingen kan mogelijk een inbreuk worden gemaakt bij verkeerde uitvoering van het ai-systeem? Welke acties worden genomen om dit te voorkomen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 2. Op welk van deze grondrechtelijke bepalingen kan mogelijk een inbreuk worden gemaakt")
    thisalinea.textcontent.append("bij verkeerde uitvoering van het ai-systeem? Welke acties worden genomen om dit te")
    thisalinea.textcontent.append("voorkomen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Bias"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 47
    thisalinea.parentID = 40
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "bias betekent het doen van aannames over dingen, mensen of groepen. Dit heeft twee kanten. Enerzijds is het noodzakelijk om conclusies over data op een nieuwe situatie te projecteren. We maken in generalisaties namelijk altijd aannames. Tegelijkertijd is het van belang dat er geen onrechtmatige vertekening ontstaat met vormen van onterechte en onwenselijke bias die in strijd kunnen zijn met de rechten van de mens. Bias kan zitten alle facetten van het systeem: bias in de input, bias in het model en bias in de output. Er zijn verschillende typen bias die relevant zijn tijdens het ontwikkelen en inzetten van "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("bias betekent het doen van aannames over dingen, mensen of groepen. Dit heeft twee kanten. Enerzijds is")
    thisalinea.textcontent.append("het noodzakelijk om conclusies over data op een nieuwe situatie te projecteren. We maken in generalisaties")
    thisalinea.textcontent.append("namelijk altijd aannames. Tegelijkertijd is het van belang dat er geen onrechtmatige vertekening ontstaat")
    thisalinea.textcontent.append("met vormen van onterechte en onwenselijke bias die in strijd kunnen zijn met de rechten van de mens.")
    thisalinea.textcontent.append("Bias kan zitten alle facetten van het systeem: bias in de input, bias in het model en bias in de output.")
    thisalinea.textcontent.append("Er zijn verschillende typen bias die relevant zijn tijdens het ontwikkelen en inzetten van AI, bijvoorbeeld")
    thisalinea.textcontent.append("data bias en design bias. Deze soorten bias worden vaak veroorzaakt door socio-economische aan-names")
    thisalinea.textcontent.append("en kunnen als gevolg versterkte socio-economische aannames hebben. Deze soorten bias kunnen ervoor")
    thisalinea.textcontent.append("zorgen dat AI-systemen niet voor alle betrokkenen goed werken als er niet voor wordt gecorrigeerd.")
    thisalinea.textcontent.append("Het kernelement van dit thema is bewustzijn en integriteit. Het is onmogelijk om volledig zonder bias te")
    thisalinea.textcontent.append("werken. Vaak bestaat bias al decennia lang en zal deze (onterecht) niet als zodanig worden herkend. Dus in")
    thisalinea.textcontent.append("plaats van ons richten op bias-loze AI, moeten we ernaar streven om ons zoveel mogelijk bewust te zijn van")
    thisalinea.textcontent.append("mogelijke discriminatie. Het is verder van belang kritische vragen te stellen over de herkomst en inhoud")
    thisalinea.textcontent.append("van data en de werking van AI-systemen.")
    thisalinea.textcontent.append("Bias hangt nauw samen met diversiteit, gelijkheid en eerlijkheid tussen mensen, maar het is van")
    thisalinea.textcontent.append("belang om bewust te zijn dat aannames ook over niet-menselijke aspecten kunnen gaan, zoals de natuur of")
    thisalinea.textcontent.append("leefomgeving. Daarnaast kan het voor de wijze waarop je bias wilt mitigeren relevant zijn om onderscheid")
    thisalinea.textcontent.append("te maken tussen negatieve impact, geen positieve impact en een positieve impact die de bias kan")
    thisalinea.textcontent.append("hebben.")
    thisalinea.textcontent.append("Denk bij positieve impact aan het volgende. In de statistiek is bias een systematische fout of afwijking.")
    thisalinea.textcontent.append("Dat is niet altijd verkeerd. Deze systematische fout wordt namelijk vaak bewust toegepast in modellen,")
    thisalinea.textcontent.append("bijvoorbeeld in de vorm van regularisatie. Op deze manier kan ervoor worden gezorgd dat de variantie")
    thisalinea.textcontent.append("wordt verkleind, ook al gaat dit ten koste van een (kleine) systematische afwijking. Bias kan ook positief")
    thisalinea.textcontent.append("worden ingezet. Een AI-systeem kan bijvoorbeeld bewust worden ontwikkeld om niet of minder te")
    thisalinea.textcontent.append("discrimineren, juist door het introduceren van bias.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "f 4. Hoe wordt rekening gehouden met mogelijk onwenselijke bias in de input, bias in ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 48
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "f 4. Hoe wordt rekening gehouden met mogelijk onwenselijke bias in de input, bias in het model en bias in de output van het ai-systeem?4★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("f 4. Hoe wordt rekening gehouden met mogelijk onwenselijke bias in de input, bias in het model")
    thisalinea.textcontent.append("en bias in de output van het ai-systeem?4★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Bias in de input(data)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 49
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "fo 3. Is de input(data) data representatief voor het onderwerp waarover een beslissing moet worden genomen? fo 4. Worden indien nodig subpopulaties beschermd bij het trekken van steekproeven? fo 5. Is de keuze voor de inputvariabelen onderbouwd en afgestemd met de betrokkenen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "fo 3. Is de input(data) data representatief voor het onderwerp waarover een beslissing moet worden ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 50
    thisalinea.parentID = 49
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "fo 3. Is de input(data) data representatief voor het onderwerp waarover een beslissing moet worden genomen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 3. Is de input(data) data representatief voor het onderwerp waarover een beslissing moet worden")
    thisalinea.textcontent.append("genomen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "fo 4. Worden indien nodig subpopulaties beschermd bij het trekken van steekproeven? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 51
    thisalinea.parentID = 49
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "fo 4. Worden indien nodig subpopulaties beschermd bij het trekken van steekproeven? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 4. Worden indien nodig subpopulaties beschermd bij het trekken van steekproeven?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "fo 5. Is de keuze voor de inputvariabelen onderbouwd en afgestemd met de betrokkenen? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 52
    thisalinea.parentID = 49
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "fo 5. Is de keuze voor de inputvariabelen onderbouwd en afgestemd met de betrokkenen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 5. Is de keuze voor de inputvariabelen onderbouwd en afgestemd met de betrokkenen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Bias in het model"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 53
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "fo 6. Op welke manier wordt er rekening gehouden met het feit dat er geen onterechte of onrechtvaardige bias in een AI-systeem wordt gecreëerd of versterkt? fo 7. Is het AI-systeem te gebruiken door de beoogde eindgebruikers (dus ongeacht diens kenmerken zoals leeftijd, geslacht of capaciteit)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "fo 6. Op welke manier wordt er rekening gehouden met het feit dat er geen ..."
    thisalinea.titlefontsize = "9.000000000000028"
    thisalinea.nativeID = 54
    thisalinea.parentID = 53
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "fo 6. Op welke manier wordt er rekening gehouden met het feit dat er geen onterechte of onrechtvaardige bias in een AI-systeem wordt gecreëerd of versterkt? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 6. Op welke manier wordt er rekening gehouden met het feit dat er geen onterechte of")
    thisalinea.textcontent.append("onrechtvaardige bias in een AI-systeem wordt gecreëerd of versterkt?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "fo 7. Is het AI-systeem te gebruiken door de beoogde eindgebruikers (dus ongeacht diens ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 55
    thisalinea.parentID = 53
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "fo 7. Is het AI-systeem te gebruiken door de beoogde eindgebruikers (dus ongeacht diens kenmerken zoals leeftijd, geslacht of capaciteit)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 7. Is het AI-systeem te gebruiken door de beoogde eindgebruikers (dus ongeacht diens")
    thisalinea.textcontent.append("kenmerken zoals leeftijd, geslacht of capaciteit)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Bias in de output(data)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 56
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "fo 8. Zijn er stop-, toezicht- of controle- mechanisme ingesteld om te voorkomen dat groepen in de maatschappij disproportioneel getroffen kunnen worden door de negatieve implicaties van het AI-systeem? Specifiek voor ILT: maak hier onderscheid tussen ondertoezichtstaanden (OTS) en de rest van de maatschappij. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "fo 8. Zijn er stop-, toezicht- of controle- mechanisme ingesteld om te voorkomen dat groepen ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 57
    thisalinea.parentID = 56
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "fo 8. Zijn er stop-, toezicht- of controle- mechanisme ingesteld om te voorkomen dat groepen in de maatschappij disproportioneel getroffen kunnen worden door de negatieve implicaties van het AI-systeem? Specifiek voor ILT: maak hier onderscheid tussen ondertoezichtstaanden (OTS) en de rest van de maatschappij. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 8. Zijn er stop-, toezicht- of controle- mechanisme ingesteld om te voorkomen dat groepen in de")
    thisalinea.textcontent.append("maatschappij disproportioneel getroffen kunnen worden door de negatieve implicaties van het")
    thisalinea.textcontent.append("AI-systeem? Specifiek voor ILT: maak hier onderscheid tussen ondertoezichtstaanden (OTS) en")
    thisalinea.textcontent.append("de rest van de maatschappij.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Stakeholderparticipatie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 58
    thisalinea.parentID = 40
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Bij stakeholder participatie worden verschillende doelgroepen betrokken in het kader van diversiteit, non-discriminatie en rechtvaardigheid. Om rechtvaardige AI te realiseren, moet er goed nagedacht worden over inclusie en diversiteit gedurende de gehele levenscyclus van het AI-systeem. In deze AIIA gaat het in deze context ook vaak over betrokkenen. Om te voorkomen dat de ontwikkelaars van een AI-systeem te veel in een eigen denkwereld blijven en zich niet bewust zijn van impliciete aannames of gevolgen, is afstemming over AI-systemen essentieel. Je doet dit door bijvoorbeeld af te stemmen met je eigen team, de klant, eindgebruiker, betrokkenen, ervaringsdeskundigen, domeinexperts als universiteiten, andere "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Bij stakeholder participatie worden verschillende doelgroepen betrokken in het kader van diversiteit,")
    thisalinea.textcontent.append("non-discriminatie en rechtvaardigheid. Om rechtvaardige AI te realiseren, moet er goed nagedacht worden")
    thisalinea.textcontent.append("over inclusie en diversiteit gedurende de gehele levenscyclus van het AI-systeem. In deze AIIA gaat het in")
    thisalinea.textcontent.append("deze context ook vaak over betrokkenen.")
    thisalinea.textcontent.append("Om te voorkomen dat de ontwikkelaars van een AI-systeem te veel in een eigen denkwereld blijven en")
    thisalinea.textcontent.append("zich niet bewust zijn van impliciete aannames of gevolgen, is afstemming over AI-systemen essentieel.")
    thisalinea.textcontent.append("Je doet dit door bijvoorbeeld af te stemmen met je eigen team, de klant, eindgebruiker, betrokkenen,")
    thisalinea.textcontent.append("ervaringsdeskundigen, domeinexperts als universiteiten, andere overheidsorganisaties etc. Een moreel")
    thisalinea.textcontent.append("beraad5 organiseren is aanbevolen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "f 5. Zijn alle stakeholders in kaart gebracht middels een stakeholderanalyse en is met hen ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 59
    thisalinea.parentID = 58
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "f 5. Zijn alle stakeholders in kaart gebracht middels een stakeholderanalyse en is met hen het gesprek aangegaan? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("f 5. Zijn alle stakeholders in kaart gebracht middels een stakeholderanalyse en is met hen het")
    thisalinea.textcontent.append("gesprek aangegaan?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 9. Met welke mensen en/of groepen is er afgestemd bij het ontwikkelen van ai-systeem? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 60
    thisalinea.parentID = 58
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "fo 9. Met welke mensen en/of groepen is er afgestemd bij het ontwikkelen van ai-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 9. Met welke mensen en/of groepen is er afgestemd bij het ontwikkelen van ai-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 10. Zijn de stakeholders op de hoogte waarom er gekozen is voor bepaalde input ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 61
    thisalinea.parentID = 58
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "fo 10. Zijn de stakeholders op de hoogte waarom er gekozen is voor bepaalde input variabelen (waar zij wellicht in staan)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 10. Zijn de stakeholders op de hoogte waarom er gekozen is voor bepaalde input variabelen")
    thisalinea.textcontent.append("(waar zij wellicht in staan)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 11. Welke feedback is er verzameld van teams of groepen die verschillende achtergronden en ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 62
    thisalinea.parentID = 58
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "fo 11. Welke feedback is er verzameld van teams of groepen die verschillende achtergronden en ervaringen representeren? En wat is hier vervolgens mee gedaan? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 11. Welke feedback is er verzameld van teams of groepen die verschillende achtergronden en")
    thisalinea.textcontent.append("ervaringen representeren? En wat is hier vervolgens mee gedaan?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 12. Hoe wordt de invoering van het AI-systeem geïntroduceerd richting collega’s van IenW? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 63
    thisalinea.parentID = 58
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "fo 12. Hoe wordt de invoering van het AI-systeem geïntroduceerd richting collega’s van IenW? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 12. Hoe wordt de invoering van het AI-systeem geïntroduceerd richting collega’s van IenW?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "fo 13. Hoe wordt de invoering van het AI-systeem geïntroduceerd richting de samenleving? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 64
    thisalinea.parentID = 58
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "fo 13. Hoe wordt de invoering van het AI-systeem geïntroduceerd richting de samenleving? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("fo 13. Hoe wordt de invoering van het AI-systeem geïntroduceerd richting de samenleving?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Technische robuustheid"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 65
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "Of een ai-systeem werkt waarvoor het bedoeld is wordt afgevangen met technische robuustheid. Een ai-systeem moet over het algemeen goed presteren. Om de kans op verkeerde beoordelingen te minimaliseren, is het belangrijk doorlopend de prestaties van een AI-systeem te meten. Dit omvat het meten van het AI-systeem in zowel de ontwikkel- als productiefase. Ook de kwaliteit van de gebruikte data is van belang. Een AI-systeem is dus nooit af; het blijft noodzakelijk AI-systemen regelmatig te testen en hertrainen. Het is wenselijk een kwantificering te hebben van de kans waarop tóch een verkeerde beoordeling wordt gemaakt. accuraatheid van het systeem kan "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Of een ai-systeem werkt waarvoor het bedoeld is wordt afgevangen met technische robuustheid.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Accuraatheid"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 66
    thisalinea.parentID = 65
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Een ai-systeem moet over het algemeen goed presteren. Om de kans op verkeerde beoordelingen te minimaliseren, is het belangrijk doorlopend de prestaties van een AI-systeem te meten. Dit omvat het meten van het AI-systeem in zowel de ontwikkel- als productiefase. Ook de kwaliteit van de gebruikte data is van belang. Een AI-systeem is dus nooit af; het blijft noodzakelijk AI-systemen regelmatig te testen en hertrainen. Het is wenselijk een kwantificering te hebben van de kans waarop tóch een verkeerde beoordeling wordt gemaakt. accuraatheid van het systeem kan je bepalen door acceptatiecriteria op te stellen voor zowel de data als het "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Een ai-systeem moet over het algemeen goed presteren. Om de kans op verkeerde beoordelingen te")
    thisalinea.textcontent.append("minimaliseren, is het belangrijk doorlopend de prestaties van een AI-systeem te meten. Dit omvat het")
    thisalinea.textcontent.append("meten van het AI-systeem in zowel de ontwikkel- als productiefase. Ook de kwaliteit van de gebruikte")
    thisalinea.textcontent.append("data is van belang. Een AI-systeem is dus nooit af; het blijft noodzakelijk AI-systemen regelmatig te testen")
    thisalinea.textcontent.append("en hertrainen. Het is wenselijk een kwantificering te hebben van de kans waarop tóch een verkeerde")
    thisalinea.textcontent.append("beoordeling wordt gemaakt.")
    thisalinea.textcontent.append("accuraatheid van het systeem kan je bepalen door acceptatiecriteria op te stellen voor zowel de data")
    thisalinea.textcontent.append("als het systeem en deze te monitoren middels een metriek. Acceptatiecriteria kunnen bijvoorbeeld een")
    thisalinea.textcontent.append("hoeveelheid data zijn of bepaalde drempelwaardes van het meetsysteem. Er zijn veel verschillende soorten")
    thisalinea.textcontent.append("meetsystemen (vaak ‘performance metrics’ genoemd door data scientists) beschikbaar om de kwaliteit")
    thisalinea.textcontent.append("van modellen te kwantificeren, denk bijvoorbeeld aan een accuratesse, precision en recall of F1-score.")
    thisalinea.textcontent.append("Hierbij is het van belang dat het meetsysteem en de acceptatiecriteria goed worden afgestemd op de data")
    thisalinea.textcontent.append("en het beoogde doel van het AI-systeem.6 Dit moet samenhangen met onder andere de bevindingen uit de")
    thisalinea.textcontent.append("risicoanalyse (zie ‘Risicobeheer’), omdat in de loop van tijd nieuwe of andere risico’s zich kunnen voordoen")
    thisalinea.textcontent.append("met de inzet van een AI-systeem. Ook is het van belang dat de kwaliteit van het systeem doorlopend")
    thisalinea.textcontent.append("gemonitord wordt en indien nodig tijdens het hertrainen of doorontwikkelen de acceptatiecriteria en keuze")
    thisalinea.textcontent.append("voor meetsystemen opnieuw geëvalueerd worden.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "t 1. Hoe wordt de doorlopende accuraatheid van het systeem gemeten en gewaarborgd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 67
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "t 1. Hoe wordt de doorlopende accuraatheid van het systeem gemeten en gewaarborgd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("t 1. Hoe wordt de doorlopende accuraatheid van het systeem gemeten en gewaarborgd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 1. Wat zijn de opgezette acceptatiecriteria om de kwaliteit van de input(data) en output(data) ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 68
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "to 1. Wat zijn de opgezette acceptatiecriteria om de kwaliteit van de input(data) en output(data) van het model aan te toetsen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 1. Wat zijn de opgezette acceptatiecriteria om de kwaliteit van de input(data) en output(data)")
    thisalinea.textcontent.append("van het model aan te toetsen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 2. Passen de acceptatiecriteria bij de data en het doel van het AI-systeem? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 69
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "to 2. Passen de acceptatiecriteria bij de data en het doel van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 2. Passen de acceptatiecriteria bij de data en het doel van het AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 3. Welke evaluatie meetsystemen (performance metrics) ga je gebruiken om de ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 70
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "to 3. Welke evaluatie meetsystemen (performance metrics) ga je gebruiken om de acceptatiecriteria te waarborgen en waarom?7★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 3. Welke evaluatie meetsystemen (performance metrics) ga je gebruiken om de")
    thisalinea.textcontent.append("acceptatiecriteria te waarborgen en waarom?7★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 4. Hoe wordt de output(data) (periodiek) steekproefsgewijs en doorlopend getest op juistheid? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 71
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "to 4. Hoe wordt de output(data) (periodiek) steekproefsgewijs en doorlopend getest op juistheid? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 4. Hoe wordt de output(data) (periodiek) steekproefsgewijs en doorlopend getest op juistheid?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 5. Hoe worden afwijkingen in de output(data) ten opzichte van acceptatiecriteria tijdig ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 72
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "to 5. Hoe worden afwijkingen in de output(data) ten opzichte van acceptatiecriteria tijdig geanalyseerd en gecorrigeerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 5. Hoe worden afwijkingen in de output(data) ten opzichte van acceptatiecriteria tijdig")
    thisalinea.textcontent.append("geanalyseerd en gecorrigeerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 6. Wat zijn de resultaten als er alternatieve modellen zouden worden ingezet? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 73
    thisalinea.parentID = 66
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "to 6. Wat zijn de resultaten als er alternatieve modellen zouden worden ingezet? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 6. Wat zijn de resultaten als er alternatieve modellen zouden worden ingezet?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Betrouwbaarheid"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 74
    thisalinea.parentID = 65
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Een betrouwbaar AI-systeem geeft in vergelijkbare gevallen dezelfde resultaten. De vraag die centraal staat bij betrouwbaarheid is of de individuele output(data) nogmaals te verkrijgen is met behulp van hetzelfde model en dezelfde input(data), dezelfde instellingen en dezelfde parameters. Ook is het van belang dat het systeem een betrouwbare indicatie geeft van hoe goed het model gaat presteren in nieuwe situaties. t 2. Is het ai-systeem betrouwbaar? to 7. Wat zijn de belangrijkste factoren die de prestaties van het ai-systeem beïnvloeden? to 8. Wordt een deel van de (sub)dataset uitgesloten voor het leren van het model en alleen gebruikt voor het "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Een betrouwbaar AI-systeem geeft in vergelijkbare gevallen dezelfde resultaten. De vraag die centraal staat")
    thisalinea.textcontent.append("bij betrouwbaarheid is of de individuele output(data) nogmaals te verkrijgen is met behulp van hetzelfde")
    thisalinea.textcontent.append("model en dezelfde input(data), dezelfde instellingen en dezelfde parameters. Ook is het van belang dat")
    thisalinea.textcontent.append("het systeem een betrouwbare indicatie geeft van hoe goed het model gaat presteren in nieuwe situaties.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "t 2. Is het ai-systeem betrouwbaar? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 75
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "t 2. Is het ai-systeem betrouwbaar? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("t 2. Is het ai-systeem betrouwbaar?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 7. Wat zijn de belangrijkste factoren die de prestaties van het ai-systeem beïnvloeden? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 76
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "to 7. Wat zijn de belangrijkste factoren die de prestaties van het ai-systeem beïnvloeden? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 7. Wat zijn de belangrijkste factoren die de prestaties van het ai-systeem beïnvloeden?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 8. Wordt een deel van de (sub)dataset uitgesloten voor het leren van het model ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 77
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "to 8. Wordt een deel van de (sub)dataset uitgesloten voor het leren van het model en alleen gebruikt voor het bepalen van de betrouwbaarheid of wordt de betrouwbaarheid van het model berekend met behulp van cross-validatie? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 8. Wordt een deel van de (sub)dataset uitgesloten voor het leren van het model en alleen gebruikt")
    thisalinea.textcontent.append("voor het bepalen van de betrouwbaarheid of wordt de betrouwbaarheid van het model")
    thisalinea.textcontent.append("berekend met behulp van cross-validatie?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 9. Hoe is de (hyper)parameter-tuning onderbouwd en getoetst? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 78
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "to 9. Hoe is de (hyper)parameter-tuning onderbouwd en getoetst? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 9. Hoe is de (hyper)parameter-tuning onderbouwd en getoetst?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Technische implementatie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 79
    thisalinea.parentID = 65
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "De technische implementatie beschrijft hoe het AI systeem technisch binnen het ICT-landschap van de organisatie is geïntegreerd. De specifieke eisen van het AI-systeem aan hardware en software zijn gedocumenteerd zodat hier rekening mee gehouden kan worden bij het uitrollen en beheer van het systeem. Daarnaast wordt uit de systeemarchitectuur duidelijk hoe de verschillende softwarecomponenten zich tot elkaar verhouden. Een goed doordachte architectuur vermindert de bedrijfsrisico's die gepaard gaan met het bouwen van een technische oplossing en slaat een brug tussen bedrijfs- en technische vereisten. t 3. Hoe is het AI systeem technisch geïmplementeerd? to 10. Is er nagedacht hoe het "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("De technische implementatie beschrijft hoe het AI systeem technisch binnen het ICT-landschap van")
    thisalinea.textcontent.append("de organisatie is geïntegreerd. De specifieke eisen van het AI-systeem aan hardware en software zijn")
    thisalinea.textcontent.append("gedocumenteerd zodat hier rekening mee gehouden kan worden bij het uitrollen en beheer van het")
    thisalinea.textcontent.append("systeem. Daarnaast wordt uit de systeemarchitectuur duidelijk hoe de verschillende softwarecomponenten")
    thisalinea.textcontent.append("zich tot elkaar verhouden. Een goed doordachte architectuur vermindert de bedrijfsrisico's die gepaard gaan")
    thisalinea.textcontent.append("met het bouwen van een technische oplossing en slaat een brug tussen bedrijfs- en technische vereisten.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "t 3. Hoe is het AI systeem technisch geïmplementeerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 80
    thisalinea.parentID = 79
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "t 3. Hoe is het AI systeem technisch geïmplementeerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("t 3. Hoe is het AI systeem technisch geïmplementeerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 10. Is er nagedacht hoe het AI-systeem past in de al bestaande technische- en ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 81
    thisalinea.parentID = 79
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "to 10. Is er nagedacht hoe het AI-systeem past in de al bestaande technische- en systeeminfrastructuur en zijn hier passende maatregelen voor genomen om deze uit te rollen (indien van toepassing)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 10. Is er nagedacht hoe het AI-systeem past in de al bestaande technische- en")
    thisalinea.textcontent.append("systeeminfrastructuur en zijn hier passende maatregelen voor genomen om deze uit te rollen")
    thisalinea.textcontent.append("(indien van toepassing)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 11. Hoe ziet de systeemarchitectuur eruit (hoe verhouden de softwarecomponenten zicht tot ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 82
    thisalinea.parentID = 79
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "to 11. Hoe ziet de systeemarchitectuur eruit (hoe verhouden de softwarecomponenten zicht tot elkaar)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 11. Hoe ziet de systeemarchitectuur eruit (hoe verhouden de softwarecomponenten zicht tot")
    thisalinea.textcontent.append("elkaar)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 12. Zijn eventuele specifieke hardware- en software-eisen gedocumenteerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 83
    thisalinea.parentID = 79
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "to 12. Zijn eventuele specifieke hardware- en software-eisen gedocumenteerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 12. Zijn eventuele specifieke hardware- en software-eisen gedocumenteerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Reproduceerbaarheid"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 84
    thisalinea.parentID = 65
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Bij reproduceerbaarheid kun je denken aan het vastleggen van welke data gebruikt zijn, hoe het model tot stand is gekomen, of wijzigingen in de data zijn bijgehouden, of uit dezelfde input(data) dezelfde resultaten voortvloeien, en of er bepaalde situaties of condities zijn waarin de output(data) beïnvloed kunnen worden. Reproduceerbaarheid gaat over trainen, valideren en testen. Reproduceerbaarheid hangt nauw samen met traceerbaarheid. Bij traceerbaarheid gaat het er voor- namelijk om dat de datasets en processen goed worden gedocumenteerd. Versiebeheer op de data, het en de training speelt daarin een belangrijke rol. t 4. Is het ai-systeem reproduceerbaar? Is er een proces "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Bij reproduceerbaarheid kun je denken aan het vastleggen van welke data gebruikt zijn, hoe het model")
    thisalinea.textcontent.append("tot stand is gekomen, of wijzigingen in de data zijn bijgehouden, of uit dezelfde input(data) dezelfde")
    thisalinea.textcontent.append("resultaten voortvloeien, en of er bepaalde situaties of condities zijn waarin de output(data) beïnvloed")
    thisalinea.textcontent.append("kunnen worden. Reproduceerbaarheid gaat over trainen, valideren en testen.")
    thisalinea.textcontent.append("Reproduceerbaarheid hangt nauw samen met traceerbaarheid. Bij traceerbaarheid gaat het er voor-")
    thisalinea.textcontent.append("namelijk om dat de datasets en processen goed worden gedocumenteerd. Versiebeheer op de data,")
    thisalinea.textcontent.append("het en de training speelt daarin een belangrijke rol.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "t 4. Is het ai-systeem reproduceerbaar? Is er een proces ingesteld om dit te meten? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 85
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "t 4. Is het ai-systeem reproduceerbaar? Is er een proces ingesteld om dit te meten? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("t 4. Is het ai-systeem reproduceerbaar? Is er een proces ingesteld om dit te meten?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 13. Kan je een verkregen output(data) nu of in de toekomst reconstrueren (dus bijvoorbeeld ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 86
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "to 13. Kan je een verkregen output(data) nu of in de toekomst reconstrueren (dus bijvoorbeeld zijn oude versies van het model, datasets en omstandigheden opgeslagen middels versiebeheer)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 13. Kan je een verkregen output(data) nu of in de toekomst reconstrueren (dus bijvoorbeeld zijn")
    thisalinea.textcontent.append("oude versies van het model, datasets en omstandigheden opgeslagen middels versiebeheer)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 14. Is het mogelijk om gegeven de parameters en een vaste seed het model ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 87
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "to 14. Is het mogelijk om gegeven de parameters en een vaste seed het model te reconstrueren? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 14. Is het mogelijk om gegeven de parameters en een vaste seed het model te reconstrueren?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 15. Is het ai-systeem aan de hand van documentatie op hoofdlijnen te reproduceren? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 88
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "to 15. Is het ai-systeem aan de hand van documentatie op hoofdlijnen te reproduceren? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 15. Is het ai-systeem aan de hand van documentatie op hoofdlijnen te reproduceren?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 16. Hoe worden de wijzigingen tijdens de levensduur van het systeem gedocumenteerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 89
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "to 16. Hoe worden de wijzigingen tijdens de levensduur van het systeem gedocumenteerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 16. Hoe worden de wijzigingen tijdens de levensduur van het systeem gedocumenteerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Uitlegbaarheid"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 90
    thisalinea.parentID = 65
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Technische uitlegbaarheid heeft te maken met het vermogen om zowel technische processen als daaraan gerelateerde menselijke beslissingen te kunnen begrijpen. Verder moet helder zijn welke verschillende ontwerpkeuzes zijn gemaakt en wat de rationale is voor het inzetten van het ai-systeem. Zie ook ‘Verantwoordingsplicht’ voor uitlegbaarheid richting betrokkenen. t 5. Is het ai-systeem voldoende uitlegbaar en te interpreteren voor de ontwikkelaars? to 17. Hoe heb je bij het ontwikkelen van het AI-systeem gekeken naar de uitlegbaarheid van het model? to 18. In hoeverre is het mogelijk om een verklaring te geven aan een externe AI-expert hoe het AI-systeem op een bepaalde "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Technische uitlegbaarheid heeft te maken met het vermogen om zowel technische processen als daaraan")
    thisalinea.textcontent.append("gerelateerde menselijke beslissingen te kunnen begrijpen. Verder moet helder zijn welke verschillende")
    thisalinea.textcontent.append("ontwerpkeuzes zijn gemaakt en wat de rationale is voor het inzetten van het ai-systeem. Zie ook")
    thisalinea.textcontent.append("‘Verantwoordingsplicht’ voor uitlegbaarheid richting betrokkenen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "t 5. Is het ai-systeem voldoende uitlegbaar en te interpreteren voor de ontwikkelaars? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 91
    thisalinea.parentID = 90
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "t 5. Is het ai-systeem voldoende uitlegbaar en te interpreteren voor de ontwikkelaars? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("t 5. Is het ai-systeem voldoende uitlegbaar en te interpreteren voor de ontwikkelaars?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 17. Hoe heb je bij het ontwikkelen van het AI-systeem gekeken naar de uitlegbaarheid ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 92
    thisalinea.parentID = 90
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "to 17. Hoe heb je bij het ontwikkelen van het AI-systeem gekeken naar de uitlegbaarheid van het model? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 17. Hoe heb je bij het ontwikkelen van het AI-systeem gekeken naar de uitlegbaarheid van het")
    thisalinea.textcontent.append("model?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 18. In hoeverre is het mogelijk om een verklaring te geven aan een externe ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 93
    thisalinea.parentID = 90
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "to 18. In hoeverre is het mogelijk om een verklaring te geven aan een externe AI-expert hoe het AI-systeem op een bepaalde manier werkt (zie ook ‘Uitlegbaarheid’)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 18. In hoeverre is het mogelijk om een verklaring te geven aan een externe AI-expert hoe het")
    thisalinea.textcontent.append("AI-systeem op een bepaalde manier werkt (zie ook ‘Uitlegbaarheid’)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "to 19. Is de benodigde deskundigheid voor het beheer van AI-systeem gedocumenteerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 94
    thisalinea.parentID = 90
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "to 19. Is de benodigde deskundigheid voor het beheer van AI-systeem gedocumenteerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("to 19. Is de benodigde deskundigheid voor het beheer van AI-systeem gedocumenteerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Data governance"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 95
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Data governance gaat over een (bestuurlijke) werkwijze rondom data met betrekking tot toegang, eigenaarschap, bruikbaarheid, integriteit en veiligheid. Daarnaast is er aandacht voor de kwaliteit van de data die wordt gebruikt. Onder data governance valt ook privacy. Privacy is een van de fundamentele rechten van de mens, die mogelijk door AI kan worden aangetast. Het is daarom belangrijk dat er adequate data governance en bescherming van persoonsgegevens conform de Algemene Verordening Gegevensbescherming (AVG) is. Voor AI-systemen is het essentieel om informatiebeveiligings- en privacyrisico’s inzichtelijk te maken, deze risico’s terug te brengen naar een acceptabel niveau en periodiek (technisch) te laten "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Data governance gaat over een (bestuurlijke) werkwijze rondom data met betrekking tot toegang,")
    thisalinea.textcontent.append("eigenaarschap, bruikbaarheid, integriteit en veiligheid. Daarnaast is er aandacht voor de kwaliteit van de")
    thisalinea.textcontent.append("data die wordt gebruikt.")
    thisalinea.textcontent.append("Onder data governance valt ook privacy. Privacy is een van de fundamentele rechten van de mens, die")
    thisalinea.textcontent.append("mogelijk door AI kan worden aangetast. Het is daarom belangrijk dat er adequate data governance en")
    thisalinea.textcontent.append("bescherming van persoonsgegevens conform de Algemene Verordening Gegevensbescherming (AVG) is.")
    thisalinea.textcontent.append("Voor AI-systemen is het essentieel om informatiebeveiligings- en privacyrisico’s inzichtelijk te maken,")
    thisalinea.textcontent.append("deze risico’s terug te brengen naar een acceptabel niveau en periodiek (technisch) te laten testen (bv.")
    thisalinea.textcontent.append("door het uitvoeren van een pentest). Om dit te realiseren moet het risicomanagementproces voor")
    thisalinea.textcontent.append("informatiebeveiliging en privacy van de organisatie worden doorlopen voor de AI-implementatie.")
    thisalinea.textcontent.append("Producten die daarbij onder meer moeten worden opgeleverd zijn: BIV-classificatie (BIA), implementatie")
    thisalinea.textcontent.append("van en toets aan de BIO, DPIA (in geval van verwerking persoonsgegevens), security testen en indien")
    thisalinea.textcontent.append("noodzakelijk een verbeterplan.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Kwaliteit en integriteit van data"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 96
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Datakwaliteit is essentieel voor de werking van een ai-systeem. Verzamelde gegevens kunnen bijvoorbeeld sociaal geconstrueerde bias, onjuistheden, fouten en vergissingen bevatten (zie ook ‘Bias’). Dit moet worden geadresseerd voordat er verder met deze data wordt gewerkt. De datasets en de werkwijze moeten worden getest en gedocumenteerd bij iedere stap: training, testen, uitrolfase en operationele fase. Dit geldt ook voor AI-systemen die niet intern gebouwd zijn, maar elders zijn verworven. De archiefwet9 stelt eisen aan de manier van opslaan en bewaartermijn van data. d 1. Hoe wordt de kwaliteit van de data gewaarborgd?8★ do 1. Is de gebruikte data noodzakelijk voor "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Datakwaliteit is essentieel voor de werking van een ai-systeem. Verzamelde gegevens kunnen bijvoorbeeld")
    thisalinea.textcontent.append("sociaal geconstrueerde bias, onjuistheden, fouten en vergissingen bevatten (zie ook ‘Bias’). Dit moet")
    thisalinea.textcontent.append("worden geadresseerd voordat er verder met deze data wordt gewerkt. De datasets en de werkwijze moeten")
    thisalinea.textcontent.append("worden getest en gedocumenteerd bij iedere stap: training, testen, uitrolfase en operationele fase. Dit geldt")
    thisalinea.textcontent.append("ook voor AI-systemen die niet intern gebouwd zijn, maar elders zijn verworven. De archiefwet9 stelt eisen")
    thisalinea.textcontent.append("aan de manier van opslaan en bewaartermijn van data.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "d 1. Hoe wordt de kwaliteit van de data gewaarborgd?8★ "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 97
    thisalinea.parentID = 96
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "d 1. Hoe wordt de kwaliteit van de data gewaarborgd?8★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("d 1. Hoe wordt de kwaliteit van de data gewaarborgd?8★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Overkoepelend"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 98
    thisalinea.parentID = 96
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "do 1. Is de gebruikte data noodzakelijk voor het ai-systeem? do 2. Hoe voorkom je onbedoelde verdubbelingen van data? do 3. Is het mogelijk om de trainings- en testgegevens te actualiseren als de situatie daar om vraagt? Wanneer besluit je het AI-systeem te her-trainen, tijdelijk stop te zetten, of door te ontwikkelen?10  Input(data) do 4. Voldoet de data aan de aannames van het model? do 5. Op welke manier is de input(data) die wordt gebruikt in het AI-systeem verzameld en samengevoegd? do 6. Hoe wordt de data gelabeld? do 7. Welke factoren hebben invloed op de kwaliteit van de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 1. Is de gebruikte data noodzakelijk voor het ai-systeem? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 99
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "do 1. Is de gebruikte data noodzakelijk voor het ai-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 1. Is de gebruikte data noodzakelijk voor het ai-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 2. Hoe voorkom je onbedoelde verdubbelingen van data? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 100
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "do 2. Hoe voorkom je onbedoelde verdubbelingen van data? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 2. Hoe voorkom je onbedoelde verdubbelingen van data?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 3. Is het mogelijk om de trainings- en testgegevens te actualiseren als de situatie ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 101
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "do 3. Is het mogelijk om de trainings- en testgegevens te actualiseren als de situatie daar om vraagt? Wanneer besluit je het AI-systeem te her-trainen, tijdelijk stop te zetten, of door te ontwikkelen?10  Input(data) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 3. Is het mogelijk om de trainings- en testgegevens te actualiseren als de situatie daar om")
    thisalinea.textcontent.append("vraagt? Wanneer besluit je het AI-systeem te her-trainen, tijdelijk stop te zetten, of door te")
    thisalinea.textcontent.append("ontwikkelen?10  Input(data)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 4. Voldoet de data aan de aannames van het model? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 102
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "do 4. Voldoet de data aan de aannames van het model? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 4. Voldoet de data aan de aannames van het model?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 5. Op welke manier is de input(data) die wordt gebruikt in het AI-systeem verzameld ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 103
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "do 5. Op welke manier is de input(data) die wordt gebruikt in het AI-systeem verzameld en samengevoegd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 5. Op welke manier is de input(data) die wordt gebruikt in het AI-systeem verzameld en")
    thisalinea.textcontent.append("samengevoegd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 6. Hoe wordt de data gelabeld? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 104
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "do 6. Hoe wordt de data gelabeld? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 6. Hoe wordt de data gelabeld?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 7. Welke factoren hebben invloed op de kwaliteit van de input(data)? En wat kan ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 105
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "do 7. Welke factoren hebben invloed op de kwaliteit van de input(data)? En wat kan je daaraan doen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 7. Welke factoren hebben invloed op de kwaliteit van de input(data)? En wat kan je daaraan")
    thisalinea.textcontent.append("doen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 8. Is de input(data) getoetst op veranderingen die zich voordoen tijdens trainen, testen en ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 106
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "do 8. Is de input(data) getoetst op veranderingen die zich voordoen tijdens trainen, testen en evalueren? Ook door de tijd heen tijdens het gebruik van het algoritme? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 8. Is de input(data) getoetst op veranderingen die zich voordoen tijdens trainen, testen en")
    thisalinea.textcontent.append("evalueren? Ook door de tijd heen tijdens het gebruik van het algoritme?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "Output(data)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 107
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 9. Indien output(data) wordt gebruikt als nieuwe input, hoe wordt de output(data) opgeslagen ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 108
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "do 9. Indien output(data) wordt gebruikt als nieuwe input, hoe wordt de output(data) opgeslagen (denk aan een feedbackloop)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 9. Indien output(data) wordt gebruikt als nieuwe input, hoe wordt de output(data) opgeslagen")
    thisalinea.textcontent.append("(denk aan een feedbackloop)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 10. Hoe zorg je ervoor dat de output(data) tijdig beschikbaar is? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 109
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "do 10. Hoe zorg je ervoor dat de output(data) tijdig beschikbaar is? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 10. Hoe zorg je ervoor dat de output(data) tijdig beschikbaar is?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Privacy en gegevensbescherming"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 110
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Privacy en de bescherming van gegevens moeten gewaarborgd zijn gedurende de hele levenscyclus van het ai-systeem. Met digitaal vastgelegde gegevens van menselijk gedrag kunnen AI-systemen wellicht leeftijd, geslacht en politieke, religieuze of seksuele voorkeuren afleiden. Let erop dat wanneer je persoonsgegevens gebruikt, deze niet gebruikt kunnen worden om te discrimineren, zie ook ‘Bias’. Naast persoonsgegevens kunnen er ook andere vertrouwelijke gegevens gebruikt worden die niet zomaar openbaar gemaakt mogen worden. Dit geldt bijvoorbeeld voor het gebruik van vertrouwelijke informatie als gerubriceerde informatie of bedrijfsgeheimen. Ook deze data moet goed beschermd zijn. De AI Verordening biedt aanvullende regels voor het gebruik "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Privacy en de bescherming van gegevens moeten gewaarborgd zijn gedurende de hele levenscyclus van het")
    thisalinea.textcontent.append("ai-systeem. Met digitaal vastgelegde gegevens van menselijk gedrag kunnen AI-systemen wellicht leeftijd,")
    thisalinea.textcontent.append("geslacht en politieke, religieuze of seksuele voorkeuren afleiden. Let erop dat wanneer je persoonsgegevens")
    thisalinea.textcontent.append("gebruikt, deze niet gebruikt kunnen worden om te discrimineren, zie ook ‘Bias’.")
    thisalinea.textcontent.append("Naast persoonsgegevens kunnen er ook andere vertrouwelijke gegevens gebruikt worden die niet zomaar")
    thisalinea.textcontent.append("openbaar gemaakt mogen worden. Dit geldt bijvoorbeeld voor het gebruik van vertrouwelijke informatie")
    thisalinea.textcontent.append("als gerubriceerde informatie of bedrijfsgeheimen. Ook deze data moet goed beschermd zijn. De AI")
    thisalinea.textcontent.append("Verordening biedt aanvullende regels voor het gebruik van (persoons)gegevens in AI-systemen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "d 2. Hoe wordt er omgegaan met persoonsgegevens of vertrouwelijke gegevens? (Denk aan de ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 111
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "d 2. Hoe wordt er omgegaan met persoonsgegevens of vertrouwelijke gegevens? (Denk aan de DPIA) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("d 2. Hoe wordt er omgegaan met persoonsgegevens of vertrouwelijke gegevens? (Denk aan de")
    thisalinea.textcontent.append("DPIA)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Met betrekking tot persoonsgegevens"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 112
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "do 11. Werkt het ai-systeem met persoonsgegevens11 (is de AVG van toepassing)? Zo ja, vul de volgende vragen ook in. Zo nee, ga verder bij ‘met betrekking tot vertrouwelijke gegevens’. do 12. Is de output van het AI-systeem tot personen te herleiden (is de AVG van toepassing)? Zo ja, vul dan de volgende vragen ook in. do 13. Zijn er verregaande beschermingsmaatregelen genomen om de persoonsgegevens te beveiligen?12★ do 14. Zijn functionarissen betrokken, zoals de functionaris gegevensbescherming, privacy adviseur, informatiebeveiliger, Chief Information Officer, etc.? do 15. Hoe vaak wordt de kwaliteit en de noodzakelijkheid van de verwerking van persoonsgegevens geëvalueerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 11. Werkt het ai-systeem met persoonsgegevens11 (is de AVG van toepassing)? Zo ja, vul ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 113
    thisalinea.parentID = 112
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "do 11. Werkt het ai-systeem met persoonsgegevens11 (is de AVG van toepassing)? Zo ja, vul de volgende vragen ook in. Zo nee, ga verder bij ‘met betrekking tot vertrouwelijke gegevens’. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 11. Werkt het ai-systeem met persoonsgegevens11 (is de AVG van toepassing)? Zo ja, vul de")
    thisalinea.textcontent.append("volgende vragen ook in. Zo nee, ga verder bij ‘met betrekking tot vertrouwelijke gegevens’.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 12. Is de output van het AI-systeem tot personen te herleiden (is de AVG ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 114
    thisalinea.parentID = 112
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "do 12. Is de output van het AI-systeem tot personen te herleiden (is de AVG van toepassing)? Zo ja, vul dan de volgende vragen ook in. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 12. Is de output van het AI-systeem tot personen te herleiden (is de AVG van toepassing)?")
    thisalinea.textcontent.append("Zo ja, vul dan de volgende vragen ook in.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 13. Zijn er verregaande beschermingsmaatregelen genomen om de persoonsgegevens te ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 115
    thisalinea.parentID = 112
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "do 13. Zijn er verregaande beschermingsmaatregelen genomen om de persoonsgegevens te beveiligen?12★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 13. Zijn er verregaande beschermingsmaatregelen genomen om de persoonsgegevens te")
    thisalinea.textcontent.append("beveiligen?12★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 14. Zijn functionarissen betrokken, zoals de functionaris gegevensbescherming, privacy adviseur, ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 116
    thisalinea.parentID = 112
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "do 14. Zijn functionarissen betrokken, zoals de functionaris gegevensbescherming, privacy adviseur, informatiebeveiliger, Chief Information Officer, etc.? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 14. Zijn functionarissen betrokken, zoals de functionaris gegevensbescherming, privacy adviseur,")
    thisalinea.textcontent.append("informatiebeveiliger, Chief Information Officer, etc.?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 15. Hoe vaak wordt de kwaliteit en de noodzakelijkheid van de verwerking van persoonsgegevens ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 117
    thisalinea.parentID = 112
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "do 15. Hoe vaak wordt de kwaliteit en de noodzakelijkheid van de verwerking van persoonsgegevens geëvalueerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 15. Hoe vaak wordt de kwaliteit en de noodzakelijkheid van de verwerking van persoonsgegevens")
    thisalinea.textcontent.append("geëvalueerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 16. Is er aandacht besteed aan rechten van derden met betrekking tot verspreiding van ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 118
    thisalinea.parentID = 112
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "do 16. Is er aandacht besteed aan rechten van derden met betrekking tot verspreiding van informatie over het AI-systeem? ★★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 16. Is er aandacht besteed aan rechten van derden met betrekking tot verspreiding van informatie")
    thisalinea.textcontent.append("over het AI-systeem? ★★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Met betrekking tot vertrouwelijke gegevens (niet zijnde persoonsgegevens)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 119
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "do 17. Worden vertrouwelijke gegevens gebruikt of opgeslagen? do 18. Hoe wordt de veiligheid van deze informatie gewaarborgd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 17. Worden vertrouwelijke gegevens gebruikt of opgeslagen? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 120
    thisalinea.parentID = 119
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "do 17. Worden vertrouwelijke gegevens gebruikt of opgeslagen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 17. Worden vertrouwelijke gegevens gebruikt of opgeslagen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "do 18. Hoe wordt de veiligheid van deze informatie gewaarborgd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 121
    thisalinea.parentID = 119
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "do 18. Hoe wordt de veiligheid van deze informatie gewaarborgd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("do 18. Hoe wordt de veiligheid van deze informatie gewaarborgd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Risicobeheer"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 122
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "Het is van belang dat mogelijke risico’s in de gaten worden gehouden. Wanneer risico’s niet zijn voorzien, kan een ai-systeem tot onbetrouwbare resultaten komen. Dit kan schade veroorzaken. Het beginsel van preventie moet ervoor zorgen dat schade zoveel mogelijk wordt beperkt. Schade kan opgelopen worden door slecht functioneren van het AI-systeem, of bijvoorbeeld door hackaanvallen van buitenaf. Bij het ontwikkelen en in gebruik nemen van een ai-systeem komen gevaren kijken, die in deze AIIA zoveel mogelijk ingekaderd worden. Toch kunnen zich alsnog onvoorziene problemen voordoen. Het is belangrijk om vast te stellen hoe je met deze potentiële gevaren omgaat. Dat "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Het is van belang dat mogelijke risico’s in de gaten worden gehouden. Wanneer risico’s niet zijn voorzien,")
    thisalinea.textcontent.append("kan een ai-systeem tot onbetrouwbare resultaten komen. Dit kan schade veroorzaken. Het beginsel van")
    thisalinea.textcontent.append("preventie moet ervoor zorgen dat schade zoveel mogelijk wordt beperkt. Schade kan opgelopen worden")
    thisalinea.textcontent.append("door slecht functioneren van het AI-systeem, of bijvoorbeeld door hackaanvallen van buitenaf.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Risicobeheersing"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 123
    thisalinea.parentID = 122
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Bij het ontwikkelen en in gebruik nemen van een ai-systeem komen gevaren kijken, die in deze AIIA zoveel mogelijk ingekaderd worden. Toch kunnen zich alsnog onvoorziene problemen voordoen. Het is belangrijk om vast te stellen hoe je met deze potentiële gevaren omgaat. Dat betekent ook dat er mechanismes ingesteld moeten worden om risico’s te beheersen, en dat deze mechanismen goed zijn getoetst. Denk aan het voorkomen van data vergiftiging, de mate van beheersmaatregelen en de beveiliging van de bewaarplaats van uitkomsten. Daarnaast moet er rekening gehouden worden met het feit dat zich nieuwe risico’s kunnen voordoen na invoering van het "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Bij het ontwikkelen en in gebruik nemen van een ai-systeem komen gevaren kijken, die in deze AIIA")
    thisalinea.textcontent.append("zoveel mogelijk ingekaderd worden. Toch kunnen zich alsnog onvoorziene problemen voordoen. Het")
    thisalinea.textcontent.append("is belangrijk om vast te stellen hoe je met deze potentiële gevaren omgaat. Dat betekent ook dat er")
    thisalinea.textcontent.append("mechanismes ingesteld moeten worden om risico’s te beheersen, en dat deze mechanismen goed zijn")
    thisalinea.textcontent.append("getoetst. Denk aan het voorkomen van data vergiftiging, de mate van beheersmaatregelen en de beveiliging")
    thisalinea.textcontent.append("van de bewaarplaats van uitkomsten. Daarnaast moet er rekening gehouden worden met het feit dat zich")
    thisalinea.textcontent.append("nieuwe risico’s kunnen voordoen na invoering van het AI-systeem. De risicobeheersmaat-regelen moeten")
    thisalinea.textcontent.append("dus periodiek gecontroleerd worden.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "r 1. Hoe is het AI-systeem getest op de passende risicobeheersmaatregelen?13  "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 124
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "r 1. Hoe is het AI-systeem getest op de passende risicobeheersmaatregelen?13  "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("r 1. Hoe is het AI-systeem getest op de passende risicobeheersmaatregelen?13 ")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 1. Hoe is de toegang tot het AI-systeem en diens componenten ingericht? (Denk aan ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 125
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "ro 1. Hoe is de toegang tot het AI-systeem en diens componenten ingericht? (Denk aan de Generieke IT-beheersmaatregelen) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 1. Hoe is de toegang tot het AI-systeem en diens componenten ingericht? (Denk aan de")
    thisalinea.textcontent.append("Generieke IT-beheersmaatregelen)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 2. Hoe is het ai-systeem getest op het beoogde doel voordat het in gebruik ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 126
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "ro 2. Hoe is het ai-systeem getest op het beoogde doel voordat het in gebruik wordt genomen?14 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 2. Hoe is het ai-systeem getest op het beoogde doel voordat het in gebruik wordt genomen?14")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 3. Is het waarschijnlijk dat kwetsbare groepen (zoals kinderen) toegang zullen hebben tot het ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 127
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "ro 3. Is het waarschijnlijk dat kwetsbare groepen (zoals kinderen) toegang zullen hebben tot het AI-systeem? In dat geval moeten de risicobeheersmaatregelen extra worden aangescherpt.15 ★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 3. Is het waarschijnlijk dat kwetsbare groepen (zoals kinderen) toegang zullen hebben tot het")
    thisalinea.textcontent.append("AI-systeem? In dat geval moeten de risicobeheersmaatregelen extra worden aangescherpt.15 ★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 4. Zijn er buiten de standaard beveiligingsmaatregelingen van IenW extra maatregelen genomen ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 128
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "ro 4. Zijn er buiten de standaard beveiligingsmaatregelingen van IenW extra maatregelen genomen om het AI-systeem te beveiligen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 4. Zijn er buiten de standaard beveiligingsmaatregelingen van IenW extra maatregelen genomen")
    thisalinea.textcontent.append("om het AI-systeem te beveiligen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 5. Hoe wordt het alternatieve plan als er problemen met het ai-systeem zijn in ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 129
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "ro 5. Hoe wordt het alternatieve plan als er problemen met het ai-systeem zijn in werking gezet? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 5. Hoe wordt het alternatieve plan als er problemen met het ai-systeem zijn in werking gezet?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 6. Is de correctheid van de implementatie aangetoond? Denk hierbij bijvoorbeeld aan unit- ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 130
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "ro 6. Is de correctheid van de implementatie aangetoond? Denk hierbij bijvoorbeeld aan unit- integratie- en end-to-end tests, indien van toepassing. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 6. Is de correctheid van de implementatie aangetoond? Denk hierbij bijvoorbeeld aan unit-")
    thisalinea.textcontent.append("integratie- en end-to-end tests, indien van toepassing.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 7. Hoe kan het AI-systeem interageren met andere hardware of software (indien van ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 131
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "ro 7. Hoe kan het AI-systeem interageren met andere hardware of software (indien van toepassing)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 7. Hoe kan het AI-systeem interageren met andere hardware of software (indien van")
    thisalinea.textcontent.append("toepassing)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Alternatieve werkwijze"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 132
    thisalinea.parentID = 122
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Het is wenselijk om een plan te hebben voor wanneer er problemen optreden met het ai-systeem. Dit betekent dat er een alternatieve werkwijze beschikbaar moet zijn in het geval dat er problemen met de werking van het systeem zijn. Denk aan de mogelijkheid om van een machine learning naar een beperkter rule-based model terug te schakelen. Het is goed om er bewust van te zijn dat een mens als expert zich niet op dezelfde manier ontwikkelt als een AI-systeem. Denk hierbij aan het effect van de rekenmachine op onze vaardigheid hoofdrekenen. Een alternatieve werkwijze moet hierop ingespeeld zijn. Wat is "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Het is wenselijk om een plan te hebben voor wanneer er problemen optreden met het ai-systeem. Dit")
    thisalinea.textcontent.append("betekent dat er een alternatieve werkwijze beschikbaar moet zijn in het geval dat er problemen met de")
    thisalinea.textcontent.append("werking van het systeem zijn. Denk aan de mogelijkheid om van een machine learning naar een beperkter")
    thisalinea.textcontent.append("rule-based model terug te schakelen.")
    thisalinea.textcontent.append("Het is goed om er bewust van te zijn dat een mens als expert zich niet op dezelfde manier ontwikkelt als")
    thisalinea.textcontent.append("een AI-systeem. Denk hierbij aan het effect van de rekenmachine op onze vaardigheid hoofdrekenen. Een")
    thisalinea.textcontent.append("alternatieve werkwijze moet hierop ingespeeld zijn. Wat is de impact in het geval dat het AI-systeem foute")
    thisalinea.textcontent.append("resultaten genereert?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "r 2. Wat is het plan als er problemen met de werking van het ai-systeem ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 133
    thisalinea.parentID = 132
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "r 2. Wat is het plan als er problemen met de werking van het ai-systeem zijn? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("r 2. Wat is het plan als er problemen met de werking van het ai-systeem zijn?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 8. Wat is de impact als het AI-systeem uitvalt? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 134
    thisalinea.parentID = 132
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "ro 8. Wat is de impact als het AI-systeem uitvalt? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 8. Wat is de impact als het AI-systeem uitvalt?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 9. Zie hierboven het voorbeeld over de rekenmachine. Wat is een equivalent effect wat ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 135
    thisalinea.parentID = 132
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "ro 9. Zie hierboven het voorbeeld over de rekenmachine. Wat is een equivalent effect wat kan optreden als het AI-systeem in gebruik wordt genomen, en is dit wenselijk? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 9. Zie hierboven het voorbeeld over de rekenmachine. Wat is een equivalent effect wat kan")
    thisalinea.textcontent.append("optreden als het AI-systeem in gebruik wordt genomen, en is dit wenselijk?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 10. Is het ai-systeem bestand tegen fouten of onregelmatigheden van interactie met natuurlijke ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 136
    thisalinea.parentID = 132
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "ro 10. Is het ai-systeem bestand tegen fouten of onregelmatigheden van interactie met natuurlijke personen of andere systemen?16★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 10. Is het ai-systeem bestand tegen fouten of onregelmatigheden van interactie met natuurlijke")
    thisalinea.textcontent.append("personen of andere systemen?16★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Hackaanvallen en corruptie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 137
    thisalinea.parentID = 122
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Informatiebeveiligingsrisico zoals hackaanvallen en corruptie moeten zoveel mogelijk worden beheerst. De te voorziene risico’s moeten ingekaderd worden door deze inzichtelijk te maken via het risicomanagementproces van de organisatie. Daaronder vallen onder meer het in kaart brengen van BIV- classificatie, rubriceringsniveau van informatie, implementatie van BIO-maatregelen, security testen en, indien het beveiligingsniveau van de BIO niet voldoet, het ev. uitvoeren van een aanvullende (technische) risico-analyse. Ook is van belang om te kijken of fouten en onregelmatigheden te detecteren en technisch af te vangen. r 3. Op welke manier worden informatiebeveiligingsrisico’s inzichtelijk gemaakt, teruggebracht naar een acceptabel niveau en (technisch) getest? ro "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Informatiebeveiligingsrisico zoals hackaanvallen en corruptie moeten zoveel mogelijk worden")
    thisalinea.textcontent.append("beheerst. De te voorziene risico’s moeten ingekaderd worden door deze inzichtelijk te maken via het")
    thisalinea.textcontent.append("risicomanagementproces van de organisatie. Daaronder vallen onder meer het in kaart brengen van BIV-")
    thisalinea.textcontent.append("classificatie, rubriceringsniveau van informatie, implementatie van BIO-maatregelen, security testen en,")
    thisalinea.textcontent.append("indien het beveiligingsniveau van de BIO niet voldoet, het ev. uitvoeren van een aanvullende (technische)")
    thisalinea.textcontent.append("risico-analyse. Ook is van belang om te kijken of fouten en onregelmatigheden te detecteren en technisch")
    thisalinea.textcontent.append("af te vangen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "r 3. Op welke manier worden informatiebeveiligingsrisico’s inzichtelijk gemaakt, teruggebracht ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 138
    thisalinea.parentID = 137
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "r 3. Op welke manier worden informatiebeveiligingsrisico’s inzichtelijk gemaakt, teruggebracht naar een acceptabel niveau en (technisch) getest? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("r 3. Op welke manier worden informatiebeveiligingsrisico’s inzichtelijk gemaakt, teruggebracht")
    thisalinea.textcontent.append("naar een acceptabel niveau en (technisch) getest?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 11. Hoe wordt er voorkomen dat ongeautoriseerde derden gebruik kunnen maken van ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 139
    thisalinea.parentID = 137
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "ro 11. Hoe wordt er voorkomen dat ongeautoriseerde derden gebruik kunnen maken van kwetsbaarheden van het AI-systeem?17 ★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 11. Hoe wordt er voorkomen dat ongeautoriseerde derden gebruik kunnen maken van")
    thisalinea.textcontent.append("kwetsbaarheden van het AI-systeem?17 ★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 12. Wat is de impact als derden ongewenst toegang hebben tot de broncode, data ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 140
    thisalinea.parentID = 137
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "ro 12. Wat is de impact als derden ongewenst toegang hebben tot de broncode, data of uitkomsten van het AI- systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 12. Wat is de impact als derden ongewenst toegang hebben tot de broncode, data of uitkomsten")
    thisalinea.textcontent.append("van het AI- systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 13. Kunnen mensen misbruik maken van het feit dat er een AI-systeem wordt ingezet ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 141
    thisalinea.parentID = 137
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "ro 13. Kunnen mensen misbruik maken van het feit dat er een AI-systeem wordt ingezet in plaats van een menselijke beslissing? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 13. Kunnen mensen misbruik maken van het feit dat er een AI-systeem wordt ingezet in plaats")
    thisalinea.textcontent.append("van een menselijke beslissing?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "ro 14. Hoe wordt er geregistreerd wie er gebruik maakt van het AI-systeem en hoe ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 142
    thisalinea.parentID = 137
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "ro 14. Hoe wordt er geregistreerd wie er gebruik maakt van het AI-systeem en hoe lang?18 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("ro 14. Hoe wordt er geregistreerd wie er gebruik maakt van het AI-systeem en hoe lang?18")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Verantwoordingsplicht"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 143
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "Voor handelen binnen de Rijksoverheid moet verantwoording worden afgelegd binnen de organisatie, naar de Tweede Kamer en naar de samenleving. AI staat op dit moment extra in de belangstelling. De techniek wordt steeds vaker toegepast binnen de Rijksoverheid, maar er zijn ook veel zorgen over de ethische afwegingen bij het inzetten van AI. Daarom moeten er goede mechanismes ingesteld worden om de verantwoordelijkheid voor AI-systemen en de resultaten daarvan te kunnen garanderen. Deze sectie gaat over twee vormen van communicatie naar eindgebruikers. Ten eerste, eindgebruikers moeten ervan op de hoogte worden gesteld dat ze met de resultaten van een ai-systeem "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Voor handelen binnen de Rijksoverheid moet verantwoording worden afgelegd binnen de organisatie, naar")
    thisalinea.textcontent.append("de Tweede Kamer en naar de samenleving. AI staat op dit moment extra in de belangstelling. De techniek")
    thisalinea.textcontent.append("wordt steeds vaker toegepast binnen de Rijksoverheid, maar er zijn ook veel zorgen over de ethische")
    thisalinea.textcontent.append("afwegingen bij het inzetten van AI. Daarom moeten er goede mechanismes ingesteld worden om de")
    thisalinea.textcontent.append("verantwoordelijkheid voor AI-systemen en de resultaten daarvan te kunnen garanderen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Communicatie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 144
    thisalinea.parentID = 143
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Deze sectie gaat over twee vormen van communicatie naar eindgebruikers. Ten eerste, eindgebruikers moeten ervan op de hoogte worden gesteld dat ze met de resultaten van een ai-systeem te maken hebben. Ten tweede, eindgebruikers hebben te allen tijde het recht om te weten hoe een algoritme de uitkomsten van een AI-systeem bepaalt. Dat betekent ook dat het doel en beperkingen van het AI-systeem duidelijk en eerlijk moeten worden gecommuniceerd. Zowel technische processen als daaraan gerelateerde menselijke beslissingen moeten begrijpelijk zijn en opgevraagd kunnen worden. Bijvoorbeeld door het aanwijzen van een contactpersoon met inhoudelijke kennis over het AI-systeem. Gezien het zelflerende "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Deze sectie gaat over twee vormen van communicatie naar eindgebruikers. Ten eerste, eindgebruikers")
    thisalinea.textcontent.append("moeten ervan op de hoogte worden gesteld dat ze met de resultaten van een ai-systeem te maken hebben.")
    thisalinea.textcontent.append("Ten tweede, eindgebruikers hebben te allen tijde het recht om te weten hoe een algoritme de uitkomsten")
    thisalinea.textcontent.append("van een AI-systeem bepaalt. Dat betekent ook dat het doel en beperkingen van het AI-systeem duidelijk en")
    thisalinea.textcontent.append("eerlijk moeten worden gecommuniceerd. Zowel technische processen als daaraan gerelateerde menselijke")
    thisalinea.textcontent.append("beslissingen moeten begrijpelijk zijn en opgevraagd kunnen worden. Bijvoorbeeld door het aanwijzen van")
    thisalinea.textcontent.append("een contactpersoon met inhoudelijke kennis over het AI-systeem. Gezien het zelflerende karakter van AI")
    thisalinea.textcontent.append("kan dit niet altijd 100% te herleiden zijn. Wel moet in ieder geval mogelijk zijn om gepaste uitleg te geven")
    thisalinea.textcontent.append("over het proces aan eindgebruikers.")
    thisalinea.textcontent.append("Daarnaast is het onder elke vraag binnen deze AIIA belangrijk dat burgers informatie kunnen opvragen over")
    thisalinea.textcontent.append("het AI-systeem. Men moet in staat gesteld worden om resultaten van het AI-systeem te kunnen betwisten.")
    thisalinea.textcontent.append("Dat betekent ook dat data en de omstandigheden waarin de data ter beschikking zijn gesteld bewaard")
    thisalinea.textcontent.append("moeten worden (zie Archivering).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "v 1. Ben je transparant richting betrokkenen en eindgebruikers over de beperkingen en werking van ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 145
    thisalinea.parentID = 144
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "v 1. Ben je transparant richting betrokkenen en eindgebruikers over de beperkingen en werking van het AI-systeem? En blijven deze voldoende onder de aandacht zolang ze bestaan "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("v 1. Ben je transparant richting betrokkenen en eindgebruikers over de beperkingen en werking van")
    thisalinea.textcontent.append("het AI-systeem? En blijven deze voldoende onder de aandacht zolang ze bestaan")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "v 2. Worden er mechanismes ingesteld waarin eindgebruikers opmerkingen over het systeem ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 146
    thisalinea.parentID = 144
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "v 2. Worden er mechanismes ingesteld waarin eindgebruikers opmerkingen over het systeem (data, techniek, doelgroep, etc.) kunnen maken? En hoe of wanneer worde deze meldingen gewaarborgd (geanalyseerd en gevolgd)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("v 2. Worden er mechanismes ingesteld waarin eindgebruikers opmerkingen over het systeem")
    thisalinea.textcontent.append("(data, techniek, doelgroep, etc.) kunnen maken? En hoe of wanneer worde deze meldingen")
    thisalinea.textcontent.append("gewaarborgd (geanalyseerd en gevolgd)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Communicatie met het ai-systeem"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 147
    thisalinea.parentID = 144
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 1. Wordt er aan de eindgebruiker en betrokkenen van het AI-systeem gecommuniceerd dat de resultaten gegenereerd worden door een AI-systeem en wat dat voor hen betekent vo 2. Zijn er eindgebruiksinstructies opgesteld? Deze moeten minstens het volgende bevatten:19 - De naam en contactgegevens van de aanbieder; - Kenmerken, capaciteiten en beperkingen; - Mogelijke toekomstige wijzigingen; - Menselijk toezicht; - Verwachte levensduur. vo 3. Wat zijn de potentiële (psychologische) bijwerkingen zoals het risico op verwarring, voorkeur of cognitieve vermoeidheid van de eindgebruiker bij het gebruik maken van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 1. Wordt er aan de eindgebruiker en betrokkenen van het AI-systeem gecommuniceerd dat de ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 148
    thisalinea.parentID = 147
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 1. Wordt er aan de eindgebruiker en betrokkenen van het AI-systeem gecommuniceerd dat de resultaten gegenereerd worden door een AI-systeem en wat dat voor hen betekent "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 1. Wordt er aan de eindgebruiker en betrokkenen van het AI-systeem gecommuniceerd dat de")
    thisalinea.textcontent.append("resultaten gegenereerd worden door een AI-systeem en wat dat voor hen betekent")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 2. Zijn er eindgebruiksinstructies opgesteld? Deze moeten minstens het volgende bevatten:19 "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 149
    thisalinea.parentID = 147
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 2. Zijn er eindgebruiksinstructies opgesteld? Deze moeten minstens het volgende bevatten:19 - De naam en contactgegevens van de aanbieder; - Kenmerken, capaciteiten en beperkingen; - Mogelijke toekomstige wijzigingen; - Menselijk toezicht; - Verwachte levensduur. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 2. Zijn er eindgebruiksinstructies opgesteld? Deze moeten minstens het volgende bevatten:19")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "- De naam en contactgegevens van de aanbieder; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 150
    thisalinea.parentID = 149
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- De naam en contactgegevens van de aanbieder; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- De naam en contactgegevens van de aanbieder;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "- Kenmerken, capaciteiten en beperkingen; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 151
    thisalinea.parentID = 149
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- Kenmerken, capaciteiten en beperkingen; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Kenmerken, capaciteiten en beperkingen;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "- Mogelijke toekomstige wijzigingen; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 152
    thisalinea.parentID = 149
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "- Mogelijke toekomstige wijzigingen; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Mogelijke toekomstige wijzigingen;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "- Menselijk toezicht; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 153
    thisalinea.parentID = 149
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "- Menselijk toezicht; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Menselijk toezicht;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "- Verwachte levensduur. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 154
    thisalinea.parentID = 149
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "- Verwachte levensduur. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Verwachte levensduur.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 3. Wat zijn de potentiële (psychologische) bijwerkingen zoals het risico op verwarring, voorkeur ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 155
    thisalinea.parentID = 147
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "vo 3. Wat zijn de potentiële (psychologische) bijwerkingen zoals het risico op verwarring, voorkeur of cognitieve vermoeidheid van de eindgebruiker bij het gebruik maken van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 3. Wat zijn de potentiële (psychologische) bijwerkingen zoals het risico op verwarring, voorkeur")
    thisalinea.textcontent.append("of cognitieve vermoeidheid van de eindgebruiker bij het gebruik maken van het AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Communicatie over de uitkomsten AI-systeem"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 156
    thisalinea.parentID = 144
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 4. In hoeverre is het mogelijk om een verklaring te geven aan een betrokkene waarom het AI-systeem op een bepaalde manier werkt? vo 5. Is het systeem voldoende transparant om eindgebruikers in staat te stellen de output(data) van het systeem te interpreteren en op passende wijze te gebruiken?20 ★ vo 6. Is er iets ingericht om eindgebruikers eventuele bijscholing te verlenen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 4. In hoeverre is het mogelijk om een verklaring te geven aan een betrokkene ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 157
    thisalinea.parentID = 156
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 4. In hoeverre is het mogelijk om een verklaring te geven aan een betrokkene waarom het AI-systeem op een bepaalde manier werkt? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 4. In hoeverre is het mogelijk om een verklaring te geven aan een betrokkene waarom het")
    thisalinea.textcontent.append("AI-systeem op een bepaalde manier werkt?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 5. Is het systeem voldoende transparant om eindgebruikers in staat te stellen de output(data) ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 158
    thisalinea.parentID = 156
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 5. Is het systeem voldoende transparant om eindgebruikers in staat te stellen de output(data) van het systeem te interpreteren en op passende wijze te gebruiken?20 ★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 5. Is het systeem voldoende transparant om eindgebruikers in staat te stellen de output(data)")
    thisalinea.textcontent.append("van het systeem te interpreteren en op passende wijze te gebruiken?20 ★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 6. Is er iets ingericht om eindgebruikers eventuele bijscholing te verlenen? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 159
    thisalinea.parentID = 156
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "vo 6. Is er iets ingericht om eindgebruikers eventuele bijscholing te verlenen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 6. Is er iets ingericht om eindgebruikers eventuele bijscholing te verlenen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Communicatie naar aanleiding van het AI-systeem"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 160
    thisalinea.parentID = 144
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "vo 7. Hoe wordt ervoor gezorgd dat commentaar van betrokkenen en eindgebruikers intern goed wordt behandeld? vo 8. Als een betrokkene bezwaar wil aantekenen,21 of een klacht wil indienen tegen een besluit van het AI-systeem,22 is het dan duidelijk welke stappen hij/zij kan nemen? Hetzelfde geldt voor beroep instellen.23 ★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 7. Hoe wordt ervoor gezorgd dat commentaar van betrokkenen en eindgebruikers intern goed ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 161
    thisalinea.parentID = 160
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 7. Hoe wordt ervoor gezorgd dat commentaar van betrokkenen en eindgebruikers intern goed wordt behandeld? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 7. Hoe wordt ervoor gezorgd dat commentaar van betrokkenen en eindgebruikers intern goed")
    thisalinea.textcontent.append("wordt behandeld?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 8. Als een betrokkene bezwaar wil aantekenen,21 of een klacht wil indienen tegen een ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 162
    thisalinea.parentID = 160
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 8. Als een betrokkene bezwaar wil aantekenen,21 of een klacht wil indienen tegen een besluit van het AI-systeem,22 is het dan duidelijk welke stappen hij/zij kan nemen? Hetzelfde geldt voor beroep instellen.23 ★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 8. Als een betrokkene bezwaar wil aantekenen,21 of een klacht wil indienen tegen een besluit van")
    thisalinea.textcontent.append("het AI-systeem,22 is het dan duidelijk welke stappen hij/zij kan nemen? Hetzelfde geldt voor")
    thisalinea.textcontent.append("beroep instellen.23 ★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Controleerbaarheid"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 163
    thisalinea.parentID = 143
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Het is van belang dat er inzicht in de bronnen, het systeem en de uitkomst is. Deze verantwoordelijkheid zal doorgaans bij de gebruiker liggen. Om autonoom te kunnen zijn in het gebruik van ai-systemen, moet de eindgebruiker voldoende begrip hebben van het systeem, of de werking ervan kunnen opvragen. Ook is het belangrijk dat begrip over het AI-systeem makkelijk overgedragen kan worden wanneer er een nieuwe eindgebruiker met het systeem gaat werken die niet bij de ontwikkeling betrokken was. Daarom moeten AI-systemen zoveel mogelijk opgesteld worden in samenspraak met de beoogde eindgebruiker. Toezicht kan worden verwezenlijkt door middel van governance "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Het is van belang dat er inzicht in de bronnen, het systeem en de uitkomst is. Deze verantwoordelijkheid")
    thisalinea.textcontent.append("zal doorgaans bij de gebruiker liggen.")
    thisalinea.textcontent.append("Om autonoom te kunnen zijn in het gebruik van ai-systemen, moet de eindgebruiker voldoende begrip")
    thisalinea.textcontent.append("hebben van het systeem, of de werking ervan kunnen opvragen. Ook is het belangrijk dat begrip over het")
    thisalinea.textcontent.append("AI-systeem makkelijk overgedragen kan worden wanneer er een nieuwe eindgebruiker met het systeem gaat")
    thisalinea.textcontent.append("werken die niet bij de ontwikkeling betrokken was. Daarom moeten AI-systemen zoveel mogelijk opgesteld")
    thisalinea.textcontent.append("worden in samenspraak met de beoogde eindgebruiker. Toezicht kan worden verwezenlijkt door middel van")
    thisalinea.textcontent.append("governance mechanismen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "v 3. Hoe wordt het ai-systeem gecontroleerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 164
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "v 3. Hoe wordt het ai-systeem gecontroleerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("v 3. Hoe wordt het ai-systeem gecontroleerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "v 4. Hoe is menselijke controle en toezicht gewaarborgd? ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 165
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "v 4. Hoe is menselijke controle en toezicht gewaarborgd? Met controleerbaarheid kijken we naar op welke manier de processen voor de evaluatie van de data en het model en de resultaten gecontroleerd kunnen worden. Deze controle kan in de vorm van audits kan intern of extern plaatsvinden. Naarmate toepassing plaatsvindt op meer kritische gebieden moeten er strengere eisen worden gesteld. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("v 4. Hoe is menselijke controle en toezicht gewaarborgd?")
    thisalinea.textcontent.append("Met controleerbaarheid kijken we naar op welke manier de processen voor de evaluatie van de data en het")
    thisalinea.textcontent.append("model en de resultaten gecontroleerd kunnen worden. Deze controle kan in de vorm van audits kan intern")
    thisalinea.textcontent.append("of extern plaatsvinden. Naarmate toepassing plaatsvindt op meer kritische gebieden moeten er strengere")
    thisalinea.textcontent.append("eisen worden gesteld.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 9. Hoe wordt rekening gehouden met het ingaan van aangekondigde nieuwe wet- en ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 166
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "vo 9. Hoe wordt rekening gehouden met het ingaan van aangekondigde nieuwe wet- en regelgeving tijdens de levensduur van dit AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 9. Hoe wordt rekening gehouden met het ingaan van aangekondigde nieuwe wet- en")
    thisalinea.textcontent.append("regelgeving tijdens de levensduur van dit AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 10. Hoe wordt ervoor gezorgd dat het AI-systeem onafhankelijk kan worden gecontroleerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 167
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "vo 10. Hoe wordt ervoor gezorgd dat het AI-systeem onafhankelijk kan worden gecontroleerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 10. Hoe wordt ervoor gezorgd dat het AI-systeem onafhankelijk kan worden gecontroleerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 11. Hoe wordt de correctheid van de input(data) gecontroleerd en geïnterpreteerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 168
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "vo 11. Hoe wordt de correctheid van de input(data) gecontroleerd en geïnterpreteerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 11. Hoe wordt de correctheid van de input(data) gecontroleerd en geïnterpreteerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 12. Hoe wordt de correctheid van het model gecontroleerd en geïnterpreteerd? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 169
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "vo 12. Hoe wordt de correctheid van het model gecontroleerd en geïnterpreteerd? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 12. Hoe wordt de correctheid van het model gecontroleerd en geïnterpreteerd?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 13. Hoe wordt de correctheid van de output(data) gecontroleerd en geïnterpreteerd?24 ★ "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 170
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "vo 13. Hoe wordt de correctheid van de output(data) gecontroleerd en geïnterpreteerd?24 ★ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 13. Hoe wordt de correctheid van de output(data) gecontroleerd en geïnterpreteerd?24 ★")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Archivering"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 171
    thisalinea.parentID = 143
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Archivering is het bewaren van informatie zodat je deze informatie in de toekomst kunt hergebruiken of voor andere doelen in kan zetten. Denk bijvoorbeeld aan het herconstrueren van het model (zie ‘Reproduceerbaarheid’), of een nieuwe medewerker kunnen uitleggen hoe het systeem in elkaar zit (zie ‘Uitlegbaarheid’), of om verantwoording af te leggen naar een betrokkene (zie ‘Verantwoordingsplicht’). vo 14. Hoe wordt de input(data) opgeslagen? vo 15. Wat is de bewaartermijn van de input(data)? vo 16. Hoe wordt het model opgeslagen? vo 17. Kunnen de gebruikers de output(data) op de juiste manier interpreteren? vo 18. Wat is de bewaartermijn van de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Archivering is het bewaren van informatie zodat je deze informatie in de toekomst kunt hergebruiken")
    thisalinea.textcontent.append("of voor andere doelen in kan zetten. Denk bijvoorbeeld aan het herconstrueren van het model (zie")
    thisalinea.textcontent.append("‘Reproduceerbaarheid’), of een nieuwe medewerker kunnen uitleggen hoe het systeem in elkaar zit (zie")
    thisalinea.textcontent.append("‘Uitlegbaarheid’), of om verantwoording af te leggen naar een betrokkene (zie ‘Verantwoordingsplicht’).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Input(data)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 172
    thisalinea.parentID = 171
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 14. Hoe wordt de input(data) opgeslagen? vo 15. Wat is de bewaartermijn van de input(data)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 14. Hoe wordt de input(data) opgeslagen? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 173
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 14. Hoe wordt de input(data) opgeslagen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 14. Hoe wordt de input(data) opgeslagen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 15. Wat is de bewaartermijn van de input(data)? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 174
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 15. Wat is de bewaartermijn van de input(data)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 15. Wat is de bewaartermijn van de input(data)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Model"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 175
    thisalinea.parentID = 171
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 16. Hoe wordt het model opgeslagen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 16. Hoe wordt het model opgeslagen? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 176
    thisalinea.parentID = 175
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 16. Hoe wordt het model opgeslagen? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 16. Hoe wordt het model opgeslagen?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Output(data)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 177
    thisalinea.parentID = 171
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "vo 17. Kunnen de gebruikers de output(data) op de juiste manier interpreteren? vo 18. Wat is de bewaartermijn van de output(data)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 17. Kunnen de gebruikers de output(data) op de juiste manier interpreteren? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 178
    thisalinea.parentID = 177
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 17. Kunnen de gebruikers de output(data) op de juiste manier interpreteren? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 17. Kunnen de gebruikers de output(data) op de juiste manier interpreteren?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "vo 18. Wat is de bewaartermijn van de output(data)? "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 179
    thisalinea.parentID = 177
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 18. Wat is de bewaartermijn van de output(data)? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 18. Wat is de bewaartermijn van de output(data)?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Klimaatadaptie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 180
    thisalinea.parentID = 143
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "AI-systemen kunnen bijdragen aan oplossingen voor de meest urgente maatschappelijke zorgen, tegelijkertijd is het van belang dat dit zo milieuvriendelijk mogelijk gebeurt. Het is van belang om de milieuvriendelijkheid van de volledige toeleveringsketen van het ai-systeem te waarborgen. Aan de andere kant kan het natuurlijk ook zo zijn dat het AI-systeem juist wordt ingezet om milieuwinst te behalen. Die impact moet afgewogen tegen de milieukosten van bijvoorbeeld het laten draaien van het systeem. Hierbij is het natuurlijk wel van belang om proportionaliteit aan te houden. Als het veel tijd en energie kost om de milieu-impact van een systeem te meten "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("AI-systemen kunnen bijdragen aan oplossingen voor de meest urgente maatschappelijke zorgen,")
    thisalinea.textcontent.append("tegelijkertijd is het van belang dat dit zo milieuvriendelijk mogelijk gebeurt. Het is van belang om de")
    thisalinea.textcontent.append("milieuvriendelijkheid van de volledige toeleveringsketen van het ai-systeem te waarborgen.")
    thisalinea.textcontent.append("Aan de andere kant kan het natuurlijk ook zo zijn dat het AI-systeem juist wordt ingezet om milieuwinst")
    thisalinea.textcontent.append("te behalen. Die impact moet afgewogen tegen de milieukosten van bijvoorbeeld het laten draaien van het")
    thisalinea.textcontent.append("systeem.")
    thisalinea.textcontent.append("Hierbij is het natuurlijk wel van belang om proportionaliteit aan te houden. Als het veel tijd en energie kost")
    thisalinea.textcontent.append("om de milieu-impact van een systeem te meten dat maar een hele kleine ecologische voetafdruk heeft, kan")
    thisalinea.textcontent.append("je hiertussen een afweging maken.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 19. Is er impact op het milieu door het invoeren van het ai-systeem (ontwikkeling, ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 181
    thisalinea.parentID = 180
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "vo 19. Is er impact op het milieu door het invoeren van het ai-systeem (ontwikkeling, installatie en gebruik), en hoe wordt dit gemeten? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 19. Is er impact op het milieu door het invoeren van het ai-systeem (ontwikkeling, installatie en")
    thisalinea.textcontent.append("gebruik), en hoe wordt dit gemeten?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 20. Hoe wordt de impact van het AI-systeem afgewogen tegen de milieukosten van het ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 182
    thisalinea.parentID = 180
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "vo 20. Hoe wordt de impact van het AI-systeem afgewogen tegen de milieukosten van het laten draaien van het AI-systeem? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 20. Hoe wordt de impact van het AI-systeem afgewogen tegen de milieukosten van het laten")
    thisalinea.textcontent.append("draaien van het AI-systeem?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "vo 21. Wat voor maatregelen zijn er genomen om de milieu-impact van het AI-systeem te ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 183
    thisalinea.parentID = 180
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "vo 21. Wat voor maatregelen zijn er genomen om de milieu-impact van het AI-systeem te minimaliseren? "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("vo 21. Wat voor maatregelen zijn er genomen om de milieu-impact van het AI-systeem te")
    thisalinea.textcontent.append("minimaliseren?")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Bijlagen Begrippenlijst"
    thisalinea.titlefontsize = "18.0"
    thisalinea.nativeID = 184
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "In dit document worden begrippen gebruikt die in de literatuur vaak verschillend gedefinieerd worden. Hieronder volgen eenduidige definities die gebruikt worden in dit document. acceptatiecriteria Op het beoogde doel en data afgestemde voorwaarden, waaraan het ai-systeem moet voldoen. Dit kan bijvoorbeeld de hoeveelheid data zijn, een accuratesse maatstaaf voor de output(data) of het inrichten van een onafhankelijke controle van output. Acceptatiecriteria moeten waar mogelijk meetbaar gemaakt worden zodat deze gemonitord kunnen worden met een geschikt meetsysteem. Goede acceptatiecriteria zijn SMART en voldoende verschillend zodat alle relevante aspecten van het AI-systeem goed gemonitord worden accuraatheid Zeer nauwgezet, precies of zorgvuldig; als "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In dit document worden begrippen gebruikt die in de literatuur vaak verschillend gedefinieerd worden.")
    thisalinea.textcontent.append("Hieronder volgen eenduidige definities die gebruikt worden in dit document.")
    thisalinea.textcontent.append("acceptatiecriteria Op het beoogde doel en data afgestemde voorwaarden, waaraan het")
    thisalinea.textcontent.append("ai-systeem moet voldoen. Dit kan bijvoorbeeld de hoeveelheid data")
    thisalinea.textcontent.append("zijn, een accuratesse maatstaaf voor de output(data) of het inrichten")
    thisalinea.textcontent.append("van een onafhankelijke controle van output. Acceptatiecriteria moeten")
    thisalinea.textcontent.append("waar mogelijk meetbaar gemaakt worden zodat deze gemonitord kunnen")
    thisalinea.textcontent.append("worden met een geschikt meetsysteem. Goede acceptatiecriteria zijn SMART")
    thisalinea.textcontent.append("en voldoende verschillend zodat alle relevante aspecten van het AI-systeem")
    thisalinea.textcontent.append("goed gemonitord worden")
    thisalinea.textcontent.append("accuraatheid Zeer nauwgezet, precies of zorgvuldig; als een systeem in staat is")
    thisalinea.textcontent.append("om juiste én accuratesse beoordelingen te maken. In een formule:")
    thisalinea.textcontent.append("TP+TN/(TP+TN+FP+FN). TP= werkelijke positief, TN=Werkelijk negatief,")
    thisalinea.textcontent.append("FP=Verkeerde positief, FN= Verkeerd negatief. Hoe meer werkelijke")
    thisalinea.textcontent.append("resultaten t.o.v. verkeerde resultaten hoe hoger de accuraatheid.")
    thisalinea.textcontent.append("ai met beperkt risico De AI Verordening stelt vast wat beperkt risico AI is. AI ingericht op")
    thisalinea.textcontent.append("interactie met mensen, emoties herkennen, of gemanipuleerde beelden")
    thisalinea.textcontent.append("produceren. Denk aan spamfilters, het samenvatten van teksten, het")
    thisalinea.textcontent.append("classificeren van onderwerpen van luchtvaartvoorvallen, of bijvoorbeeld")
    thisalinea.textcontent.append("AI-systemen die kantoorverlichting regelen.")
    thisalinea.textcontent.append("ai met hoog risico De AI Verordening stelt vast wat hoog risico AI is. Dit zijn vaak producten die")
    thisalinea.textcontent.append("nauw te maken hebben met fundamentele rechten en/of productveiligheid.")
    thisalinea.textcontent.append("Denk hierbij bijvoorbeeld aan AI in vliegtuigen, vaartuigen, voertuigen, rails,")
    thisalinea.textcontent.append("wegverkeer, vliegnavigatie en drinkwatertoevoer. Zo lang de AI Verordening")
    thisalinea.textcontent.append("nog niet in werking is gesteld, gaat het erom dat we bewust met AI omgaan.")
    thisalinea.textcontent.append("Dat betekent dat we ons moeten realiseren wanneer AI een hoog risico")
    thisalinea.textcontent.append("heeft.")
    thisalinea.textcontent.append("ai met minimaal risico Alle AI-systemen die niet verboden zijn of onder ai met hoog risico of")
    thisalinea.textcontent.append("ai met beperkt risico vallen.")
    thisalinea.textcontent.append("ai-systeem Een systeem welke (deels) tot stand is gekomen door middel van het")
    thisalinea.textcontent.append("toepassen van zelflerende algoritmes (machine learning, statistiek of logica)")
    thisalinea.textcontent.append("op historische data, met het doel om voorspellingen of aanbevelingen te")
    thisalinea.textcontent.append("doen, of om zelfstandig beslissingen te nemen.")
    thisalinea.textcontent.append("algoritme Een ‘recept’, of eindige reeks van wiskundige instructies die vanuit een")
    thisalinea.textcontent.append("gegeven begintoestand naar een vooraf gesteld doel leiden. Doorgaans zijn")
    thisalinea.textcontent.append("deze algoritmes geïmplementeerd in een computerprogramma.")
    thisalinea.textcontent.append("artificial intelligence AI kent geen eenduidige definitie. Wij hanteren de omschrijving van AI")
    thisalinea.textcontent.append("door de Algemene Rekenkamer: “het vermogen [..] om externe gegevens")
    thisalinea.textcontent.append("correct te interpreteren, om te leren van deze gegevens en om deze lessen")
    thisalinea.textcontent.append("te gebruiken om specifieke doelen en taken te verwezenlijken via flexibele")
    thisalinea.textcontent.append("aanpassing”. Ook belichten wij graag al die van de Europese Commissie")
    thisalinea.textcontent.append("alhoewel deze nog niet gehanteerd wordt in dit document: AI omvat")
    thisalinea.textcontent.append("systemen die intelligent gedrag vertonen door hun omgeving te analyseren")
    thisalinea.textcontent.append("en – met een zekere mate van zelfstandigheid – actie ondernemen om")
    thisalinea.textcontent.append("specifieke doelen te bereiken.")
    thisalinea.textcontent.append("beheerorganisatie")
    thisalinea.textcontent.append("Een organisatie die applicatiebeheer van het ai-systeem inricht en")
    thisalinea.textcontent.append("optimaliseert.")
    thisalinea.textcontent.append("belangengroep")
    thisalinea.textcontent.append("betrokkenen")
    thisalinea.textcontent.append("Samenstelling van stakeholders om diversiteit te meten. Dit kan zowel")
    thisalinea.textcontent.append("een groep van eindgebruikers zijn als een groep van mensen die impact")
    thisalinea.textcontent.append("ervaren door het systeem.")
    thisalinea.textcontent.append("Natuurlijk persoon of organisatie die bij het gebruik of de uitkomsten van")
    thisalinea.textcontent.append("het systeem belang heeft, of belang denkt te hebben. Hier wordt bewust")
    thisalinea.textcontent.append("niet het woord ‘belanghebbende’ gebruikt, omdat het meer omvat dan het")
    thisalinea.textcontent.append("in het bestuursrecht gedefinieerde ‘belanghebbende’. Denk aan burgers,")
    thisalinea.textcontent.append("een onder toezicht staande, maar ook de eindgebruiker zelf.")
    thisalinea.textcontent.append("betrouwbaar")
    thisalinea.textcontent.append("De eigenschap beschikken van consistent gedrag en consistente resultaten.")
    thisalinea.textcontent.append("bias")
    thisalinea.textcontent.append("Vooringenomenheid. Het doen van aannames over dingen, mensen of")
    thisalinea.textcontent.append("groepen die vaak niet gebaseerd zijn op werkelijke metingen.")
    thisalinea.textcontent.append("bias in de input")
    thisalinea.textcontent.append("Kwaliteit, consistentie en integriteit van data is een belangrijke voorwaarde")
    thisalinea.textcontent.append("voor een unbiased analyse.")
    thisalinea.textcontent.append("bias in de output De manier waarop de output(data) wordt gebruikt kan invloed hebben")
    thisalinea.textcontent.append("op de levens van mensen. Het is belangrijk dat hierbij geen onterechte")
    thisalinea.textcontent.append("correlatie gaat leiden tot causaliteit.")
    thisalinea.textcontent.append("bias in het model Hoe correct zijn de modellen; in hoeverre corrigeren ze voor bekende")
    thisalinea.textcontent.append("gebreken in representativiteit van de data? Dit kan bijvoorbeeld ook gaan")
    thisalinea.textcontent.append("over wat het ai-systeem leert en wat ongewenste leereffecten zijn.")
    thisalinea.textcontent.append("cio")
    thisalinea.textcontent.append("ciso")
    thisalinea.textcontent.append("corruptie")
    thisalinea.textcontent.append("Chief Information Officer.")
    thisalinea.textcontent.append("Chief Information Security Officer.")
    thisalinea.textcontent.append("Het misbruiken of uitbuiten van fouten van het systeem, of het uitbuiten")
    thisalinea.textcontent.append("van ogenschijnlijke neutrale eigenschappen van het systeem.25 We maken")
    thisalinea.textcontent.append("onderscheid met onbedoelde corruptie.")
    thisalinea.textcontent.append("data bias")
    thisalinea.textcontent.append("Wanneer de steekproef niet representatief is voor de gehele populatie.")
    thisalinea.textcontent.append("data pipeline")
    thisalinea.textcontent.append("Hoe de data vanuit het veld naar het model komt; het proces dat de data")
    thisalinea.textcontent.append("doorloopt.")
    thisalinea.textcontent.append("design bias Problemen in het technisch ontwerp, inclusief beperkingen van computerhulpmiddelen")
    thisalinea.textcontent.append("zoals hardware en software.")
    thisalinea.textcontent.append("diversiteit Hieronder verstaan we het herkennen van verschillende typen 'subjecten' in onze analyses.")
    thisalinea.textcontent.append("Wij proberen hierbij te voorkomen dat groepen van relevante subjecten onterecht niet")
    thisalinea.textcontent.append("worden meegenomen in ontwikkelen van een ai-systeem, waardoor het systeem niet op")
    thisalinea.textcontent.append("hen aansluit.")
    thisalinea.textcontent.append("doel 1 De Algemene Rekenkamer noemt 3 doelen die AI kunnen hebben. Doel 1 is gericht op")
    thisalinea.textcontent.append("het automatiseren van eenvoudige menselijke handelingen. Kenmerkend aan dit soort")
    thisalinea.textcontent.append("algoritmes is dat ze vaak voorschrijvend zijn en automatisch een handeling uitvoeren,")
    thisalinea.textcontent.append("zonder tussenkomst van een mens. Het risico op fouten met impact op de burger is hierbij")
    thisalinea.textcontent.append("laag, gezien de hoge technische transparantie en eenvoudig toepassingsgebied.")
    thisalinea.textcontent.append("doel 2 De Algemene Rekenkamer noemt 3 doelen die AI kunnen hebben. Doel 2 is gericht op het")
    thisalinea.textcontent.append("faciliteren van bedrijfsvoering. Hierbij wordt vaak complexere data gebruikt dan bij doel")
    thisalinea.textcontent.append("doel 3 De Algemene Rekenkamer noemt 3 doelen die AI kunnen hebben. Doel 3 is gericht op")
    thisalinea.textcontent.append("(risico-)voorspellingen. Er is geen sprake van automatische besluitvorming. Het risico op")
    thisalinea.textcontent.append("fouten met impact op de burger is hoog. Bijvoorbeeld dat de resultaten in strijd zijn met")
    thisalinea.textcontent.append("de wet, of (ongewenste) afwijking vertonen op basis van de verbogen beperkingen van")
    thisalinea.textcontent.append("input(data). Verklaarbaarheid komt hierbij in gevaar. Daarnaast bestaat de kans dat het")
    thisalinea.textcontent.append("advies van het algoritme de uiteindelijke beslissing van de medewerker beïnvloedt.")
    thisalinea.textcontent.append("domeinexpert Iemand die veel kennis heeft over het probleemgebied waarin het ai-systeem gebouwd")
    thisalinea.textcontent.append("wordt.")
    thisalinea.textcontent.append("eerlijkheid Als niet elk subject een gelijke behandeling krijgt, moet dat verklaard kunnen worden.")
    thisalinea.textcontent.append("Hierbij is het van belang dat we zoveel mogelijk onderscheidende subjectkenmerken in")
    thisalinea.textcontent.append("beeld hebben. Zowel om aan te kunnen tonen welke kenmerken daadwerkelijk een rol")
    thisalinea.textcontent.append("spelen (en partij A een lager risico toebedelen dan partij B) en welke kenmerken dit juist")
    thisalinea.textcontent.append("niet zijn (waardoor partij A en B een onderbouwd gelijkwaardig risico hebben).")
    thisalinea.textcontent.append("eindgebruiker Eindgebruikers zijn de personen die het ai-systeem in de praktijk toepassen binnen de")
    thisalinea.textcontent.append("‘gebruiker’ als organisatie. Het gaat hierbij om een natuurlijk persoon. Wie zitten er")
    thisalinea.textcontent.append("met de handen aan de knoppen? Wie vergaart binnen de organisatie informatie uit het")
    thisalinea.textcontent.append("AI-systeem? Denk aan een inspecteur of een wegverkeersleider.")
    thisalinea.textcontent.append("eindverantwoordelijke Een rol binnen de organisatie die de verantwoordelijkheid over het ai-systeem draagt.")
    thisalinea.textcontent.append("Dat betekent bijvoorbeeld de verantwoordelijkheid over dat de juiste resultaten van het")
    thisalinea.textcontent.append("AI-systeem bereikt worden.")
    thisalinea.textcontent.append("entiteit Een functie binnen een afdeling van een organisatie.")
    thisalinea.textcontent.append("gebruiker Volgens de AI Verordening “een (…) overheidsinstantie, agentschap of ander")
    thisalinea.textcontent.append("orgaan die/dat een ai-systeem onder eigen verantwoordelijkheid gebruikt")
    thisalinea.textcontent.append("(…)”. De gebruiker zet het systeem in. Dit is nooit een natuurlijk persoon.")
    thisalinea.textcontent.append("Bijvoorbeeld de ILT of RWS.")
    thisalinea.textcontent.append("geen positieve impact betrokkenen die niet per definitie negatieve impact ervaren van de inzet")
    thisalinea.textcontent.append("van het AI-systeem, maar bijvoorbeeld in dezelfde situatie blijven als")
    thisalinea.textcontent.append("daarvoor. Daarbij kan een gevaar zijn dat deze betrokkenen niet dezelfde")
    thisalinea.textcontent.append("‘positieve impact’ van het AI-systeem ervaren dat andere betrokkenen wel")
    thisalinea.textcontent.append("krijgen.")
    thisalinea.textcontent.append("gelijkheid Hieronder verstaan we de gedachte dat elk gelijksoortig subject een gelijke")
    thisalinea.textcontent.append("behandeling krijgt.")
    thisalinea.textcontent.append("governance De handeling of de wijze van besturen, de gedragscode en het toezicht")
    thisalinea.textcontent.append("op organisaties. Het betreft beslissingen die verwachtingen bepalen,")
    thisalinea.textcontent.append("macht verlenen of prestaties verifiëren. Het bestaat ofwel uit een")
    thisalinea.textcontent.append("afzonderlijk proces ofwel uit een specifiek deel van management- of")
    thisalinea.textcontent.append("leiderschapsprocessen.")
    thisalinea.textcontent.append("hackaanval")
    thisalinea.textcontent.append("Inbreken in het ai-systeem. Met als gevolg bijvoorbeeld vervuiling van data,")
    thisalinea.textcontent.append("het ongewenst uitlekken van (de werking van) een AI-systeem, of aantasting")
    thisalinea.textcontent.append("van software of hardware.")
    thisalinea.textcontent.append("in gebruik nemen Het moment dat een AI-systeem ‘in gebruik wordt genomen’ betekent het")
    thisalinea.textcontent.append("moment waarop deze voor het eerst buiten de deur wordt gebruikt. In de")
    thisalinea.textcontent.append("praktijk betekent dit dus ook een externe test of pilot. Op het moment van")
    thisalinea.textcontent.append("in gebruik name moet de AIIA af zijn.")
    thisalinea.textcontent.append("input(data) Die gegevens welke worden verwerkt met een vooropgesteld doel. In de")
    thisalinea.textcontent.append("context van een ai-systeem kunnen dit ruwe data zijn, bijvoorbeeld de")
    thisalinea.textcontent.append("waarnemingen uit de werkelijkheid. In de context van het model zijn dit")
    thisalinea.textcontent.append("normaal gesproken voorbewerkte data.")
    thisalinea.textcontent.append("model Een (versimpelde) wiskundige vertegenwoordiging van de werkelijkheid,")
    thisalinea.textcontent.append("welke wordt gebruikt om informatie te verwerken. In een ai-systeem wordt")
    thisalinea.textcontent.append("de wiskundige vertegenwoordiging vaak deels of in zijn geheel volgens een")
    thisalinea.textcontent.append("algoritme ‘geleerd’, waardoor zelfs door de ontwikkelaars niet volledig")
    thisalinea.textcontent.append("uit te leggen is hoe het model aan diens uitkomsten komt.")
    thisalinea.textcontent.append("moreel beraad Overlegorgaan Fysieke Leefomgeving (mei 2021), Moreel Beraad.")
    thisalinea.textcontent.append("negatieve impact betrokkenen die nadelige gevolgen ervaren door de toepassing van het")
    thisalinea.textcontent.append("ai-systeem, bijvoorbeeld omdat ze gediscrimineerd worden op basis van")
    thisalinea.textcontent.append("een bias in het AI-systeem.")
    thisalinea.textcontent.append("onbedoelde corruptie Zonder kwaadwillende bedoelingen de werking van het ai-systeem")
    thisalinea.textcontent.append("beïnvloeden door bijvoorbeeld verkeerde input te voeden, of de")
    thisalinea.textcontent.append("verkeerde knoppen in te drukken. Onbedoelde corruptie valt onder")
    thisalinea.textcontent.append("betrouwbaarheid. We maken onderscheid met (bedoelde) corruptie.")
    thisalinea.textcontent.append("ontwikkelaar Een organisatie of een persoon die een ai-systeem ontwerpt, ontwikkelt en/")
    thisalinea.textcontent.append("of traint.")
    thisalinea.textcontent.append("opdrachtgever Een persoon of organisatieonderdeel die een opdracht verstrekt")
    thisalinea.textcontent.append("aan een opdrachtnemer. Deze is ook (samen met de projectleider)")
    thisalinea.textcontent.append("eindverantwoordelijk voor het maken van een AIIA.")
    thisalinea.textcontent.append("output(data) De gegevens die een ai-systeem oplevert. Dit zijn de resultaten van het")
    thisalinea.textcontent.append("model.")
    thisalinea.textcontent.append("parameter Een variabele binnen het model. Wanneer deze variabele gewijzigd wordt,")
    thisalinea.textcontent.append("wordt ook de resulterende grootheid van het model of van de berekening")
    thisalinea.textcontent.append("gewijzigd.")
    thisalinea.textcontent.append("positieve impact betrokkenen die gunstige gevolgen ervaren van de inzet van het")
    thisalinea.textcontent.append("ai-systeem. Denk aan een minderheidsgroep die wordt bevoordeeld.")
    thisalinea.textcontent.append("Daarbij kan het gevaar zijn dat deze positieve bias te optimistisch is, en dus")
    thisalinea.textcontent.append("niet waarheidsgetrouw. Ook kan de keerzijde hiervan een ‘negatieve impact’")
    thisalinea.textcontent.append("voor andere betrokkenen zijn.")
    thisalinea.textcontent.append("projectleider De eindverantwoordelijke voor het project waarbinnen het ai-systeem valt.")
    thisalinea.textcontent.append("Deze is ook (samen met de opdrachtgever) eindverantwoordelijk voor")
    thisalinea.textcontent.append("het maken van een AIIA.")
    thisalinea.textcontent.append("proportioneel AI is een ingrijpende techniek, met verklaarbaarheidsproblemen. Staat het")
    thisalinea.textcontent.append("gebruik van AI in verhouding tot het probleem wat er met het algoritme")
    thisalinea.textcontent.append("opgelost gaat worden? Het verwachte voordeel moet groter zijn dan het")
    thisalinea.textcontent.append("risico dat AI met zich meebrengt.")
    thisalinea.textcontent.append("reproduceerbaar Het steeds opnieuw kunnen bereiken van een vergelijkbaar resultaat")
    thisalinea.textcontent.append("wanneer een beschreven procedure wordt uitgevoerd.")
    thisalinea.textcontent.append("robuustheid Met een preventieve benadering ontwikkeld zijn; zich gedragen zoals")
    thisalinea.textcontent.append("voorzien en van tevoren beschreven. Onaanvaardbare schade vermijden.")
    thisalinea.textcontent.append("seed Een “seed” is het uitgangspunt van een willekeurig getal generator. Deze")
    thisalinea.textcontent.append("generator maakt altijd vanuit dit uitgangspunt volgens dezelfde “route”")
    thisalinea.textcontent.append("nieuwe (pseudo) willekeurige getallen. Door de “seed” te documenteren")
    thisalinea.textcontent.append("kan de “route” van (pseudo) willekeurige getallen worden herhaald.")
    thisalinea.textcontent.append("Dit betekent dat deze seed nodig is om reconstructie van een model te")
    thisalinea.textcontent.append("controleren wanneer het model ergens gebruik maakt van willekeurige")
    thisalinea.textcontent.append("getallen.")
    thisalinea.textcontent.append("de seed zelf is ook een getal Er zijn geen specifieke eisen aan dit getal, dus vaak wordt er voor iets")
    thisalinea.textcontent.append("“herkenbaars” gekozen (bijvoorbeeld “123456”, of “0, 42, 1234” of de")
    thisalinea.textcontent.append("geboortedatum van een ontwikkelaar).")
    thisalinea.textcontent.append("stakeholder Persoon of organisatie die een beslissing of activiteit kan beïnvloeden,")
    thisalinea.textcontent.append("erdoor kan worden beïnvloed, of zichzelf als beïnvloed beschouwd. Een")
    thisalinea.textcontent.append("stakeholder kan bijvoorbeeld ook de eigenaar van gebruikte data zijn.")
    thisalinea.textcontent.append("subsidiair AI is een ingrijpende techniek, met verklaarbaarheidsproblemen. Kan het")
    thisalinea.textcontent.append("probleem ook met minder vergaande middelen opgelost worden?")
    thisalinea.textcontent.append("traceerbaarheid Wanneer processen en resultaten te controleren zijn.")
    thisalinea.textcontent.append("transparant Wanneer de werking en doelen van het ai-systeem duidelijk worden")
    thisalinea.textcontent.append("gecommuniceerd en resultaten van het AI-systeem uitlegbaar zijn.")
    thisalinea.textcontent.append("type algoritmes Verschillende technieken kunnen gebruikt worden om AI te maken,")
    thisalinea.textcontent.append("zoals neurale netwerken, random forests of andere vormen van machine")
    thisalinea.textcontent.append("learning. Maar ook minder complexe algoritmes zoals business-rules of")
    thisalinea.textcontent.append("beslisbomen kunnen gebruikt worden.")
    thisalinea.textcontent.append("uitlegbaar Een verklaring van hoe input variabelen bijdragen aan een output van het")
    thisalinea.textcontent.append("algoritme die uitgelegd moet worden.")
    thisalinea.textcontent.append("verantwoordelijk Handelingen van een entiteit kunnen op unieke wijze worden herleid tot")
    thisalinea.textcontent.append("die entiteit, en deze entiteit is voor deze handelingen aansprakelijk. Wie is")
    thisalinea.textcontent.append("wie Vul in welke personen een rol hebben gespeeld bij het beantwoorden")
    thisalinea.textcontent.append("van deze AIIA.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Het zijn vaak voorspellende algoritmes zonder automatische besluitvorming. Het ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 185
    thisalinea.parentID = 184
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Het zijn vaak voorspellende algoritmes zonder automatische besluitvorming. Het risico op fouten met impact op de burger is aanwezig maar is beperkt. Het algoritme doet namelijk alleen voorbereidend ‘werk’. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Het zijn vaak voorspellende algoritmes zonder automatische besluitvorming. Het")
    thisalinea.textcontent.append("risico op fouten met impact op de burger is aanwezig maar is beperkt. Het algoritme doet")
    thisalinea.textcontent.append("namelijk alleen voorbereidend ‘werk’.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Wie is wie"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 186
    thisalinea.parentID = 184
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Vul in welke personen een rol hebben gespeeld bij het beantwoorden van deze AIIA. Communicatieadviseur: Data scientists: Databeheerder of bronhouder: Functionaris Gegevensbescherming: Jurist: Overige leden projectteam: Strategisch adviseur ethiek: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Vul in welke personen een rol hebben gespeeld bij het beantwoorden van deze AIIA.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "belangengroep: ciso of cio:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 187
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Communicatieadviseur: Data scientists: Databeheerder of bronhouder: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Communicatieadviseur:")
    thisalinea.textcontent.append("Data scientists:")
    thisalinea.textcontent.append("Databeheerder of bronhouder:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "domeinexpert:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 188
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Functionaris Gegevensbescherming: Jurist: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Functionaris Gegevensbescherming:")
    thisalinea.textcontent.append("Jurist:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "opdrachtgever:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 189
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Overige leden projectteam: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Overige leden projectteam:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "projectleider:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 190
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Strategisch adviseur ethiek: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Strategisch adviseur ethiek:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Wie doet wat"
    thisalinea.titlefontsize = "14.0"
    thisalinea.nativeID = 191
    thisalinea.parentID = 184
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "H1 H2. H3. H4. H5. H6. Communicatieadviseur: X X X Data scientists: X X X X X Databeheerder of bronhouder: X X X X X X Functionaris Gegevensbescherming: X Jurist: X X X X X X X Overige leden projectteam: XX X X X X Strategisch adviseur ethiek: Dit is een publicatie van: Ministerie van Infrastructuur en Waterstaat Postbus 20901 2500 EX Den Haag November 2022 | 73263 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("H1 H2. H3. H4. H5. H6.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "belangengroep: ciso of cio:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 192
    thisalinea.parentID = 191
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Communicatieadviseur: X X X Data scientists: X X X X X Databeheerder of bronhouder: X "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Communicatieadviseur:")
    thisalinea.textcontent.append("X")
    thisalinea.textcontent.append("X")
    thisalinea.textcontent.append("X")
    thisalinea.textcontent.append("Data scientists:")
    thisalinea.textcontent.append("X X X X X")
    thisalinea.textcontent.append("Databeheerder of bronhouder:")
    thisalinea.textcontent.append("X")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "domeinexpert:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 193
    thisalinea.parentID = 191
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "X X X X X Functionaris Gegevensbescherming: X Jurist: X "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("X X X X X")
    thisalinea.textcontent.append("Functionaris Gegevensbescherming:")
    thisalinea.textcontent.append("X")
    thisalinea.textcontent.append("Jurist:")
    thisalinea.textcontent.append("X")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "opdrachtgever:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 194
    thisalinea.parentID = 191
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "X X X X X X Overige leden projectteam: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("X")
    thisalinea.textcontent.append("X X X X X")
    thisalinea.textcontent.append("Overige leden projectteam:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "projectleider:"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 195
    thisalinea.parentID = 191
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "XX X X X X Strategisch adviseur ethiek: Dit is een publicatie van: Ministerie van Infrastructuur en Waterstaat Postbus 20901 2500 EX Den Haag November 2022 | 73263 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("XX")
    thisalinea.textcontent.append("X")
    thisalinea.textcontent.append("X X X")
    thisalinea.textcontent.append("Strategisch adviseur ethiek:")
    thisalinea.textcontent.append("Dit is een publicatie van:")
    thisalinea.textcontent.append("Ministerie van Infrastructuur en Waterstaat")
    thisalinea.textcontent.append("Postbus 20901")
    thisalinea.textcontent.append("2500 EX Den Haag")
    thisalinea.textcontent.append("November 2022 | 73263")
    thisalinea.textcontent.append("")
    alineas.append(thisalinea)

    return alineas
