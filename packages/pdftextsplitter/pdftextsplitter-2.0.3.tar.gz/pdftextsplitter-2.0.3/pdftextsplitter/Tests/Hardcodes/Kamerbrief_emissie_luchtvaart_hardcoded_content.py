import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_Kamerbrief_emissie_luchtvaart() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document Kamerbrief_emissie_luchtvaart
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
    thisalinea.texttitle = "Kamerbrief_emissie_luchtvaart"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "De voorzitter van de Tweede Kamer der Staten-Generaal Postbus 20018 2500 EA DEN HAAG Datum 22 december 2022 Betreft Emissies door de luchtvaart Geachte voorzitter, In de Kamer is de afgelopen jaren in toenemende mate aandacht besteed aan de emissies van de luchtvaart en de gevolgen daarvan voor de lokale luchtkwaliteit, onder meer door de emissies van ultrafijn stof en zeer zorgwekkende stoffen (ZZS). Daarom wordt de Kamer een stand van zaken gegeven van diverse acties die momenteel lopen op dit gebied, waarmee tevens wordt voldaan aan een aantal toezeggingen die aan de Kamer zijn gedaan. In deze brief komen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("De voorzitter van de Tweede Kamer")
    thisalinea.textcontent.append("der Staten-Generaal")
    thisalinea.textcontent.append("Postbus 20018")
    thisalinea.textcontent.append("2500 EA DEN HAAG")
    thisalinea.textcontent.append("Datum 22 december 2022")
    thisalinea.textcontent.append("Betreft Emissies door de luchtvaart")
    thisalinea.textcontent.append("Geachte voorzitter,")
    thisalinea.textcontent.append("In de Kamer is de afgelopen jaren in toenemende mate aandacht besteed aan de")
    thisalinea.textcontent.append("emissies van de luchtvaart en de gevolgen daarvan voor de lokale luchtkwaliteit,")
    thisalinea.textcontent.append("onder meer door de emissies van ultrafijn stof en zeer zorgwekkende stoffen")
    thisalinea.textcontent.append("(ZZS). Daarom wordt de Kamer een stand van zaken gegeven van diverse acties")
    thisalinea.textcontent.append("die momenteel lopen op dit gebied, waarmee tevens wordt voldaan aan een aantal")
    thisalinea.textcontent.append("toezeggingen die aan de Kamer zijn gedaan.")
    thisalinea.textcontent.append("In deze brief komen de volgende onderwerpen aan de orde:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. Ultrafijn stof: omgeving en platformmedewerkers. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Ultrafijn stof: omgeving en platformmedewerkers. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Ultrafijn stof: omgeving en platformmedewerkers.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. Ontzwavelen van kerosine. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 2
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Ontzwavelen van kerosine. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Ontzwavelen van kerosine.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. Zeer zorgwekkende stoffen. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Zeer zorgwekkende stoffen. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Zeer zorgwekkende stoffen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "4. Uniformeren van het berekenen van emissies en concentraties. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 4
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Uniformeren van het berekenen van emissies en concentraties. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Uniformeren van het berekenen van emissies en concentraties.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "5. Emissies boven 3.000 voet. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 5
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. Emissies boven 3.000 voet. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. Emissies boven 3.000 voet.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "6. Emissies van de 440.000 vliegtuigbewegingen op Schiphol. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 6
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. Emissies van de 440.000 vliegtuigbewegingen op Schiphol. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. Emissies van de 440.000 vliegtuigbewegingen op Schiphol.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "7. Bestuursovereenkomst intenties samenwerking NOVEX Schiphol. "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 7
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "7. Bestuursovereenkomst intenties samenwerking NOVEX Schiphol. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("7. Bestuursovereenkomst intenties samenwerking NOVEX Schiphol.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. Ultrafijn stof"
    thisalinea.titlefontsize = "8.999999999999972"
    thisalinea.nativeID = 8
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Op 20 juni 2022 is het eindrapport van het RIVM-onderzoekprogramma naar de gezondheidsrisico’s van ultrafijn stof rond Schiphol aan de Kamer aangeboden1. In die brief is aangegeven welke acties al zijn uitgevoerd, lopen of nog worden opgepakt. Hieronder wordt de voortgang van enkele van die acties toegelicht. Kennisopbouw over emissie en effecten van ultrafijn stof Over de emissie en effecten van ultrafijn stof is onvoldoende bekend. Om te bezien of normstelling noodzakelijk is en een goed besluit te kunnen nemen over te nemen maatregelen, is het noodzakelijk dat de kennis over bronnen, hoeveelheden en effecten van ultrafijn stof wordt vergroot. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1 Blootstelling van de omgeving van luchthavens aan ultrafijn stof van de luchtvaart"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 9
    thisalinea.parentID = 8
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Op 20 juni 2022 is het eindrapport van het RIVM-onderzoekprogramma naar de gezondheidsrisico’s van ultrafijn stof rond Schiphol aan de Kamer aangeboden1. In die brief is aangegeven welke acties al zijn uitgevoerd, lopen of nog worden opgepakt. Hieronder wordt de voortgang van enkele van die acties toegelicht. Kennisopbouw over emissie en effecten van ultrafijn stof Over de emissie en effecten van ultrafijn stof is onvoldoende bekend. Om te bezien of normstelling noodzakelijk is en een goed besluit te kunnen nemen over te nemen maatregelen, is het noodzakelijk dat de kennis over bronnen, hoeveelheden en effecten van ultrafijn stof wordt vergroot. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Op 20 juni 2022 is het eindrapport van het RIVM-onderzoekprogramma naar de")
    thisalinea.textcontent.append("gezondheidsrisico’s van ultrafijn stof rond Schiphol aan de Kamer aangeboden1. In")
    thisalinea.textcontent.append("die brief is aangegeven welke acties al zijn uitgevoerd, lopen of nog worden")
    thisalinea.textcontent.append("opgepakt. Hieronder wordt de voortgang van enkele van die acties toegelicht.")
    thisalinea.textcontent.append("Kennisopbouw over emissie en effecten van ultrafijn stof")
    thisalinea.textcontent.append("Over de emissie en effecten van ultrafijn stof is onvoldoende bekend. Om te")
    thisalinea.textcontent.append("bezien of normstelling noodzakelijk is en een goed besluit te kunnen nemen over")
    thisalinea.textcontent.append("te nemen maatregelen, is het noodzakelijk dat de kennis over bronnen,")
    thisalinea.textcontent.append("hoeveelheden en effecten van ultrafijn stof wordt vergroot. Zoals aangegeven in")
    thisalinea.textcontent.append("de Hoofdlijnenbrief Schiphol van 24 juni 2022 2 is normering voor het kabinet het")
    thisalinea.textcontent.append("uitgangspunt. Daarom is kennisopbouw voor het kabinet van groot belang.")
    thisalinea.textcontent.append("In de Kamerbrief over het eindrapport van het RIVM-onderzoekprogramma is")
    thisalinea.textcontent.append("opgenomen dat Nederland het belang van meer kennis en inzicht over ultrafijn")
    thisalinea.textcontent.append("stof nadrukkelijk heeft opgenomen in een non-paper aan de Europese Commissie")
    thisalinea.textcontent.append("(hierna: Commissie). Doel daarvan was dat de Commissie met ultrafijn stof")
    thisalinea.textcontent.append("rekening kan houden bij de lopende herziening van de luchtkwaliteitsrichtlijnen.")
    thisalinea.textcontent.append("Op 26 oktober 2022 heeft de Commissie een voorstel gedaan voor onder meer de")
    thisalinea.textcontent.append("wijziging van de Ambient Air Quality Directives (Richtlijnen inzake de kwaliteit van")
    thisalinea.textcontent.append("de omgevingslucht)3. In het voorstel zijn onder meer bepalingen opgenomen over")
    thisalinea.textcontent.append("meten en monitoren van luchtverontreinigende stoffen, waaronder ultrafijn stof.")
    thisalinea.textcontent.append("Daarmee wordt internationaal een belangrijke stap gezet naar meer kennisopbouw")
    thisalinea.textcontent.append("over en mogelijk op termijn normstelling voor ultrafijn stof.")
    thisalinea.textcontent.append("Op 12 december 2022 heeft de Minister van Buitenlandse Zaken het BNC-fiche")
    thisalinea.textcontent.append("met de reactie op het EC-voorstel aan de Kamer aangeboden.")
    thisalinea.textcontent.append("Daarnaast zal het RIVM in 2023 zorgdragen voor verschillende internationale")
    thisalinea.textcontent.append("publicaties over het in Nederland uitgevoerde onderzoekprogramma en de")
    thisalinea.textcontent.append("conclusies daarvan. Het streven daarbij is om internationaal meer van soortgelijk")
    thisalinea.textcontent.append("onderzoek in gang te zetten, omdat meerdere, onafhankelijk van elkaar")
    thisalinea.textcontent.append("uitgevoerde studies noodzakelijk zijn om met zekerheid uitspraken te kunnen")
    thisalinea.textcontent.append("doen over de gezondheidseffecten van ultrafijn stof (causaal verband aantonen).")
    thisalinea.textcontent.append("Structureel meten en monitoren van ultrafijn stof in Nederland")
    thisalinea.textcontent.append("Het RIVM heeft op verzoek van het ministerie van IenW een voorstel gedaan voor")
    thisalinea.textcontent.append("het in Nederland structureel meten van ultrafijn stof door vaste meetpunten, die")
    thisalinea.textcontent.append("onderdeel zijn van het Landelijk meetnet luchtkwaliteit. Die meetpunten meten")
    thisalinea.textcontent.append("dan het totaal aan ultrafijn stof, dus van alle bronnen tezamen.")
    thisalinea.textcontent.append("Daarnaast is een voorstel gedaan hoe meer inzicht kan worden verkregen in de")
    thisalinea.textcontent.append("emissie van ultrafijn stof door specifieke, afzonderlijke bronnen, anders dan de")
    thisalinea.textcontent.append("luchtvaart, zoals het wegverkeer en de industrie. Hierover wordt de Kamer door")
    thisalinea.textcontent.append("de Staatssecretaris van IenW ge ïnformeerd.")
    thisalinea.textcontent.append("Met deze aanpak loopt Nederland vooruit op het in de vorige paragraaf genoemde")
    thisalinea.textcontent.append("voorstel van de Europese Commissie voor monitoringbepalingen van ultrafijn stof.")
    thisalinea.textcontent.append("Ultrafijn stof uit de luchtvaart rond regionale luchthavens")
    thisalinea.textcontent.append("Het eerdergenoemde onderzoekprogramma van het RIVM heeft zich gericht op het")
    thisalinea.textcontent.append("vliegverkeer en de omgeving van de luchthaven Schiphol. Uiteraard wordt ook op")
    thisalinea.textcontent.append("de regionale luchthavens ultrafijn stof door de vliegtuigen geëmitteerd.")
    thisalinea.textcontent.append("Het ministerie van IenW laat in de eerste helft van 2023 voor de luchthavens")
    thisalinea.textcontent.append("Eindhoven Airport, Rotterdam The Hague Airport, Maastricht Aachen Airport en")
    thisalinea.textcontent.append("Groningen Airport Eelde door het NLR berekenen welke concentraties ultrafijn stof")
    thisalinea.textcontent.append("daar kunnen optreden als gevolg van het vliegverkeer op de afzonderlijke")
    thisalinea.textcontent.append("luchthavens. Het RIVM zal aanvullend, op basis van de bevindingen in het")
    thisalinea.textcontent.append("Schiphol-onderzoek, aangeven welke risico’s zijn verbonden aan de berekende")
    thisalinea.textcontent.append("concentraties rond de regionale luchthavens. Hiermee wordt voldaan aan de")
    thisalinea.textcontent.append("informatiebehoefte van de omwonenden van die luchthavens en kan worden")
    thisalinea.textcontent.append("bezien of het noodzakelijk is om beleidsmaatregelen te nemen.")
    thisalinea.textcontent.append("Cumulatie")
    thisalinea.textcontent.append("In 2023 wordt door het RIVM een notitie opgesteld, waarin wordt verkend welke")
    thisalinea.textcontent.append("stappen nodig zijn om de gecumuleerde gezondheidsrisico’s rond Schiphol meer")
    thisalinea.textcontent.append("expliciet te maken, en welke belemmeringen en kansen hierbij spelen. Op basis")
    thisalinea.textcontent.append("van deze notitie zal bepaald worden of, en zo ja , welke vervolgstappen kunnen")
    thisalinea.textcontent.append("worden uitgevoerd, eventueel in NOVEX-verband (zie paragraaf 7 van deze brief).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2 Blootstelling van platformmedewerkers aan ultrafijn stof en andere stoffen"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 10
    thisalinea.parentID = 8
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Op 1 oktober 2021 heeft de Kamer het RIVM-rapport ‘Verkenning haalbaarheid gezondheidsonderzoek werknemers Schiphol’4 ontvangen. Hieronder wordt aangegeven hoe de sector de aanbevelingen uit dat rapport heeft opgepakt. Daarbij maak ik onder meer gebruik van door Schiphol verstrekte informatie. Gecoördineerde aanpak door de sector In de brief van 15 februari 20225, met de beantwoording van Kamervragen over dit thema, is aangegeven dat de sector bezig was met het instellen van een taskforce. Inmiddels is deze sectorbrede taskforce Stoffen volop actief en kent meerdere onderdelen (zie figuur 1). De taskforce richt zich niet alleen op ultrafijn stof, maar ook op andere "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Op 1 oktober 2021 heeft de Kamer het RIVM-rapport ‘Verkenning haalbaarheid")
    thisalinea.textcontent.append("gezondheidsonderzoek werknemers Schiphol’4 ontvangen. Hieronder wordt")
    thisalinea.textcontent.append("aangegeven hoe de sector de aanbevelingen uit dat rapport heeft opgepakt.")
    thisalinea.textcontent.append("Daarbij maak ik onder meer gebruik van door Schiphol verstrekte informatie.")
    thisalinea.textcontent.append("Gecoördineerde aanpak door de sector")
    thisalinea.textcontent.append("In de brief van 15 februari 20225, met de beantwoording van Kamervragen over")
    thisalinea.textcontent.append("dit thema, is aangegeven dat de sector bezig was met het instellen van een")
    thisalinea.textcontent.append("taskforce.")
    thisalinea.textcontent.append("Inmiddels is deze sectorbrede taskforce Stoffen volop actief en kent meerdere")
    thisalinea.textcontent.append("onderdelen (zie figuur 1). De taskforce richt zich niet alleen op ultrafijn stof, maar")
    thisalinea.textcontent.append("ook op andere stoffen afkomstig van vliegtuigmotoren.")
    thisalinea.textcontent.append("De begeleidingscommissie binnen de taskforce heeft een onafhankelijk voorzitter")
    thisalinea.textcontent.append("en er zijn inhoudelijke werkgroepen gestart. Daarnaast is een validatiecommissie")
    thisalinea.textcontent.append("in oprichting. De coördinatiegroep coördineert de werkzaamheden van de")
    thisalinea.textcontent.append("werkgroepen, bewaakt de samenhang, heeft een besluitvormende rol en is de link")
    thisalinea.textcontent.append("met de begeleidingscommissie.")
    thisalinea.textcontent.append("Onderwerpen werkgroepen")
    thisalinea.textcontent.append("De werkgroep ‘Blootstelling en gezondheid’ is belast met de volgende")
    thisalinea.textcontent.append("onderwerpen:")
    thisalinea.textcontent.append("In de werkgroep ‘Maatregelen’ worden de maatregelen bekeken die kunnen leiden")
    thisalinea.textcontent.append("tot een vermindering van de blootstelling van platformmedewerkers aan de")
    thisalinea.textcontent.append("emissies van de vliegtuigen. Er wordt onder meer gekeken naar:")
    thisalinea.textcontent.append("Voor het mogelijk maken van bepaalde operationele maatregelen wordt nog")
    thisalinea.textcontent.append("overleg met LVNL gevoerd, omdat maatregelen een impact op de operatie van de")
    thisalinea.textcontent.append("luchthaven tot gevolg (kunnen) hebben. Van belang is dat maatregelen veilig en")
    thisalinea.textcontent.append("beheerst kunnen worden uitgevoerd. Zo moeten meer of andere bewegingen van")
    thisalinea.textcontent.append("vliegtuigen en voertuigen veilig kunnen worden geaccommodeerd. Operationele")
    thisalinea.textcontent.append("maatregelen kunnen daarom niet van vandaag op morgen worden gerealiseerd,")
    thisalinea.textcontent.append("maar uiteraard is het de bedoeling dat maatregelen voortvarend worden")
    thisalinea.textcontent.append("opgepakt.")
    thisalinea.textcontent.append("Onderzoek Nederlandse arbeidsinspectie")
    thisalinea.textcontent.append("Onder het vorige kopje is beschreven hoe de sector bezig is met het verminderen")
    thisalinea.textcontent.append("van de blootstelling van medewerkers aan ultrafijn stof. De Nederlandse")
    thisalinea.textcontent.append("arbeidsinspectie voert een onderzoek uit naar de arbeidsomstandigheden op de")
    thisalinea.textcontent.append("platforms. De verwachting is dat de inspectie begin 2023 zal rapporteren.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Blootstellingsonderzoek: er is zicht op de concentraties van ultrafijnstof op ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 11
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = " Blootstellingsonderzoek: er is zicht op de concentraties van ultrafijnstof op het platform (aan airside) op Schiphol. Onbekend is nog in welke mate individuele medewerkers worden blootgesteld aan ultrafijn stof. Daarom wordt gestart met een persoonlijk blootstellingsonderzoek. Zo’n onderzoek geeft inzicht in de concentraties waaraan een medewerker gedurende een werkdag wordt blootgesteld. Momenteel worden voorbereidende werkzaamheden uitgevoerd om dit onderzoek op wetenschappelijk juiste wijze uit te voere n. Dit betreft bijvoorbeeld het valideren van de meetinstrumenten. Het onderzoek wordt opgezet met een onafhankelijk kennisinstituut en in 2023 uitgevoerd. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Blootstellingsonderzoek: er is zicht op de concentraties van ultrafijnstof op")
    thisalinea.textcontent.append("het platform (aan airside) op Schiphol. Onbekend is nog in welke mate")
    thisalinea.textcontent.append("individuele medewerkers worden blootgesteld aan ultrafijn stof. Daarom")
    thisalinea.textcontent.append("wordt gestart met een persoonlijk blootstellingsonderzoek. Zo’n onderzoek")
    thisalinea.textcontent.append("geeft inzicht in de concentraties waaraan een medewerker gedurende een")
    thisalinea.textcontent.append("werkdag wordt blootgesteld.")
    thisalinea.textcontent.append("Momenteel worden voorbereidende werkzaamheden uitgevoerd om dit")
    thisalinea.textcontent.append("onderzoek op wetenschappelijk juiste wijze uit te voere n. Dit betreft")
    thisalinea.textcontent.append("bijvoorbeeld het valideren van de meetinstrumenten. Het onderzoek wordt")
    thisalinea.textcontent.append("opgezet met een onafhankelijk kennisinstituut en in 2023 uitgevoerd.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Gezondheidskundig onderzoek: de eerste stap daarin is het inzichtelijk ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 12
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = " Gezondheidskundig onderzoek: de eerste stap daarin is het inzichtelijk maken van de algemene fysieke staat en de gezondheid van medewerkers die werkzaam zijn op het platform. Hiermee worden de huidige gezondheidssituatie en eventuele gezondheidsklachten van medewerkers op het platform in kaart gebracht. Ook kunnen er door dit onderzoek mogelijk aanwijzingen worden gevonden of medewerkers op het platform een verhoogd risico lopen op bepaalde medische aandoeningen. Het gaat dan om gezondheidsaandoeningen die verband houden met blootstelling aan luchtverontreinigende stoffen, waaronder ultrafijn stof. Het RIVM (2022) en de Gezondheidsraad (2021) hebben in kaart gebracht om welke aandoeningen het zou kunnen gaan, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Gezondheidskundig onderzoek: de eerste stap daarin is het inzichtelijk")
    thisalinea.textcontent.append("maken van de algemene fysieke staat en de gezondheid van medewerkers")
    thisalinea.textcontent.append("die werkzaam zijn op het platform. Hiermee worden de huidige")
    thisalinea.textcontent.append("gezondheidssituatie en eventuele gezondheidsklachten van medewerkers")
    thisalinea.textcontent.append("op het platform in kaart gebracht. Ook kunnen er door dit onderzoek")
    thisalinea.textcontent.append("mogelijk aanwijzingen worden gevonden of medewerkers op het platform")
    thisalinea.textcontent.append("een verhoogd risico lopen op bepaalde medische aandoeningen. Het gaat")
    thisalinea.textcontent.append("dan om gezondheidsaandoeningen die verband houden met blootstelling")
    thisalinea.textcontent.append("aan luchtverontreinigende stoffen, waaronder ultrafijn stof. Het RIVM")
    thisalinea.textcontent.append("(2022) en de Gezondheidsraad (2021) hebben in kaart gebracht om welke")
    thisalinea.textcontent.append("aandoeningen het zou kunnen gaan, zoals effecten op het hart- en")
    thisalinea.textcontent.append("vaatstelsel en de luchtwegen.")
    thisalinea.textcontent.append("Om een dergelijk onderzoek met betrouwbare data te 'vullen', zijn veel")
    thisalinea.textcontent.append("individuele gezondheidskundige gegevens van medewerkers nodig. Het is")
    thisalinea.textcontent.append("de bedoeling dat deze uit individuele Periodieke Arbeidskundige")
    thisalinea.textcontent.append("gezondheidsonderzoeken (PAGO) worden verzameld. Deze PAGO’s worden")
    thisalinea.textcontent.append("sectorbreed uitgevoerd, de deelname hieraan is vrijwillig. De komende")
    thisalinea.textcontent.append("maanden wordt uitgewerkt welke vragen en/of medische testen aan")
    thisalinea.textcontent.append("bestaande PAGO’s moeten worden toegevoegd. Het streven is het")
    thisalinea.textcontent.append("aangepaste PAGO aan het eind van het eerste kwartaal 2023 gereed te")
    thisalinea.textcontent.append("hebben. Op advies van gezondheidsexperts zal worden bepaald hoe vaak")
    thisalinea.textcontent.append("het PAGO aan medewerkers zal worden aangeboden.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Meetprogramma: er wordt een meetnet ingericht met stationaire ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 13
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = " Meetprogramma: er wordt een meetnet ingericht met stationaire ultrafijnstof-meetpunten. Het is de bedoelding dat dit meetnet, aanvullend op de metingen die door TNO in het tweede kwartaal van 2021 zijn gedaan6, informatie oplevert over de effectiviteit van de in te zetten maatregelen. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Meetprogramma: er wordt een meetnet ingericht met stationaire")
    thisalinea.textcontent.append("ultrafijnstof-meetpunten. Het is de bedoelding dat dit meetnet, aanvullend")
    thisalinea.textcontent.append("op de metingen die door TNO in het tweede kwartaal van 2021 zijn")
    thisalinea.textcontent.append("gedaan6, informatie oplevert over de effectiviteit van de in te zetten")
    thisalinea.textcontent.append("maatregelen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Het zoveel mogelijk beperken van de emissies van zowel de ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 14
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = " Het zoveel mogelijk beperken van de emissies van zowel de vliegtuigmotoren als de hulpmotor (APU). Voor iedere functionaliteit wordt gekeken of er alternatieven mogelijk zijn, zoals taxiën zonder het gebruik van vliegtuigmotoren (lange termijn maatregel) of het overnemen van de koeling/ventilatie in het vliegtuig door een Preconditioned Air unit (PCA, kortere termijn maatregel). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Het zoveel mogelijk beperken van de emissies van zowel de")
    thisalinea.textcontent.append("vliegtuigmotoren als de hulpmotor (APU). Voor iedere functionaliteit wordt")
    thisalinea.textcontent.append("gekeken of er alternatieven mogelijk zijn, zoals taxiën zonder het gebruik")
    thisalinea.textcontent.append("van vliegtuigmotoren (lange termijn maatregel) of het overnemen van de")
    thisalinea.textcontent.append("koeling/ventilatie in het vliegtuig door een Preconditioned Air unit (PCA,")
    thisalinea.textcontent.append("kortere termijn maatregel).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Alternatieven voor dieselaangedreven apparatuur. Hieronder valt een ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 15
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = " Alternatieven voor dieselaangedreven apparatuur. Hieronder valt een versnelling in de vervanging van diesel Ground Power Units (GPU’s) door een emissievrij alternatief (E-GPU’s of walstroom). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Alternatieven voor dieselaangedreven apparatuur. Hieronder valt een")
    thisalinea.textcontent.append("versnelling in de vervanging van diesel Ground Power Units (GPU’s) door")
    thisalinea.textcontent.append("een emissievrij alternatief (E-GPU’s of walstroom).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Het aanpassen van vertrek- en aankomstprocedures, zoals een langere ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 16
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = " Het aanpassen van vertrek- en aankomstprocedures, zoals een langere sleepprocedure voor vliegtuigen. Doel daarvan is de blootstelling van medewerkers aan emissies uit startende motoren zoveel mogelijk te verminderen. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Het aanpassen van vertrek- en aankomstprocedures, zoals een langere")
    thisalinea.textcontent.append("sleepprocedure voor vliegtuigen. Doel daarvan is de blootstelling van")
    thisalinea.textcontent.append("medewerkers aan emissies uit startende motoren zoveel mogelijk te")
    thisalinea.textcontent.append("verminderen.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Het verstrekken van persoonsgebonden beschermingsmiddelen. Sinds 1 ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 17
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = " Het verstrekken van persoonsgebonden beschermingsmiddelen. Sinds 1 oktober 2022 worden er FFP2-mondneusmaskers beschikbaar gesteld door de werkgevers. Deze mondneusmaskers zijn vrijwillig te gebruiken. Bij correct gebruik, filteren deze mondneusmaskers tot 97% van het ultrafijn stof. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Het verstrekken van persoonsgebonden beschermingsmiddelen. Sinds 1")
    thisalinea.textcontent.append("oktober 2022 worden er FFP2-mondneusmaskers beschikbaar gesteld door")
    thisalinea.textcontent.append("de werkgevers. Deze mondneusmaskers zijn vrijwillig te gebruiken. Bij")
    thisalinea.textcontent.append("correct gebruik, filteren deze mondneusmaskers tot 97% van het ultrafijn")
    thisalinea.textcontent.append("stof.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. Ontzwavelen van kerosine"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 18
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "Fossiele kerosine bevat onder meer zwavel. Die zwavel is een belangrijke bron van het ontstaan van ultrafijn stof bij de verbranding van de kerosine. Ontzwavelen van kerosine zou daarom de emissie van ultrafijn stof kunnen verminderen. Zoals toegezegd aan het lid Kröger in het Commissiedebat Verduurzaming luchtvaart op 16 juni 2022 is het ministerie van IenW in gesprek gegaan met de Duurzame Luchtvaarttafel over ontzwaveling van fossiele kerosine. Partijen gaven aan ontzwaveling te zien als kortetermijnoplossing totdat duurzame brandstoffen op grote schaal beschikbaar komen, maar vragen aandacht voor de additionele kosten die ontzwaveling met zich meebrengt. De duurzame brandstoffen bevatten "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Fossiele kerosine bevat onder meer zwavel. Die zwavel is een belangrijke bron van")
    thisalinea.textcontent.append("het ontstaan van ultrafijn stof bij de verbranding van de kerosine. Ontzwavelen")
    thisalinea.textcontent.append("van kerosine zou daarom de emissie van ultrafijn stof kunnen verminderen.")
    thisalinea.textcontent.append("Zoals toegezegd aan het lid Kröger in het Commissiedebat Verduurzaming")
    thisalinea.textcontent.append("luchtvaart op 16 juni 2022 is het ministerie van IenW in gesprek gegaan met de")
    thisalinea.textcontent.append("Duurzame Luchtvaarttafel over ontzwaveling van fossiele kerosine. Partijen gaven")
    thisalinea.textcontent.append("aan ontzwaveling te zien als kortetermijnoplossing totdat duurzame brandstoffen")
    thisalinea.textcontent.append("op grote schaal beschikbaar komen, maar vragen aandacht voor de additionele")
    thisalinea.textcontent.append("kosten die ontzwaveling met zich meebrengt. De duurzame brandstoffen bevatten")
    thisalinea.textcontent.append("doorgaans geen zwavel en weinig aromatische koolwaterstoffen. De partijen gaven")
    thisalinea.textcontent.append("aan dat dit onderwerp vooral in internationaal verband moet worden opgepakt.")
    thisalinea.textcontent.append("Op 17 maart 2022 is de Kamer per brief7 een onderzoek aangeboden naar de rol")
    thisalinea.textcontent.append("van kerosinesamenstelling in niet-CO2-emissies. Hoewel dit een complex dossier")
    thisalinea.textcontent.append("is, is het van belang doelen en mogelijke middelen daartoe scherp te formuleren.")
    thisalinea.textcontent.append("Zwavel speelt een significante rol in de emissies uit kerosineverbranding. Voor een")
    thisalinea.textcontent.append("reductie van de klimaatschade door condensstrepen is het volgens onderzoek")
    thisalinea.textcontent.append("echter van groter belang om de aromatische koolwaterstoffen, en daarbinnen de")
    thisalinea.textcontent.append("zogeheten naftalenen met twee aromatische verbindingen, in kerosine te")
    thisalinea.textcontent.append("verminderen. De inzet die het ministerie al heeft gepleegd en nog beoogt, is dus")
    thisalinea.textcontent.append("niet alleen gericht op ontzwaveling, maar op het aanscherpen van kwaliteitseisen")
    thisalinea.textcontent.append("voor fossiele kerosine om zo de luchtkwaliteit te verbeteren en klimaatschade te")
    thisalinea.textcontent.append("verminderen.")
    thisalinea.textcontent.append("Zoals aangegeven in de Kamerbrief van 3 maart 2020 8 ligt de mondiale")
    thisalinea.textcontent.append("zwavelnorm voor luchtvaart op 0,3%. De kerosine op de West-Europese markt ligt")
    thisalinea.textcontent.append("in de praktijk ruim onder de mondiale standaard. De nationale ruimte om")
    thisalinea.textcontent.append("kwaliteitseisen voor kerosine te stellen, lijkt beperkt. Ook is dit praktisch")
    thisalinea.textcontent.append("onwerkbaar in een zeer internationale markt met grootschalig,")
    thisalinea.textcontent.append("grensoverschrijdend transport door onder meer buisleidingen. Als een raffinaderij")
    thisalinea.textcontent.append("in Nederland investeringen doet om zwavel en/of aromaten te reduceren, is in een")
    thisalinea.textcontent.append("internationale markt niet op voorhand te zeggen wat het effect is op de getankte")
    thisalinea.textcontent.append("brandstof op Nederlandse luchthavens. De baten voor de luchtkwaliteit in")
    thisalinea.textcontent.append("Nederland en het klimaat zijn dus onzeker en de kans is aanwezig dat de")
    thisalinea.textcontent.append("investeringen in de raffinaderij niet kunnen worden doorgerekend aan afnemers.")
    thisalinea.textcontent.append("Sinds het Commissiedebat van 16 juni 2022 over verduurzaming luchtvaart zijn de")
    thisalinea.textcontent.append("onderhandelingen van het fit-for-55 pakket, waaronder de voorgestelde ReFuelEU-")
    thisalinea.textcontent.append("verordening, voortgezet. Nederland heeft expliciete tekstvoorstellen gedaan om in")
    thisalinea.textcontent.append("de ReFuelEU-verordening voor het eerst monitoring van kerosinesamenstelling")
    thisalinea.textcontent.append("wettelijk vast te leggen, ook met het doel o m hier op termijn meer op te sturen in")
    thisalinea.textcontent.append("Europees verband. De verwachting is ook dat de Europese Commissie via de")
    thisalinea.textcontent.append("verordening door het Parlement zal worden opgeroepen op korte termijn een")
    thisalinea.textcontent.append("effectbeoordeling te doen naar de mogelijkheden en kosten en baten van een")
    thisalinea.textcontent.append("eigen Europese kwaliteitseis voor fossiele kerosine.")
    thisalinea.textcontent.append("De meest kansrijke route is, naast primair in te blijven zetten op het gebruik van")
    thisalinea.textcontent.append("duurzame luchtvaartbrandstof, een aanscherping van de mondiale kwaliteitseisen,")
    thisalinea.textcontent.append("om zoveel mogelijk milieuvoordeel met geringe concurrentienadelen te realiseren.")
    thisalinea.textcontent.append("De organisatie met de grootste impact op de kerosine in Nederland is de")
    thisalinea.textcontent.append("standaardenorganisatie ASTM International. Hierin heeft de Nederlandse overheid")
    thisalinea.textcontent.append("geen rol. Voor overheden is het belangrijkste platform de VN-")
    thisalinea.textcontent.append("burgerluchtvaartorganisatie ICAO. Het ministerie zal de kerosinekwaliteit daarom")
    thisalinea.textcontent.append("actief in ICAO-verband agenderen. Aanvullend zal met nationale stakeholders en")
    thisalinea.textcontent.append("gelijkgestemde (Europese en andere) overheden nader worden verkend hoe dit")
    thisalinea.textcontent.append("dossier mondiaal verder kan worden gebracht.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. Emissie van zeer zorgwekkende stoffen (ZZS)"
    thisalinea.titlefontsize = "8.999999999999972"
    thisalinea.nativeID = 19
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "In antwoord op Kamervragen in maart 2022 9 en tijdens het Commissiedebat Verduurzaming luchtvaart van 16 juni 2022 10 is aan de vaste commissie toegezegd dat de Kamer wordt geïnformeerd over de noodzaak van het nemen van beleidsmaatregelen om de uitstoot van ZZS door de luchtvaart te beperken. Daartoe zou eerst onderzoek worden uitgevoerd naar de uitstoot van ZZS door de luchtvaart en de daaruit volgende concentraties rond Nederlandse luchthavens van nationale betekenis. Het streven was om de hiervoor genoemde informatie in de tweede helft van 2022 aan de Kamer te sturen. Gelet op grote drukte bij onderzoekspartijen heeft het "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In antwoord op Kamervragen in maart 2022 9 en tijdens het Commissiedebat")
    thisalinea.textcontent.append("Verduurzaming luchtvaart van 16 juni 2022 10 is aan de vaste commissie")
    thisalinea.textcontent.append("toegezegd dat de Kamer wordt geïnformeerd over de noodzaak van het nemen")
    thisalinea.textcontent.append("van beleidsmaatregelen om de uitstoot van ZZS door de luchtvaart te beperken.")
    thisalinea.textcontent.append("Daartoe zou eerst onderzoek worden uitgevoerd naar de uitstoot van ZZS door de")
    thisalinea.textcontent.append("luchtvaart en de daaruit volgende concentraties rond Nederlandse luchthavens van")
    thisalinea.textcontent.append("nationale betekenis.")
    thisalinea.textcontent.append("Het streven was om de hiervoor genoemde informatie in de tweede helft van 2022")
    thisalinea.textcontent.append("aan de Kamer te sturen. Gelet op grote drukte bij onderzoekspartijen heeft het")
    thisalinea.textcontent.append("onderzoek helaas vertraging opgelopen.")
    thisalinea.textcontent.append("De eerste stap in het onderzoeksproject is afgerond. TNO heeft berekend welke")
    thisalinea.textcontent.append("emissies van ZZS plaatsvinden door het vliegverkeer van de luchthavens Schiphol,")
    thisalinea.textcontent.append("Rotterdam The Hague Airport, Eindhoven Airport, Maastricht Aachen Airport en")
    thisalinea.textcontent.append("Groningen Airport Eelde. Een belangrijke bevinding is dat de meeste ZZS door de")
    thisalinea.textcontent.append("vliegtuigen worden geëmitteerd tijdens het taxiën op de luchthavens (rond de")
    thisalinea.textcontent.append("90%), dus niet tijdens het vliegen. De reden daarvoor is dat bij taxiën de")
    thisalinea.textcontent.append("verbranding van kerosine niet optimaal is, omdat dan maar een heel beperkt deel")
    thisalinea.textcontent.append("van het vermogen van de vliegtuigmotoren wordt gebruikt.")
    thisalinea.textcontent.append("De volgende stap in het onderzoek is dat moet worden berekend welke")
    thisalinea.textcontent.append("concentraties in de omgeving van de luchthavens worden veroorzaakt do or de")
    thisalinea.textcontent.append("emissies van de ZZS door de vliegtuigen. Het gaat immers niet alleen om de")
    thisalinea.textcontent.append("omvang van de emissies, maar ook om wat die emissies betekenen voor de")
    thisalinea.textcontent.append("blootstelling van de omgeving. De concentratieberekeningen worden in de eerste")
    thisalinea.textcontent.append("helft van 2023 door het NLR uitgevoerd. Op basis van de berekende concentraties")
    thisalinea.textcontent.append("worden beleidsconclusies geformuleerd en zal de Kamer over alle berekeningen en")
    thisalinea.textcontent.append("het vervolg in het derde kwartaal van 2023 worden geïnformeerd.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "4. Uniformeren van het berekenen van emissies en concentraties"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 20
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "Het ministerie van IenW is vorig jaar gestart met het uniformer en transparanter maken van de rekenmethodiek voor luchtvaartemissies. De aangrijpingspunten daarvoor zijn in oktober 2021 in een rapport vastgesteld, dat ter informatie bij deze brief is gevoegd. Naar aanleiding van dat rapport zijn vervolgstappen gezet. De eerste stap naar meer uniformiteit was het opstellen van een Nationale database vliegtuigemissies. In deze database zijn onder meer per motortype het brandstofverbruik en de emissiefactoren van verschillende stoffen opgenomen. Deze emissiefactoren zijn uitgesplitst naar de verschillende vliegfasen van de Landing & Take -Off (LTO, start- en landcyclus) cycle, te weten approach (nadering), "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Het ministerie van IenW is vorig jaar gestart met het uniformer en transparanter")
    thisalinea.textcontent.append("maken van de rekenmethodiek voor luchtvaartemissies. De aangrijpingspunten")
    thisalinea.textcontent.append("daarvoor zijn in oktober 2021 in een rapport vastgesteld, dat ter informatie bij")
    thisalinea.textcontent.append("deze brief is gevoegd.")
    thisalinea.textcontent.append("Naar aanleiding van dat rapport zijn vervolgstappen gezet. De eerste stap naar")
    thisalinea.textcontent.append("meer uniformiteit was het opstellen van een Nationale database vliegtuigemissies.")
    thisalinea.textcontent.append("In deze database zijn onder meer per motortype het brandstofverbruik en de")
    thisalinea.textcontent.append("emissiefactoren van verschillende stoffen opgenomen. Deze emissiefactoren zijn")
    thisalinea.textcontent.append("uitgesplitst naar de verschillende vliegfasen van de Landing & Take -Off (LTO,")
    thisalinea.textcontent.append("start- en landcyclus) cycle, te weten approach (nadering), idle/taxi (taxiën), take -")
    thisalinea.textcontent.append("off (opstijgen) en climb-out (wegklimmen). Ook zijn in de database")
    thisalinea.textcontent.append("emissiefactoren opgenomen voor APU’s (auxiliary power units, de hulpmotoren in")
    thisalinea.textcontent.append("vliegtuigen) en GPU’s (ground power units, mobiele stroomvoorziening die wordt")
    thisalinea.textcontent.append("gebruikt op luchthavens).")
    thisalinea.textcontent.append("De database zorgt ervoor dat iedereen die berekeningen uitvoert, dezelfde input")
    thisalinea.textcontent.append("gebruikt, waardoor achteraf geen discussie kan ontstaan over de voor de")
    thisalinea.textcontent.append("berekeningen gebruikte invoergegevens. De database is in september 2022")
    thisalinea.textcontent.append("beschikbaar gekomen op de website van het Informatiepunt leefomgeving (Iplo)11.")
    thisalinea.textcontent.append("De tweede stap is het uniformeren van de rekenregels. Daartoe is in november")
    thisalinea.textcontent.append("2022 een offerte-uitvraag gedaan. De verwachting is dat een opdracht begin 2023")
    thisalinea.textcontent.append("kan worden verstrekt.")
    thisalinea.textcontent.append("De uniforme rekenregels kunnen worden gebruikt voor het vaststellen en")
    thisalinea.textcontent.append("handhaven van grenswaarden voor de emissie van luchtverontreinigende stoffen")
    thisalinea.textcontent.append("(zoals in artikel 4.3.1. van het Luchthavenverkeerbesluit Schiphol), voor het")
    thisalinea.textcontent.append("opstellen van internationale rapportageverplichtingen en bij het opstellen van")
    thisalinea.textcontent.append("milieueffectrapporten (MER-ren) voor luchthaven(verkeer)besluiten. Bovendien")
    thisalinea.textcontent.append("kunnen de luchtvaartemissies die volgens de rekenregels worden berekend,")
    thisalinea.textcontent.append("dienen als invoergegevens bij de vaststelling en handhaving van")
    thisalinea.textcontent.append("concentratienormen en depositieberekeningen (AERIUS).")
    thisalinea.textcontent.append("De rekenregels dienen zoveel mogelijk aan te sluiten bij de invoergegevens voor")
    thisalinea.textcontent.append("geluidsberekening, zoals de vliegtuigregistratie, vliegtuigprestaties, routegebruik")
    thisalinea.textcontent.append("en de vliegprofielen. De Kamer zal in de tweede helft van 2023 worden")
    thisalinea.textcontent.append("geïnformeerd over de voortgang van dit project.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "5. Emissies boven 3.000 voet"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 21
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "In de Emissieregistratie van het RIVM worden de emissies inzichtelijk gemaakt tot een hoogte van 3.000 voet (ongeveer 1 kilometer). Deze emissies worden elk jaar internationaal gerapporteerd, onder andere aan de Europese Commissie. In 2019 heeft de Kamer opgeroepen om ook de uitstoot van stikstofoxiden boven de 3 .000 voet inzichtelijk te maken12. Ook in reactie op het deelrapport luchtvaart van het Adviescollege Stikstofproblematiek is aangegeven dat het Ministerie van IenW zich hier hard voor gaat maken13. Het RIVM is voornemens om vanaf 2023 ook de emissies boven 3.000 voet inzichtelijk te maken. Dat geldt niet alleen voor de emissies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In de Emissieregistratie van het RIVM worden de emissies inzichtelijk gemaakt tot")
    thisalinea.textcontent.append("een hoogte van 3.000 voet (ongeveer 1 kilometer). Deze emissies worden elk jaar")
    thisalinea.textcontent.append("internationaal gerapporteerd, onder andere aan de Europese Commissie. In 2019")
    thisalinea.textcontent.append("heeft de Kamer opgeroepen om ook de uitstoot van stikstofoxiden boven de 3 .000")
    thisalinea.textcontent.append("voet inzichtelijk te maken12. Ook in reactie op het deelrapport luchtvaart van het")
    thisalinea.textcontent.append("Adviescollege Stikstofproblematiek is aangegeven dat het Ministerie van IenW zich")
    thisalinea.textcontent.append("hier hard voor gaat maken13.")
    thisalinea.textcontent.append("Het RIVM is voornemens om vanaf 2023 ook de emissies boven 3.000 voet")
    thisalinea.textcontent.append("inzichtelijk te maken. Dat geldt niet alleen voor de emissies van stikstofoxiden,")
    thisalinea.textcontent.append("maar ook voor zoveel mogelijk andere stoffen. Komend jaar zal nodig zijn om de")
    thisalinea.textcontent.append("systematiek goed te implementeren. Mocht dit tot onvoorziene vertraging zorgen,")
    thisalinea.textcontent.append("dan zal de opname van de emissies bove n 3.000 voet vanaf 2024 in de")
    thisalinea.textcontent.append("Emissieregistratie plaatsvinden.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "6. Emissies van 440.000 vliegtuigbewegingen op Schiphol"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 22
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "Op 24 juni 202214 heeft het kabinet besloten om het jaarlijks aantal toegestane vluchten op Schiphol te reduceren van 500.000 naar 440.000 vliegtuigbewegingen. Minder vluchten leiden in beginsel tot minder emissies . Dit is echter wel afhankelijk van het type vliegtuigen dat wordt ingezet en de wijze waarop wordt gevlogen. Het ministerie van IenW laat daarom voor verschillende scenario’s in kaart brengen wat de effecten van de capaciteitsreductie zijn op de emissies van verschillende stoffen. De Kamer wordt over de resultaten hiervan naar verwachting in het voorjaar van 2023 via de periodieke voortgangsbrief Programma Omgeving Luchthaven Schiphol geïnformeerd. Zoals aangegeven "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Op 24 juni 202214 heeft het kabinet besloten om het jaarlijks aantal toegestane")
    thisalinea.textcontent.append("vluchten op Schiphol te reduceren van 500.000 naar 440.000")
    thisalinea.textcontent.append("vliegtuigbewegingen.")
    thisalinea.textcontent.append("Minder vluchten leiden in beginsel tot minder emissies . Dit is echter wel")
    thisalinea.textcontent.append("afhankelijk van het type vliegtuigen dat wordt ingezet en de wijze waarop wordt")
    thisalinea.textcontent.append("gevlogen. Het ministerie van IenW laat daarom voor verschillende scenario’s in")
    thisalinea.textcontent.append("kaart brengen wat de effecten van de capaciteitsreductie zijn op de emissies van")
    thisalinea.textcontent.append("verschillende stoffen. De Kamer wordt over de resultaten hiervan naar")
    thisalinea.textcontent.append("verwachting in het voorjaar van 2023 via de periodieke voortgangsbrief")
    thisalinea.textcontent.append("Programma Omgeving Luchthaven Schiphol geïnformeerd. Zoals aangegeven in de")
    thisalinea.textcontent.append("Hoofdlijnenbrief Schiphol van 24 juni 2022 is het uitgangspunt om te komen tot")
    thisalinea.textcontent.append("normering van de milieueffecten. Vanaf dat moment wordt geborgd dat negatieve")
    thisalinea.textcontent.append("gezondheidseffecten van Schiphol stapsgewijs afnemen. De vermindering van het")
    thisalinea.textcontent.append("aantal vluchten is een eerste stap.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "7. Bestuursovereenkomst intenties samenwerking NOVEX Schipholregio"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 23
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "Zoals in de tweede voortgangsbrief van het IenW Programma Omgeving Luchthaven Schiphol15 is opgenomen, wordt in de NOVEX Schipholregio samengewerkt door Rijk en regio om de leefomgevingskwaliteit in de Schipholregio te verbeteren. Eén van de acht hoofdopgaven uit de Bestuursovereenkomst ‘intenties samenwerking NOVEX Schipholregio’ betreft luchtkwaliteit en ultrafijn stof. Er wordt in de NOVEX-aanpak breder gekeken dan alleen naar luchtvaart, ook naar andere bronnen die emissies uitstoten , zoals wegverkeer en industrie. Hierbij wordt ook de aanbeveling van de Gezondheidsraad 16 betrokken, om de leefomgeving zodanig in te richten dat langdurig verhoogde blootstelling aan ultrafijn stof wordt beperkt. Dat kan "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Zoals in de tweede voortgangsbrief van het IenW Programma Omgeving")
    thisalinea.textcontent.append("Luchthaven Schiphol15 is opgenomen, wordt in de NOVEX Schipholregio")
    thisalinea.textcontent.append("samengewerkt door Rijk en regio om de leefomgevingskwaliteit in de")
    thisalinea.textcontent.append("Schipholregio te verbeteren. Eén van de acht hoofdopgaven uit de")
    thisalinea.textcontent.append("Bestuursovereenkomst ‘intenties samenwerking NOVEX Schipholregio’ betreft")
    thisalinea.textcontent.append("luchtkwaliteit en ultrafijn stof. Er wordt in de NOVEX-aanpak breder gekeken dan")
    thisalinea.textcontent.append("alleen naar luchtvaart, ook naar andere bronnen die emissies uitstoten , zoals")
    thisalinea.textcontent.append("wegverkeer en industrie.")
    thisalinea.textcontent.append("Hierbij wordt ook de aanbeveling van de Gezondheidsraad 16 betrokken, om de")
    thisalinea.textcontent.append("leefomgeving zodanig in te richten dat langdurig verhoogde blootstelling aan")
    thisalinea.textcontent.append("ultrafijn stof wordt beperkt. Dat kan bijvoorbeeld door bij de bouw van woningen")
    thisalinea.textcontent.append("rekening te houden met de aanwezigheid van drukke (snel)wegen en overige")
    thisalinea.textcontent.append("ultrafijnstofbronnen, zoals Schiphol.")
    thisalinea.textcontent.append("Ter uitvoering van de bestuursovereenkomst wordt nu gewerkt aan de")
    thisalinea.textcontent.append("concretiseringsfase. De verwachting is dat de Kamer rond de zomer 2023 over de")
    thisalinea.textcontent.append("resultaten van deze fase kan worden geïnformeerd via de periodieke")
    thisalinea.textcontent.append("voortgangsbrief Programma Omgeving Luchthaven Schiphol.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Tot slot"
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 24
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "Uit het hiervoor staande blijkt dat er langs verschillende lijnen stappen worden gezet om de invloed van luchtvaartemissies op de lokale luchtkwaliteit en de gezondheidseffecten daarvan, te beperken. Hoogachtend, DE MINISTER VAN INFRASTRUCTUUR EN WATERSTAAT, Mark Harbers "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Uit het hiervoor staande blijkt dat er langs verschillende lijnen stappen worden")
    thisalinea.textcontent.append("gezet om de invloed van luchtvaartemissies op de lokale luchtkwaliteit en de")
    thisalinea.textcontent.append("gezondheidseffecten daarvan, te beperken.")
    thisalinea.textcontent.append("Hoogachtend,")
    thisalinea.textcontent.append("DE MINISTER VAN INFRASTRUCTUUR EN WATERSTAAT,")
    thisalinea.textcontent.append("Mark Harbers")
    alineas.append(thisalinea)

    return alineas
