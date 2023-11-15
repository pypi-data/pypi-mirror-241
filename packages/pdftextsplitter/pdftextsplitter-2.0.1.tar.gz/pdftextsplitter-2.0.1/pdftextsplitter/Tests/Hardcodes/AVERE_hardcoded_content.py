import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_AVERE() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document AVERE
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
    thisalinea.texttitle = "AVERE"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Avec le soutien de 1. Synthèse 3.1.3. Incertitudes sur la part des alternatives technologiques à la mobilité lourde à batterie électrique 3.2.1. Faible disponibilité du foncier sur grands axes routiers pour accueillir des stations de recharge, en particulier pour poids lourds 3.2.3. Investissements importants nécessaires, en particulier pour la recharge DC 3.2.4. Délais de fourniture des bornes de recharge et autres défis relatifs à la chaîne d’approvisionnement 5 11 11 13 15 16 16 17 18 20 23 23 23 24 24 25 25 26 26 27 27 27 28 29 30 30 30 31 31 31 5.1. Vue détaillée "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Septembre 2023 HIT THE ROAD TOME 2 DÉPLOIEMENT DE LA RECHARGE SUR LES GRANDS AXES ROUTIERS"
    thisalinea.titlefontsize = "22.0"
    thisalinea.nativeID = 1
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Avec le soutien de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Avec le soutien de")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "SOMMAIRE"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 2
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "1. Synthèse 3.1.3. Incertitudes sur la part des alternatives technologiques à la mobilité lourde à batterie électrique 3.2.1. Faible disponibilité du foncier sur grands axes routiers pour accueillir des stations de recharge, en particulier pour poids lourds 3.2.3. Investissements importants nécessaires, en particulier pour la recharge DC 3.2.4. Délais de fourniture des bornes de recharge et autres défis relatifs à la chaîne d’approvisionnement 5 11 11 13 15 16 16 17 18 20 23 23 23 24 24 25 25 26 26 27 27 27 28 29 30 30 30 31 31 31 5.1. Vue détaillée par axe routier des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Synthèse "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Synthèse "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Synthèse")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Modélisation des besoins en IRVE pour 2030-2035"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 4
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.1 Méthodologie et hypothèses générales"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 5
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.1.1. Projection du parc de véhicules électriques"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 6
    thisalinea.parentID = 5
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.1.2. Évolution technique des véhicules"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 7
    thisalinea.parentID = 5
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2. Zoom sur les besoins en recharge sur les grands axes routiers"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 8
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.2.1. Analyse du comportement de recharge lors de l’itinérance"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 9
    thisalinea.parentID = 8
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.2.2. Estimation des besoins énergétiques pour la recharge publique"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 10
    thisalinea.parentID = 8
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.2.3. Évaluation du nombre de points de charge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 11
    thisalinea.parentID = 8
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.3. Synthèse des besoins en recharge publique sur le territoire français"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 12
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Obstacles au déploiement d’une infrastructure de recharge publique"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 13
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3.1.3. Incertitudes sur la part des alternatives technologiques à la mobilité lourde à batterie électrique 3.2.1. Faible disponibilité du foncier sur grands axes routiers pour accueillir des stations de recharge, en particulier pour poids lourds 3.2.3. Investissements importants nécessaires, en particulier pour la recharge DC 3.2.4. Délais de fourniture des bornes de recharge et autres défis relatifs à la chaîne d’approvisionnement 5 11 11 13 15 16 16 17 18 20 23 23 23 24 24 25 25 26 26 27 27 27 28 29 30 30 30 31 31 31 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.1. Obstacles à la planification optimale des IRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 14
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "3.1.3. Incertitudes sur la part des alternatives technologiques à la mobilité lourde à batterie électrique "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.1.1. Raccordement électrique des IRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 15
    thisalinea.parentID = 14
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.1.2. Visibilité insuffisante pour la bonne élaboration des SDIRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 16
    thisalinea.parentID = 14
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "3.1.3. Incertitudes sur la part des alternatives technologiques à la mobilité lourde à batterie électrique "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3.1.3. Incertitudes sur la part des alternatives technologiques")
    thisalinea.textcontent.append("à la mobilité lourde à batterie électrique")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2. Obstacles à l’installation des IRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 17
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "3.2.1. Faible disponibilité du foncier sur grands axes routiers pour accueillir des stations de recharge, en particulier pour poids lourds 3.2.3. Investissements importants nécessaires, en particulier pour la recharge DC 3.2.4. Délais de fourniture des bornes de recharge et autres défis relatifs à la chaîne d’approvisionnement "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3.2.1. Faible disponibilité du foncier sur grands axes routiers")
    thisalinea.textcontent.append("pour accueillir des stations de recharge, en particulier pour poids lourds")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.2.2. Faible disponibilité du foncier en zone urbaine dense"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 18
    thisalinea.parentID = 17
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "3.2.3. Investissements importants nécessaires, en particulier pour la recharge DC 3.2.4. Délais de fourniture des bornes de recharge et autres défis relatifs à la chaîne d’approvisionnement "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3.2.3. Investissements importants nécessaires,")
    thisalinea.textcontent.append("en particulier pour la recharge DC")
    thisalinea.textcontent.append("3.2.4. Délais de fourniture des bornes de recharge")
    thisalinea.textcontent.append("et autres défis relatifs à la chaîne d’approvisionnement")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.3. Obstacles à l’opération des IRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 19
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.3.1. Rentabilité insuffisante"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 20
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.3.2. Durée légale des contrats de sous-concessions autoroutières"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 21
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.3.3. Défis de la maintenance et du taux de disponibilité"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 22
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.3.4. Volatilité des prix de l’énergie"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 23
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.4. Obstacles à l’achat de véhicules électriques liés à la recharge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 24
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "5 11 11 13 15 16 16 17 18 20 23 23 23 24 24 25 25 26 26 27 27 27 28 29 30 30 30 31 31 31 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.4.1. Complexité du parcours de recharge"
    thisalinea.titlefontsize = "9.999999999999986"
    thisalinea.nativeID = 25
    thisalinea.parentID = 24
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.4.2. Opacité de la tarification et prix de la recharge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 26
    thisalinea.parentID = 24
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.4.3. Anxiété à la recharge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 27
    thisalinea.parentID = 24
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.4.4. Indisponibilité de recharge de proximité abordable"
    thisalinea.titlefontsize = "10.000000000000007"
    thisalinea.nativeID = 28
    thisalinea.parentID = 24
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "5 11 11 13 15 16 16 17 18 20 23 23 23 24 24 25 25 26 26 27 27 27 28 29 30 30 30 31 31 31 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5")
    thisalinea.textcontent.append("11")
    thisalinea.textcontent.append("11")
    thisalinea.textcontent.append("13")
    thisalinea.textcontent.append("15")
    thisalinea.textcontent.append("16")
    thisalinea.textcontent.append("16")
    thisalinea.textcontent.append("17")
    thisalinea.textcontent.append("18")
    thisalinea.textcontent.append("20")
    thisalinea.textcontent.append("23")
    thisalinea.textcontent.append("23")
    thisalinea.textcontent.append("23")
    thisalinea.textcontent.append("24")
    thisalinea.textcontent.append("24")
    thisalinea.textcontent.append("25")
    thisalinea.textcontent.append("25")
    thisalinea.textcontent.append("26")
    thisalinea.textcontent.append("26")
    thisalinea.textcontent.append("27")
    thisalinea.textcontent.append("27")
    thisalinea.textcontent.append("27")
    thisalinea.textcontent.append("28")
    thisalinea.textcontent.append("29")
    thisalinea.textcontent.append("30")
    thisalinea.textcontent.append("30")
    thisalinea.textcontent.append("30")
    thisalinea.textcontent.append("31")
    thisalinea.textcontent.append("31")
    thisalinea.textcontent.append("31")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Mesures-clés pour réussir le déploiement d’une infrastructure de recharge publique 32"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 29
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "5.1. Vue détaillée par axe routier des besoins en points de charge à horizon 2035 pour le scénario Haut, Central et Bas Infrastructures de recharge (définitions réglementaires) 32 32 33 34 35 36 37 37 38 38 39 40 41 41 43 43 43 44 5. Annexes 6. Définitions 7. Abréviations 8. Table des figures "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.1. Mesures-clés « Grands axes routiers »"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 30
    thisalinea.parentID = 29
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.1.1. Anticipation des besoins en raccordements"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 31
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.1.2. Allongement des durées de contrats de sous-concession"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 32
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.1.3. Réduction des pointes de trafic en amont"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 33
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.1.4. Absorption des pointes de trafic via des solutions ad hoc"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 34
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.1.5. L’autoroute électrique"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 35
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.2. Mesures-clés transverses"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 36
    thisalinea.parentID = 29
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "5.1. Vue détaillée par axe routier des besoins en points de charge à horizon 2035 pour le scénario Haut, Central et Bas Infrastructures de recharge (définitions réglementaires) 32 32 33 34 35 36 37 37 38 38 39 40 41 41 43 43 43 44 5. Annexes 6. Définitions 7. Abréviations 8. Table des figures "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.2.1. Création d’une entité publique en charge de la planification des IRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 37
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.2.2. Promotion des offres de raccordements intelligentes"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 38
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.2.3. Fiabilité des données en open data"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 39
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.2.4. Standardisation progressive du 800 V"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 40
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4.2.5. Soutien à l’acquisition des poids lourds"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 41
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5.1. Vue détaillée par axe routier des besoins en points de charge à horizon 2035 pour le scénario Haut, Central et Bas Infrastructures de recharge (définitions réglementaires) 32 32 33 34 35 36 37 37 38 38 39 40 41 41 43 43 43 44 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5.1. Vue détaillée par axe routier des besoins en points de charge")
    thisalinea.textcontent.append("à horizon 2035 pour le scénario Haut, Central et Bas")
    thisalinea.textcontent.append("Infrastructures de recharge (définitions réglementaires)")
    thisalinea.textcontent.append("32")
    thisalinea.textcontent.append("32")
    thisalinea.textcontent.append("33")
    thisalinea.textcontent.append("34")
    thisalinea.textcontent.append("35")
    thisalinea.textcontent.append("36")
    thisalinea.textcontent.append("37")
    thisalinea.textcontent.append("37")
    thisalinea.textcontent.append("38")
    thisalinea.textcontent.append("38")
    thisalinea.textcontent.append("39")
    thisalinea.textcontent.append("40")
    thisalinea.textcontent.append("41")
    thisalinea.textcontent.append("41")
    thisalinea.textcontent.append("43")
    thisalinea.textcontent.append("43")
    thisalinea.textcontent.append("43")
    thisalinea.textcontent.append("44")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "5. Annexes "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 42
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "5. Annexes "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. Annexes")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "6. Définitions "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 43
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "6. Définitions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. Définitions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "7. Abréviations "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 44
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "7. Abréviations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("7. Abréviations")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "8. Table des figures "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 45
    thisalinea.parentID = 36
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "8. Table des figures "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("8. Table des figures")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. Synthèse"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 46
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Dans le cadre du projet « Hit the Road » pour l’Avere-France, AFRY a réalisé la présente étude sur les besoins en recharge publique à horizon 2035. Elle comporte un Tome 1 – État des lieux de la recharge en France, ainsi que deux analyses s’appuyant sur une modé- lisation des besoins et proposant des mesures clés de succès pour traiter deux enjeux spécifiques : le Tome 2 – Déploiement de la recharge sur les grands axes routiers et le Tome 3 – Déploiement de la recharge dans les zones à pourvoir. Ces documents se veulent complémentaires, et proposent des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "ARTICULATION DE L’ÉTUDE HIT THE ROAD"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 47
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Dans le cadre du projet « Hit the Road » pour l’Avere-France, AFRY a réalisé la présente étude sur les besoins en recharge publique à horizon 2035. Elle comporte un Tome 1 – État des lieux de la recharge en France, ainsi que deux analyses s’appuyant sur une modé- lisation des besoins et proposant des mesures clés de succès pour traiter deux enjeux spécifiques : le Tome 2 – Déploiement de la recharge sur les grands axes routiers et le Tome 3 – Déploiement de la recharge dans les zones à pourvoir. Ces documents se veulent complémentaires, et proposent des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Dans le cadre du projet « Hit the Road » pour l’Avere-France, AFRY a réalisé la présente")
    thisalinea.textcontent.append("étude sur les besoins en recharge publique à horizon 2035. Elle comporte un Tome 1 – État")
    thisalinea.textcontent.append("des lieux de la recharge en France, ainsi que deux analyses s’appuyant sur une modé-")
    thisalinea.textcontent.append("lisation des besoins et proposant des mesures clés de succès pour traiter deux enjeux")
    thisalinea.textcontent.append("spécifiques : le Tome 2 – Déploiement de la recharge sur les grands axes routiers et le")
    thisalinea.textcontent.append("Tome 3 – Déploiement de la recharge dans les zones à pourvoir. Ces documents se veulent")
    thisalinea.textcontent.append("complémentaires, et proposent des mesures transverses.")
    thisalinea.textcontent.append("Les infrastructures de recharge de véhicules")
    thisalinea.textcontent.append("de la Transition énergétique. La dynamique")
    thisalinea.textcontent.append("électriques (IRVE) sur les axes routiers seront")
    thisalinea.textcontent.append("est lancée, avec une forte croissance dans le")
    thisalinea.textcontent.append("essentielles d’une part pour assurer l’électri-")
    thisalinea.textcontent.append("déploiement des IRVE sur les derniers mois.")
    thisalinea.textcontent.append("fication des trajets longue distance, d’autre")
    thisalinea.textcontent.append("Mais certaines zones restent moins pourvues")
    thisalinea.textcontent.append("part pour les poids lourds parcourant plusieurs")
    thisalinea.textcontent.append("dizaines de milliers de kilomètres chaque année.")
    thisalinea.textcontent.append("que d’autres, en particulier les routes natio-")
    thisalinea.textcontent.append("nales et les autoroutes non concédées. Sur")
    thisalinea.textcontent.append("En mai 2023, le cap des 100 000 points de")
    thisalinea.textcontent.append("service étaient équipées en recharge rapide")
    thisalinea.textcontent.append("charge ouverts au public a été franchi, d’après")
    thisalinea.textcontent.append("le baromètre de l’Avere-France et le ministère")
    thisalinea.textcontent.append("au 31 décembre 2022. Cela correspondait à une")
    thisalinea.textcontent.append("station de recharge tous les 60km1.")
    thisalinea.textcontent.append("les autoroutes concédées, 80 % des aires de")
    thisalinea.textcontent.append("Figure 1 : Cartographie des points de charge sur les grands axes routiers")
    thisalinea.textcontent.append("Pour cette première vague de déploiement sur")
    thisalinea.textcontent.append("les autoroutes, prévue pour s’achever en 2023,")
    thisalinea.textcontent.append("des moyens importants ont été mobilisés par")
    thisalinea.textcontent.append("les SCA (Sociétés concessionnaires d’autoroutes)")
    thisalinea.textcontent.append("La modélisation des besoins à horizon 2030-")
    thisalinea.textcontent.append("grands axes.")
    thisalinea.textcontent.append("un trafic de véhicules électrifiés en moyenne à")
    thisalinea.textcontent.append("27 % (scénario Central d’électrification), dans le")
    thisalinea.textcontent.append("cas d’un taux d’utilisation de 12,5 %.")
    thisalinea.textcontent.append("Le sujet du taux d’utilisation est un indicateur")
    thisalinea.textcontent.append("important dans la planification des projets de")
    thisalinea.textcontent.append("déploiement d’IRVE, avec des impacts directs")
    thisalinea.textcontent.append("sur la rentabilité. Cela représente la valeur")
    thisalinea.textcontent.append("moyenne sur une année du nombre d’heures")
    thisalinea.textcontent.append("actuelle, de l’ordre de 2 %6, sa valeur devrait aug-")
    thisalinea.textcontent.append("menter au fur et à mesure que la transition des")
    thisalinea.textcontent.append("usagers vers le véhicule électrique se réalisera.")
    thisalinea.textcontent.append("La Commission européenne7 cible pour 2030")
    thisalinea.textcontent.append("un taux d’utilisation de 12,5 % pour les chargeurs")
    thisalinea.textcontent.append("d’utilisation d’un point par jour, c’est-à-dire le")
    thisalinea.textcontent.append("les plus rapides. C’est ainsi que cette valeur a")
    thisalinea.textcontent.append("nombre d’heures où le point de charge délivre")
    thisalinea.textcontent.append("été retenue dans le cadre de la modélisation")
    thisalinea.textcontent.append("de l’énergie à un ou plusieurs véhicules. Alors")
    thisalinea.textcontent.append("du besoin en points de charge sur les grands")
    thisalinea.textcontent.append("que le taux d’utilisation moyen des points de")
    thisalinea.textcontent.append("axes routiers.")
    thisalinea.textcontent.append("charge à l’échelle du territoire est, à l’heure")
    thisalinea.textcontent.append("Figure 2 : Besoin en nombre de points de charge")
    thisalinea.textcontent.append("pour la recharge publique sur les grands axes routiers8")
    thisalinea.textcontent.append("Total")
    thisalinea.textcontent.append("Véhicules légers")
    thisalinea.textcontent.append("Poids lourds")
    thisalinea.textcontent.append("L’électrification du parc de véhicules va")
    thisalinea.textcontent.append("demander une croissance du réseau d’in-")
    thisalinea.textcontent.append("frastructure de recharge, même dans le")
    thisalinea.textcontent.append("cadre du scénario Bas avec l’objectif de 20 000")
    thisalinea.textcontent.append("points qui est bien supérieur aux 4 000 points9")
    thisalinea.textcontent.append("environ actuellement présents sur les grands")
    thisalinea.textcontent.append("axes routiers. La Figure 3 illustre par exemple")
    thisalinea.textcontent.append("le besoin en nombre de points pour quelques")
    thisalinea.textcontent.append("grands axes, tout en comparant avec la situation")
    thisalinea.textcontent.append("actuelle.")
    thisalinea.textcontent.append("Figure 3 : Besoin en nombre de points sur quelques axes routiers pour les véhicules légers")
    thisalinea.textcontent.append("et pour les poids lourds dans les différents scénarios par rapport à l’actuel")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "■ Étape n° 2 : Application de 3 scénarios de taux ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 48
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Étape n° 2 : Application de 3 scénarios de taux d’électrification. Les projections de véhicules électriques de RTE3,4 et de BNEF5 ont été utilisées. et les acteurs de la mobilité ; par ailleurs, des mécanismes de soutien à l’installation ont été Cela permet d’obtenir des scénarios : mis en place (subvention des investissements, majoration dérogatoire du taux de réfaction à 75 %). La vague suivante, qui nécessitera des raccordements et des puissances installées supplémentaires (avec notamment l’arrivée de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 2 : Application de 3 scénarios de taux")
    thisalinea.textcontent.append("d’électrification. Les projections de véhicules")
    thisalinea.textcontent.append("électriques de RTE3,4 et de BNEF5 ont été")
    thisalinea.textcontent.append("utilisées.")
    thisalinea.textcontent.append("et les acteurs de la mobilité ; par ailleurs, des")
    thisalinea.textcontent.append("mécanismes de soutien à l’installation ont été")
    thisalinea.textcontent.append("Cela permet d’obtenir des scénarios :")
    thisalinea.textcontent.append("mis en place (subvention des investissements,")
    thisalinea.textcontent.append("majoration dérogatoire du taux de réfaction")
    thisalinea.textcontent.append("à 75 %). La vague suivante, qui nécessitera des")
    thisalinea.textcontent.append("raccordements et des puissances installées")
    thisalinea.textcontent.append("supplémentaires (avec notamment l’arrivée de")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– Haut, Central et Bas pour les véhicules légers ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 49
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– Haut, Central et Bas pour les véhicules légers respectivement à 31 %, 27 % et 16 % pour le taux d’électrification du parc à horizon 2035 ; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Haut, Central et Bas pour les véhicules légers")
    thisalinea.textcontent.append("respectivement à 31 %, 27 % et 16 % pour le")
    thisalinea.textcontent.append("taux d’électrification du parc à horizon 2035 ;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– Pour les poids lourds, le scénario Haut repré- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 50
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– Pour les poids lourds, le scénario Haut repré- sente une vision constructeur avec un taux la mobilité lourde), devra faire des choix straté- d’électrification de près de 40 % et des taux giques concernant la gestion de l’affluence et du à 18 % et 3 % pour les deux autres scénarios. dimensionnement du réseau. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Pour les poids lourds, le scénario Haut repré-")
    thisalinea.textcontent.append("sente une vision constructeur avec un taux")
    thisalinea.textcontent.append("la mobilité lourde), devra faire des choix straté-")
    thisalinea.textcontent.append("d’électrification de près de 40 % et des taux")
    thisalinea.textcontent.append("giques concernant la gestion de l’affluence et du")
    thisalinea.textcontent.append("à 18 % et 3 % pour les deux autres scénarios.")
    thisalinea.textcontent.append("dimensionnement du réseau.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "■ Étape n° 3 : Considération des consommations ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 51
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "■ Étape n° 3 : Considération des consommations moyennes des véhicules, des autonomies et 2035 doit permettre de mieux cibler les efforts des trajets types pour en déduire le besoin de déploiement des IRVE au niveau des axes énergétique pour la recharge publique sur les routiers. Ces voies de circulation se caractérisent par un trafic qui peut être variable selon les jours de l’année et les différents scénarios considé- rés apportent de la sensibilité aux résultats. À "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 3 : Considération des consommations")
    thisalinea.textcontent.append("moyennes des véhicules, des autonomies et")
    thisalinea.textcontent.append("2035 doit permettre de mieux cibler les efforts")
    thisalinea.textcontent.append("des trajets types pour en déduire le besoin")
    thisalinea.textcontent.append("de déploiement des IRVE au niveau des axes")
    thisalinea.textcontent.append("énergétique pour la recharge publique sur les")
    thisalinea.textcontent.append("routiers. Ces voies de circulation se caractérisent")
    thisalinea.textcontent.append("par un trafic qui peut être variable selon les jours")
    thisalinea.textcontent.append("de l’année et les différents scénarios considé-")
    thisalinea.textcontent.append("rés apportent de la sensibilité aux résultats. À")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "■ Étape n° 4 : Traduction du besoin énergétique ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 52
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "■ Étape n° 4 : Traduction du besoin énergétique en nombre de points de charge au travers noter que la modélisation a pour vocation de d’une augmentation linéaire du taux d’utili- dresser un bilan des besoins par axe, en prenant sation de 6 % (2022) à 12,5 % (2035) et d’une en compte l’affluence, mais des analyses plus répartition des technologies de charge selon détaillées, aire par aire, permettront de mieux le cas d’usage (recharge lente des poids lourds identifier ces besoins et répondre à des problé- lors des pauses longues, recharge ultra-rapide, matiques précises telles que la gestion du "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 4 : Traduction du besoin énergétique")
    thisalinea.textcontent.append("en nombre de points de charge au travers")
    thisalinea.textcontent.append("noter que la modélisation a pour vocation de")
    thisalinea.textcontent.append("d’une augmentation linéaire du taux d’utili-")
    thisalinea.textcontent.append("dresser un bilan des besoins par axe, en prenant")
    thisalinea.textcontent.append("sation de 6 % (2022) à 12,5 % (2035) et d’une")
    thisalinea.textcontent.append("en compte l’affluence, mais des analyses plus")
    thisalinea.textcontent.append("répartition des technologies de charge selon")
    thisalinea.textcontent.append("détaillées, aire par aire, permettront de mieux")
    thisalinea.textcontent.append("le cas d’usage (recharge lente des poids lourds")
    thisalinea.textcontent.append("identifier ces besoins et répondre à des problé-")
    thisalinea.textcontent.append("lors des pauses longues, recharge ultra-rapide,")
    thisalinea.textcontent.append("matiques précises telles que la gestion du fon-")
    thisalinea.textcontent.append("voire MCS, pour les pauses courtes).")
    thisalinea.textcontent.append("cier, la périodicité, le foisonnement entre poids")
    thisalinea.textcontent.append("lourds (PL) et véhicules légers (VL)2, etc.")
    thisalinea.textcontent.append("Les résultats de la modélisation (Figure 2)")
    thisalinea.textcontent.append("présentent un besoin total de plus de 40 000")
    thisalinea.textcontent.append("Les différentes étapes de la modélisation sont :")
    thisalinea.textcontent.append("points de charge à horizon 2035 pour alimenter")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "■ Étape n° 1 : Considération des données de ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 53
    thisalinea.parentID = 47
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "■ Étape n° 1 : Considération des données de trafic des véhicules légers et des poids lourds de chacun des grands axes routiers français (routes nationales, autoroutes concédées et autoroutes non concédées) avec 3 scénarios pour représenter différentes tendances de trafic. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape  n° 1 :  Considération des données de")
    thisalinea.textcontent.append("trafic des véhicules légers et des poids lourds")
    thisalinea.textcontent.append("de chacun des grands axes routiers français")
    thisalinea.textcontent.append("(routes nationales, autoroutes concédées et")
    thisalinea.textcontent.append("autoroutes non concédées) avec 3 scénarios")
    thisalinea.textcontent.append("pour représenter différentes tendances de")
    thisalinea.textcontent.append("trafic.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Obstacles et mesures-clés"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 54
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Les entretiens et ateliers avec les parties pre- OBSTACLES À LA PLANIFICATION OPTIMALE DES IRVE – obstacles à la planification optimale des nantes de l’écosystème de la mobilité électrique IRVE ; ont permis d’identifier des obstacles à toutes les – obstacles à l’installation des IRVE ; étapes du déploiement des IRVE sur le territoire – obstacles à l’opération des IRVE ; et notamment sur les grands axes : – obstacles à l’achat des véhicules électriques liés à la recharge. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Les entretiens et ateliers avec les parties pre-")
    thisalinea.textcontent.append("OBSTACLES À LA PLANIFICATION OPTIMALE DES IRVE")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– obstacles à la planification optimale des ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 55
    thisalinea.parentID = 54
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– obstacles à la planification optimale des nantes de l’écosystème de la mobilité électrique IRVE ; ont permis d’identifier des obstacles à toutes les "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– obstacles à la planification optimale des")
    thisalinea.textcontent.append("nantes de l’écosystème de la mobilité électrique")
    thisalinea.textcontent.append("IRVE ;")
    thisalinea.textcontent.append("ont permis d’identifier des obstacles à toutes les")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– obstacles à l’installation des IRVE ; ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 56
    thisalinea.parentID = 54
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– obstacles à l’installation des IRVE ; étapes du déploiement des IRVE sur le territoire "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– obstacles à l’installation des IRVE ;")
    thisalinea.textcontent.append("étapes du déploiement des IRVE sur le territoire")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– obstacles à l’opération des IRVE ; ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 57
    thisalinea.parentID = 54
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– obstacles à l’opération des IRVE ; et notamment sur les grands axes : "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– obstacles à l’opération des IRVE ;")
    thisalinea.textcontent.append("et notamment sur les grands axes :")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– obstacles à l’achat des véhicules électriques ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 58
    thisalinea.parentID = 54
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– obstacles à l’achat des véhicules électriques liés à la recharge. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– obstacles à l’achat des véhicules électriques")
    thisalinea.textcontent.append("liés à la recharge.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1 Raccordement électrique"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 59
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2 Visibilité insuffisante pour la bonne élaboration des SDIRVE"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 60
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Figure 4 : Obstacles au déploiement des IRVE "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Figure 4 : Obstacles au déploiement des IRVE")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.3 Incertitudes sur la part des alternatives technologiques à la mobilité lourde électrique"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 61
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "OBSTACLES À L’INSTALLATION DES IRVE "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("OBSTACLES À L’INSTALLATION DES IRVE")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.1 Faible disponibilité du foncier (grands axes routiers)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 62
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.2 Faible disponibilité du foncier (zone urbaine dense)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 63
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.3 Investissements importants nécessaires (recharge DC)"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 64
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "2.4 Délais de fourniture des bornes et autres défis relatifs à la chaîne d’approvisionnement OBSTACLES À L’OPÉRATION DES IRVE "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2.4 Délais de fourniture des bornes et autres défis relatifs à la chaîne d’approvisionnement")
    thisalinea.textcontent.append("OBSTACLES À L’OPÉRATION DES IRVE")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.1 Rentabilité insuffisante"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 65
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.2 Durée légale des contrats de sous-concessions autoroutières"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 66
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.3 Défis de la maintenance et du taux de disponibilité"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 67
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.4 Volatilité des prix de l’énergie"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 68
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "OBSTACLES À L’OPÉRATION DES IRVE "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("OBSTACLES À L’OPÉRATION DES IRVE")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4.1 Complexité du parcours de recharge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 69
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4.2 Opacité de la tarification et prix de la recharge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 70
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4.3 Anxiété à la recharge"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 71
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4.4 Indisponibilité de recharge de proximité abordable"
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 72
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "Pour répondre à ces obstacles, l’étude a iden- entre les deux tomes de l’étude ; sont reprises tifié des « mesures clés », qui s’appuient elles ici uniquement les mesures relatives aux grands aussi sur les échanges avec l’écosystème lors des ateliers, ainsi que sur les résultats de la axes routiers, ainsi que les mesures transverses identifiées. modélisation. Ces mesures ont été réparties Figure 5 : Mesures-clés relatives aux grands axes routiers GRANDS AXES ROUTIERS Anticipation des besoins en raccordement OBSTACLES TRAITÉS 1.1 | 1.3 | 2.1 | 2.3 Parties prenantes État, collectivités, SCA, GRDE Levier(s) Décision politique et législative, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Pour répondre à ces obstacles, l’étude a iden-")
    thisalinea.textcontent.append("entre les deux tomes de l’étude ; sont reprises")
    thisalinea.textcontent.append("tifié des « mesures clés », qui s’appuient elles")
    thisalinea.textcontent.append("ici uniquement les mesures relatives aux grands")
    thisalinea.textcontent.append("aussi sur les échanges avec l’écosystème lors")
    thisalinea.textcontent.append("des ateliers, ainsi que sur les résultats de la")
    thisalinea.textcontent.append("axes routiers, ainsi que les mesures transverses")
    thisalinea.textcontent.append("identifiées.")
    thisalinea.textcontent.append("modélisation. Ces mesures ont été réparties")
    thisalinea.textcontent.append("Figure 5 : Mesures-clés relatives aux grands axes routiers")
    thisalinea.textcontent.append("GRANDS AXES ROUTIERS")
    thisalinea.textcontent.append("Anticipation des besoins en raccordement")
    thisalinea.textcontent.append("OBSTACLES TRAITÉS")
    thisalinea.textcontent.append("1.1 | 1.3 | 2.1 | 2.3")
    thisalinea.textcontent.append("Parties prenantes État, collectivités, SCA, GRDE")
    thisalinea.textcontent.append("Levier(s) Décision politique et législative, modification(s)")
    thisalinea.textcontent.append("réglementaire(s)")
    thisalinea.textcontent.append("Allongement des durées de contrats de sous-concession 3.2")
    thisalinea.textcontent.append("Parties prenantes État")
    thisalinea.textcontent.append("Levier(s) Modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Réduction des pointes de trafic en amont")
    thisalinea.textcontent.append("4.1 | 4.3")
    thisalinea.textcontent.append("Parties prenantes Constructeurs, e-MSP, État, SCA")
    thisalinea.textcontent.append("Levier(s) Modification(s) réglementaire(s), communication")
    thisalinea.textcontent.append("et accompagnement du changement")
    thisalinea.textcontent.append("Absorption des pointes de trafic via des solutions ad hoc 4.1 | 4.3")
    thisalinea.textcontent.append("Parties prenantes SCA, collectivités")
    thisalinea.textcontent.append("Levier(s) Expérimentation à conduire,")
    thisalinea.textcontent.append("soutien aux investissements à réaliser")
    thisalinea.textcontent.append("Innovations de type « route électrique »")
    thisalinea.textcontent.append("2.1")
    thisalinea.textcontent.append("Parties prenantes SCA, collectivités, constructeurs")
    thisalinea.textcontent.append("Levier(s) Retour d’expérience sur les précédents AAP")
    thisalinea.textcontent.append("et décision politique")
    thisalinea.textcontent.append("Figure 6 : Mesures-clés transverses")
    thisalinea.textcontent.append("TRANSVERSES")
    thisalinea.textcontent.append("OBSTACLES TRAITÉS")
    thisalinea.textcontent.append("Création d’une entité publique en charge de la planification IRVE 1.1 | 1.2 | 1.3")
    thisalinea.textcontent.append("Parties prenantes État")
    thisalinea.textcontent.append("Levier(s) Décision politique, modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Offres de raccordement intelligentes (ORI)")
    thisalinea.textcontent.append("1.1 | 2.3")
    thisalinea.textcontent.append("Parties prenantes État, collectivités, SCA, GRDE")
    thisalinea.textcontent.append("Levier(s) Communication et accompagnement du changement,")
    thisalinea.textcontent.append("modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Complétude et fiabilité des données en open data 1.2 | 4.1 | 4.3")
    thisalinea.textcontent.append("Parties prenantes État, collectivités, opérateurs")
    thisalinea.textcontent.append("Levier(s) Ressources administratives")
    thisalinea.textcontent.append("Standardisation progressive du 800 V 4.1")
    thisalinea.textcontent.append("Parties prenantes Constructeurs")
    thisalinea.textcontent.append("Levier(s) Modification(s) réglementaire(s)")
    thisalinea.textcontent.append("ou de cahier des charges")
    thisalinea.textcontent.append("Soutien à l’acquisition des poids lourds")
    thisalinea.textcontent.append("Amorçage")
    thisalinea.textcontent.append("Parties prenantes Constructeurs, utilisateurs")
    thisalinea.textcontent.append("Levier(s) Décision politique")
    thisalinea.textcontent.append("À l’issue de la modélisation et des différentes")
    thisalinea.textcontent.append("2035 par l’autorité publique est la meilleure")
    thisalinea.textcontent.append("itérations avec l’écosystème, la présente étude")
    thisalinea.textcontent.append("option pour optimiser les coûts de raccorde-")
    thisalinea.textcontent.append("dresse quatre conclusions essentielles :")
    thisalinea.textcontent.append("ment des aires de service et de repos sur grands")
    thisalinea.textcontent.append("axes.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1) Un effort conséquent de déploiement reste ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 73
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1) Un effort conséquent de déploiement reste nécessaire, avec presque 40 000 points à instal- ler, en totalité pour les VL et les PL, dans le cadre du scénario Central, pour répondre aux besoins de recharge à horizon 2035 sur les grands axes routiers. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1) Un effort conséquent de déploiement reste")
    thisalinea.textcontent.append("nécessaire, avec presque 40 000 points à instal-")
    thisalinea.textcontent.append("ler, en totalité pour les VL et les PL, dans le cadre")
    thisalinea.textcontent.append("du scénario Central, pour répondre aux besoins")
    thisalinea.textcontent.append("de recharge à horizon 2035 sur les grands axes")
    thisalinea.textcontent.append("routiers.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3) Les estimations de besoin en recharge aire ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 74
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "3) Les estimations de besoin en recharge aire par aire devront prendre en compte les enjeux spécifiques de la mobilité lourde (foncier, foi- sonnement avec les VL, périodicité, MCS). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3) Les estimations de besoin en recharge aire")
    thisalinea.textcontent.append("par aire devront prendre en compte les enjeux")
    thisalinea.textcontent.append("spécifiques de la mobilité lourde (foncier, foi-")
    thisalinea.textcontent.append("sonnement avec les VL, périodicité, MCS).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2) L’anticipation stratégique des besoins pour "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 75
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "2) L’anticipation stratégique des besoins pour "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2) L’anticipation stratégique des besoins pour")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4) Les besoins en recharge électrique lors des ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 76
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4) Les besoins en recharge électrique lors des pointes de trafic devront être traités par une réduction en amont du flux (itinéraires alterna- tifs, communication sur le trafic) et en aval par le déploiement de solutions de recharge ad hoc. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4) Les besoins en recharge électrique lors des")
    thisalinea.textcontent.append("pointes de trafic devront être traités par une")
    thisalinea.textcontent.append("réduction en amont du flux (itinéraires alterna-")
    thisalinea.textcontent.append("tifs, communication sur le trafic) et en aval par")
    thisalinea.textcontent.append("le déploiement de solutions de recharge ad hoc.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. Modélisation des besoins en IRVE pour 2030-2035"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 77
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Afin d’évaluer les besoins de recharge en France En effet, les comportements de recharge et les à horizon 2035, AFRY a distingué deux grandes typologies de déplacements (Figure 7) et pour chacune une modélisation adaptée à leurs spé- cificités et aux données disponibles : besoins en énergie associés sont différents. Un raisonnement sur le trafic est plus pertinent sur les grands axes routiers ; les données sur le parc de véhicules reflètent davantage les besoins en recharge du quotidien. Figure 7 : Évaluation du besoin en recharge selon la typologie du trajet La Figure 8 explicite la méthodologie pour la "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.1 Méthodologie et hypothèses générales"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 78
    thisalinea.parentID = 77
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Afin d’évaluer les besoins de recharge en France En effet, les comportements de recharge et les à horizon 2035, AFRY a distingué deux grandes typologies de déplacements (Figure 7) et pour chacune une modélisation adaptée à leurs spé- cificités et aux données disponibles : besoins en énergie associés sont différents. Un raisonnement sur le trafic est plus pertinent sur les grands axes routiers ; les données sur le parc de véhicules reflètent davantage les besoins en recharge du quotidien. Figure 7 : Évaluation du besoin en recharge selon la typologie du trajet La Figure 8 explicite la méthodologie pour la "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Afin d’évaluer les besoins de recharge en France")
    thisalinea.textcontent.append("En effet, les comportements de recharge et les")
    thisalinea.textcontent.append("à horizon 2035, AFRY a distingué deux grandes")
    thisalinea.textcontent.append("typologies de déplacements (Figure 7) et pour")
    thisalinea.textcontent.append("chacune une modélisation adaptée à leurs spé-")
    thisalinea.textcontent.append("cificités et aux données disponibles :")
    thisalinea.textcontent.append("besoins en énergie associés sont différents. Un")
    thisalinea.textcontent.append("raisonnement sur le trafic est plus pertinent sur")
    thisalinea.textcontent.append("les grands axes routiers ; les données sur le parc")
    thisalinea.textcontent.append("de véhicules reflètent davantage les besoins en")
    thisalinea.textcontent.append("recharge du quotidien.")
    thisalinea.textcontent.append("Figure 7 : Évaluation du besoin en recharge selon la typologie du trajet")
    thisalinea.textcontent.append("La Figure 8 explicite la méthodologie pour la")
    thisalinea.textcontent.append("modélisation des besoins hors grands axes")
    thisalinea.textcontent.append("routiers en termes d’énergie et de points de")
    thisalinea.textcontent.append("charge publics. Le besoin en recharge publique")
    thisalinea.textcontent.append("est estimé à l’échelle de chaque commune avec")
    thisalinea.textcontent.append("une méthodologie qui repose sur un groupe")
    thisalinea.textcontent.append("d’hypothèses structurantes. Différents scénarios")
    thisalinea.textcontent.append("apportent de la sensibilité aux résultats.")
    thisalinea.textcontent.append("d’électrification pour les véhicules légers et")
    thisalinea.textcontent.append("les poids lourds. Les projections de véhicules")
    thisalinea.textcontent.append("électriques de RTE10,11 et de BNEF12 ont été")
    thisalinea.textcontent.append("utilisées :")
    thisalinea.textcontent.append("Figure 8 : Méthodologie utilisée pour la modélisation")
    thisalinea.textcontent.append("des besoins de recharge hors grands axes routiers")
    thisalinea.textcontent.append("Pour la seconde modélisation, schématisée")
    thisalinea.textcontent.append("Figure 9, il s’agit d’évaluer les besoins de")
    thisalinea.textcontent.append("recharge lors de l’itinérance sur l’ensemble du")
    thisalinea.textcontent.append("réseau national routier, et plus précisément")
    thisalinea.textcontent.append("pour chaque axe routier. L’évaluation du besoin")
    thisalinea.textcontent.append("des trajets types pour en déduire le besoin")
    thisalinea.textcontent.append("énergétique pour la recharge publique sur les")
    thisalinea.textcontent.append("grands axes.")
    thisalinea.textcontent.append("Figure 9 : Méthodologie utilisée dans le cadre de la modélisation")
    thisalinea.textcontent.append("des besoins de recharge sur les grands axes routiers")
    thisalinea.textcontent.append("Les résultats et les hypothèses spécifiques à ces")
    thisalinea.textcontent.append("les parties suivantes. Le détail des données")
    thisalinea.textcontent.append("deux modèles sont davantage explicités dans")
    thisalinea.textcontent.append("utilisées est présenté en partie 5.1.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1) La grande itinérance (ou sur les grands axes ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 79
    thisalinea.parentID = 78
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1) La grande itinérance (ou sur les grands axes routiers). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1) La grande itinérance (ou sur les grands axes")
    thisalinea.textcontent.append("routiers).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2) Les déplacements du quotidien à l’échelle du ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 80
    thisalinea.parentID = 78
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2) Les déplacements du quotidien à l’échelle du département et de la commune (hors grands axes routiers). ■ Étape n° 1 : Considération du parc de véhicules par commune et application de 3 scénarios – Haut, Central et Bas pour les véhicules légers respectivement à 31 %, 27 % et 16 % pour le taux d’électrification du parc à horizon 2035 ; – Pour les poids lourds, le scénario Haut repré- sente une vision constructeur avec un taux d’électrification de près de 40 % et des taux à 18 % et 3 % pour les deux autres scénarios. moyennes des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2) Les déplacements du quotidien à l’échelle du")
    thisalinea.textcontent.append("département et de la commune (hors grands")
    thisalinea.textcontent.append("axes routiers).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 1 : Considération du parc de véhicules ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 81
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Étape n° 1 : Considération du parc de véhicules par commune et application de 3 scénarios "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 1 : Considération du parc de véhicules")
    thisalinea.textcontent.append("par commune et application de 3 scénarios")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– Haut, Central et Bas pour les véhicules légers ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 82
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– Haut, Central et Bas pour les véhicules légers respectivement à 31 %, 27 % et 16 % pour le taux d’électrification du parc à horizon 2035 ; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Haut, Central et Bas pour les véhicules légers")
    thisalinea.textcontent.append("respectivement à 31 %, 27 % et 16 % pour le")
    thisalinea.textcontent.append("taux d’électrification du parc à horizon 2035 ;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– Pour les poids lourds, le scénario Haut repré- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 83
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– Pour les poids lourds, le scénario Haut repré- sente une vision constructeur avec un taux d’électrification de près de 40 % et des taux à 18 % et 3 % pour les deux autres scénarios. moyennes des véhicules pour en déduire le besoin énergétique pour la recharge publique. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Pour les poids lourds, le scénario Haut repré-")
    thisalinea.textcontent.append("sente une vision constructeur avec un taux")
    thisalinea.textcontent.append("d’électrification de près de 40 % et des taux")
    thisalinea.textcontent.append("à 18 % et 3 % pour les deux autres scénarios.")
    thisalinea.textcontent.append("moyennes des véhicules pour en déduire le")
    thisalinea.textcontent.append("besoin énergétique pour la recharge publique.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 2 : Groupement de comportement ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 84
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "■ Étape n° 2 : Groupement de comportement en fonction des différentes catégories de véhi- cules (distance parcourue annuellement, part "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 2 : Groupement de comportement")
    thisalinea.textcontent.append("en fonction des différentes catégories de véhi-")
    thisalinea.textcontent.append("cules (distance parcourue annuellement, part")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 4 : Traduction du besoin énergétique ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 85
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "■ Étape n° 4 : Traduction du besoin énergétique en nombre de points de charge au travers de d’utilisation des routes locales, disponibilité 3 scénarios sur le taux d’utilisation et d’une de la recharge à domicile, part de la recharge répartition des technologies de charge selon publique, etc.). le cas d’usage (recharge lente à proximité du domicile, recharge rapide à destination, etc.). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 4 : Traduction du besoin énergétique")
    thisalinea.textcontent.append("en nombre de points de charge au travers de")
    thisalinea.textcontent.append("d’utilisation des routes locales, disponibilité")
    thisalinea.textcontent.append("3 scénarios sur le taux d’utilisation et d’une")
    thisalinea.textcontent.append("de la recharge à domicile, part de la recharge")
    thisalinea.textcontent.append("répartition des technologies de charge selon")
    thisalinea.textcontent.append("publique, etc.).")
    thisalinea.textcontent.append("le cas d’usage (recharge lente à proximité du")
    thisalinea.textcontent.append("domicile, recharge rapide à destination, etc.).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 3 : Considération des consommations "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 86
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "■ Étape n° 3 : Considération des consommations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 3 : Considération des consommations")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 2 : Application des 3 scénarios du ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 87
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "■ Étape n° 2 : Application des 3 scénarios du taux d’électrification. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 2 : Application des 3 scénarios du")
    thisalinea.textcontent.append("taux d’électrification.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 3 : Considération des consommations ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 88
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "■ Étape n° 3 : Considération des consommations moyennes des véhicules, des autonomies et en recharge publique repose sur un groupe d’hypothèses structurantes. Différents scénarios apportent de la sensibilité aux résultats. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■  Étape n° 3 : Considération des consommations")
    thisalinea.textcontent.append("moyennes des véhicules, des autonomies et")
    thisalinea.textcontent.append("en recharge publique repose sur un groupe")
    thisalinea.textcontent.append("d’hypothèses structurantes. Différents scénarios")
    thisalinea.textcontent.append("apportent de la sensibilité aux résultats.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 1 : Le point de départ repose sur les ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 89
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "■ Étape n° 1 : Le point de départ repose sur les données de trafic mises à disposition par "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 1 : Le point de départ repose sur les")
    thisalinea.textcontent.append("données de trafic mises à disposition par")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Étape n° 4 : Traduction du besoin énergétique ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 90
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "■ Étape n° 4 : Traduction du besoin énergétique en nombre de points de charge au travers le gouvernement. Près de 315 axes routiers d’une augmentation linéaire du taux d’utili- (autoroutes et routes nationales) sont recensés sation de 6 % (2022) à 12,5 % (2035) et d’une dans le jeu de données et donnent une vue répartition des technologies de charge selon sur 98 % du réseau national. Des données sur le cas d’usage (recharge lente des poids lourds la fréquentation des poids lourds sur ces axes lors des pauses longues, recharge ultra-rapide, sont aussi fournies au travers d’un ratio. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Étape n° 4 : Traduction du besoin énergétique")
    thisalinea.textcontent.append("en nombre de points de charge au travers")
    thisalinea.textcontent.append("le gouvernement. Près de 315 axes routiers")
    thisalinea.textcontent.append("d’une augmentation linéaire du taux d’utili-")
    thisalinea.textcontent.append("(autoroutes et routes nationales) sont recensés")
    thisalinea.textcontent.append("sation de 6 % (2022) à 12,5 % (2035) et d’une")
    thisalinea.textcontent.append("dans le jeu de données et donnent une vue")
    thisalinea.textcontent.append("répartition des technologies de charge selon")
    thisalinea.textcontent.append("sur 98 % du réseau national. Des données sur")
    thisalinea.textcontent.append("le cas d’usage (recharge lente des poids lourds")
    thisalinea.textcontent.append("la fréquentation des poids lourds sur ces axes")
    thisalinea.textcontent.append("lors des pauses longues, recharge ultra-rapide,")
    thisalinea.textcontent.append("sont aussi fournies au travers d’un ratio. Trois")
    thisalinea.textcontent.append("voire MCS, pour les pauses courtes).")
    thisalinea.textcontent.append("scénarios sont considérés pour représenter")
    thisalinea.textcontent.append("différentes tendances de trafic.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.1.1. Projection du parc de véhicules électriques"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 91
    thisalinea.parentID = 78
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Basés sur les projections de RTE et de BNEF, trois scénarios sont considérés pour les véhi- cules légers et les poids lourds. La Figure 11 représente la flotte de véhicules légers élec- l’hypothèse de RTE pour le ratio BEV/PHEV15 avec une répartition 78 % / 22 % dans le cas des projections Haut et Central et une répartition 60 % / 40 % pour le scénario Bas. triques avec la vision de BNEF pour le scénario Haut et les projections « Haut » et « Central » de RTE13 comme sources respectives pour les scénarios Central et Bas représentés ci-dessous. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Basés sur les projections de RTE et de BNEF,")
    thisalinea.textcontent.append("trois scénarios sont considérés pour les véhi-")
    thisalinea.textcontent.append("cules légers et les poids lourds. La Figure 11")
    thisalinea.textcontent.append("représente la flotte de véhicules légers élec-")
    thisalinea.textcontent.append("l’hypothèse de RTE pour le ratio BEV/PHEV15")
    thisalinea.textcontent.append("avec une répartition 78 % / 22 % dans le cas des")
    thisalinea.textcontent.append("projections Haut et Central et une répartition")
    thisalinea.textcontent.append("60 % / 40 % pour le scénario Bas.")
    thisalinea.textcontent.append("triques avec la vision de BNEF pour le scénario")
    thisalinea.textcontent.append("Haut et les projections « Haut » et « Central »")
    thisalinea.textcontent.append("de RTE13 comme sources respectives pour les")
    thisalinea.textcontent.append("scénarios Central et Bas représentés ci-dessous.")
    thisalinea.textcontent.append("Le degré de confiance dans les projections de")
    thisalinea.textcontent.append("BNEF, avec près de 17,9 millions de véhicules")
    thisalinea.textcontent.append("légers électrifiés (véhicules BEV & PHEV), a")
    thisalinea.textcontent.append("récemment été renforcé par la vision actualisée")
    thisalinea.textcontent.append("de RTE14.")
    thisalinea.textcontent.append("Afin de calculer le taux d’électrification du parc,")
    thisalinea.textcontent.append("représenté en Figure 13, AFRY a considéré une")
    thisalinea.textcontent.append("légère variation du parc de véhicules, avec un")
    thisalinea.textcontent.append("gain de 3 % sur le parc en 2029 par rapport à")
    thisalinea.textcontent.append("aujourd’hui, suivi d’une baisse avec la même")
    thisalinea.textcontent.append("tendance, mais négative (-3 %), jusqu’à 2035. Le")
    thisalinea.textcontent.append("raisonnement est de prolonger la croissance du")
    thisalinea.textcontent.append("parc total observée sur les dix dernières années,")
    thisalinea.textcontent.append("sur un rythme ralenti, et d’instaurer ensuite une")
    thisalinea.textcontent.append("Le scénario Central considère une flotte de")
    thisalinea.textcontent.append("15,6 millions de véhicules légers électrifiés en")
    thisalinea.textcontent.append("2035 et le scénario Bas une flotte de 7 millions")
    thisalinea.textcontent.append("de véhicules électrifiés. AFRY a ensuite appliqué")
    thisalinea.textcontent.append("légère décroissance en lien avec une réduction")
    thisalinea.textcontent.append("de l’usage de la voiture et un report modal")
    thisalinea.textcontent.append("progressif. La Figure 10 représente à date la")
    thisalinea.textcontent.append("répartition du parc automobile tous carburants")
    thisalinea.textcontent.append("confondus. À noter que dans le cas des taxis et")
    thisalinea.textcontent.append("les obligations de décarbonation grandissantes")
    thisalinea.textcontent.append("VTC, l’hypothèse d’un parc électrifié à hauteur")
    thisalinea.textcontent.append("du secteur et le taux de remplacement de ces")
    thisalinea.textcontent.append("de 50 % a été considérée pour être en ligne avec")
    thisalinea.textcontent.append("véhicules (supérieur à la moyenne).")
    thisalinea.textcontent.append("Figure 10 : Parc de véhicules, tous carburants confondus,")
    thisalinea.textcontent.append("en millions de véhicules")
    thisalinea.textcontent.append("VL")
    thisalinea.textcontent.append("38,3")
    thisalinea.textcontent.append("Taxi")
    thisalinea.textcontent.append("0,1")
    thisalinea.textcontent.append("VUL")
    thisalinea.textcontent.append("6,5")
    thisalinea.textcontent.append("Poids lourd")
    thisalinea.textcontent.append("0,6")
    thisalinea.textcontent.append("Figure 11 : Parc de véhicules électriques (BEV)")
    thisalinea.textcontent.append("en millions de véhicules")
    thisalinea.textcontent.append("Concernant les poids lourds, le scénario « Bas »")
    thisalinea.textcontent.append("de RTE52 a été utilisé pour le scénario Bas de la")
    thisalinea.textcontent.append("modélisation. La question de la décarbonation")
    thisalinea.textcontent.append("Cette vision « constructeurs » est utilisée pour")
    thisalinea.textcontent.append("le scénario Haut et correspond à une part de")
    thisalinea.textcontent.append("près de 40 % de poids lourds électriques en")
    thisalinea.textcontent.append("des poids lourds prend de plus en plus de place")
    thisalinea.textcontent.append("au sein des discussions à l’échelle de l’Europe")
    thisalinea.textcontent.append("2035. Mais comme le mentionne RTE dans son")
    thisalinea.textcontent.append("rapport53, des doutes subsistent :")
    thisalinea.textcontent.append("et les objectifs de réduction des émissions de")
    thisalinea.textcontent.append("CO2 ont été revus à la hausse, avec une réduc-")
    thisalinea.textcontent.append("tion de 45 % ciblée d’ici à 2030 par rapport aux")
    thisalinea.textcontent.append("Par ailleurs, les constructeurs européens de")
    thisalinea.textcontent.append("Une vision « modérée » de 110 000 camions")
    thisalinea.textcontent.append("poids lourds affichent des objectifs de ventes")
    thisalinea.textcontent.append("de poids lourds électriques de 50 % dès 2030.")
    thisalinea.textcontent.append("électriques sera donc utilisée comme référence")
    thisalinea.textcontent.append("pour le scénario Central.")
    thisalinea.textcontent.append("gène, bio-carburant, etc.).")
    thisalinea.textcontent.append("Figure 12 : Parc de poids lourds électriques (BEV)")
    thisalinea.textcontent.append("en millier de véhicules")
    thisalinea.textcontent.append("Figure 13 : Taux d’électrification des véhicules légers (à gauche)")
    thisalinea.textcontent.append("et des poids lourds (à droite)")
    thisalinea.textcontent.append("Au niveau de la modélisation, ces différents")
    thisalinea.textcontent.append("progressif des véhicules thermiques de chaque")
    thisalinea.textcontent.append("scénarios du taux d’électrification sont appli-")
    thisalinea.textcontent.append("commune, en suivant une unique tendance")
    thisalinea.textcontent.append("qués au parc de véhicules des différentes com-")
    thisalinea.textcontent.append("nationale.")
    thisalinea.textcontent.append("munes afin d’illustrer le remplacement")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– vis-à-vis de la capacité de la filière à lever les ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 92
    thisalinea.parentID = 91
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– vis-à-vis de la capacité de la filière à lever les verrous technologiques et économiques, et ; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– vis-à-vis de la capacité de la filière à lever les")
    thisalinea.textcontent.append("verrous technologiques et économiques, et ;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– par rapport à la capacité de pénétration du ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 93
    thisalinea.parentID = 91
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– par rapport à la capacité de pénétration du niveaux de 2019, puis de 65 % d’ici à 2035. tout électrique face aux alternatives (hydro- "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– par rapport à la capacité de pénétration du")
    thisalinea.textcontent.append("niveaux de 2019, puis de 65 % d’ici à 2035.")
    thisalinea.textcontent.append("tout électrique face aux alternatives (hydro-")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.1.2. Évolution technique des véhicules"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 94
    thisalinea.parentID = 78
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Dans l’évaluation de la demande énergétique des véhicules, l’efficience intervient et peut évoluer au fur et à mesure que des progrès technologiques sont réalisés par les construc- teurs automobiles. La Figure 14 représente les moyennes pondérées de consommation de dif- férents véhicules. Les valeurs actuelles reposent sur des statistiques du gouvernement16 et l’évo- lution à la baisse observée a pour objectif de refléter les progrès technologiques. Figure 14 : Consommation moyenne de différentes catégories de véhicules en kWh/km Année VUL Porteurs < 12 t Porteurs 12-19 t Porteurs > 19 t VASP lourd17 Tracteur routier 2023 0,18 0,23 0,20 0,6 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Dans l’évaluation de la demande énergétique")
    thisalinea.textcontent.append("des véhicules, l’efficience intervient et peut")
    thisalinea.textcontent.append("évoluer au fur et à mesure que des progrès")
    thisalinea.textcontent.append("technologiques sont réalisés par les construc-")
    thisalinea.textcontent.append("teurs automobiles. La Figure 14 représente les")
    thisalinea.textcontent.append("moyennes pondérées de consommation de dif-")
    thisalinea.textcontent.append("férents véhicules. Les valeurs actuelles reposent")
    thisalinea.textcontent.append("sur des statistiques du gouvernement16 et l’évo-")
    thisalinea.textcontent.append("lution à la baisse observée a pour objectif de")
    thisalinea.textcontent.append("refléter les progrès technologiques.")
    thisalinea.textcontent.append("Figure 14 : Consommation moyenne de différentes catégories")
    thisalinea.textcontent.append("de véhicules en kWh/km")
    thisalinea.textcontent.append("Année")
    thisalinea.textcontent.append("VUL")
    thisalinea.textcontent.append("Porteurs")
    thisalinea.textcontent.append("< 12 t")
    thisalinea.textcontent.append("Porteurs")
    thisalinea.textcontent.append("12-19 t")
    thisalinea.textcontent.append("Porteurs")
    thisalinea.textcontent.append("> 19 t")
    thisalinea.textcontent.append("VASP")
    thisalinea.textcontent.append("lourd17")
    thisalinea.textcontent.append("Tracteur")
    thisalinea.textcontent.append("routier")
    thisalinea.textcontent.append("2023 0,18 0,23 0,20 0,6 0,9 1,15 0,44 1,3")
    thisalinea.textcontent.append("2035 0,17 0,22 0,19 0,58 0,86 1,10 0,42 1,25")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.2. Zoom sur les besoins en recharge sur les grands axes routiers"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 95
    thisalinea.parentID = 77
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Dans les circonstances d’une itinérance, où le se recharger en public que pour le minimum conducteur parcoure plusieurs centaines de nécessaire afin d’atteindre sa destination. Au kilomètres en empruntant des grands axes rou- tiers tels que l’autoroute ou une route nationale, travers des données actuelles sur l’autonomie des véhicules électriques et une estimation de le comportement de recharge est étroitement leur évolution, il est alors possible d’en déduire lié à l’autonomie du véhicule. Les données issues de l’enquête de mobilité de 201918 indiquent que dans le cas des trajets de plus de 80 km, la distance moyenne parcourue le besoin "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.1. Analyse du comportement de recharge lors de l’itinérance"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 96
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Dans les circonstances d’une itinérance, où le se recharger en public que pour le minimum conducteur parcoure plusieurs centaines de nécessaire afin d’atteindre sa destination. Au kilomètres en empruntant des grands axes rou- tiers tels que l’autoroute ou une route nationale, travers des données actuelles sur l’autonomie des véhicules électriques et une estimation de le comportement de recharge est étroitement leur évolution, il est alors possible d’en déduire lié à l’autonomie du véhicule. Les données issues de l’enquête de mobilité de 201918 indiquent que dans le cas des trajets de plus de 80 km, la distance moyenne parcourue le besoin "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.2.1.1. Cas des véhicules légers"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 97
    thisalinea.parentID = 96
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Dans les circonstances d’une itinérance, où le se recharger en public que pour le minimum conducteur parcoure plusieurs centaines de nécessaire afin d’atteindre sa destination. Au kilomètres en empruntant des grands axes rou- tiers tels que l’autoroute ou une route nationale, travers des données actuelles sur l’autonomie des véhicules électriques et une estimation de le comportement de recharge est étroitement leur évolution, il est alors possible d’en déduire lié à l’autonomie du véhicule. Les données issues de l’enquête de mobilité de 201918 indiquent que dans le cas des trajets de plus de 80 km, la distance moyenne parcourue le besoin "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Dans les circonstances d’une itinérance, où le")
    thisalinea.textcontent.append("se recharger en public que pour le minimum")
    thisalinea.textcontent.append("conducteur parcoure plusieurs centaines de")
    thisalinea.textcontent.append("nécessaire afin d’atteindre sa destination. Au")
    thisalinea.textcontent.append("kilomètres en empruntant des grands axes rou-")
    thisalinea.textcontent.append("tiers tels que l’autoroute ou une route nationale,")
    thisalinea.textcontent.append("travers des données actuelles sur l’autonomie")
    thisalinea.textcontent.append("des véhicules électriques et une estimation de")
    thisalinea.textcontent.append("le comportement de recharge est étroitement")
    thisalinea.textcontent.append("leur évolution, il est alors possible d’en déduire")
    thisalinea.textcontent.append("lié à l’autonomie du véhicule.")
    thisalinea.textcontent.append("Les données issues de l’enquête de mobilité de")
    thisalinea.textcontent.append("201918 indiquent que dans le cas des trajets de")
    thisalinea.textcontent.append("plus de 80 km, la distance moyenne parcourue")
    thisalinea.textcontent.append("le besoin en recharge moyen d’un véhicule sur")
    thisalinea.textcontent.append("les grands axes routiers. La Figure 15 représente")
    thisalinea.textcontent.append("l’évolution en besoin de recharge publique")
    thisalinea.textcontent.append("lors d’une itinérance au cours du temps. Pour")
    thisalinea.textcontent.append("considérer l’anticipation par le conducteur du")
    thisalinea.textcontent.append("est environ de 580 km. En considérant que le")
    thisalinea.textcontent.append("besoin en recharge avant que la batterie ne soit")
    thisalinea.textcontent.append("conducteur part initialement avec un véhicule")
    thisalinea.textcontent.append("totalement vide, AFRY a considéré une réduc-")
    thisalinea.textcontent.append("chargé à 100 % et qu’il dispose d’une possibilité")
    thisalinea.textcontent.append("tion de l’autonomie réelle des véhicules de 20 %.")
    thisalinea.textcontent.append("de recharge à destination, l’automobiliste ne va")
    thisalinea.textcontent.append("Figure 15 : Évolution des besoins en recharge publique")
    thisalinea.textcontent.append("au cours du temps, en %")
    thisalinea.textcontent.append("Année")
    thisalinea.textcontent.append("2023")
    thisalinea.textcontent.append("2030 2035")
    thisalinea.textcontent.append("Évolution de l’autonomie réelle19 264 km 284 km 296 km")
    thisalinea.textcontent.append("Besoin en recharge pour un trajet")
    thisalinea.textcontent.append("moyen20")
    thisalinea.textcontent.append("54 % 51 % 49 %")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2.2.1.2. Cas des tracteurs routiers"
    thisalinea.titlefontsize = "11.0"
    thisalinea.nativeID = 98
    thisalinea.parentID = 96
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "La part de poids lourds dans le trafic moyen considérant que le poids lourd est limité dans journalier figurant dans les données du gou- ses manœuvres dans une aire de service ou de vernement concerne des véhicules d’un poids total supérieur ou égal à 3,5 tonnes21. Du point de vue des caractéristiques techniques et des repos et que le véhicule va monopoliser une place avec un point de recharge électrique sur la durée de la pause, la valeur de 46 % peut comportements de recharge, AFRY n’a consi- être associée au besoin de recharge afin de déré que la catégorie "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("La part de poids lourds dans le trafic moyen")
    thisalinea.textcontent.append("considérant que le poids lourd est limité dans")
    thisalinea.textcontent.append("journalier figurant dans les données du gou-")
    thisalinea.textcontent.append("ses manœuvres dans une aire de service ou de")
    thisalinea.textcontent.append("vernement concerne des véhicules d’un poids")
    thisalinea.textcontent.append("total supérieur ou égal à 3,5 tonnes21. Du point")
    thisalinea.textcontent.append("de vue des caractéristiques techniques et des")
    thisalinea.textcontent.append("repos et que le véhicule va monopoliser une")
    thisalinea.textcontent.append("place avec un point de recharge électrique sur")
    thisalinea.textcontent.append("la durée de la pause, la valeur de 46 % peut")
    thisalinea.textcontent.append("comportements de recharge, AFRY n’a consi-")
    thisalinea.textcontent.append("être associée au besoin de recharge afin de")
    thisalinea.textcontent.append("déré que la catégorie des tracteurs routiers")
    thisalinea.textcontent.append("dimensionner le nombre de points de charge.")
    thisalinea.textcontent.append("pour les poids lourds réalisant de l’itinérance.")
    thisalinea.textcontent.append("Il s’agit donc d’une vue à tendance maxima-")
    thisalinea.textcontent.append("Ces véhicules remorquent des charges lourdes")
    thisalinea.textcontent.append("liste, et ce d’autant plus que le Comité national")
    thisalinea.textcontent.append("sur les routes tout au long de l’année et sont")
    thisalinea.textcontent.append("routier mentionne que l’approvisionnement en")
    thisalinea.textcontent.append("caractérisés par un trafic relativement constant.")
    thisalinea.textcontent.append("En lien avec la stratégie des transporteurs et")
    thisalinea.textcontent.append("logisticiens, la planification et l’optimisation du")
    thisalinea.textcontent.append("carburant via les cuves privées, c’est-à-dire en")
    thisalinea.textcontent.append("entrepôt, est de 65 %22 environ en 2022. Cela")
    thisalinea.textcontent.append("signifie que le plein de carburant réalisé dans")
    thisalinea.textcontent.append("trajet pour ces véhicules est primordiale afin de")
    thisalinea.textcontent.append("les stations essences ne correspond qu’à 35 %")
    thisalinea.textcontent.append("minimiser les coûts. La clé pour assurer l’essor")
    thisalinea.textcontent.append("du besoin d’un tracteur routier français sur une")
    thisalinea.textcontent.append("des tracteurs routiers électriques résidera donc")
    thisalinea.textcontent.append("année.")
    thisalinea.textcontent.append("dans la possibilité de recharger ces véhicules sur")
    thisalinea.textcontent.append("les temps de pauses réglementaires.")
    thisalinea.textcontent.append("Progressivement, l’obtention d’une meilleure")
    thisalinea.textcontent.append("vision sur la gestion du foncier sur les aires de")
    thisalinea.textcontent.append("La réglementation actuelle fixe au minimum")
    thisalinea.textcontent.append("service et de repos, sur les évolutions technolo-")
    thisalinea.textcontent.append("une pause de 45 minutes après 4 h 30 de")
    thisalinea.textcontent.append("giques des batteries des poids lourds et sur les")
    thisalinea.textcontent.append("conduite et une pause nocturne de 11 heures,")
    thisalinea.textcontent.append("stratégies d’investissement des transporteurs")
    thisalinea.textcontent.append("sauf 3 fois dans la semaine où elle peut être de")
    thisalinea.textcontent.append("vis-à-vis de la recharge rapide en entrepôt")
    thisalinea.textcontent.append("9 heures. Dans ces circonstances, le temps de")
    thisalinea.textcontent.append("affineront l’évaluation du besoin en recharge")
    thisalinea.textcontent.append("pause moyen sur une journée pour un conduc-")
    thisalinea.textcontent.append("publique des poids lourds.")
    thisalinea.textcontent.append("teur de poids lourd peut être évalué à 46 %. En")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.2. Estimation des besoins énergétiques pour la recharge publique"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 99
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Pour les grands axes routiers, l’estimation du Les trois scénarios Haut, Central et Bas ici adoptés reprennent les trois projections du taux d’électrification. Des variations du TMJA pour chaque axe routier sont ensuite appliquées afin Cette décroissance de 0,45 % est observée de considérer différents besoins de recharge en considérant la variation entre les valeurs selon l’affluence : de 2009 et 2019 sur la circulation annuelle moyenne des véhicules. besoin en recharge. Mais la méthodologie uti- lisée ici donne une visualisation satisfaisante du besoin en recharge sur les grands axes. Les axes routiers au travers de cette modélisation sont présentés "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Pour les grands axes routiers, l’estimation du")
    thisalinea.textcontent.append("Les trois scénarios Haut, Central et Bas ici")
    thisalinea.textcontent.append("adoptés reprennent les trois projections du taux")
    thisalinea.textcontent.append("d’électrification. Des variations du TMJA pour")
    thisalinea.textcontent.append("chaque axe routier sont ensuite appliquées afin")
    thisalinea.textcontent.append("Cette décroissance de 0,45 % est observée")
    thisalinea.textcontent.append("de considérer différents besoins de recharge")
    thisalinea.textcontent.append("en considérant la variation entre les valeurs")
    thisalinea.textcontent.append("selon l’affluence :")
    thisalinea.textcontent.append("de 2009 et 2019 sur la circulation annuelle")
    thisalinea.textcontent.append("moyenne des véhicules.")
    thisalinea.textcontent.append("besoin en recharge. Mais la méthodologie uti-")
    thisalinea.textcontent.append("lisée ici donne une visualisation satisfaisante")
    thisalinea.textcontent.append("du besoin en recharge sur les grands axes. Les")
    thisalinea.textcontent.append("axes routiers au travers de cette modélisation")
    thisalinea.textcontent.append("sont présentés en Figure 16. Des études plus")
    thisalinea.textcontent.append("avancées, en amont d’une nouvelle vague de")
    thisalinea.textcontent.append("déploiement d’IRVE, permettront d’affiner le")
    thisalinea.textcontent.append("baisse de 0,45 % annuelle de la circulation.")
    thisalinea.textcontent.append("résultat et de mieux cibler le besoin aire par aire.")
    thisalinea.textcontent.append("Figure 16 : Besoin énergétique pour la recharge publique")
    thisalinea.textcontent.append("sur les grands axes routiers")
    thisalinea.textcontent.append("Total")
    thisalinea.textcontent.append("Véhicules légers")
    thisalinea.textcontent.append("Poids lourds")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ La consommation des véhicules. ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 100
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ La consommation des véhicules. besoin énergétique se base sur : "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ La consommation des véhicules.")
    thisalinea.textcontent.append("besoin énergétique se base sur :")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le trafic moyen journalier annuel (TMJA) de ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 101
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Le trafic moyen journalier annuel (TMJA) de l’axe routier, avec la proportion associée de poids lourds. Les données statistiques du gouvernement23 font état de 315 axes routiers recensés, dont 82 axes routiers sans données sur le TMJA24 et plus de 100 axes sans données sur la proportion de poids lourds25. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le trafic moyen journalier annuel (TMJA) de")
    thisalinea.textcontent.append("l’axe routier, avec la proportion associée de")
    thisalinea.textcontent.append("poids lourds. Les données statistiques du")
    thisalinea.textcontent.append("gouvernement23 font état de 315 axes routiers")
    thisalinea.textcontent.append("recensés, dont 82 axes routiers sans données")
    thisalinea.textcontent.append("sur le TMJA24 et plus de 100 axes sans données")
    thisalinea.textcontent.append("sur la proportion de poids lourds25.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le taux d’électrification. "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 102
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Le taux d’électrification. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le taux d’électrification.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le comportement de recharge. "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 103
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "■ Le comportement de recharge. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le comportement de recharge.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Scénario Haut : Une augmentation de 7 % a ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 104
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "■ Scénario Haut : Une augmentation de 7 % a été appliquée au trafic moyen journalier de La considération des caractéristiques de cha- chaque axe routier. Cette valeur permet de cune des routes (nombre de voies, débit horaire, représenter une affluence plus importante, etc.) ainsi que l’affluence à l’échelle des aires notamment lors des trajets estivaux, et sem- permettraient une évaluation plus précise du blerait être un ratio convenable pour retrans- crire un dimensionnement à la 30e heure. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Scénario Haut : Une augmentation de 7 % a")
    thisalinea.textcontent.append("été appliquée au trafic moyen journalier de")
    thisalinea.textcontent.append("La considération des caractéristiques de cha-")
    thisalinea.textcontent.append("chaque axe routier. Cette valeur permet de")
    thisalinea.textcontent.append("cune des routes (nombre de voies, débit horaire,")
    thisalinea.textcontent.append("représenter une affluence plus importante,")
    thisalinea.textcontent.append("etc.) ainsi que l’affluence à l’échelle des aires")
    thisalinea.textcontent.append("notamment lors des trajets estivaux, et sem-")
    thisalinea.textcontent.append("permettraient une évaluation plus précise du")
    thisalinea.textcontent.append("blerait être un ratio convenable pour retrans-")
    thisalinea.textcontent.append("crire un dimensionnement à la 30e heure.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Scénario Central : valeurs moyennes pondé- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 105
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "■ Scénario Central : valeurs moyennes pondé- résultats du besoin en énergie sur les grands rées du TMJA de chaque axe routier. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Scénario Central : valeurs moyennes pondé-")
    thisalinea.textcontent.append("résultats du besoin en énergie sur les grands")
    thisalinea.textcontent.append("rées du TMJA de chaque axe routier.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Scénario Bas : Prise en compte d’un potentiel ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 106
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "■ Scénario Bas : Prise en compte d’un potentiel effet de report modal progressif, avec une "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Scénario Bas : Prise en compte d’un potentiel")
    thisalinea.textcontent.append("effet de report modal progressif, avec une")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.3. Évaluation du nombre de points de charge"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 107
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "À la manière du modèle pour les trajets locaux, prendre en considération la diversité du parc la dernière étape est la conversion du besoin automobile et les différentes puissances de énergétique en nombre de points de charge. La Figure 17 présente la puissance moyenne acceptée sur les grands axes routiers, avec pour référence l’analyse de l’ICCT26 et des estimations du besoin en termes de vitesse de recharge sur charge acceptées selon les catégories de véhi- cules. Ainsi, la puissance moyenne acceptée en 2035 est de l’ordre de 141 kW. Pour les poids lourds, le besoin énergétique est satisfait à 50 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("À la manière du modèle pour les trajets locaux,")
    thisalinea.textcontent.append("prendre en considération la diversité du parc")
    thisalinea.textcontent.append("la dernière étape est la conversion du besoin")
    thisalinea.textcontent.append("automobile et les différentes puissances de")
    thisalinea.textcontent.append("énergétique en nombre de points de charge.")
    thisalinea.textcontent.append("La Figure 17 présente la puissance moyenne")
    thisalinea.textcontent.append("acceptée sur les grands axes routiers, avec pour")
    thisalinea.textcontent.append("référence l’analyse de l’ICCT26 et des estimations")
    thisalinea.textcontent.append("du besoin en termes de vitesse de recharge sur")
    thisalinea.textcontent.append("charge acceptées selon les catégories de véhi-")
    thisalinea.textcontent.append("cules. Ainsi, la puissance moyenne acceptée")
    thisalinea.textcontent.append("en 2035 est de l’ordre de 141 kW. Pour les poids")
    thisalinea.textcontent.append("lourds, le besoin énergétique est satisfait à 50 %")
    thisalinea.textcontent.append("par la catégorie de chargeur DC, répondant au")
    thisalinea.textcontent.append("les pauses réglementaires pour les poids lourds.")
    thisalinea.textcontent.append("besoin de recharge lors de la pause longue,")
    thisalinea.textcontent.append("Pour les véhicules légers, le besoin énergétique")
    thisalinea.textcontent.append("futur, MCS) et répondant au besoin des pauses")
    thisalinea.textcontent.append("et 50 % par la recharge ultra-rapide (dans le")
    thisalinea.textcontent.append("est satisfait à 50 % par les chargeurs rapides")
    thisalinea.textcontent.append("courtes.")
    thisalinea.textcontent.append("et 85 % par les chargeurs ultra-rapides afin de")
    thisalinea.textcontent.append("Figure 17 : Puissance moyenne acceptée pour différents chargeurs")
    thisalinea.textcontent.append("par les véhicules à différentes dates sur les grands axes routiers")
    thisalinea.textcontent.append("Année")
    thisalinea.textcontent.append("2023")
    thisalinea.textcontent.append("2030")
    thisalinea.textcontent.append("2035")
    thisalinea.textcontent.append("VL – Chargeur")
    thisalinea.textcontent.append("VL – Chargeur")
    thisalinea.textcontent.append("PL – Chargeur")
    thisalinea.textcontent.append("DC rapide")
    thisalinea.textcontent.append("DC ultra-rapide")
    thisalinea.textcontent.append("35")
    thisalinea.textcontent.append("69")
    thisalinea.textcontent.append("90")
    thisalinea.textcontent.append("60")
    thisalinea.textcontent.append("115")
    thisalinea.textcontent.append("150")
    thisalinea.textcontent.append("DC")
    thisalinea.textcontent.append("50")
    thisalinea.textcontent.append("69")
    thisalinea.textcontent.append("80")
    thisalinea.textcontent.append("PL – Chargeur")
    thisalinea.textcontent.append("ultra-rapide")
    thisalinea.textcontent.append("(MCS)")
    thisalinea.textcontent.append("90")
    thisalinea.textcontent.append("317")
    thisalinea.textcontent.append("670")
    thisalinea.textcontent.append("Concernant le taux d’utilisation des points de")
    thisalinea.textcontent.append("charge sur les grands axes routiers, AFRY a")
    thisalinea.textcontent.append("considéré une évolution linéaire de 1,5 heure")
    thisalinea.textcontent.append("routes nationales et la Figure 19 donne une indi-")
    thisalinea.textcontent.append("cation sur le besoin pour quelques axes routiers.")
    thisalinea.textcontent.append("(6 %) en 2022 à 3 heures (12,5 %) d’ici à 2035.")
    thisalinea.textcontent.append("Les chargeurs des grands axes routiers vont")
    thisalinea.textcontent.append("Il est à noter que même avec le scénario Bas,")
    thisalinea.textcontent.append("le nombre de points présents actuellement ne")
    thisalinea.textcontent.append("plus facilement atteindre de telles valeurs de")
    thisalinea.textcontent.append("suffirait pas pour répondre au besoin de 2035.")
    thisalinea.textcontent.append("taux d’utilisation, comme l’indiquent certains")
    thisalinea.textcontent.append("rapports27.")
    thisalinea.textcontent.append("De nouvelles vagues de déploiement sur les")
    thisalinea.textcontent.append("grands axes routiers seront donc nécessaires,")
    thisalinea.textcontent.append("AFRY évalue le besoin à un peu plus de 43 000")
    thisalinea.textcontent.append("points de charge en 2035 pour le scénario")
    thisalinea.textcontent.append("Central. La Figure 18  présente en détail les")
    thisalinea.textcontent.append("résultats pour l’ensemble des autoroutes et des")
    thisalinea.textcontent.append("et ce, d’autant plus sur les réseaux non concé-")
    thisalinea.textcontent.append("dés et un certain nombre de routes nationales")
    thisalinea.textcontent.append("déficitaires en points de charge actuellement.")
    thisalinea.textcontent.append("L’annexe 5.1 donne une vue plus détaillée pour")
    thisalinea.textcontent.append("plusieurs autres grands axes routiers.")
    thisalinea.textcontent.append("Figure 18 : Résultats de la modélisation pour les besoins")
    thisalinea.textcontent.append("en nombre de points de charge sur les grands axes routiers28")
    thisalinea.textcontent.append("Total")
    thisalinea.textcontent.append("Véhicules légers")
    thisalinea.textcontent.append("Poids lourds")
    thisalinea.textcontent.append("Figure 19 : Évolution du besoin en nombre de points sur quelques axes routiers")
    thisalinea.textcontent.append("pour les véhicules légers et pour les poids lourds")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.3. Synthèse des besoins en recharge publique sur le territoire français"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 108
    thisalinea.parentID = 77
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "AFRY présente ici les résultats combinés des La Figure 20 présente la demande énergétique totale de recharge publique pour différents cas d’usage : Figure 20 : Évolution du besoin énergétique (TWh/an) de la recharge publique par typologie de recharge pour le scénario Central En finalité, AFRY évalue le besoin en points de d’utilisation de 12,5 % pour obtenir un meilleur charge à horizon 2035 entre 300 000 et 400 000 points. Cela permet de considérer différentes possibilités d’évolutions du taux d’électrification du parc automobile tout en visant un taux équilibre entre le confort des usagers et la ren- tabilité des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("AFRY présente ici les résultats combinés des")
    thisalinea.textcontent.append("La Figure 20 présente la demande énergétique")
    thisalinea.textcontent.append("totale de recharge publique pour différents cas")
    thisalinea.textcontent.append("d’usage :")
    thisalinea.textcontent.append("Figure 20 : Évolution du besoin énergétique (TWh/an) de la recharge publique")
    thisalinea.textcontent.append("par typologie de recharge pour le scénario Central")
    thisalinea.textcontent.append("En finalité, AFRY évalue le besoin en points de")
    thisalinea.textcontent.append("d’utilisation de 12,5 % pour obtenir un meilleur")
    thisalinea.textcontent.append("charge à horizon 2035 entre 300 000 et 400 000")
    thisalinea.textcontent.append("points. Cela permet de considérer différentes")
    thisalinea.textcontent.append("possibilités d’évolutions du taux d’électrification")
    thisalinea.textcontent.append("du parc automobile tout en visant un taux")
    thisalinea.textcontent.append("équilibre entre le confort des usagers et la ren-")
    thisalinea.textcontent.append("tabilité des bornes. La Figure 22 donne la répar-")
    thisalinea.textcontent.append("tition en termes de typologie de points des")
    thisalinea.textcontent.append("résultats présentés en Figure 21.")
    thisalinea.textcontent.append("Figure 21 : Résultat de la modélisation")
    thisalinea.textcontent.append("pour les besoins en nombre de points de charge29")
    thisalinea.textcontent.append("Taux d’utilisation [4 % - 8 %]")
    thisalinea.textcontent.append("Taux d’utilisation")
    thisalinea.textcontent.append("[6 % - 12,5 %]")
    thisalinea.textcontent.append("Taux d’utilisation")
    thisalinea.textcontent.append("[8 % - 17 %]")
    thisalinea.textcontent.append("Les différentes catégories mentionnées dans")
    thisalinea.textcontent.append("la Figure 22 sont les suivantes :")
    thisalinea.textcontent.append("80-90 kW pour les poids lourds30 (correspon-")
    thisalinea.textcontent.append("dant à des chargeurs DC de 50 à 150 kW) en")
    thisalinea.textcontent.append("2035.")
    thisalinea.textcontent.append("Figure 22 : Répartition des typologies de points")
    thisalinea.textcontent.append("avec un taux d’utilisation de 12,5 % en 203531")
    thisalinea.textcontent.append("284 140")
    thisalinea.textcontent.append("(74 %)")
    thisalinea.textcontent.append("231 900")
    thisalinea.textcontent.append("(76 %)")
    thisalinea.textcontent.append("154 210")
    thisalinea.textcontent.append("(81 %)")
    thisalinea.textcontent.append("69 690")
    thisalinea.textcontent.append("(18 %)")
    thisalinea.textcontent.append("31 970")
    thisalinea.textcontent.append("(8 %)")
    thisalinea.textcontent.append("47 210")
    thisalinea.textcontent.append("(16 %)")
    thisalinea.textcontent.append("24 790")
    thisalinea.textcontent.append("(8 %)")
    thisalinea.textcontent.append("23 340")
    thisalinea.textcontent.append("(12 %)")
    thisalinea.textcontent.append("13 050")
    thisalinea.textcontent.append("(7 %)")
    thisalinea.textcontent.append("Le nombre et la répartition en typologie de")
    thisalinea.textcontent.append("points modélisés pour 2035 dans le cas du")
    thisalinea.textcontent.append("électrique léger à batterie. Le pays serait donc")
    thisalinea.textcontent.append("aligné avec les recommandations de l’AFIR, tout")
    thisalinea.textcontent.append("scénario Central avec un taux d’utilisation à")
    thisalinea.textcontent.append("en s’insérant dans une démarche de sobriété")
    thisalinea.textcontent.append("12,5 % permettraient à la France d’avoir une")
    thisalinea.textcontent.append("capacité  installée  de  1,4 kW  par  véhicule")
    thisalinea.textcontent.append("et de recherche de rentabilité acceptable des")
    thisalinea.textcontent.append("points de charge présents sur le territoire.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "■ Le besoin en recharge lente sur voirie se réfère ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 109
    thisalinea.parentID = 108
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Le besoin en recharge lente sur voirie se réfère deux modélisations pour illustrer le besoin par exemple au besoin des automobilistes ne global en énergie pour la recharge publique et possédant pas de possibilité de recharge à en points de charge sur l’ensemble du territoire. domicile ou à de la recharge publique pour Ces résultats sont étroitement liés aux hypo- les petits trajets du quotidien. thèses explicitées dans les parties précédentes, mais la présence de plusieurs scénarios pour le "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le besoin en recharge lente sur voirie se réfère")
    thisalinea.textcontent.append("deux modélisations pour illustrer le besoin")
    thisalinea.textcontent.append("par exemple au besoin des automobilistes ne")
    thisalinea.textcontent.append("global en énergie pour la recharge publique et")
    thisalinea.textcontent.append("possédant pas de possibilité de recharge à")
    thisalinea.textcontent.append("en points de charge sur l’ensemble du territoire.")
    thisalinea.textcontent.append("domicile ou à de la recharge publique pour")
    thisalinea.textcontent.append("Ces résultats sont étroitement liés aux hypo-")
    thisalinea.textcontent.append("les petits trajets du quotidien.")
    thisalinea.textcontent.append("thèses explicitées dans les parties précédentes,")
    thisalinea.textcontent.append("mais la présence de plusieurs scénarios pour le")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "■ Sur les grands axes, la catégorie de recharge ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 110
    thisalinea.parentID = 108
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Sur les grands axes, la catégorie de recharge taux d’électrification, pour l’évolution du trafic rapide inclut la recharge prolongée des poids sur les autoroutes et vis-à-vis du taux d’utilisa- lourds lors de leurs pauses réglementaires et tion permet d’avoir une vue consolidée sur les la recharge depuis des points de 150 kW pour besoins à horizon 2035. les véhicules légers. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Sur les grands axes, la catégorie de recharge")
    thisalinea.textcontent.append("taux d’électrification, pour l’évolution du trafic")
    thisalinea.textcontent.append("rapide inclut la recharge prolongée des poids")
    thisalinea.textcontent.append("sur les autoroutes et vis-à-vis du taux d’utilisa-")
    thisalinea.textcontent.append("lourds lors de leurs pauses réglementaires et")
    thisalinea.textcontent.append("tion permet d’avoir une vue consolidée sur les")
    thisalinea.textcontent.append("la recharge depuis des points de 150 kW pour")
    thisalinea.textcontent.append("besoins à horizon 2035.")
    thisalinea.textcontent.append("les véhicules légers.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "■ La recharge ultra-rapide correspond aux ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 111
    thisalinea.parentID = 108
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ La recharge ultra-rapide correspond aux technologies MCS pour les poids lourds et aux bornes de puissance 350 kW pour les véhicules légers. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ La recharge ultra-rapide correspond aux")
    thisalinea.textcontent.append("technologies MCS pour les poids lourds et")
    thisalinea.textcontent.append("aux bornes de puissance 350 kW pour les")
    thisalinea.textcontent.append("véhicules légers.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "■ « Type lent » : puissance moyenne acceptée ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 112
    thisalinea.parentID = 108
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "■ « Type lent » : puissance moyenne acceptée de 5,4 kW et de 9,5 kW (correspondant à des chargeurs AC, de 7 kW à 22 kW) en 2035. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ « Type lent » : puissance moyenne acceptée")
    thisalinea.textcontent.append("de 5,4 kW et de 9,5 kW (correspondant à des")
    thisalinea.textcontent.append("chargeurs AC, de 7 kW à 22 kW) en 2035.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "■ « Type rapide » : puissance moyenne accep- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 113
    thisalinea.parentID = 108
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "■ « Type rapide » : puissance moyenne accep- tée de 90 kW pour les véhicules légers et de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ « Type rapide » : puissance moyenne accep-")
    thisalinea.textcontent.append("tée de 90 kW pour les véhicules légers et de")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "■ « Type ultra-rapide » : puissance moyenne ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 114
    thisalinea.parentID = 108
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "■ « Type ultra-rapide » : puissance moyenne acceptée de 150 kW pour les véhicules légers et de 670 kW pour les poids lourds (corres- pondant à des chargeurs CCS 350 kW et MCS) en 2035. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ « Type ultra-rapide » : puissance moyenne")
    thisalinea.textcontent.append("acceptée de 150 kW pour les véhicules légers")
    thisalinea.textcontent.append("et de 670 kW pour les poids lourds (corres-")
    thisalinea.textcontent.append("pondant à des chargeurs CCS 350 kW et MCS)")
    thisalinea.textcontent.append("en 2035.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. Obstacles au déploiement d’une infrastructure de recharge publique"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 115
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Les acteurs de la mobilité ont mentionné par l’écosystème. recharge publique, les incertitudes technolo- ■ En opération, en plus des considérations de des obstacles qui freinent ou empêchent un maintenance et les risques inhérents à la vola- déploiement optimal de l’infrastructure de tilité des marchés de l’énergie, la rentabilité recharge publique en France. des IRVE est souvent qualifiée d’insuffisante ■ Lors de la planification de l’infrastructure de ■ De façon générale, le déploiement de l’in- giques (place de l’hydrogène pour les poids frastructure et l’électrification du parc sont lourds), le manque de visibilité et le court-ter- intrinsèquement liés ; il "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Les acteurs de la mobilité ont mentionné")
    thisalinea.textcontent.append("par l’écosystème.")
    thisalinea.textcontent.append("recharge publique, les incertitudes technolo-")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "■ En opération, en plus des considérations de ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 116
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ En opération, en plus des considérations de des obstacles qui freinent ou empêchent un maintenance et les risques inhérents à la vola- déploiement optimal de l’infrastructure de tilité des marchés de l’énergie, la rentabilité recharge publique en France. des IRVE est souvent qualifiée d’insuffisante "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ En opération, en plus des considérations de")
    thisalinea.textcontent.append("des obstacles qui freinent ou empêchent un")
    thisalinea.textcontent.append("maintenance et les risques inhérents à la vola-")
    thisalinea.textcontent.append("déploiement optimal de l’infrastructure de")
    thisalinea.textcontent.append("tilité des marchés de l’énergie, la rentabilité")
    thisalinea.textcontent.append("recharge publique en France.")
    thisalinea.textcontent.append("des IRVE est souvent qualifiée d’insuffisante")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "■ Lors de la planification de l’infrastructure de "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 117
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Lors de la planification de l’infrastructure de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Lors de la planification de l’infrastructure de")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "■ De façon générale, le déploiement de l’in- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 118
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ De façon générale, le déploiement de l’in- giques (place de l’hydrogène pour les poids frastructure et l’électrification du parc sont lourds), le manque de visibilité et le court-ter- intrinsèquement liés ; il est nécessaire que les misme sur les raccordements conduisent à IRVE ne soient pas un frein à l’achat des véhi- un déploiement suboptimal. cules électriques, et donc que « l’expérience client » des bornes soit satisfaisante. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ De façon générale, le déploiement de l’in-")
    thisalinea.textcontent.append("giques (place de l’hydrogène pour les poids")
    thisalinea.textcontent.append("frastructure et l’électrification du parc sont")
    thisalinea.textcontent.append("lourds), le manque de visibilité et le court-ter-")
    thisalinea.textcontent.append("intrinsèquement liés ; il est nécessaire que les")
    thisalinea.textcontent.append("misme sur les raccordements conduisent à")
    thisalinea.textcontent.append("IRVE ne soient pas un frein à l’achat des véhi-")
    thisalinea.textcontent.append("un déploiement suboptimal.")
    thisalinea.textcontent.append("cules électriques, et donc que « l’expérience")
    thisalinea.textcontent.append("client » des bornes soit satisfaisante.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "■ Installer les IRVE nécessite de sécuriser le ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 119
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "■ Installer les IRVE nécessite de sécuriser le foncier approprié (particulièrement pour la recharge pour poids lourds), des investisse- ments importants, et une chaîne logistique parfois grippée par la demande croissante. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Installer les IRVE nécessite de sécuriser le")
    thisalinea.textcontent.append("foncier approprié (particulièrement pour la")
    thisalinea.textcontent.append("recharge pour poids lourds), des investisse-")
    thisalinea.textcontent.append("ments importants, et une chaîne logistique")
    thisalinea.textcontent.append("parfois grippée par la demande croissante.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.1. Obstacles à la planification optimale des IRVE"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 120
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Le raccordement au réseau de distribution est La procédure « Enedis-PRO-RAC_14E » de 2021 un jalon essentiel du déploiement des IRVE ; détaille le traitement des demandes de raccor- mais la multiplication des demandes de rac- dement des installations de consommation cordements de bornes, concomitantes avec individuelle ou collective en BT > 36 kVA et en l’accélération des énergies renouvelables, met HTA, cadre qui inclue les IRVE. Les demandes une forte pression sur les GRDE (Gestionnaires de raccordement sont ainsi traitées chronologi- de réseau de distribution d’énergie). quement à partir de leur date de dépôt, ou de Le raccordement électrique "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.1.1. Raccordement électrique des IRVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 121
    thisalinea.parentID = 120
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Le raccordement au réseau de distribution est La procédure « Enedis-PRO-RAC_14E » de 2021 un jalon essentiel du déploiement des IRVE ; détaille le traitement des demandes de raccor- mais la multiplication des demandes de rac- dement des installations de consommation cordements de bornes, concomitantes avec individuelle ou collective en BT > 36 kVA et en l’accélération des énergies renouvelables, met HTA, cadre qui inclue les IRVE. Les demandes une forte pression sur les GRDE (Gestionnaires de raccordement sont ainsi traitées chronologi- de réseau de distribution d’énergie). quement à partir de leur date de dépôt, ou de Le raccordement électrique "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Le raccordement au réseau de distribution est")
    thisalinea.textcontent.append("La procédure « Enedis-PRO-RAC_14E » de 2021")
    thisalinea.textcontent.append("un jalon essentiel du déploiement des IRVE ;")
    thisalinea.textcontent.append("détaille le traitement des demandes de raccor-")
    thisalinea.textcontent.append("mais la multiplication des demandes de rac-")
    thisalinea.textcontent.append("dement des installations de consommation")
    thisalinea.textcontent.append("cordements de bornes, concomitantes avec")
    thisalinea.textcontent.append("individuelle ou collective en BT > 36 kVA et en")
    thisalinea.textcontent.append("l’accélération des énergies renouvelables, met")
    thisalinea.textcontent.append("HTA, cadre qui inclue les IRVE. Les demandes")
    thisalinea.textcontent.append("une forte pression sur les GRDE (Gestionnaires")
    thisalinea.textcontent.append("de raccordement sont ainsi traitées chronologi-")
    thisalinea.textcontent.append("de réseau de distribution d’énergie).")
    thisalinea.textcontent.append("quement à partir de leur date de dépôt, ou de")
    thisalinea.textcontent.append("Le raccordement électrique des IRVE suit")
    thisalinea.textcontent.append("des procédures définies à partir du Code de")
    thisalinea.textcontent.append("l’Énergie, des décrets applicables, et des déli-")
    thisalinea.textcontent.append("bérations de la CRE (Commission de régulation")
    thisalinea.textcontent.append("de l’énergie). L’ensemble des GRDE y sont sou-")
    thisalinea.textcontent.append("mis ; l’étude prend ici principalement l’exemple")
    thisalinea.textcontent.append("la date de dépôt de la demande anticipée de")
    thisalinea.textcontent.append("raccordement. Des délais importants dans les")
    thisalinea.textcontent.append("raccordements d’IRVE sont toutefois remontés")
    thisalinea.textcontent.append("par une majorité d’acteurs du secteur et obser-")
    thisalinea.textcontent.append("vés dans les données publiées par la CRE32 sur")
    thisalinea.textcontent.append("l’activité 2022.")
    thisalinea.textcontent.append("d’Enedis, qui représente 95 % du réseau français,")
    thisalinea.textcontent.append("Des mesures avaient été prises pour facili-")
    thisalinea.textcontent.append("mais les observations et mesures identifiées se")
    thisalinea.textcontent.append("ter notamment les raccordements sur les")
    thisalinea.textcontent.append("rapportent à l’ensemble des GRD concernés.")
    thisalinea.textcontent.append("aires de service des grands axes routiers.")
    thisalinea.textcontent.append("En particulier, la procédure dérogatoire")
    thisalinea.textcontent.append("« Enedis-PRO-RAC_028E » détaille une simplifi-")
    thisalinea.textcontent.append("cation de la procédure standard pour les IRVE :")
    thisalinea.textcontent.append("Par ailleurs, comme indiqué dans le Tome 1 –")
    thisalinea.textcontent.append("État des lieux de la recharge en France, le taux")
    thisalinea.textcontent.append("de réfaction majoré ne s’appliquait que pour les")
    thisalinea.textcontent.append("renforcements supplémentaires du réseau")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Les SCA (Sociétés concessionnaires d’au- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 122
    thisalinea.parentID = 121
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Les SCA (Sociétés concessionnaires d’au- premiers raccordements des aires de service ; toroutes) sont autorisées à anticiper une or, les puissances demandées en raccordement demande de raccordement avant la désigna- lors de la première vague d’installations ont été tion explicite de l’opérateur IRVE. limitées à une valeur au-delà de laquelle des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Les SCA (Sociétés concessionnaires d’au-")
    thisalinea.textcontent.append("premiers raccordements des aires de service ;")
    thisalinea.textcontent.append("toroutes) sont autorisées à anticiper une")
    thisalinea.textcontent.append("or, les puissances demandées en raccordement")
    thisalinea.textcontent.append("demande de raccordement avant la désigna-")
    thisalinea.textcontent.append("lors de la première vague d’installations ont été")
    thisalinea.textcontent.append("tion explicite de l’opérateur IRVE.")
    thisalinea.textcontent.append("limitées à une valeur au-delà de laquelle des")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ La fourniture de l’autorisation d’urbanisme ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 123
    thisalinea.parentID = 121
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ La fourniture de l’autorisation d’urbanisme devenaient nécessaires. Le taux de réfaction délivrée, de la localisation précise du poste majoré n’a donc pas été utilisé au maximum de livraison HTA client, et des caractéristiques de son potentiel, ce qui rendra les investisse- techniques détaillées ne sont pas nécessaires ments relatifs aux prochains raccordements pour entrer dans la file d’attente ; la puissance (pour augmenter la puissance à mesure que de raccordement demandée ne peut cepen- l’électrification du parc s’intensifie) significati- dant pas être modifiée. vement moins accessibles. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ La fourniture de l’autorisation d’urbanisme")
    thisalinea.textcontent.append("devenaient nécessaires. Le taux de réfaction")
    thisalinea.textcontent.append("délivrée, de la localisation précise du poste")
    thisalinea.textcontent.append("majoré n’a donc pas été utilisé au maximum")
    thisalinea.textcontent.append("de livraison HTA client, et des caractéristiques")
    thisalinea.textcontent.append("de son potentiel, ce qui rendra les investisse-")
    thisalinea.textcontent.append("techniques détaillées ne sont pas nécessaires")
    thisalinea.textcontent.append("ments relatifs aux prochains raccordements")
    thisalinea.textcontent.append("pour entrer dans la file d’attente ; la puissance")
    thisalinea.textcontent.append("(pour augmenter la puissance à mesure que")
    thisalinea.textcontent.append("de raccordement demandée ne peut cepen-")
    thisalinea.textcontent.append("l’électrification du parc s’intensifie) significati-")
    thisalinea.textcontent.append("dant pas être modifiée.")
    thisalinea.textcontent.append("vement moins accessibles.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.1.2. Visibilité insuffisante pour la bonne élaboration des SDIRVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 124
    thisalinea.parentID = 120
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Les SDIRVE (S chéma dire c teur des Pour l’élaboration des SDIRVE, les opérateurs Infrastructures de recharges pour véhicules électriques) offrent la possibilité à une collec- tivité ou un établissement public d’organiser sont tenus par le Décret n° 2021-566 du 10 mai 202134 de fournir des données concernant l’utili- sation des bornes sur leur réseau. À partir de ces le déploiement des IRVE sur son territoire de données peuvent être construits les schémas manière concertée et cohérente ; au premier directeurs. trimestre 2023, seule une trentaine de SDIRVE ont été validés, sur 116 engagés à l’échelle nationale33. Toutefois, les plans "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Les SDIRVE (S chéma dire c teur des")
    thisalinea.textcontent.append("Pour l’élaboration des SDIRVE, les opérateurs")
    thisalinea.textcontent.append("Infrastructures de recharges pour véhicules")
    thisalinea.textcontent.append("électriques) offrent la possibilité à une collec-")
    thisalinea.textcontent.append("tivité ou un établissement public d’organiser")
    thisalinea.textcontent.append("sont tenus par le Décret n° 2021-566 du 10 mai")
    thisalinea.textcontent.append("202134 de fournir des données concernant l’utili-")
    thisalinea.textcontent.append("sation des bornes sur leur réseau. À partir de ces")
    thisalinea.textcontent.append("le déploiement des IRVE sur son territoire de")
    thisalinea.textcontent.append("données peuvent être construits les schémas")
    thisalinea.textcontent.append("manière concertée et cohérente ; au premier")
    thisalinea.textcontent.append("directeurs.")
    thisalinea.textcontent.append("trimestre 2023, seule une trentaine de SDIRVE")
    thisalinea.textcontent.append("ont été validés, sur 116 engagés à l’échelle")
    thisalinea.textcontent.append("nationale33.")
    thisalinea.textcontent.append("Toutefois, les plans des déploiements à venir des")
    thisalinea.textcontent.append("opérateurs privés ne sont pas toujours commu-")
    thisalinea.textcontent.append("niqués dans la réalité, et les SDIRVE risquent de")
    thisalinea.textcontent.append("Ils ont été introduits par la Loi d’orientation des")
    thisalinea.textcontent.append("pâtir d’obsolescence accélérée si une démarche")
    thisalinea.textcontent.append("mobilités de 2019, et permettent en particulier")
    thisalinea.textcontent.append("contraignante de mise à disposition des don-")
    thisalinea.textcontent.append("de bénéficier d’un taux de réfaction majoré à")
    thisalinea.textcontent.append("nées n’est pas mise en place et respectée par")
    thisalinea.textcontent.append("75 % pour le raccordement des IRVE qui s’ins-")
    thisalinea.textcontent.append("les développeurs et opérateurs d’IRVE.")
    thisalinea.textcontent.append("crivent dans le SDIRVE.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.1.3. Incertitudes sur la part des alternatives technologiques à la mobilité lourde à batterie électrique"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 125
    thisalinea.parentID = 120
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Les incertitudes entourant le développement de L’hydrogène a été considéré comme une solu- l’hydrogène en tant que source d’énergie pour tion prometteuse pour les véhicules lourds la mobilité lourde ont contribué à retarder le tels que les camions et les bus, offrant une déploiement des bornes de recharge électrique alternative aux carburants fossiles et permet- adaptées à cet usage spécifique. tant des temps de recharge plus rapides ainsi qu’une autonomie étendue. Les constructeurs continuent d’investir dans la technologie, mais à haute pression ou liquide sont donc très limi- une forme de consensus a semblé émerger ces tées en France. À "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Les incertitudes entourant le développement de")
    thisalinea.textcontent.append("L’hydrogène a été considéré comme une solu-")
    thisalinea.textcontent.append("l’hydrogène en tant que source d’énergie pour")
    thisalinea.textcontent.append("tion prometteuse pour les véhicules lourds")
    thisalinea.textcontent.append("la mobilité lourde ont contribué à retarder le")
    thisalinea.textcontent.append("tels que les camions et les bus, offrant une")
    thisalinea.textcontent.append("déploiement des bornes de recharge électrique")
    thisalinea.textcontent.append("alternative aux carburants fossiles et permet-")
    thisalinea.textcontent.append("adaptées à cet usage spécifique.")
    thisalinea.textcontent.append("tant des temps de recharge plus rapides ainsi")
    thisalinea.textcontent.append("qu’une autonomie étendue. Les constructeurs")
    thisalinea.textcontent.append("continuent d’investir dans la technologie, mais")
    thisalinea.textcontent.append("à haute pression ou liquide sont donc très limi-")
    thisalinea.textcontent.append("une forme de consensus a semblé émerger ces")
    thisalinea.textcontent.append("tées en France. À l’inverse, la recharge électrique")
    thisalinea.textcontent.append("derniers mois en faveur de l’électrique à bat-")
    thisalinea.textcontent.append("bénéficie d’une technologie éprouvée (bien qu’à")
    thisalinea.textcontent.append("terie, au moins pour la décennie à venir. Cela")
    thisalinea.textcontent.append("adapter aux hautes puissances, jusqu’au MCS)")
    thisalinea.textcontent.append("s’est matérialisé par d’importantes levées de")
    thisalinea.textcontent.append("et d’une infrastructure existante plus dévelop-")
    thisalinea.textcontent.append("fonds dans le secteur et des annonces en ce")
    thisalinea.textcontent.append("sens émanant des constructeurs35.")
    thisalinea.textcontent.append("pée pour les véhicules légers.")
    thisalinea.textcontent.append("Les coûts élevés associés à l’infrastructure de")
    thisalinea.textcontent.append("de la mobilité hydrogène reste néanmoins une")
    thisalinea.textcontent.append("l’hydrogène, notamment la construction de sta-")
    thisalinea.textcontent.append("inconnue dimensionnante dans le déploiement")
    thisalinea.textcontent.append("tions de ravitaillement spécialisées, le transport")
    thisalinea.textcontent.append("à plus long terme de l’infrastructure de recharge")
    thisalinea.textcontent.append("Bien qu’une tendance claire se dessine, le futur")
    thisalinea.textcontent.append("ou les pipelines, pèsent dans cette tendance. À")
    thisalinea.textcontent.append("électrique.")
    thisalinea.textcontent.append("date, les possibilités de ravitaillement hydrogène")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.2. Obstacles à l’installation des IRVE"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 126
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Sur les grands axes routiers, la disponibilité Les poids lourds nécessiteront donc des limitée du foncier peut poser un défi pour l’ins- infrastructures de recharge spécifiques et tallation de stations de recharge. Les espaces cohérentes avec les temps de pause, à savoir le long de ces axes sont prisés par différentes des technologies MCS pour les temps de pause activités commerciales, se caractérisent par des courts et des bornes DC du type 50 à ~100 kW coûts élevés du foncier et peuvent être soumis pour la recharge nocturne. L’enjeu portera sur à des réglementations limitant l’utilisation des l’aménagement optimal des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.1. Faible disponibilité du foncier sur grands axes routiers pour accueillir des stations de recharge, en particulier pour poids lourds"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 127
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Sur les grands axes routiers, la disponibilité Les poids lourds nécessiteront donc des limitée du foncier peut poser un défi pour l’ins- infrastructures de recharge spécifiques et tallation de stations de recharge. Les espaces cohérentes avec les temps de pause, à savoir le long de ces axes sont prisés par différentes des technologies MCS pour les temps de pause activités commerciales, se caractérisent par des courts et des bornes DC du type 50 à ~100 kW coûts élevés du foncier et peuvent être soumis pour la recharge nocturne. L’enjeu portera sur à des réglementations limitant l’utilisation des l’aménagement optimal des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Sur les grands axes routiers, la disponibilité")
    thisalinea.textcontent.append("Les poids lourds nécessiteront donc des")
    thisalinea.textcontent.append("limitée du foncier peut poser un défi pour l’ins-")
    thisalinea.textcontent.append("infrastructures de recharge spécifiques et")
    thisalinea.textcontent.append("tallation de stations de recharge. Les espaces")
    thisalinea.textcontent.append("cohérentes avec les temps de pause, à savoir")
    thisalinea.textcontent.append("le long de ces axes sont prisés par différentes")
    thisalinea.textcontent.append("des technologies MCS pour les temps de pause")
    thisalinea.textcontent.append("activités commerciales, se caractérisent par des")
    thisalinea.textcontent.append("courts et des bornes DC du type 50 à ~100 kW")
    thisalinea.textcontent.append("coûts élevés du foncier et peuvent être soumis")
    thisalinea.textcontent.append("pour la recharge nocturne. L’enjeu portera sur")
    thisalinea.textcontent.append("à des réglementations limitant l’utilisation des")
    thisalinea.textcontent.append("l’aménagement optimal des aires de service ou")
    thisalinea.textcontent.append("terrains. Dans le cas des poids lourds, où suffi-")
    thisalinea.textcontent.append("de repos afin de gérer au mieux l’affluence des")
    thisalinea.textcontent.append("samment d’espace sera requis pour faciliter les")
    thisalinea.textcontent.append("poids lourds, de limiter le temps d’attente et de")
    thisalinea.textcontent.append("manœuvres et fluidifier le flux de véhicules, la")
    thisalinea.textcontent.append("faciliter les manœuvres.")
    thisalinea.textcontent.append("problématique se pose d’autant plus.")
    thisalinea.textcontent.append("Trouver des emplacements appropriés pour ins-")
    thisalinea.textcontent.append("La gestion de la logistique est cruciale pour les")
    thisalinea.textcontent.append("taller ces infrastructures de recharge représen-")
    thisalinea.textcontent.append("transporteurs et cela implique une planification")
    thisalinea.textcontent.append("tera un défi en raison de la disponibilité limitée")
    thisalinea.textcontent.append("efficace des temps de pause pour les conduc-")
    thisalinea.textcontent.append("teurs afin de respecter les réglementations en")
    thisalinea.textcontent.append("vigueur et d’optimiser les opérations de trans-")
    thisalinea.textcontent.append("du foncier le long des grands axes routiers. Les")
    thisalinea.textcontent.append("terrains disponibles peuvent déjà être utilisés")
    thisalinea.textcontent.append("pour d’autres fins, tels que des stations-ser-")
    thisalinea.textcontent.append("port. Pour favoriser la transition vers les poids")
    thisalinea.textcontent.append("vice traditionnelles, des aires de repos avec un")
    thisalinea.textcontent.append("lourds électriques, il apparaît donc que la facilité")
    thisalinea.textcontent.append("minimum d’artificialisation ou des installations")
    thisalinea.textcontent.append("d’accès à des points de charge lors des temps")
    thisalinea.textcontent.append("existantes. De plus, l’acquisition ou la location")
    thisalinea.textcontent.append("de pause réglementaires sera primordiale. Les")
    thisalinea.textcontent.append("de foncier pour installer des infrastructures")
    thisalinea.textcontent.append("conducteurs doivent réaliser une pause de")
    thisalinea.textcontent.append("45 minutes36 après 4,5 heures de conduite et")
    thisalinea.textcontent.append("un repos réglementaire de 11 heures, pouvant")
    thisalinea.textcontent.append("être réduit à 9 heures trois fois par semaine.")
    thisalinea.textcontent.append("de recharge représente un investissement ou")
    thisalinea.textcontent.append("des coûts importants et peut complexifier le")
    thisalinea.textcontent.append("déploiement.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.2. Faible disponibilité du foncier en zone urbaine dense"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 128
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Le déploiement d’infrastructures de recharge clé sera de proposer des options de recharge en zone urbaine dense peut représenter un défi lente en nombre suffisant afin de répondre au important en raison de l’espace limité et de la besoin de recharge « de proximité » des foyers concurrence pour l’utilisation du foncier. Les ne disposant pas de stationnement privatif avec zones urbaines denses sont souvent caractéri- possibilité de recharge. À noter qu’en milieu sées par une forte tension au niveau des places urbain, il y aura aussi une demande pour des de stationnement et cela constitue donc un bornes de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Le déploiement d’infrastructures de recharge")
    thisalinea.textcontent.append("clé sera de proposer des options de recharge")
    thisalinea.textcontent.append("en zone urbaine dense peut représenter un défi")
    thisalinea.textcontent.append("lente en nombre suffisant afin de répondre au")
    thisalinea.textcontent.append("important en raison de l’espace limité et de la")
    thisalinea.textcontent.append("besoin de recharge « de proximité » des foyers")
    thisalinea.textcontent.append("concurrence pour l’utilisation du foncier. Les")
    thisalinea.textcontent.append("ne disposant pas de stationnement privatif avec")
    thisalinea.textcontent.append("zones urbaines denses sont souvent caractéri-")
    thisalinea.textcontent.append("possibilité de recharge. À noter qu’en milieu")
    thisalinea.textcontent.append("sées par une forte tension au niveau des places")
    thisalinea.textcontent.append("urbain, il y aura aussi une demande pour des")
    thisalinea.textcontent.append("de stationnement et cela constitue donc un")
    thisalinea.textcontent.append("bornes de recharge DC rapide et ultra-rapide,")
    thisalinea.textcontent.append("réel obstacle au déploiement d’infrastructures")
    thisalinea.textcontent.append("notamment de la part des professionnels")
    thisalinea.textcontent.append("de recharge. Le problème de la voiture « ven-")
    thisalinea.textcontent.append("touse »37 est particulièrement épineux puisqu’il")
    thisalinea.textcontent.append("faut s’assurer que le point de recharge soit le")
    thisalinea.textcontent.append("plus souvent disponible.")
    thisalinea.textcontent.append("tels que les chauffeurs VTC et les loueurs de")
    thisalinea.textcontent.append("véhicules, qui souhaitent une recharge rapide")
    thisalinea.textcontent.append("pendant leurs heures de travail. L’idée est")
    thisalinea.textcontent.append("donc d’évaluer au mieux le besoin de chaque")
    thisalinea.textcontent.append("commune pour déployer les technologies de")
    thisalinea.textcontent.append("En termes de technologies de recharge, la")
    thisalinea.textcontent.append("recharge adéquates.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.3. Investissements importants nécessaires, en particulier pour la recharge DC"
    thisalinea.titlefontsize = "12.000000000000057"
    thisalinea.nativeID = 129
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "L’installation d’infrastructures de recharge se recharge varient selon la technologie. Les coûts associés au déploiement de bornes rapides en transformateur, câblage, borne de recharge, courant continu sont plus élevés, notamment : etc. Ces travaux peuvent être d’autant plus coûteux si des mises à niveau sont nécessaires Les investissements pour les bornes de ■ Coût de fourniture des bornes. 350 kW contre ~2 000 € pour du AC38 ; Ces investissements plus importants peuvent constituer un frein important au déploiement de l’infrastructure DC rapide, notamment pour les collectivités. ■ Coût éventuel lié au foncier si son acquisition caractérise par un certain "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("L’installation d’infrastructures de recharge se")
    thisalinea.textcontent.append("recharge varient selon la technologie. Les coûts")
    thisalinea.textcontent.append("associés au déploiement de bornes rapides en")
    thisalinea.textcontent.append("transformateur, câblage, borne de recharge,")
    thisalinea.textcontent.append("courant continu sont plus élevés, notamment :")
    thisalinea.textcontent.append("etc. Ces travaux peuvent être d’autant plus")
    thisalinea.textcontent.append("coûteux si des mises à niveau sont nécessaires")
    thisalinea.textcontent.append("Les investissements pour les bornes de")
    thisalinea.textcontent.append("■  Coût de fourniture des bornes.")
    thisalinea.textcontent.append("350 kW contre ~2 000 € pour du AC38 ;")
    thisalinea.textcontent.append("Ces investissements plus importants peuvent")
    thisalinea.textcontent.append("constituer un frein important au déploiement")
    thisalinea.textcontent.append("de l’infrastructure DC rapide, notamment pour")
    thisalinea.textcontent.append("les collectivités.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Coût éventuel lié au foncier si son acquisition ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 130
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Coût éventuel lié au foncier si son acquisition caractérise par un certain nombre de postes est souhaitée plutôt qu’une location. de coûts : "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Coût éventuel lié au foncier si son acquisition")
    thisalinea.textcontent.append("caractérise par un certain nombre de postes")
    thisalinea.textcontent.append("est souhaitée plutôt qu’une location.")
    thisalinea.textcontent.append("de coûts :")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Coût de l’infrastructure électrique correspon- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 131
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Coût de l’infrastructure électrique correspon- dant aux différents équipements électriques : "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Coût de l’infrastructure électrique correspon-")
    thisalinea.textcontent.append("dant aux différents équipements électriques :")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Installation : de ~25 000 à 30 000 € pour du ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 132
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Installation : de ~25 000 à 30 000 € pour du pour répondre à la demande de puissance des DC contre moins de 5 000 € pour du AC ; bornes de recharge. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Installation : de ~25 000 à 30 000 € pour du")
    thisalinea.textcontent.append("pour répondre à la demande de puissance des")
    thisalinea.textcontent.append("DC contre moins de 5 000 € pour du AC ;")
    thisalinea.textcontent.append("bornes de recharge.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Fourniture : jusqu’à ~75 000 € pour du DC "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 133
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "■ Fourniture : jusqu’à ~75 000 € pour du DC "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Fourniture : jusqu’à ~75 000 € pour du DC")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Coût d’installation de la borne incluant la ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 134
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "■ Coût d’installation de la borne incluant la main-d’œuvre, les travaux de génie civil pour la mise en place des bases, les frais de raccor- dement électrique, etc. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Coût d’installation de la borne incluant la")
    thisalinea.textcontent.append("main-d’œuvre, les travaux de génie civil pour")
    thisalinea.textcontent.append("la mise en place des bases, les frais de raccor-")
    thisalinea.textcontent.append("dement électrique, etc.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.4. Délais de fourniture des bornes de recharge et autres défis relatifs à la chaîne d’approvisionnement"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 135
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "L’accélération du déploiement des bornes de aux semi-conducteurs (diodes, microcontrô- recharge représente une opportunité pour les leurs, capteurs…), nécessitent de passer des fabricants de bornes, mais engendre des défis commandes importantes, et donc d’avancer en termes de disponibilité du matériel, de leur des dépenses pour pouvoir sécuriser des acheminement et de leur production. approvisionnements suffisants. Cela pose des contraintes d’approvisionnement Malgré une cadence soutenue de production, pour les constructeurs eux-mêmes, qui doivent l’écosystème observe un allongement des passer des commandes de plus en plus impor- délais de livraison des bornes de recharge, qui tantes à leurs fournisseurs, voire mobiliser des "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("L’accélération du déploiement des bornes de")
    thisalinea.textcontent.append("aux semi-conducteurs (diodes, microcontrô-")
    thisalinea.textcontent.append("recharge représente une opportunité pour les")
    thisalinea.textcontent.append("leurs, capteurs…), nécessitent de passer des")
    thisalinea.textcontent.append("fabricants de bornes, mais engendre des défis")
    thisalinea.textcontent.append("commandes importantes, et donc d’avancer")
    thisalinea.textcontent.append("en termes de disponibilité du matériel, de leur")
    thisalinea.textcontent.append("des dépenses pour pouvoir sécuriser des")
    thisalinea.textcontent.append("acheminement et de leur production.")
    thisalinea.textcontent.append("approvisionnements suffisants.")
    thisalinea.textcontent.append("Cela pose des contraintes d’approvisionnement")
    thisalinea.textcontent.append("Malgré une cadence soutenue de production,")
    thisalinea.textcontent.append("pour les constructeurs eux-mêmes, qui doivent")
    thisalinea.textcontent.append("l’écosystème observe un allongement des")
    thisalinea.textcontent.append("passer des commandes de plus en plus impor-")
    thisalinea.textcontent.append("délais de livraison des bornes de recharge, qui")
    thisalinea.textcontent.append("tantes à leurs fournisseurs, voire mobiliser des")
    thisalinea.textcontent.append("peuvent, pour certains constructeurs, atteindre")
    thisalinea.textcontent.append("efforts commerciaux supplémentaires pour en")
    thisalinea.textcontent.append("une année.")
    thisalinea.textcontent.append("sécuriser de nouveaux.")
    thisalinea.textcontent.append("Tous les composants n’ont cependant pas la")
    thisalinea.textcontent.append("obligent les installateurs de bornes à anticiper")
    thisalinea.textcontent.append("même criticité pour les fabricants de bornes :")
    thisalinea.textcontent.append("les commandes pour ne pas retarder la livraison")
    thisalinea.textcontent.append("des points de charge. En particulier pour les")
    thisalinea.textcontent.append("opérateurs locaux, cela nécessite un regroupe-")
    thisalinea.textcontent.append("liques) : peu critiques, disponibles.")
    thisalinea.textcontent.append("ment de ceux-ci pour passer des commandes")
    thisalinea.textcontent.append("Ces tensions sur la chaîne d’approvisionnement")
    thisalinea.textcontent.append("fournis par des grands groupes électroniques,")
    thisalinea.textcontent.append("capables d’absorber cette augmentation de")
    thisalinea.textcontent.append("De manière générale, les tensions sur l’offre")
    thisalinea.textcontent.append("la demande.")
    thisalinea.textcontent.append("de bornes, en particulier européenne, ont un")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le matériel de base (exemple : armoires métal- "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 136
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Le matériel de base (exemple : armoires métal- "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le matériel de base (exemple : armoires métal-")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Les composants techniques non-critiques (par ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 137
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Les composants techniques non-critiques (par communes aux fournisseurs de bornes, et ainsi exemple : les disjoncteurs), sont généralement raccourcir les délais et optimiser les coûts. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Les composants techniques non-critiques (par")
    thisalinea.textcontent.append("communes aux fournisseurs de bornes, et ainsi")
    thisalinea.textcontent.append("exemple : les disjoncteurs), sont généralement")
    thisalinea.textcontent.append("raccourcir les délais et optimiser les coûts.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Les composants critiques, c’est-à-dire les tran- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 138
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Les composants critiques, c’est-à-dire les tran- impact négatif sur la cadence de déploiement sistors de puissance et autres composants liés des points de charge. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Les composants critiques, c’est-à-dire les tran-")
    thisalinea.textcontent.append("impact négatif sur la cadence de déploiement")
    thisalinea.textcontent.append("sistors de puissance et autres composants liés")
    thisalinea.textcontent.append("des points de charge.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.3. Obstacles à l’opération des IRVE"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 139
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "Le modèle d’affaires des IRVE est fondé sur un équilibre entre des CAPEX importants et les revenus issus des sessions de recharge, qui sont améliorer le taux d’utilisation, mais le besoin restera structurellement trop faible. en fonction de la tarification et du taux d’utilisa- Pour l’instant, le taux moyen d’utilisation des IRVE est estimé être de l’ordre de 2 %39, compte tenu de la taille du parc actuel comparé au nombre et à la puissance des points de charge Dans la modélisation générale, 3 scénarios avec sur le territoire. Les acteurs de l’écosystème ont 3 évolutions du taux d’utilisation entre "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.3.1. Rentabilité insuffisante"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 140
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Le modèle d’affaires des IRVE est fondé sur un équilibre entre des CAPEX importants et les revenus issus des sessions de recharge, qui sont améliorer le taux d’utilisation, mais le besoin restera structurellement trop faible. en fonction de la tarification et du taux d’utilisa- Pour l’instant, le taux moyen d’utilisation des IRVE est estimé être de l’ordre de 2 %39, compte tenu de la taille du parc actuel comparé au nombre et à la puissance des points de charge Dans la modélisation générale, 3 scénarios avec sur le territoire. Les acteurs de l’écosystème ont 3 évolutions du taux d’utilisation entre "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Le modèle d’affaires des IRVE est fondé sur un")
    thisalinea.textcontent.append("équilibre entre des CAPEX importants et les")
    thisalinea.textcontent.append("revenus issus des sessions de recharge, qui sont")
    thisalinea.textcontent.append("améliorer le taux d’utilisation, mais le besoin")
    thisalinea.textcontent.append("restera structurellement trop faible.")
    thisalinea.textcontent.append("en fonction de la tarification et du taux d’utilisa-")
    thisalinea.textcontent.append("Pour l’instant, le taux moyen d’utilisation des")
    thisalinea.textcontent.append("IRVE est estimé être de l’ordre de 2 %39, compte")
    thisalinea.textcontent.append("tenu de la taille du parc actuel comparé au")
    thisalinea.textcontent.append("nombre et à la puissance des points de charge")
    thisalinea.textcontent.append("Dans la modélisation générale, 3 scénarios avec")
    thisalinea.textcontent.append("sur le territoire. Les acteurs de l’écosystème ont")
    thisalinea.textcontent.append("3 évolutions du taux d’utilisation entre 2023")
    thisalinea.textcontent.append("signalé une faible rentabilité, voire des modèles")
    thisalinea.textcontent.append("et 2035 ont été considérés : de 4 % (1 h) à 8 %")
    thisalinea.textcontent.append("déficitaires, ce qui est cohérent avec cette esti-")
    thisalinea.textcontent.append("(2 h), de 6 % (1 h 30) à 12,5 % (3 h) et de 8 % (2 h)")
    thisalinea.textcontent.append("mation du taux d’utilisation.")
    thisalinea.textcontent.append("à 17 % (4 h). L’évolution est linéaire entre 2022")
    thisalinea.textcontent.append("et 2035.")
    thisalinea.textcontent.append("Figure 23 : Correspondance entre taux d’utilisation")
    thisalinea.textcontent.append("et nombre d’heures d’utilisation quotidienne moyenne sur une année")
    thisalinea.textcontent.append("Scénario")
    thisalinea.textcontent.append("[4 % - 8 %]")
    thisalinea.textcontent.append("[6 % - 12 %]")
    thisalinea.textcontent.append("[8 % - 17 %]")
    thisalinea.textcontent.append("Heures d’utilisation quotidienne")
    thisalinea.textcontent.append("en 2023")
    thisalinea.textcontent.append("1 h")
    thisalinea.textcontent.append("1 h 30")
    thisalinea.textcontent.append("2 h")
    thisalinea.textcontent.append("en 2035")
    thisalinea.textcontent.append("2 h")
    thisalinea.textcontent.append("3 h")
    thisalinea.textcontent.append("4 h")
    thisalinea.textcontent.append("Une approximation d’un modèle d’affaires sou-")
    thisalinea.textcontent.append("mécanisme de la TIRUERT (seulement les pre-")
    thisalinea.textcontent.append("mis à ces différents taux d’utilisation a été étu-")
    thisalinea.textcontent.append("dié, en particulier pour le cas d’usage « point de")
    thisalinea.textcontent.append("mières années), le TRI sur 15 ans passe à ~15 %")
    thisalinea.textcontent.append("dans le scénario [8 %-17 %]. Dans le scénario")
    thisalinea.textcontent.append("charge 7 kW AC sur voirie pour de la recharge")
    thisalinea.textcontent.append("de proximité ». Des CAPEX simplifiés ont été")
    thisalinea.textcontent.append("[6 %-12 %], le TRI descend à 6 %. Enfin dans le")
    thisalinea.textcontent.append("scénario [4 %-8 %], le TRI est négatif.40")
    thisalinea.textcontent.append("estimés à ~4 000 € (fourniture ~2 000 €, instal-")
    thisalinea.textcontent.append("lation et raccordement ~2 000 €) et des OPEX")
    thisalinea.textcontent.append("Puisqu’à l’heure actuelle le taux d’utilisation")
    thisalinea.textcontent.append("(hors coût de l’énergie) à ~400 €. À partir des")
    thisalinea.textcontent.append("effectif est en moyenne encore inférieur, le")
    thisalinea.textcontent.append("courbes de prix AFRY pour le marché européen,")
    thisalinea.textcontent.append("problème de rentabilité sur les bornes AC 7 kW")
    thisalinea.textcontent.append("et un prix de 33 centimes € du kWh pratiqué")
    thisalinea.textcontent.append("est un enjeu majeur si les tarifs doivent rester")
    thisalinea.textcontent.append("à la borne, la rentabilité est très faible dans le")
    thisalinea.textcontent.append("modérés.")
    thisalinea.textcontent.append("scénario [8 %-17 %] (de l’ordre de 1 % de TRI), et")
    thisalinea.textcontent.append("négatif dans les scénarios [6 %-12 %] et [4 %-8 %]")
    thisalinea.textcontent.append("À noter que certains modes de tarification pra-")
    thisalinea.textcontent.append("en l’absence de mécanismes de soutien.")
    thisalinea.textcontent.append("tiqués (systèmes d’abonnements notamment)")
    thisalinea.textcontent.append("peuvent permettre d’équilibrer le modèle des")
    thisalinea.textcontent.append("Toutefois, en ajoutant une prime ADVENIR")
    thisalinea.textcontent.append("opérateurs à l’échelle de leur réseau entier, mais")
    thisalinea.textcontent.append("(~1 000 € de CAPEX) et une approximation du")
    thisalinea.textcontent.append("n’ont pas été modélisés dans le cadre de l’étude.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Lorsque les besoins futurs ont été anticipés, ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 141
    thisalinea.parentID = 140
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Lorsque les besoins futurs ont été anticipés, tion annuel moyen. Un faible taux d’utilisation et qu’à l’heure actuelle le taux d’électrification s’observe : ne suffit pas à générer une fréquentation significative : "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Lorsque les besoins futurs ont été anticipés,")
    thisalinea.textcontent.append("tion annuel moyen. Un faible taux d’utilisation")
    thisalinea.textcontent.append("et qu’à l’heure actuelle le taux d’électrification")
    thisalinea.textcontent.append("s’observe :")
    thisalinea.textcontent.append("ne suffit pas à générer une fréquentation")
    thisalinea.textcontent.append("significative :")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Lorsque le besoin en recharge pour la « petite "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 142
    thisalinea.parentID = 140
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Lorsque le besoin en recharge pour la « petite "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Lorsque le besoin en recharge pour la « petite")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– L’électrification du parc automobile amélio- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 143
    thisalinea.parentID = 140
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– L’électrification du parc automobile amélio- itinérance » est faible ou très faible aux alen- rera progressivement la rentabilité. tours de la borne ou d’une hypothétique borne (population, axes à proximité, lieux excentrés ou peu pratiques, etc.) : "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– L’électrification du parc automobile amélio-")
    thisalinea.textcontent.append("itinérance » est faible ou très faible aux alen-")
    thisalinea.textcontent.append("rera progressivement la rentabilité.")
    thisalinea.textcontent.append("tours de la borne ou d’une hypothétique")
    thisalinea.textcontent.append("borne (population, axes à proximité, lieux")
    thisalinea.textcontent.append("excentrés ou peu pratiques, etc.) :")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– L’électrification du parc automobile pourra "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 144
    thisalinea.parentID = 140
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– L’électrification du parc automobile pourra "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– L’électrification du parc automobile pourra")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.3.2. Durée légale des contrats de sous-concessions autoroutières"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 145
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Sur les autoroutes concédées, l’installation leurs sous-concessionnaires ne peuvent pas et l’opération d’IRVE sur les aires de service dépasser une durée de 15 ans, en application doivent passer par un processus d’appel de l’article R122-42 du Code de la voirie routière. d’offres transparent, à l’issue duquel une L’État a récemment autorisé que les contrats société sous-concessionnaire est sélection- de sous-concession IRVE puissent dépasser la née comme CPO. Les contrats entre les durée résiduelle des concessions autoroutières, sociétés concessionnaires d’autoroutes et ce qui a écarté un premier obstacle contractuel. Toutefois, puisque les investissements réalisés des durées de contrat au-delà de 15 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Sur les autoroutes concédées, l’installation")
    thisalinea.textcontent.append("leurs sous-concessionnaires ne peuvent pas")
    thisalinea.textcontent.append("et l’opération d’IRVE sur les aires de service")
    thisalinea.textcontent.append("dépasser une durée de 15 ans, en application")
    thisalinea.textcontent.append("doivent passer par un processus d’appel")
    thisalinea.textcontent.append("de l’article R122-42 du Code de la voirie routière.")
    thisalinea.textcontent.append("d’offres transparent, à l’issue duquel une")
    thisalinea.textcontent.append("L’État a récemment autorisé que les contrats")
    thisalinea.textcontent.append("société sous-concessionnaire est sélection-")
    thisalinea.textcontent.append("de sous-concession IRVE puissent dépasser la")
    thisalinea.textcontent.append("née comme CPO. Les contrats entre les")
    thisalinea.textcontent.append("durée résiduelle des concessions autoroutières,")
    thisalinea.textcontent.append("sociétés concessionnaires d’autoroutes et")
    thisalinea.textcontent.append("ce qui a écarté un premier obstacle contractuel.")
    thisalinea.textcontent.append("Toutefois, puisque les investissements réalisés")
    thisalinea.textcontent.append("des durées de contrat au-delà de 15 ans, ce qui")
    thisalinea.textcontent.append("sont importants (notamment sur la recharge DC")
    thisalinea.textcontent.append("n’est pas possible à date et peut constituer un")
    thisalinea.textcontent.append("ultra-rapide, ou sur les infrastructures destinées")
    thisalinea.textcontent.append("frein.")
    thisalinea.textcontent.append("aux poids lourds), il peut être nécessaire de fixer")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.3.3. Défis de la maintenance et du taux de disponibilité"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 146
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Un point de charge est considéré comme dispo- une zone avec un faible maillage. Certains opé- nible s’il n’est ni en maintenance ni hors-service. L’Avere-France41 indique dans son baromètre un taux de disponibilité de 84 % en moyenne rateurs ont remonté qu’un simple appel pour régler le problème à distance pourrait souvent suffire. La mise en place d’un programme de pour un point de recharge AC, 83 % pour un maintenance préventive régulière est un moyen point rapide (DC < 150 kW) et 77 % pour un point ultra-rapide (DC > 150 kW)42. La charge normale semble donc souffrir de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Un point de charge est considéré comme dispo-")
    thisalinea.textcontent.append("une zone avec un faible maillage. Certains opé-")
    thisalinea.textcontent.append("nible s’il n’est ni en maintenance ni hors-service.")
    thisalinea.textcontent.append("L’Avere-France41 indique dans son baromètre")
    thisalinea.textcontent.append("un taux de disponibilité de 84 % en moyenne")
    thisalinea.textcontent.append("rateurs ont remonté qu’un simple appel pour")
    thisalinea.textcontent.append("régler le problème à distance pourrait souvent")
    thisalinea.textcontent.append("suffire. La mise en place d’un programme de")
    thisalinea.textcontent.append("pour un point de recharge AC, 83 % pour un")
    thisalinea.textcontent.append("maintenance préventive régulière est un moyen")
    thisalinea.textcontent.append("point rapide (DC < 150 kW) et 77 % pour un point")
    thisalinea.textcontent.append("ultra-rapide (DC > 150 kW)42. La charge normale")
    thisalinea.textcontent.append("semble donc souffrir de moins de périodes d’in-")
    thisalinea.textcontent.append("de réduire les pannes et minimiser les délais")
    thisalinea.textcontent.append("de maintenance. Cela implique l’inspection")
    thisalinea.textcontent.append("régulière des bornes, le remplacement des")
    thisalinea.textcontent.append("disponibilité que la charge rapide. En revanche,")
    thisalinea.textcontent.append("pièces usées ou défectueuses, le nettoyage des")
    thisalinea.textcontent.append("elle présente des taux de sessions engagées")
    thisalinea.textcontent.append("connecteurs, etc.")
    thisalinea.textcontent.append("avec succès inférieurs à la moyenne nationale,")
    thisalinea.textcontent.append("comme l’indique l’AFIREV43 en 2022. Au-delà")
    thisalinea.textcontent.append("des technologies de recharge, des disparités")
    thisalinea.textcontent.append("La filière de la maintenance en mobilité élec-")
    thisalinea.textcontent.append("trique est en pleine croissance, et doit être")
    thisalinea.textcontent.append("fortes peuvent aussi être présentes entre les")
    thisalinea.textcontent.append("couplée à une montée en compétences. La")
    thisalinea.textcontent.append("régions. Par exemple, les taux moyens de succès")
    thisalinea.textcontent.append("disponibilité d’un support technique réactif et")
    thisalinea.textcontent.append("d’une session de recharge peuvent varier de")
    thisalinea.textcontent.append("83,7 % en Occitanie à 60,7 % en Normandie43.")
    thisalinea.textcontent.append("compétent aura un impact significatif sur les")
    thisalinea.textcontent.append("délais de maintenance. L’utilisation des données")
    thisalinea.textcontent.append("provenant des bornes pour détecter rapide-")
    thisalinea.textcontent.append("La maintenance apparaît comme le sujet")
    thisalinea.textcontent.append("ment les pannes ou les problèmes techniques")
    thisalinea.textcontent.append("clé derrière ces taux de disponibilité et un")
    thisalinea.textcontent.append("en temps réel est aussi un facteur clé dans")
    thisalinea.textcontent.append("certain nombre d’améliorations ont besoin")
    thisalinea.textcontent.append("l’amélioration de la durée d’indisponibilité. Par")
    thisalinea.textcontent.append("d’être apportées. Tout d’abord, l’urgence de")
    thisalinea.textcontent.append("ailleurs, le marché des véhicules électriques bas-")
    thisalinea.textcontent.append("la maintenance peut être différente selon si le")
    thisalinea.textcontent.append("cule des « early adopters » à des utilisateurs plus")
    thisalinea.textcontent.append("point de charge est sur une autoroute, et plus")
    thisalinea.textcontent.append("sensibles à des dysfonctionnements, d’où le")
    thisalinea.textcontent.append("précisément une station avec plusieurs autres")
    thisalinea.textcontent.append("besoin accru d’un service de qualité afin que la")
    thisalinea.textcontent.append("points, ou dans une zone rurale où il peut ne")
    thisalinea.textcontent.append("transition vers l’électrique continue d’accélérer.")
    thisalinea.textcontent.append("pas y avoir d’autres points à proximité. C’est")
    thisalinea.textcontent.append("ainsi qu’un meilleur diagnostic de la nature")
    thisalinea.textcontent.append("des pannes semble pertinent afin de réduire")
    thisalinea.textcontent.append("au maximum les délais, et d’autant plus dans")
    thisalinea.textcontent.append("Mais de manière générale, des gains au niveau")
    thisalinea.textcontent.append("des indicateurs de qualité sont déjà visibles à")
    thisalinea.textcontent.append("l’échelle nationale par rapport aux résultats de")
    thisalinea.textcontent.append("l’observatoire de l’AFIREV de 202143.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.3.4. Volatilité des prix de l’énergie"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 147
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "La volatilité des prix de l’énergie en Europe de tarification dynamique, où les prix de la constitue un défi majeur pour la constitution recharge varient en fonction des prix de l’élec- d’un modèle d’affaires solide pour les bornes de tricité. De cette manière, les gestionnaires de recharge publiques. Les fluctuations des prix de bornes de recharge peuvent répercuter les l’énergie ont un impact significatif sur les coûts variations des coûts d’énergie sur les utilisateurs, d’exploitation, ce qui rend difficile la prévision tout en maintenant une certaine compétitivité des revenus et la rentabilité à long terme de par rapport aux autres "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("La volatilité des prix de l’énergie en Europe")
    thisalinea.textcontent.append("de tarification dynamique, où les prix de la")
    thisalinea.textcontent.append("constitue un défi majeur pour la constitution")
    thisalinea.textcontent.append("recharge varient en fonction des prix de l’élec-")
    thisalinea.textcontent.append("d’un modèle d’affaires solide pour les bornes de")
    thisalinea.textcontent.append("tricité. De cette manière, les gestionnaires de")
    thisalinea.textcontent.append("recharge publiques. Les fluctuations des prix de")
    thisalinea.textcontent.append("bornes de recharge peuvent répercuter les")
    thisalinea.textcontent.append("l’énergie ont un impact significatif sur les coûts")
    thisalinea.textcontent.append("variations des coûts d’énergie sur les utilisateurs,")
    thisalinea.textcontent.append("d’exploitation, ce qui rend difficile la prévision")
    thisalinea.textcontent.append("tout en maintenant une certaine compétitivité")
    thisalinea.textcontent.append("des revenus et la rentabilité à long terme de")
    thisalinea.textcontent.append("par rapport aux autres options de carburant.")
    thisalinea.textcontent.append("ces infrastructures. Les opérateurs de bornes")
    thisalinea.textcontent.append("de recharge doivent constamment s’adapter")
    thisalinea.textcontent.append("Cependant, la variabilité des prix de l’énergie")
    thisalinea.textcontent.append("aux fluctuations des prix de l’électricité, ce qui")
    thisalinea.textcontent.append("peut entraîner une incertitude pour les utili-")
    thisalinea.textcontent.append("peut entraîner des difficultés pour équilibrer")
    thisalinea.textcontent.append("sateurs de bornes de recharge publiques. Les")
    thisalinea.textcontent.append("les coûts d’exploitation et les revenus générés.")
    thisalinea.textcontent.append("conducteurs de véhicules électriques peuvent")
    thisalinea.textcontent.append("hésiter à passer à l’électrique si les prix sont")
    thisalinea.textcontent.append("Pour surmonter ces défis, les opérateurs de")
    thisalinea.textcontent.append("perçus comme trop élevés ou imprévisibles.")
    thisalinea.textcontent.append("bornes de recharge peuvent a minima négocier")
    thisalinea.textcontent.append("Cela peut à terme compromettre la demande,")
    thisalinea.textcontent.append("des contrats à prix fixes avec leurs fournisseurs")
    thisalinea.textcontent.append("d’autant plus dans un contexte post-crise de")
    thisalinea.textcontent.append("d’électricité, voire passer directement par des")
    thisalinea.textcontent.append("CPPA44. Des stratégies de flexibilité s’envisagent")
    thisalinea.textcontent.append("également ; cela peut inclure des mécanismes")
    thisalinea.textcontent.append("l’énergie de l’hiver 2022, qui a connu une forte")
    thisalinea.textcontent.append("médiatisation et a tourné l’attention vers la")
    thisalinea.textcontent.append("volatilité des prix de l’électricité.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.4. Obstacles à l’achat de véhicules électriques liés à la recharge"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 148
    thisalinea.parentID = 115
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Le parcours utilisateur d’une borne de recharge connecteur Combo CSS (Combined Charging électrique peut s’avérer complexe. Ce processus System) ou le connecteur CHAdeMO. est confronté à divers défis qui peuvent rendre la recharge déroutante, frustrante et peu pra- Cette diversité de normes peut rendre complexe tique pour les utilisateurs. Les systèmes de l’interopérabilité entre les bornes de recharge recharge divers et les systèmes de paiement et les véhicules électriques. Les utilisateurs fragmentés contribuent à créer une expérience doivent s’assurer d’avoir le bon type de connec- utilisateur complexe, en particulier pour les nouveaux usagers. teur ou utiliser un adaptateur approprié pour "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.4.1. Complexité du parcours de recharge"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 149
    thisalinea.parentID = 148
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Le parcours utilisateur d’une borne de recharge connecteur Combo CSS (Combined Charging électrique peut s’avérer complexe. Ce processus System) ou le connecteur CHAdeMO. est confronté à divers défis qui peuvent rendre la recharge déroutante, frustrante et peu pra- Cette diversité de normes peut rendre complexe tique pour les utilisateurs. Les systèmes de l’interopérabilité entre les bornes de recharge recharge divers et les systèmes de paiement et les véhicules électriques. Les utilisateurs fragmentés contribuent à créer une expérience doivent s’assurer d’avoir le bon type de connec- utilisateur complexe, en particulier pour les nouveaux usagers. teur ou utiliser un adaptateur approprié pour "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Le parcours utilisateur d’une borne de recharge")
    thisalinea.textcontent.append("connecteur Combo CSS (Combined Charging")
    thisalinea.textcontent.append("électrique peut s’avérer complexe. Ce processus")
    thisalinea.textcontent.append("System) ou le connecteur CHAdeMO.")
    thisalinea.textcontent.append("est confronté à divers défis qui peuvent rendre")
    thisalinea.textcontent.append("la recharge déroutante, frustrante et peu pra-")
    thisalinea.textcontent.append("Cette diversité de normes peut rendre complexe")
    thisalinea.textcontent.append("tique pour les utilisateurs. Les systèmes de")
    thisalinea.textcontent.append("l’interopérabilité entre les bornes de recharge")
    thisalinea.textcontent.append("recharge divers et les systèmes de paiement")
    thisalinea.textcontent.append("et les véhicules électriques. Les utilisateurs")
    thisalinea.textcontent.append("fragmentés contribuent à créer une expérience")
    thisalinea.textcontent.append("doivent s’assurer d’avoir le bon type de connec-")
    thisalinea.textcontent.append("utilisateur complexe, en particulier pour les")
    thisalinea.textcontent.append("nouveaux usagers.")
    thisalinea.textcontent.append("teur ou utiliser un adaptateur approprié pour")
    thisalinea.textcontent.append("se connecter à une borne spécifique. De plus,")
    thisalinea.textcontent.append("certains véhicules électriques sont compatibles")
    thisalinea.textcontent.append("Avec la multiplication des fabricants de véhi-")
    thisalinea.textcontent.append("avec différents niveaux de puissance de charge,")
    thisalinea.textcontent.append("cules électriques, il existe différents types de")
    thisalinea.textcontent.append("ce qui nécessite une attention particulière pour")
    thisalinea.textcontent.append("prises, de connecteurs et de protocoles de com-")
    thisalinea.textcontent.append("choisir la borne de recharge offrant la puissance")
    thisalinea.textcontent.append("munication utilisés pour la recharge. Même si le")
    thisalinea.textcontent.append("adaptée à leur véhicule.")
    thisalinea.textcontent.append("connecteur type 2 (Mennekes) triphasé tend à")
    thisalinea.textcontent.append("se généraliser, certains véhicules et bornes uti-")
    thisalinea.textcontent.append("Enfin, la tension de recharge admise par les")
    thisalinea.textcontent.append("lisent encore les connecteurs de type 1 (J1772).")
    thisalinea.textcontent.append("véhicules électriques s’oriente vers du 800 V,")
    thisalinea.textcontent.append("et remplace progressivement les batteries en")
    thisalinea.textcontent.append("De plus, il existe également des normes spé-")
    thisalinea.textcontent.append("400 V. Les 800 V permettent une recharge plus")
    thisalinea.textcontent.append("cifiques pour la recharge rapide, telles que le")
    thisalinea.textcontent.append("rapide sur les bornes compatibles ; elles restent")
    thisalinea.textcontent.append("fonctionnelles quand branchées sur des bornes")
    thisalinea.textcontent.append("plus que cette information sur les bornes n’est")
    thisalinea.textcontent.append("400 V, mais la recharge est significativement")
    thisalinea.textcontent.append("pas facilement accessible (pas de remontée en")
    thisalinea.textcontent.append("plus lente. Cela peut conduire à de la confusion")
    thisalinea.textcontent.append("open data ou sur les applications de planifica-")
    thisalinea.textcontent.append("supplémentaire pour les utilisateurs, d’autant")
    thisalinea.textcontent.append("tion d’itinéraire).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.4.2. Opacité de la tarification et prix de la recharge"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 150
    thisalinea.parentID = 148
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "À l’heure actuelle, une certaine diversité dans les Pour répondre à ces critiques, la réglementation modes de tarification des bornes est présente européenne AFIR précisera la tarification et les et complexifie l’expérience des automobilistes. modes de paiement minimaux : Un manque de transparence est bien souvent remonté de la part des utilisateurs, avec des tarification à la minute en plus pour découra- ger les stationnements trop longs. tarifaire, il est difficile d’avoir une vue précise de l’ensemble des prix des bornes publiques et de ■ Possibilité de payer par carte bancaire sur tarifs qui sont très variables selon la technologie "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("À l’heure actuelle, une certaine diversité dans les")
    thisalinea.textcontent.append("Pour répondre à ces critiques, la réglementation")
    thisalinea.textcontent.append("modes de tarification des bornes est présente")
    thisalinea.textcontent.append("européenne AFIR précisera la tarification et les")
    thisalinea.textcontent.append("et complexifie l’expérience des automobilistes.")
    thisalinea.textcontent.append("modes de paiement minimaux :")
    thisalinea.textcontent.append("Un manque de transparence est bien souvent")
    thisalinea.textcontent.append("remonté de la part des utilisateurs, avec des")
    thisalinea.textcontent.append("tarification à la minute en plus pour découra-")
    thisalinea.textcontent.append("ger les stationnements trop longs.")
    thisalinea.textcontent.append("tarifaire, il est difficile d’avoir une vue précise de")
    thisalinea.textcontent.append("l’ensemble des prix des bornes publiques et de")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Possibilité de payer par carte bancaire sur ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 151
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Possibilité de payer par carte bancaire sur tarifs qui sont très variables selon la technologie toutes les nouvelles bornes > 50 kW (et rétrofit de la borne, l’opérateur, la période de recharge, obligatoire sur tout le réseau TEN-T). la présence d’un abonnement ou d’offres de recharge via un e-MSP. Les utilisateurs ont du "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Possibilité de payer par carte bancaire sur")
    thisalinea.textcontent.append("tarifs qui sont très variables selon la technologie")
    thisalinea.textcontent.append("toutes les nouvelles bornes > 50 kW (et rétrofit")
    thisalinea.textcontent.append("de la borne, l’opérateur, la période de recharge,")
    thisalinea.textcontent.append("obligatoire sur tout le réseau TEN-T).")
    thisalinea.textcontent.append("la présence d’un abonnement ou d’offres de")
    thisalinea.textcontent.append("recharge via un e-MSP. Les utilisateurs ont du")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Pour les bornes d’une puissance > 50 kW, le ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 152
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Pour les bornes d’une puissance > 50 kW, le mal à comprendre comment les tarifs sont prix doit être au kWh, avec la possibilité d’une déterminés et quels sont les frais supplémen- taires éventuels. Conséquence de cette diversité "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Pour les bornes d’une puissance > 50 kW, le")
    thisalinea.textcontent.append("mal à comprendre comment les tarifs sont")
    thisalinea.textcontent.append("prix doit être au kWh, avec la possibilité d’une")
    thisalinea.textcontent.append("déterminés et quels sont les frais supplémen-")
    thisalinea.textcontent.append("taires éventuels. Conséquence de cette diversité")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le prix doit être indiqué de manière trans- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 153
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Le prix doit être indiqué de manière trans- déduire une valeur moyenne à l’échelle du pays. parente, en indiquant, dans l’ordre, le prix au kWh, le prix par minute, le prix par session et Une certaine confusion est donc présente tout autre élément de tarification. parmi les utilisateurs de bornes de recharge qui peuvent difficilement prévoir combien ils vont payer en finalité. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le prix doit être indiqué de manière trans-")
    thisalinea.textcontent.append("déduire une valeur moyenne à l’échelle du pays.")
    thisalinea.textcontent.append("parente, en indiquant, dans l’ordre, le prix au")
    thisalinea.textcontent.append("kWh, le prix par minute, le prix par session et")
    thisalinea.textcontent.append("Une certaine confusion est donc présente")
    thisalinea.textcontent.append("tout autre élément de tarification.")
    thisalinea.textcontent.append("parmi les utilisateurs de bornes de recharge")
    thisalinea.textcontent.append("qui peuvent difficilement prévoir combien ils")
    thisalinea.textcontent.append("vont payer en finalité.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.4.3. Anxiété à la recharge"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 154
    thisalinea.parentID = 148
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "La recharge électrique est source d’anxiété pour À mesure que le véhicule électrique se démo- de nombreux utilisateurs ; cela constitue un frein cratisera, une autre anxiété prendra le relais, à l’achat très significatif, que le déploiement celle liée aux files d’attente pour se recharger ; massif des IRVE tente de résoudre. Les utilisa- ce phénomène, pour l’instant rarement observé, teurs souhaitent qu’un maillage serré quadrille pourrait particulièrement se manifester sur les le territoire finement, pour être rassurés quant à grands axes routiers lors des grands départs en la possibilité de se recharger et ne pas tomber vacances, pendant la "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("La recharge électrique est source d’anxiété pour")
    thisalinea.textcontent.append("À mesure que le véhicule électrique se démo-")
    thisalinea.textcontent.append("de nombreux utilisateurs ; cela constitue un frein")
    thisalinea.textcontent.append("cratisera, une autre anxiété prendra le relais,")
    thisalinea.textcontent.append("à l’achat très significatif, que le déploiement")
    thisalinea.textcontent.append("celle liée aux files d’attente pour se recharger ;")
    thisalinea.textcontent.append("massif des IRVE tente de résoudre. Les utilisa-")
    thisalinea.textcontent.append("ce phénomène, pour l’instant rarement observé,")
    thisalinea.textcontent.append("teurs souhaitent qu’un maillage serré quadrille")
    thisalinea.textcontent.append("pourrait particulièrement se manifester sur les")
    thisalinea.textcontent.append("le territoire finement, pour être rassurés quant à")
    thisalinea.textcontent.append("grands axes routiers lors des grands départs en")
    thisalinea.textcontent.append("la possibilité de se recharger et ne pas tomber")
    thisalinea.textcontent.append("vacances, pendant la période estivale.")
    thisalinea.textcontent.append("en « panne sèche ». La possibilité qu’une borne")
    thisalinea.textcontent.append("indiquée comme disponible soit en réalité indis-")
    thisalinea.textcontent.append("ponible (occupée, en maintenance, non-fonc-")
    thisalinea.textcontent.append("tionnelle) participe de cette anxiété.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.4.4. Indisponibilité de recharge de proximité abordable"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 155
    thisalinea.parentID = 148
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Certains foyers possèdent un véhicule mais pas emplacement dans un jardin, place réservée en de solution de stationnement privé (garage, copropriété). Puisque leur véhicule stationne sur la voirie ou sur parking public, ils n’ont donc pas recharge (si elle est effectuée uniquement sur accès facilement à la recharge ou bien n’ont pas borne DC par exemple) peut devenir prohibitif. la possibilité de se recharger à un prix modéré, qu’il est possible d’obtenir via une installation En particulier dans les centres urbains, cela peut de borne à domicile. Certaines communes pra- engendrer une moindre adoption du véhicule tiquent des tarifs nocturnes "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Certains foyers possèdent un véhicule mais pas")
    thisalinea.textcontent.append("emplacement dans un jardin, place réservée en")
    thisalinea.textcontent.append("de solution de stationnement privé (garage,")
    thisalinea.textcontent.append("copropriété). Puisque leur véhicule stationne sur")
    thisalinea.textcontent.append("la voirie ou sur parking public, ils n’ont donc pas")
    thisalinea.textcontent.append("recharge (si elle est effectuée uniquement sur")
    thisalinea.textcontent.append("accès facilement à la recharge ou bien n’ont pas")
    thisalinea.textcontent.append("borne DC par exemple) peut devenir prohibitif.")
    thisalinea.textcontent.append("la possibilité de se recharger à un prix modéré,")
    thisalinea.textcontent.append("qu’il est possible d’obtenir via une installation")
    thisalinea.textcontent.append("En particulier dans les centres urbains, cela peut")
    thisalinea.textcontent.append("de borne à domicile. Certaines communes pra-")
    thisalinea.textcontent.append("engendrer une moindre adoption du véhicule")
    thisalinea.textcontent.append("tiquent des tarifs nocturnes plus avantageux,")
    thisalinea.textcontent.append("électrique pour des raisons économiques ou")
    thisalinea.textcontent.append("mais lorsque ce n’est pas le cas, le coût de la")
    thisalinea.textcontent.append("de praticité de la recharge.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "4. Mesures-clés pour réussir le déploiement d’une infrastructure de recharge publique"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 156
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Sur les grands axes routiers, les possibilités Le défi des jours de pointes (grands départs) d’emplacement pour l’installation de bornes de sera d’éviter la saturation des aires sur grands recharge sont limitées. Les aires de service et les axes, qui ne sont aujourd’hui pas dimensionnées aires de repos constituent les seules options qui pour accueillir un stock de véhicules patientant ne nécessitent pas de création d’infrastructures pour se recharger ; de plus, les zones de parking supplémentaires d’entrée et de sortie de grands axes. Dans un contexte d’objectif ZAN (zéro sur aires ne sont généralement pas traversantes, ce qui engendre "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Sur les grands axes routiers, les possibilités")
    thisalinea.textcontent.append("Le défi des jours de pointes (grands départs)")
    thisalinea.textcontent.append("d’emplacement pour l’installation de bornes de")
    thisalinea.textcontent.append("sera d’éviter la saturation des aires sur grands")
    thisalinea.textcontent.append("recharge sont limitées. Les aires de service et les")
    thisalinea.textcontent.append("axes, qui ne sont aujourd’hui pas dimensionnées")
    thisalinea.textcontent.append("aires de repos constituent les seules options qui")
    thisalinea.textcontent.append("pour accueillir un stock de véhicules patientant")
    thisalinea.textcontent.append("ne nécessitent pas de création d’infrastructures")
    thisalinea.textcontent.append("pour se recharger ; de plus, les zones de parking")
    thisalinea.textcontent.append("supplémentaires d’entrée et de sortie de grands")
    thisalinea.textcontent.append("axes. Dans un contexte d’objectif ZAN (zéro")
    thisalinea.textcontent.append("sur aires ne sont généralement pas traversantes,")
    thisalinea.textcontent.append("ce qui engendre des manœuvres et ralentit le")
    thisalinea.textcontent.append("artificialisation nette) pour 2050, il est d’autant")
    thisalinea.textcontent.append("temps total nécessaire pour se recharger. Éviter")
    thisalinea.textcontent.append("plus pertinent de s’en tenir aux aires et zones")
    thisalinea.textcontent.append("la saturation représentera non seulement un")
    thisalinea.textcontent.append("déjà artificialisées.")
    thisalinea.textcontent.append("enjeu de sécurité (file d’attente qui pourrait")
    thisalinea.textcontent.append("déborder sur la voie principale), mais aussi")
    thisalinea.textcontent.append("Ainsi, la réponse aux besoins en recharge sur")
    thisalinea.textcontent.append("d’acceptabilité pour les usagers, qui pourraient")
    thisalinea.textcontent.append("autoroute se fera principalement sur ces aires,")
    thisalinea.textcontent.append("le cas échéant être découragés d’acquérir un")
    thisalinea.textcontent.append("et les raccordements au réseau de distribu-")
    thisalinea.textcontent.append("véhicule électrique à batterie.")
    thisalinea.textcontent.append("tion devront pouvoir y répondre. Alors qu’une")
    thisalinea.textcontent.append("deuxième vague de déploiement apparaît")
    thisalinea.textcontent.append("La pointe devra donc être traitée par une réduc-")
    thisalinea.textcontent.append("nécessaire dans les prochaines années sur les")
    thisalinea.textcontent.append("tion en amont du flux (itinéraires alternatifs,")
    thisalinea.textcontent.append("aires de service, une optimisation planifiée du")
    thisalinea.textcontent.append("communication sur le trafic) et en aval par le")
    thisalinea.textcontent.append("déploiement pourrait limiter les coûts pour")
    thisalinea.textcontent.append("déploiement de solutions de recharge ad hoc.")
    thisalinea.textcontent.append("toutes les parties prenantes et s’insérer dans")
    thisalinea.textcontent.append("une nécessaire logique de sobriété tout en")
    thisalinea.textcontent.append("fluidifiant les installations.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4.1. Mesures-clés « Grands axes routiers »"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 157
    thisalinea.parentID = 156
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Impact : réduction des coûts de raccordement, amélioration de la rentabilité, accélération des déploiements KPI : coûts de raccordement évités et durée d’installation (scénario sans anticipation – scé- Parties prenantes : État, collectivités, SCA, GRDE nario anticipé) Levier(s) : décision politique et législative, modification(s) réglementaire(s) Une autorité publique dédiée pourrait être L’autorité publique pourra faire appel aux créée (cf. mesures transverses) et réaliser ou Gestionnaires de réseau de distribution d’éner- commander une estimation aire par aire des gie (GRDE) pour prendre en compte des esti- raccordements nécessaires pour 2035 sur les mations de coût de raccordement. grands axes à l’échelle "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.1.1. Anticipation des besoins en raccordements"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 158
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Impact : réduction des coûts de raccordement, amélioration de la rentabilité, accélération des déploiements KPI : coûts de raccordement évités et durée d’installation (scénario sans anticipation – scé- Parties prenantes : État, collectivités, SCA, GRDE nario anticipé) Levier(s) : décision politique et législative, modification(s) réglementaire(s) Une autorité publique dédiée pourrait être L’autorité publique pourra faire appel aux créée (cf. mesures transverses) et réaliser ou Gestionnaires de réseau de distribution d’éner- commander une estimation aire par aire des gie (GRDE) pour prendre en compte des esti- raccordements nécessaires pour 2035 sur les mations de coût de raccordement. grands axes à l’échelle "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : réduction des coûts de raccordement, amélioration de la rentabilité,")
    thisalinea.textcontent.append("accélération des déploiements")
    thisalinea.textcontent.append("KPI : coûts de raccordement évités et durée")
    thisalinea.textcontent.append("d’installation (scénario sans anticipation – scé-")
    thisalinea.textcontent.append("Parties  prenantes : État, collectivités, SCA,")
    thisalinea.textcontent.append("GRDE")
    thisalinea.textcontent.append("nario anticipé)")
    thisalinea.textcontent.append("Levier(s) : décision politique et législative, modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Une autorité publique dédiée pourrait être")
    thisalinea.textcontent.append("L’autorité publique pourra faire appel aux")
    thisalinea.textcontent.append("créée (cf. mesures transverses) et réaliser ou")
    thisalinea.textcontent.append("Gestionnaires de réseau de distribution d’éner-")
    thisalinea.textcontent.append("commander une estimation aire par aire des")
    thisalinea.textcontent.append("gie (GRDE) pour prendre en compte des esti-")
    thisalinea.textcontent.append("raccordements nécessaires pour 2035 sur les")
    thisalinea.textcontent.append("mations de coût de raccordement.")
    thisalinea.textcontent.append("grands axes à l’échelle nationale, en fonction")
    thisalinea.textcontent.append("des besoins identifiés.")
    thisalinea.textcontent.append("Une fois l’estimation réalisée, l’autorité publique")
    thisalinea.textcontent.append("dédiée devrait exprimer les besoins de raccor-")
    thisalinea.textcontent.append("Cette estimation devrait inclure les aires de")
    thisalinea.textcontent.append("dements sur chacune des aires, tels que dimen-")
    thisalinea.textcontent.append("repos ; les situations et coûts de raccorde-")
    thisalinea.textcontent.append("sionnés dans l’estimation ; puis les demandes")
    thisalinea.textcontent.append("ment sur les aires de repos sont disparates")
    thisalinea.textcontent.append("effectives de raccordement seraient émises")
    thisalinea.textcontent.append("et dépendent de la proximité avec un poste.")
    thisalinea.textcontent.append("par les acteurs pertinents (collectivités pour")
    thisalinea.textcontent.append("Équiper les aires de repos permettrait un")
    thisalinea.textcontent.append("le réseau non concédé, SCA pour le réseau")
    thisalinea.textcontent.append("maillage plus serré sur les grands axes et un")
    thisalinea.textcontent.append("concédé), sans déroger aux prescriptions de")
    thisalinea.textcontent.append("allégement des aires de service (qui serviront")
    thisalinea.textcontent.append("puissance demandées par l’autorité publique.")
    thisalinea.textcontent.append("la majorité de la demande en volume). Un équi-")
    thisalinea.textcontent.append("libre doit cependant être trouvé pour conserver")
    thisalinea.textcontent.append("Puis, à mesure des appels d’offres des SCA et")
    thisalinea.textcontent.append("leurs avantages (proximité avec la nature, moins")
    thisalinea.textcontent.append("de l’État auprès des opérateurs, un mécanisme")
    thisalinea.textcontent.append("artificialisées) et les besoins en foncier bétonné")
    thisalinea.textcontent.append("de répartition des coûts de raccordement (ex :")
    thisalinea.textcontent.append("pour l’installation d’IRVE.")
    thisalinea.textcontent.append("quote-part) serait appliqué à ces derniers.")
    thisalinea.textcontent.append("L’estimation devrait également prendre en")
    thisalinea.textcontent.append("Cette mesure permettrait l’accélération du")
    thisalinea.textcontent.append("compte les raccordements dits « pendulaires »")
    thisalinea.textcontent.append("déploiement et éviterait la confrontation avec")
    thisalinea.textcontent.append("de part et d’autre d’un grand axe, sur deux aires")
    thisalinea.textcontent.append("un mur d’investissements ; elle implique cepen-")
    thisalinea.textcontent.append("face à face. Leur pic de charge étant générale-")
    thisalinea.textcontent.append("dant un équilibre à trouver entre les périmètres")
    thisalinea.textcontent.append("ment en alternance, cela permettrait de mutua-")
    thisalinea.textcontent.append("des différentes parties prenantes, et un cadre")
    thisalinea.textcontent.append("liser le raccordement et de réduire les coûts.")
    thisalinea.textcontent.append("légal adapté.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.1.2. Allongement des durées de contrats de sous-concession"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 159
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Impact : amélioration de la rentabilité (TRI) des projets et de l’attractivité des sous-concessions KPI : nombre de bornes proposées par aires Parties prenantes : État Levier(s) : modification(s) réglementaire(s) Les contrats de sous-concession sur les auto- routes concédées ne peuvent dépasser 15 ans d’exploitation devrait être considérée. Hors réseau concédé, cette limitation n’a pas cours, et à l’heure actuelle (Article R122-42 du Code de une durée contractuelle supérieure permettrait la voirie coutière). Pour les IRVE, des investis- de réduire les mécanismes de soutien néces- sements significatifs peuvent être nécessaires saires à la rentabilité de l’investissement. et une augmentation de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : amélioration de la rentabilité (TRI) des projets et de l’attractivité des sous-concessions")
    thisalinea.textcontent.append("KPI : nombre de bornes proposées par aires Parties prenantes : État")
    thisalinea.textcontent.append("Levier(s) : modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Les contrats de sous-concession sur les auto-")
    thisalinea.textcontent.append("routes concédées ne peuvent dépasser 15 ans")
    thisalinea.textcontent.append("d’exploitation devrait être considérée. Hors")
    thisalinea.textcontent.append("réseau concédé, cette limitation n’a pas cours, et")
    thisalinea.textcontent.append("à l’heure actuelle (Article R122-42 du Code de")
    thisalinea.textcontent.append("une durée contractuelle supérieure permettrait")
    thisalinea.textcontent.append("la voirie coutière). Pour les IRVE, des investis-")
    thisalinea.textcontent.append("de réduire les mécanismes de soutien néces-")
    thisalinea.textcontent.append("sements significatifs peuvent être nécessaires")
    thisalinea.textcontent.append("saires à la rentabilité de l’investissement.")
    thisalinea.textcontent.append("et une augmentation de la durée des contrats")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.1.3. Réduction des pointes de trafic en amont"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 160
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Impact : réduction de l’intensité des pics, amélioration de l’expérience usager, dimensionnement moins coûteux du réseau KPI : trafic évité, durée moyenne et max d’at- tente avant recharge Parties prenantes : constructeurs automobiles, e-MSP, État, SCA Levier(s) : modification(s) réglementaire(s), communication et accompagnement du changement Pour limiter le stock de voitures électriques au sens large, et impose la proposition d’un patientant pour se recharger lors des week- ends de grands départs, il est concevable que des itinéraires alternatifs soient employés pour itinéraire alternatif plus vertueux pour l’environ- nement (moins émetteur de CO2, notamment via une vitesse réduite). Dans cet esprit, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : réduction de l’intensité des pics, amélioration de l’expérience usager, dimensionnement")
    thisalinea.textcontent.append("moins coûteux du réseau")
    thisalinea.textcontent.append("KPI : trafic évité, durée moyenne et max d’at-")
    thisalinea.textcontent.append("tente avant recharge")
    thisalinea.textcontent.append("Parties prenantes : constructeurs automobiles,")
    thisalinea.textcontent.append("e-MSP, État, SCA")
    thisalinea.textcontent.append("Levier(s) : modification(s) réglementaire(s), communication et accompagnement du changement")
    thisalinea.textcontent.append("Pour limiter le stock de voitures électriques")
    thisalinea.textcontent.append("au sens large, et impose la proposition d’un")
    thisalinea.textcontent.append("patientant pour se recharger lors des week-")
    thisalinea.textcontent.append("ends de grands départs, il est concevable que")
    thisalinea.textcontent.append("des itinéraires alternatifs soient employés pour")
    thisalinea.textcontent.append("itinéraire alternatif plus vertueux pour l’environ-")
    thisalinea.textcontent.append("nement (moins émetteur de CO2, notamment")
    thisalinea.textcontent.append("via une vitesse réduite). Dans cet esprit, les ERP")
    thisalinea.textcontent.append("éviter l’attente, ou que la recharge sur auto-")
    thisalinea.textcontent.append("pourraient également être soumis à certaines")
    thisalinea.textcontent.append("route soit mieux répartie. Ainsi, le rôle des ERP")
    thisalinea.textcontent.append("obligations de propositions d’itinéraires et de")
    thisalinea.textcontent.append("(Electric Route Planner) sera déterminant pour")
    thisalinea.textcontent.append("recharge, dans le but d’alléger la charge sur le")
    thisalinea.textcontent.append("moduler les flux sur les grands axes ; ils pourront")
    thisalinea.textcontent.append("réseau et d’éviter les files d’attente aux bornes.")
    thisalinea.textcontent.append("ainsi proposer des itinéraires hors autoroute, des")
    thisalinea.textcontent.append("arrêts avec des points d’intérêt (type « village")
    thisalinea.textcontent.append("étape »), ou conseiller des heures optimales de")
    thisalinea.textcontent.append("Une tarification dynamique de la recharge sur")
    thisalinea.textcontent.append("autoroute en fonction du trafic pourrait être")
    thisalinea.textcontent.append("départ ou de recharge.")
    thisalinea.textcontent.append("étudiée pour inciter les usagers à voyager à des")
    thisalinea.textcontent.append("horaires moins congestionnés. Cependant, le")
    thisalinea.textcontent.append("Pour l’instant, tous les véhicules électriques")
    thisalinea.textcontent.append("risque de non-acceptation de la mesure est fort,")
    thisalinea.textcontent.append("n’intègrent pas forcément d’ERP embarqué, et")
    thisalinea.textcontent.append("et si une telle tarification était mise en place,")
    thisalinea.textcontent.append("beaucoup d’utilisateurs sont dépendants d’ap-")
    thisalinea.textcontent.append("elle devrait être régulée pour éviter un effet")
    thisalinea.textcontent.append("plications tierces ; mais celles-ci n’ont pas accès")
    thisalinea.textcontent.append("d’emballement sur les prix lors des pointes. Des")
    thisalinea.textcontent.append("aux données de conduite qu’ont les systèmes")
    thisalinea.textcontent.append("baisses de prix pour la recharge hors autoroute")
    thisalinea.textcontent.append("embarqués. Les ERP auront également besoin")
    thisalinea.textcontent.append("les jours de pointe pourraient contourner ce")
    thisalinea.textcontent.append("d’avoir accès à des données fiables en temps")
    thisalinea.textcontent.append("problème d’acceptabilité.")
    thisalinea.textcontent.append("réel sur l’ensemble des points de charge du")
    thisalinea.textcontent.append("réseau, en particulier leur bon état de marche")
    thisalinea.textcontent.append("Le report modal vers d’autres moyens de")
    thisalinea.textcontent.append("et s’ils sont en cours d’utilisation. Le parcours de")
    thisalinea.textcontent.append("transport décarbonés (développement du rail,")
    thisalinea.textcontent.append("l’usager pourra être adapté en conséquence :")
    thisalinea.textcontent.append("relance des trains de nuit) pour la grande itiné-")
    thisalinea.textcontent.append("recharge en début de trajet plutôt qu’à la fin,")
    thisalinea.textcontent.append("rance sera également un facteur de réduction")
    thisalinea.textcontent.append("aire de service moins fréquentée ou mieux")
    thisalinea.textcontent.append("dimensionnée, etc. La recommandation de")
    thisalinea.textcontent.append("sortir des grands axes devra être modulée")
    thisalinea.textcontent.append("des pointes, et devra être encouragé. D’après")
    thisalinea.textcontent.append("l’étude RTE-IPSOS de 202345, il existe bien des")
    thisalinea.textcontent.append("« marges de manœuvre possibles mais actuelle-")
    thisalinea.textcontent.append("en fonction du trafic et des capacités des")
    thisalinea.textcontent.append("ment contraintes » pour des changements des")
    thisalinea.textcontent.append("échangeurs, pour éviter des saturations à ces")
    thisalinea.textcontent.append("habitudes de la population (report modal en")
    thisalinea.textcontent.append("niveaux-là également (remontée de file sur les")
    thisalinea.textcontent.append("tête, suivi de l’optimisation des déplacements")
    thisalinea.textcontent.append("diffuseurs et échangeurs, source d’accidents).")
    thisalinea.textcontent.append("en voiture).")
    thisalinea.textcontent.append("Le Décret n° 2022-1119 du 3 août 2022 relatif aux")
    thisalinea.textcontent.append("Enfin, l’étalement de ces grands départs sur plu-")
    thisalinea.textcontent.append("services numériques d’assistance aux dépla-")
    thisalinea.textcontent.append("sieurs jours constitue une solution envisageable,")
    thisalinea.textcontent.append("cements a constitué une première mesure de")
    thisalinea.textcontent.append("qui nécessiterait toutefois des changements")
    thisalinea.textcontent.append("l’État pour réguler les planificateurs d’itinéraires")
    thisalinea.textcontent.append("de société significatifs : sortie du modèle des")
    thisalinea.textcontent.append("locations du samedi au samedi, flexibilisation de")
    thisalinea.textcontent.append("la prise de congés, changement des vacances")
    thisalinea.textcontent.append("scolaires, etc.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.1.4. Absorption des pointes de trafic via des solutions ad hoc"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 161
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Impact : amélioration de l’expérience usager, dimensionnement moins coûteux du réseau KPI : durée moyenne et max d’attente avant recharge Parties prenantes : SCA, collectivités Levier(s) : expérimentation à conduire, soutien aux investissements à réaliser Pour gérer les pointes de trafic et éviter les encombrements dans et à l’entrée des aires de service lors des week-ends de grand départ, des utilitaire et de le déployer où le besoin se trouve46. Il est également envisageable de déployer rapidement une station de recharge solutions ad hoc ou « mobiles » pourront être de la taille d’une place de parking, surmontée déployées ponctuellement "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : amélioration de l’expérience usager, dimensionnement moins coûteux du réseau")
    thisalinea.textcontent.append("KPI : durée moyenne et max d’attente avant")
    thisalinea.textcontent.append("recharge")
    thisalinea.textcontent.append("Parties prenantes : SCA, collectivités")
    thisalinea.textcontent.append("Levier(s) : expérimentation à conduire, soutien aux investissements à réaliser")
    thisalinea.textcontent.append("Pour gérer les pointes de trafic et éviter les")
    thisalinea.textcontent.append("encombrements dans et à l’entrée des aires de")
    thisalinea.textcontent.append("service lors des week-ends de grand départ, des")
    thisalinea.textcontent.append("utilitaire et de le déployer où le besoin se")
    thisalinea.textcontent.append("trouve46. Il est également envisageable de")
    thisalinea.textcontent.append("déployer rapidement une station de recharge")
    thisalinea.textcontent.append("solutions ad hoc ou « mobiles » pourront être")
    thisalinea.textcontent.append("de la taille d’une place de parking, surmontée")
    thisalinea.textcontent.append("déployées ponctuellement pour mieux absorber")
    thisalinea.textcontent.append("le pic. Celles-ci se présenteraient sous la forme")
    thisalinea.textcontent.append("de panneaux solaires couplés à une batterie, et")
    thisalinea.textcontent.append("qui fonctionne hors réseau47.")
    thisalinea.textcontent.append("de stations de recharge mobiles, alimentées")
    thisalinea.textcontent.append("par une source d’énergie la plus décarbonée")
    thisalinea.textcontent.append("La question se pose cependant des capacités")
    thisalinea.textcontent.append("possible. Cette source pourrait être :")
    thisalinea.textcontent.append("solaires nécessaires pour alimenter une borne")
    thisalinea.textcontent.append("de recharge DC rapide ou ultra-rapide. Sur")
    thisalinea.textcontent.append("soire 100 kVA pour alimenter une station de")
    thisalinea.textcontent.append("recharge (2 bornes 120 kW DC et 1 borne double")
    thisalinea.textcontent.append("11 kW AC) 48. Cela représentait une surface")
    thisalinea.textcontent.append("importante sur l’aire.")
    thisalinea.textcontent.append("Enfin, l’amélioration des outils digitaux tels que")
    thisalinea.textcontent.append("de paiement participeront à la fluidité de la")
    thisalinea.textcontent.append("recharge, mais plutôt sur le moyen long terme.")
    thisalinea.textcontent.append("Par exemple, il est possible d’embarquer une")
    thisalinea.textcontent.append("batterie (déjà chargée) à bord d’un véhicule")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le réseau de distribution – si le raccordement ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 162
    thisalinea.parentID = 161
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Le réseau de distribution – si le raccordement l’aire de Trémentines A87, 75 kWc de panneaux a été surdimensionné par rapport aux besoins solaires ont été installés et couplés avec une actuels en anticipation des besoins futurs. batterie-container et un raccordement provi- "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le réseau de distribution – si le raccordement")
    thisalinea.textcontent.append("l’aire de Trémentines A87, 75 kWc de panneaux")
    thisalinea.textcontent.append("a été surdimensionné par rapport aux besoins")
    thisalinea.textcontent.append("solaires ont été installés et couplés avec une")
    thisalinea.textcontent.append("actuels en anticipation des besoins futurs.")
    thisalinea.textcontent.append("batterie-container et un raccordement provi-")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Des BESS (Systèmes de stockage d’énergie de ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 163
    thisalinea.parentID = 161
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Des BESS (Systèmes de stockage d’énergie de batterie) mobiles (pouvant atteindre la taille d’un conteneur), rechargées soit en amont sur le réseau, soit via du photovoltaïque sur site. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Des BESS (Systèmes de stockage d’énergie de")
    thisalinea.textcontent.append("batterie) mobiles (pouvant atteindre la taille")
    thisalinea.textcontent.append("d’un conteneur), rechargées soit en amont sur")
    thisalinea.textcontent.append("le réseau, soit via du photovoltaïque sur site.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Des générateurs sur site, fonctionnant avec ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 164
    thisalinea.parentID = 161
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Des générateurs sur site, fonctionnant avec la réservation de bornes en avance ou la facilité des carburants décarbonés (bio et électrocar- burants, hydrogène, etc.) ; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Des générateurs sur site, fonctionnant avec")
    thisalinea.textcontent.append("la réservation de bornes en avance ou la facilité")
    thisalinea.textcontent.append("des carburants décarbonés (bio et électrocar-")
    thisalinea.textcontent.append("burants, hydrogène, etc.) ;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.1.5. L’autoroute électrique"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 165
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Impact : réduction du nombre de bornes de recharge à installer pour la mobilité lourde, réduction des tailles de batterie à embarquer KPI : coûts bénéfices des différentes technologies après les projets pilotes Parties prenantes : SCA, collectivités, constructeurs Levier(s) : retour d’expérience sur les précédents AAP et décision politique Dans le processus de transition vers le tout La Suède a annoncé récemment la construc- électrique, un certain nombre d’innovations tion de 3 000 km de route électrique. Un pre- viendront potentiellement compléter les tech- nologies de véhicules à batterie avec recharge sur des bornes. C’est notamment le cas de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : réduction du nombre de bornes de recharge à installer pour la mobilité lourde, réduction")
    thisalinea.textcontent.append("des tailles de batterie à embarquer")
    thisalinea.textcontent.append("KPI : coûts bénéfices des différentes")
    thisalinea.textcontent.append("technologies après les projets pilotes")
    thisalinea.textcontent.append("Parties prenantes : SCA, collectivités,")
    thisalinea.textcontent.append("constructeurs")
    thisalinea.textcontent.append("Levier(s) : retour d’expérience sur les précédents AAP et décision politique")
    thisalinea.textcontent.append("Dans le processus de transition vers le tout")
    thisalinea.textcontent.append("La Suède a annoncé récemment la construc-")
    thisalinea.textcontent.append("électrique, un certain nombre d’innovations")
    thisalinea.textcontent.append("tion de 3 000 km de route électrique. Un pre-")
    thisalinea.textcontent.append("viendront potentiellement compléter les tech-")
    thisalinea.textcontent.append("nologies de véhicules à batterie avec recharge")
    thisalinea.textcontent.append("sur des bornes. C’est notamment le cas de")
    thisalinea.textcontent.append("mier tronçon de 20 km devrait être construit")
    thisalinea.textcontent.append("d’ici 2025 et destiné d’abord aux camions49.")
    thisalinea.textcontent.append("L’autoroute choisie est la route européenne E20,")
    thisalinea.textcontent.append("l’autoroute électrique, Electric Road System")
    thisalinea.textcontent.append("qui relie les hubs logistiques entre Hallsberg et")
    thisalinea.textcontent.append("ou ERS, qui vise à intégrer des fonctionnalités")
    thisalinea.textcontent.append("Örebro, situés au milieu des trois grandes villes")
    thisalinea.textcontent.append("de recharge électrique directement dans les")
    thisalinea.textcontent.append("du pays, Stockholm, Göteborg et Malmö.")
    thisalinea.textcontent.append("routes, permettant aux véhicules de se rechar-")
    thisalinea.textcontent.append("ger en mouvement. Il y a principalement trois")
    thisalinea.textcontent.append("types de solutions technologiques :")
    thisalinea.textcontent.append("De par les coûts importants associés à ces tech-")
    thisalinea.textcontent.append("nologies (~4 millions d’euros du kilomètre pour")
    thisalinea.textcontent.append("la route à induction d’après le groupe de travail")
    thisalinea.textcontent.append("sur le système des routes électriques50), les")
    thisalinea.textcontent.append("routes électriques semblent apparaître comme")
    thisalinea.textcontent.append("des véhicules électriques grâce à l’induction")
    thisalinea.textcontent.append("une solution pour un usage localisé autour des")
    thisalinea.textcontent.append("magnétique.")
    thisalinea.textcontent.append("principaux hubs et nécessiteront encore des")
    thisalinea.textcontent.append("mécanismes incitatifs pour les opérateurs. Ces")
    thisalinea.textcontent.append("sujet avant le déploiement des infrastructures")
    thisalinea.textcontent.append("de recharge pour les poids lourds, pour que le")
    thisalinea.textcontent.append("dimensionnement soit correct.")
    thisalinea.textcontent.append("de telles technologies, comme en Allemagne")
    thisalinea.textcontent.append("avec une dizaine de kilomètres équipée de")
    thisalinea.textcontent.append("BPI France a lancé un appel à projets « Mobilités")
    thisalinea.textcontent.append("caténaires pour les poids lourds, ou en Suède,")
    thisalinea.textcontent.append("routières automatisées, infrastructures de")
    thisalinea.textcontent.append("avec un tronçon de 2 kilomètres disposant de")
    thisalinea.textcontent.append("rails, et une route à induction de 1,6 kilomètre")
    thisalinea.textcontent.append("sur l’île de Gotland.")
    thisalinea.textcontent.append("services connectées et bas carbone », ouvert")
    thisalinea.textcontent.append("en 2021 et clôturé le 11 janvier 2023 51, dans")
    thisalinea.textcontent.append("le cadre du Programme d’investissement")
    thisalinea.textcontent.append("d’Avenir PIA4 – stratégie transport. Cet appel")
    thisalinea.textcontent.append("Une autre expérimentation va être menée sur")
    thisalinea.textcontent.append("à projet visait entre autres le développement")
    thisalinea.textcontent.append("une portion de l’A10, non loin de Saint-Arnoult")
    thisalinea.textcontent.append("de démonstrateurs ERS. Les 8 projets lauréats,")
    thisalinea.textcontent.append("issus de la 1re et 2e relèves de l’appel à projets,")
    thisalinea.textcontent.append("concernent des pilotes de services de transport")
    thisalinea.textcontent.append("en Yvelines ; les travaux vont démarrer en sep-")
    thisalinea.textcontent.append("tembre 202354. Des poids lourds électriques")
    thisalinea.textcontent.append("pourront se recharger en roulant sur l’autoroute")
    thisalinea.textcontent.append("automatisé de voyageurs (services réguliers, de")
    thisalinea.textcontent.append("grâce aux technologies de l’induction et du rail")
    thisalinea.textcontent.append("transports à la demande, ou rabattements vers")
    thisalinea.textcontent.append("des pôles multimodaux)52. Par ailleurs, d’après")
    thisalinea.textcontent.append("la presse53, un consortium public-privé, avec le")
    thisalinea.textcontent.append("soutien financier de BPI France serait en cours")
    thisalinea.textcontent.append("conductif.")
    thisalinea.textcontent.append("Au vu des considérations techniques et de la")
    thisalinea.textcontent.append("teneur des entretiens avec l’écosystème, la")
    thisalinea.textcontent.append("de constitution pour le lancement d’un projet")
    thisalinea.textcontent.append("présente étude a dimensionné la modélisation")
    thisalinea.textcontent.append("démonstrateur d’électrification de 2 km d’au-")
    thisalinea.textcontent.append("sans prendre en compte un déploiement d’une")
    thisalinea.textcontent.append("toroute dans le sud de l’Alsace. Ce projet n’est")
    thisalinea.textcontent.append("forme ou d’une autre de « route électrique » à")
    thisalinea.textcontent.append("pas officiellement annoncé.")
    thisalinea.textcontent.append("horizon 2035.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Solutions inductives : La recharge par induc- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 166
    thisalinea.parentID = 165
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Solutions inductives : La recharge par induc- tion consistant en une recharge sans câble "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Solutions inductives : La recharge par induc-")
    thisalinea.textcontent.append("tion consistant en une recharge sans câble")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Solutions conductives au sol ou latérale en ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 167
    thisalinea.parentID = 165
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Solutions conductives au sol ou latérale en solutions pourraient permettre de réduire forte- bord de route. ment la taille de la batterie des poids lourds et donc réduire les besoins en matières premières "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Solutions conductives au sol ou latérale en")
    thisalinea.textcontent.append("solutions pourraient permettre de réduire forte-")
    thisalinea.textcontent.append("bord de route.")
    thisalinea.textcontent.append("ment la taille de la batterie des poids lourds et")
    thisalinea.textcontent.append("donc réduire les besoins en matières premières")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Solutions conductives aériennes, avec l’utili- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 168
    thisalinea.parentID = 165
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Solutions conductives aériennes, avec l’utili- des batteries, comme le lithium, le nickel et le sation d’une caténaire électrique pour trans- cobalt. Cependant, le choix d’investissement mettre l’énergie. relève d’une décision politique, et prenant en compte les résultats des expérimentations ; Ces technologies sont encore en développe- les autorités publiques doivent statuer sur le ment. Des démonstrateurs ont été lancés dans plusieurs localisations à travers l’Europe et cer- taines portions de routes sont déjà équipées "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Solutions conductives aériennes, avec l’utili-")
    thisalinea.textcontent.append("des batteries, comme le lithium, le nickel et le")
    thisalinea.textcontent.append("sation d’une caténaire électrique pour trans-")
    thisalinea.textcontent.append("cobalt. Cependant, le choix d’investissement")
    thisalinea.textcontent.append("mettre l’énergie.")
    thisalinea.textcontent.append("relève d’une décision politique, et prenant en")
    thisalinea.textcontent.append("compte les résultats des expérimentations ;")
    thisalinea.textcontent.append("Ces technologies sont encore en développe-")
    thisalinea.textcontent.append("les autorités publiques doivent statuer sur le")
    thisalinea.textcontent.append("ment. Des démonstrateurs ont été lancés dans")
    thisalinea.textcontent.append("plusieurs localisations à travers l’Europe et cer-")
    thisalinea.textcontent.append("taines portions de routes sont déjà équipées")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4.2. Mesures-clés transverses"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 169
    thisalinea.parentID = 156
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Impact : pilotage stratégique du déploiement des IRVE KPI : création de l’entité et budget affecté Parties prenantes : État Levier(s) : décision politique, modification(s) réglementaire(s) Le déploiement des IRVE est un enjeu national rentabilité », et pour garantir l’accessibilité des indispensable pour l’atteinte des objectifs de tarifs pratiqués sur les infrastructures subven- neutralité carbone, qui dépasse les logiques de tionnées, la mobilisation des pouvoirs publics rentabilité économique stricte et nécessite des est un prérequis. investissements importants. autorités publiques. soient fléchées vers les zones à pourvoir en priorité, pour éviter les effets d’aubaine. ■ Le coût global du réseau IRVE "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.2.1. Création d’une entité publique en charge de la planification des IRVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 170
    thisalinea.parentID = 169
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Impact : pilotage stratégique du déploiement des IRVE KPI : création de l’entité et budget affecté Parties prenantes : État Levier(s) : décision politique, modification(s) réglementaire(s) Le déploiement des IRVE est un enjeu national rentabilité », et pour garantir l’accessibilité des indispensable pour l’atteinte des objectifs de tarifs pratiqués sur les infrastructures subven- neutralité carbone, qui dépasse les logiques de tionnées, la mobilisation des pouvoirs publics rentabilité économique stricte et nécessite des est un prérequis. investissements importants. autorités publiques. soient fléchées vers les zones à pourvoir en priorité, pour éviter les effets d’aubaine. ■ Le coût global du réseau IRVE "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : pilotage stratégique du déploiement des IRVE")
    thisalinea.textcontent.append("KPI : création de l’entité et budget affecté Parties prenantes : État")
    thisalinea.textcontent.append("Levier(s) : décision politique, modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Le déploiement des IRVE est un enjeu national")
    thisalinea.textcontent.append("rentabilité », et pour garantir l’accessibilité des")
    thisalinea.textcontent.append("indispensable pour l’atteinte des objectifs de")
    thisalinea.textcontent.append("tarifs pratiqués sur les infrastructures subven-")
    thisalinea.textcontent.append("neutralité carbone, qui dépasse les logiques de")
    thisalinea.textcontent.append("tionnées, la mobilisation des pouvoirs publics")
    thisalinea.textcontent.append("rentabilité économique stricte et nécessite des")
    thisalinea.textcontent.append("est un prérequis.")
    thisalinea.textcontent.append("investissements importants.")
    thisalinea.textcontent.append("autorités publiques.")
    thisalinea.textcontent.append("soient fléchées vers les zones à pourvoir en")
    thisalinea.textcontent.append("priorité, pour éviter les effets d’aubaine.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le coût global du réseau IRVE peut être réduit ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 171
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "■ Le coût global du réseau IRVE peut être réduit ropérabilité par les opérateurs, et notamment par une planification adéquate, notamment de la collecte des données, devra s’appuyer en dimensionnant correctement les raccor- sur des leviers administratifs (ex : application dements à effectuer pour les aires de service des sanctions prévues). L’autorité publique et aires de repos à travers les prérogatives des devra également garantir que les subventions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le coût global du réseau IRVE peut être réduit")
    thisalinea.textcontent.append("ropérabilité par les opérateurs, et notamment")
    thisalinea.textcontent.append("par une planification adéquate, notamment")
    thisalinea.textcontent.append("de la collecte des données, devra s’appuyer")
    thisalinea.textcontent.append("en dimensionnant correctement les raccor-")
    thisalinea.textcontent.append("sur des leviers administratifs (ex : application")
    thisalinea.textcontent.append("dements à effectuer pour les aires de service")
    thisalinea.textcontent.append("des sanctions prévues). L’autorité publique")
    thisalinea.textcontent.append("et aires de repos à travers les prérogatives des")
    thisalinea.textcontent.append("devra également garantir que les subventions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Le respect des dispositions de qualité et d’inte- "
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 172
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "■ Le respect des dispositions de qualité et d’inte- "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Le respect des dispositions de qualité et d’inte-")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "■ Centraliser, garder à jour et analyser les nom- ..."
    thisalinea.titlefontsize = "10.0"
    thisalinea.nativeID = 173
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "■ Centraliser, garder à jour et analyser les nom- breuses données relatives au déploiement et à Un « haut conseil », « conseil supérieur », ou un l’opération des IRVE publiques et ouvertes au « secrétariat à la planification des IRVE », doté de public, demande d’avoir des équipes dédiées moyens adéquats (en propre) pour mener à bien sur le long terme. En particulier, pour mener ses activités, pourrait être envisagé pour porter à bien les appels d’offres de type « clusters de le rôle de l’État planificateur et aménageur du territoire. Il serait en charge d’organiser la coor- entité "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("■ Centraliser, garder à jour et analyser les nom-")
    thisalinea.textcontent.append("breuses données relatives au déploiement et à")
    thisalinea.textcontent.append("Un « haut conseil », « conseil supérieur », ou un")
    thisalinea.textcontent.append("l’opération des IRVE publiques et ouvertes au")
    thisalinea.textcontent.append("« secrétariat à la planification des IRVE », doté de")
    thisalinea.textcontent.append("public, demande d’avoir des équipes dédiées")
    thisalinea.textcontent.append("moyens adéquats (en propre) pour mener à bien")
    thisalinea.textcontent.append("sur le long terme. En particulier, pour mener")
    thisalinea.textcontent.append("ses activités, pourrait être envisagé pour porter")
    thisalinea.textcontent.append("à bien les appels d’offres de type « clusters de")
    thisalinea.textcontent.append("le rôle de l’État planificateur et aménageur du")
    thisalinea.textcontent.append("territoire. Il serait en charge d’organiser la coor-")
    thisalinea.textcontent.append("entité avec les autres instances existantes")
    thisalinea.textcontent.append("dination avec les territoires, en amont lors de")
    thisalinea.textcontent.append("dépassent le cadre de la présente étude.")
    thisalinea.textcontent.append("l’élaboration et la mise en commun des SDIRVE,")
    thisalinea.textcontent.append("et en aval dans leur déploiement. Les modalités")
    thisalinea.textcontent.append("politiques et l’équilibre du périmètre de cette")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.2.2. Promotion des offres de raccordements intelligentes"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 174
    thisalinea.parentID = 169
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Impact : réduction des coûts de raccordement, amélioration de la rentabilité KPI : coûts de raccordement évités (scénario sans anticipation – scénario anticipé) Parties prenantes : État, collectivités, SCA, GRDE Levier(s) : communication et accompagnement du changement, modification(s) réglementaire(s) Avec l’essor des énergies renouvelables et des Sur ce modèle, les GRDE pourraient proposer demandes de raccordement associées, Enedis systématiquement (avec une éventuelle évolu- a expérimenté dans le cadre du programme Smart Vendée55 des modalités alternatives de raccordement pour les EnR. Ces ORI (offres de tion réglementaire associée, à partir d’un seuil fixé) des raccordements moins coûteux aux opérateurs de bornes "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : réduction des coûts de raccordement, amélioration de la rentabilité")
    thisalinea.textcontent.append("KPI : coûts de raccordement évités (scénario")
    thisalinea.textcontent.append("sans anticipation – scénario anticipé)")
    thisalinea.textcontent.append("Parties  prenantes :  État, collectivités, SCA,")
    thisalinea.textcontent.append("GRDE")
    thisalinea.textcontent.append("Levier(s) : communication et accompagnement du changement, modification(s) réglementaire(s)")
    thisalinea.textcontent.append("Avec l’essor des énergies renouvelables et des")
    thisalinea.textcontent.append("Sur ce modèle, les GRDE pourraient proposer")
    thisalinea.textcontent.append("demandes de raccordement associées, Enedis")
    thisalinea.textcontent.append("systématiquement (avec une éventuelle évolu-")
    thisalinea.textcontent.append("a expérimenté dans le cadre du programme")
    thisalinea.textcontent.append("Smart Vendée55 des modalités alternatives de")
    thisalinea.textcontent.append("raccordement pour les EnR. Ces ORI (offres de")
    thisalinea.textcontent.append("tion réglementaire associée, à partir d’un seuil")
    thisalinea.textcontent.append("fixé) des raccordements moins coûteux aux")
    thisalinea.textcontent.append("opérateurs de bornes de recharge, en échange")
    thisalinea.textcontent.append("raccordement intelligentes) ou offres de raccor-")
    thisalinea.textcontent.append("de services au réseau (limitation du soutirage")
    thisalinea.textcontent.append("dement alternatives à modulation de puissance,")
    thisalinea.textcontent.append("par exemple). Cela deviendra particulièrement")
    thisalinea.textcontent.append("telles qu’elles sont désormais industrialisées")
    thisalinea.textcontent.append("depuis 202156, proposent de réduire les coûts")
    thisalinea.textcontent.append("et délais de raccordement, en contrepartie")
    thisalinea.textcontent.append("d’une possibilité de limitation ponctuelle de la")
    thisalinea.textcontent.append("puissance d’injection.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.2.3. Fiabilité des données en open data"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 175
    thisalinea.parentID = 169
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "pertinent à mesure que les puissances de rac- cordement nécessaires augmenteront. Impact : meilleure estimation des besoins, optimisation du déploiement, augmentation du taux d’utilisation et amélioration de la rentabilité KPI : pourcentage de complétude de la base en open data, fréquence de mise à jour Levier(s) : ressources administratives Parties prenantes : État, collectivités, opérateurs Un certain nombre de mesures-clés ont pour à jour de la base de données IRVE en open data, condition préalable la disponibilité de don- disponible et gérée par data.gouv.fr, intitulée nées complètes et à jour sur l’infrastructure de « Fichier consolidé des bornes de recharge "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("pertinent à mesure que les puissances de rac-")
    thisalinea.textcontent.append("cordement nécessaires augmenteront.")
    thisalinea.textcontent.append("Impact : meilleure estimation des besoins, optimisation du déploiement, augmentation du taux")
    thisalinea.textcontent.append("d’utilisation et amélioration de la rentabilité")
    thisalinea.textcontent.append("KPI : pourcentage de complétude de la base en")
    thisalinea.textcontent.append("open data, fréquence de mise à jour")
    thisalinea.textcontent.append("Levier(s) : ressources administratives")
    thisalinea.textcontent.append("Parties prenantes : État, collectivités, opérateurs")
    thisalinea.textcontent.append("Un certain nombre de mesures-clés ont pour")
    thisalinea.textcontent.append("à jour de la base de données IRVE en open data,")
    thisalinea.textcontent.append("condition préalable la disponibilité de don-")
    thisalinea.textcontent.append("disponible et gérée par data.gouv.fr, intitulée")
    thisalinea.textcontent.append("nées complètes et à jour sur l’infrastructure de")
    thisalinea.textcontent.append("« Fichier consolidé des bornes de recharge pour")
    thisalinea.textcontent.append("recharge électrique. Les autorités publiques")
    thisalinea.textcontent.append("véhicules électriques ».")
    thisalinea.textcontent.append("devraient assurer la complétude et le maintien")
    thisalinea.textcontent.append("En effet, le ministère en charge de l’énergie a")
    thisalinea.textcontent.append("d’accélération de l’élaboration des SDIRVE :")
    thisalinea.textcontent.append("pouvoir d’enquête et de sanction pour imposer")
    thisalinea.textcontent.append("leurs concepteurs déplorent de devoir passer")
    thisalinea.textcontent.append("aux opérateurs le respect des dispositions de")
    thisalinea.textcontent.append("qualité et d’interopérabilité57.")
    thisalinea.textcontent.append("La mise en place d’API (interface de program-")
    thisalinea.textcontent.append("par des solutions payantes pour avoir accès à")
    thisalinea.textcontent.append("une donnée complète.")
    thisalinea.textcontent.append("mation d’application) permettrait aux opéra-")
    thisalinea.textcontent.append("De manière générale, les mécanismes de sou-")
    thisalinea.textcontent.append("teurs de se connecter directement à data.gouv,")
    thisalinea.textcontent.append("tien devraient être conditionnés à une commu-")
    thisalinea.textcontent.append("et ainsi d’alimenter en temps réel une base de")
    thisalinea.textcontent.append("nication des métriques de taux d’utilisation, qui")
    thisalinea.textcontent.append("données « dynamique ». Dans l’autre sens, des")
    thisalinea.textcontent.append("restent nécessaires pour évaluer leur impact ;")
    thisalinea.textcontent.append("API d’extraction des données dynamiques en")
    thisalinea.textcontent.append("pour cela, une base de données et un dispositif")
    thisalinea.textcontent.append("temps réel permettraient d’améliorer les ser-")
    thisalinea.textcontent.append("fiable doivent être mis en place par l’autorité")
    thisalinea.textcontent.append("vices utilisateurs (notamment les planificateurs")
    thisalinea.textcontent.append("publique.")
    thisalinea.textcontent.append("d’itinéraires, ou les applications des opérateurs")
    thisalinea.textcontent.append("d’IRVE et des e-MSP).")
    thisalinea.textcontent.append("Cette mesure serait de surcroît un facteur")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.2.4. Standardisation progressive du 800 V"
    thisalinea.titlefontsize = "12.000000000000057"
    thisalinea.nativeID = 176
    thisalinea.parentID = 169
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Impact : amélioration de l’expérience utilisateur et de la vitesse de charge (donc réduction de l’attente moyenne à la borne) KPI : pourcentage de bornes ultra-rapides en 800 V, pourcentage de complétude de la don- Parties prenantes : constructeurs automobiles et de bornes de charge, État née « 800 V » de la base en open data Levier(s) : modification(s) réglementaire(s) ou de cahier des charges Les batteries 800 V présentent des avantages embarquer des adaptateurs pour pouvoir se de compacité et de vitesse de charge, et com- charger aussi sur du 400 V, et l’efficacité de la mencent à "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : amélioration de l’expérience utilisateur et de la vitesse de charge (donc réduction")
    thisalinea.textcontent.append("de l’attente moyenne à la borne)")
    thisalinea.textcontent.append("KPI : pourcentage de bornes ultra-rapides en")
    thisalinea.textcontent.append("800 V, pourcentage de complétude de la don-")
    thisalinea.textcontent.append("Parties prenantes : constructeurs automobiles")
    thisalinea.textcontent.append("et de bornes de charge, État")
    thisalinea.textcontent.append("née « 800 V » de la base en open data")
    thisalinea.textcontent.append("Levier(s) : modification(s) réglementaire(s) ou de cahier des charges")
    thisalinea.textcontent.append("Les batteries 800 V présentent des avantages")
    thisalinea.textcontent.append("embarquer des adaptateurs pour pouvoir se")
    thisalinea.textcontent.append("de compacité et de vitesse de charge, et com-")
    thisalinea.textcontent.append("charger aussi sur du 400 V, et l’efficacité de la")
    thisalinea.textcontent.append("mencent à être déployées plus largement chez")
    thisalinea.textcontent.append("recharge est réduite.")
    thisalinea.textcontent.append("les constructeurs – en particulier dans les véhi-")
    thisalinea.textcontent.append("cules les plus hauts de gamme58. Les bornes de")
    thisalinea.textcontent.append("recharge DC ultra-rapides devront être conçues")
    thisalinea.textcontent.append("À court moyen terme, il conviendrait de condi-")
    thisalinea.textcontent.append("tionner les mécanismes de soutien aux CAPEX")
    thisalinea.textcontent.append("pour opérer à cette tension pour que les avan-")
    thisalinea.textcontent.append("tages de ces batteries soient effectifs.")
    thisalinea.textcontent.append("En effet, les véhicules dont les batteries sont")
    thisalinea.textcontent.append("des bornes rapides à une compatibilité 800 V.")
    thisalinea.textcontent.append("De plus, dans le cadre de la transparence et la")
    thisalinea.textcontent.append("disponibilité des données, l’information de la")
    thisalinea.textcontent.append("en 400 V peuvent se charger nativement sur")
    thisalinea.textcontent.append("tension des bornes devrait être accessible pour")
    thisalinea.textcontent.append("des bornes 800 V : déployer des bornes 800 V")
    thisalinea.textcontent.append("que les utilisateurs de batteries 800 V puissent")
    thisalinea.textcontent.append("n’exclurait donc pas les véhicules 400 V exis-")
    thisalinea.textcontent.append("choisir les bornes qui leur offriront une recharge")
    thisalinea.textcontent.append("tants. En revanche, les batteries 800 V doivent")
    thisalinea.textcontent.append("optimale.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "4.2.5. Soutien à l’acquisition des poids lourds"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 177
    thisalinea.parentID = 169
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Impact : lancement de la dynamique d’électrification de la mobilité électrique KPI : ventes des camions électriques en France Parties prenantes : constructeurs, État Levier(s) : décision politique Concernant la recharge des poids lourds, les un système de primes ou de bonus forfaitaire acteurs de l’écosystème déplorent le fonction- à l’acquisition enverrait un signal fort à l’écosys- nement des mécanismes d’appel à projets, tème et permettrait de lancer la dynamique. qui donnent peu de visibilité aux candidats ; Parallèlement, cette phase de lancement des en effet, dans l’attente des résultats, les socié- camions électriques pourrait s’appuyer sur les tés doivent "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Impact : lancement de la dynamique d’électrification de la mobilité électrique")
    thisalinea.textcontent.append("KPI : ventes des camions électriques en France Parties prenantes : constructeurs, État")
    thisalinea.textcontent.append("Levier(s) : décision politique")
    thisalinea.textcontent.append("Concernant la recharge des poids lourds, les")
    thisalinea.textcontent.append("un système de primes ou de bonus forfaitaire")
    thisalinea.textcontent.append("acteurs de l’écosystème déplorent le fonction-")
    thisalinea.textcontent.append("à l’acquisition enverrait un signal fort à l’écosys-")
    thisalinea.textcontent.append("nement des mécanismes d’appel à projets,")
    thisalinea.textcontent.append("tème et permettrait de lancer la dynamique.")
    thisalinea.textcontent.append("qui donnent peu de visibilité aux candidats ;")
    thisalinea.textcontent.append("Parallèlement, cette phase de lancement des")
    thisalinea.textcontent.append("en effet, dans l’attente des résultats, les socié-")
    thisalinea.textcontent.append("camions électriques pourrait s’appuyer sur les")
    thisalinea.textcontent.append("tés doivent réaliser des investissements très")
    thisalinea.textcontent.append("modèles « truck-as-a-service », qui permet-")
    thisalinea.textcontent.append("significatifs dans leurs flottes sans pour autant")
    thisalinea.textcontent.append("traient aux logisticiens et transporteurs de faire")
    thisalinea.textcontent.append("avoir la garantie d’être lauréates. Pour lancer le")
    thisalinea.textcontent.append("évoluer leurs opérations sans porter de CAPEX")
    thisalinea.textcontent.append("mouvement de la mobilité lourde électrique,")
    thisalinea.textcontent.append("dans un premier temps.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "5. Annexes"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 178
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5.1. Vue détaillée par axe routier des besoins en points de charge à horizon 2035 pour le scénario Haut, Central et Bas"
    thisalinea.titlefontsize = "13.0"
    thisalinea.nativeID = 179
    thisalinea.parentID = 178
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "6. Définitions"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 180
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Point de recharge : une interface associée à un emplacement de stationnement qui permet de bornes de recharge associées à des emplace- ments de stationnement, exploitée par un ou recharger un seul véhicule électrique à la fois plusieurs opérateurs Borne de recharge : un appareil fixe raccordé à un point d’alimentation électrique, comprenant Point de charge ouvert au public : Ces points de charge sont installés sur des domaines privés un ou plusieurs points de charge et pouvant soumis à des restrictions d’accès spécifiques, intégrer notamment des dispositifs de com- mais non discriminatoires, telles que l’utilisation munication, de comptage, de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Infrastructures de recharge (définitions réglementaires)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 181
    thisalinea.parentID = 180
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Point de recharge : une interface associée à un emplacement de stationnement qui permet de bornes de recharge associées à des emplace- ments de stationnement, exploitée par un ou recharger un seul véhicule électrique à la fois plusieurs opérateurs Borne de recharge : un appareil fixe raccordé à un point d’alimentation électrique, comprenant Point de charge ouvert au public : Ces points de charge sont installés sur des domaines privés un ou plusieurs points de charge et pouvant soumis à des restrictions d’accès spécifiques, intégrer notamment des dispositifs de com- mais non discriminatoires, telles que l’utilisation munication, de comptage, de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Point de recharge : une interface associée à un")
    thisalinea.textcontent.append("emplacement de stationnement qui permet de")
    thisalinea.textcontent.append("bornes de recharge associées à des emplace-")
    thisalinea.textcontent.append("ments de stationnement, exploitée par un ou")
    thisalinea.textcontent.append("recharger un seul véhicule électrique à la fois")
    thisalinea.textcontent.append("plusieurs opérateurs")
    thisalinea.textcontent.append("Borne de recharge : un appareil fixe raccordé à")
    thisalinea.textcontent.append("un point d’alimentation électrique, comprenant")
    thisalinea.textcontent.append("Point de charge ouvert au public : Ces points")
    thisalinea.textcontent.append("de charge sont installés sur des domaines privés")
    thisalinea.textcontent.append("un ou plusieurs points de charge et pouvant")
    thisalinea.textcontent.append("soumis à des restrictions d’accès spécifiques,")
    thisalinea.textcontent.append("intégrer notamment des dispositifs de com-")
    thisalinea.textcontent.append("mais non discriminatoires, telles que l’utilisation")
    thisalinea.textcontent.append("munication, de comptage, de contrôle ou de")
    thisalinea.textcontent.append("sur des créneaux horaires précis. Cela concerne")
    thisalinea.textcontent.append("paiement")
    thisalinea.textcontent.append("Station de recharge : une zone comportant une")
    thisalinea.textcontent.append("borne de recharge associée à un ou des empla-")
    thisalinea.textcontent.append("cements de stationnement ou un ensemble de")
    thisalinea.textcontent.append("par exemple les points de charge dans les par-")
    thisalinea.textcontent.append("kings des grands entrepôts ou des magasins")
    thisalinea.textcontent.append("de proximité, dans les parkings souterrains, les")
    thisalinea.textcontent.append("établissements hôteliers et de restauration, etc.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "7. Abréviations"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 182
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "AC : Alternative Current, en français : courant alternatif AOM : Autorité organisatrice de la mobilité AODE : Autorité organisatrice de la distribution d’énergie AAP : Appel à projets AFIR : Alternative Fuels Infrastructure Regulation BEV : Battery Electric Vehicle, en français : véhi- cule 100 % à batterie électrique CCS : Combined Charging System, en français : système de recharge combiné CPO : Charge Point Operator, en français : opé- rateur d’infrastructure PDC : Point de charge PHEV : Plug-in Hybrid Electric Vehicle en fran- çais : véhicule hybride rechargeable PL : Poids lourd RFID : Radio Frequency Identification "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("AC : Alternative Current, en français : courant")
    thisalinea.textcontent.append("alternatif")
    thisalinea.textcontent.append("AOM : Autorité organisatrice de la mobilité")
    thisalinea.textcontent.append("AODE : Autorité organisatrice de la distribution")
    thisalinea.textcontent.append("d’énergie")
    thisalinea.textcontent.append("AAP : Appel à projets")
    thisalinea.textcontent.append("AFIR : Alternative Fuels Infrastructure")
    thisalinea.textcontent.append("Regulation")
    thisalinea.textcontent.append("BEV : Battery Electric Vehicle, en français : véhi-")
    thisalinea.textcontent.append("cule 100 % à batterie électrique")
    thisalinea.textcontent.append("CCS : Combined Charging System, en français :")
    thisalinea.textcontent.append("système de recharge combiné")
    thisalinea.textcontent.append("CPO : Charge Point Operator, en français : opé-")
    thisalinea.textcontent.append("rateur d’infrastructure")
    thisalinea.textcontent.append("PDC : Point de charge")
    thisalinea.textcontent.append("PHEV : Plug-in Hybrid Electric Vehicle en fran-")
    thisalinea.textcontent.append("çais : véhicule hybride rechargeable")
    thisalinea.textcontent.append("PL : Poids lourd")
    thisalinea.textcontent.append("RFID : Radio Frequency Identification")
    thisalinea.textcontent.append("RTE-T : réseau transeuropéen de transport,")
    thisalinea.textcontent.append("souvent en anglais « TEN-T »")
    thisalinea.textcontent.append("SDIRVE : Schéma directeur pour les infrastruc-")
    thisalinea.textcontent.append("tures de recharge")
    thisalinea.textcontent.append("TPE : Terminal de paiement électronique")
    thisalinea.textcontent.append("TMJA : Trafic moyen journalier annuel")
    thisalinea.textcontent.append("UE : Union européenne")
    thisalinea.textcontent.append("VASP : Véhicules automoteurs spécialisés")
    thisalinea.textcontent.append("DC : Direct Current, en français : courant continu")
    thisalinea.textcontent.append("VL : Véhicule léger")
    thisalinea.textcontent.append("GRDE : Gestionnaire de réseau de distribution")
    thisalinea.textcontent.append("d’électricité")
    thisalinea.textcontent.append("VP : Véhicule particulier")
    thisalinea.textcontent.append("VUL : Véhicule utilitaire léger")
    thisalinea.textcontent.append("IRVE : Infrastructure de recharge de véhicule")
    thisalinea.textcontent.append("électrique")
    thisalinea.textcontent.append("LOM (loi) : Loi d’orientation des mobilités")
    thisalinea.textcontent.append("ZNI : Zones non interconnectées")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "8. Table des figures"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 183
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "Figure 1 : Cartographie des points de charge sur les grands axes routiers Figure 2 : Besoin en nombre de points de charge pour la recharge publique sur les grands axes routiers Figure 3 : Besoin en nombre de points sur quelques axes routiers pour les véhicules légers et pour les poids lourds dans les différents scénarios par rapport à l’actuel Figure 4 : Obstacles au déploiement des IRVE Figure 5 : Mesures-clés relatives aux grands axes routiers Figure 6 : Mesures-clés transverses Figure 7 : Évaluation du besoin en recharge selon la typologie du trajet Figure 8 : Méthodologie "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Figure 1 : Cartographie des points de charge sur les grands axes routiers")
    thisalinea.textcontent.append("Figure 2 : Besoin en nombre de points de charge pour la recharge publique sur les grands axes")
    thisalinea.textcontent.append("routiers")
    thisalinea.textcontent.append("Figure 3 : Besoin en nombre de points sur quelques axes routiers pour les véhicules légers et pour")
    thisalinea.textcontent.append("les poids lourds dans les différents scénarios par rapport à l’actuel")
    thisalinea.textcontent.append("Figure 4 : Obstacles au déploiement des IRVE")
    thisalinea.textcontent.append("Figure 5 : Mesures-clés relatives aux grands axes routiers")
    thisalinea.textcontent.append("Figure 6 : Mesures-clés transverses")
    thisalinea.textcontent.append("Figure 7 : Évaluation du besoin en recharge selon la typologie du trajet")
    thisalinea.textcontent.append("Figure 8 : Méthodologie utilisée pour la modélisation des besoins de recharge hors grands axes")
    thisalinea.textcontent.append("routiers")
    thisalinea.textcontent.append("Figure 9 : Méthodologie utilisée dans le cadre de la modélisation des besoins de recharge sur les")
    thisalinea.textcontent.append("grands axes routiers")
    thisalinea.textcontent.append("Figure 10 : Parc de véhicules, tous carburants confondus, en millions de véhicules")
    thisalinea.textcontent.append("Figure 11 : Parc de véhicules électriques (BEV) en millions de véhicules")
    thisalinea.textcontent.append("Figure 12 : Parc de poids lourds électriques (BEV) en millier de véhicules")
    thisalinea.textcontent.append("Figure 13 : Taux d’électrification des véhicules légers (à gauche) et des poids lourds (à droite)")
    thisalinea.textcontent.append("Figure 14 : Consommation moyenne de différentes catégories de véhicules en kWh/km")
    thisalinea.textcontent.append("Figure 15 : Évolution des besoins en recharge publique au cours du temps, en %")
    thisalinea.textcontent.append("Figure 16 : Besoin énergétique pour la recharge publique sur les grands axes routiers")
    thisalinea.textcontent.append("Figure 17 : Puissance moyenne acceptée pour différents chargeurs par les véhicules à différentes")
    thisalinea.textcontent.append("dates sur les grands axes routiers")
    thisalinea.textcontent.append("Figure 18 : Résultats de la modélisation pour les besoins en nombre de points de charge sur les")
    thisalinea.textcontent.append("grands axes routiers")
    thisalinea.textcontent.append("Figure 19 : Évolution du besoin en nombre de points sur quelques axes routiers pour les véhicules")
    thisalinea.textcontent.append("légers et pour les poids lourds")
    thisalinea.textcontent.append("Figure 20 : Évolution du besoin énergétique (TWh/an) de la recharge publique par typologie de")
    thisalinea.textcontent.append("recharge pour le scénario Central")
    thisalinea.textcontent.append("Figure 21 : Résultat de la modélisation pour les besoins en nombre de points de charge")
    thisalinea.textcontent.append("Figure 22 : Répartition des typologies de points avec un taux d’utilisation de 12,5 % en 2035")
    thisalinea.textcontent.append("Figure 23 : Correspondance entre taux d’utilisation et nombre d’heures d’utilisation quotidienne")
    thisalinea.textcontent.append("moyenne sur une année")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "CONTACTS POUR LE PRÉSENT RAPPORT"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 184
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Clément Molizon Yasmine Assef clement.molizon@avere-france.org yasmine.assef@afry.com M : +33 6 18 25 24 84 M : + 33 7 85 92 77 41 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Clément Molizon")
    thisalinea.textcontent.append("Yasmine Assef")
    thisalinea.textcontent.append("clement.molizon@avere-france.org")
    thisalinea.textcontent.append("yasmine.assef@afry.com")
    thisalinea.textcontent.append("M : +33 6 18 25 24 84")
    thisalinea.textcontent.append("M : + 33 7 85 92 77 41")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "CONTRIBUTEURS"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 185
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Avere-France Clément Molizon, Bassem Haidar AFRY Yasmine Assef, Théo Sébastien, Arnaud Pauli "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Avere-France")
    thisalinea.textcontent.append("Clément Molizon, Bassem Haidar")
    thisalinea.textcontent.append("AFRY")
    thisalinea.textcontent.append("Yasmine Assef, Théo Sébastien,")
    thisalinea.textcontent.append("Arnaud Pauli")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "À PROPOS D’AFRY"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 186
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "AFRY fournit des services de conseil, numé- riques, de design et d’ingénierie pour accélérer la transition vers une société durable. Nous sommes 19 000 experts dévoués dans les secteurs de l’industrie, de l’énergie et de l’infrastructure. AFRY possède des racines nordiques avec une portée globale, produit des ventes nettes de 24 milliards de couronnes suédoises et est cotée au Nasdaq Stockholm. AFRY Management Consulting SAS 1, rue de Gramont 75002 Paris France "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("AFRY fournit des services de conseil, numé-")
    thisalinea.textcontent.append("riques, de design et d’ingénierie pour accélérer")
    thisalinea.textcontent.append("la transition vers une société durable.")
    thisalinea.textcontent.append("Nous sommes 19 000 experts dévoués dans")
    thisalinea.textcontent.append("les secteurs de l’industrie, de l’énergie et de")
    thisalinea.textcontent.append("l’infrastructure. AFRY possède des racines")
    thisalinea.textcontent.append("nordiques avec une portée globale, produit")
    thisalinea.textcontent.append("des ventes nettes de 24 milliards de couronnes")
    thisalinea.textcontent.append("suédoises et est cotée au Nasdaq Stockholm.")
    thisalinea.textcontent.append("AFRY Management Consulting SAS")
    thisalinea.textcontent.append("1, rue de Gramont")
    thisalinea.textcontent.append("75002 Paris")
    thisalinea.textcontent.append("France")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "À PROPOS DE L’AVERE-FRANCE"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 187
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "L’Avere-France est l’association nationale pour le développement de la mobilité électrique. Créée en 1978 pour représenter l’ensemble Avere-France, Association nationale pour le développement de la mobilité électrique 5, rue du Helder de l’écosystème de l’électro-mobilité dans les 75009 Paris domaines industriel, commercial, institutionnel France ou associatif, elle a pour objectif de faire la pro- motion de l’utilisation des véhicules électriques et hybrides rechargeables. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("L’Avere-France est l’association nationale pour")
    thisalinea.textcontent.append("le développement de la mobilité électrique.")
    thisalinea.textcontent.append("Créée en 1978 pour représenter l’ensemble")
    thisalinea.textcontent.append("Avere-France, Association nationale pour le")
    thisalinea.textcontent.append("développement de la mobilité électrique")
    thisalinea.textcontent.append("5, rue du Helder")
    thisalinea.textcontent.append("de l’écosystème de l’électro-mobilité dans les")
    thisalinea.textcontent.append("75009 Paris")
    thisalinea.textcontent.append("domaines industriel, commercial, institutionnel")
    thisalinea.textcontent.append("France")
    thisalinea.textcontent.append("ou associatif, elle a pour objectif de faire la pro-")
    thisalinea.textcontent.append("motion de l’utilisation des véhicules électriques")
    thisalinea.textcontent.append("et hybrides rechargeables.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "PARTENAIRES FINANCIERS"
    thisalinea.titlefontsize = "16.0"
    thisalinea.nativeID = 188
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "À PROPOS DE LA BANQUE DES TERRITOIRES"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 189
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Créée en 2018, la Banque des Territoires est un des Dépôts afin d’être mieux identifiée auprès des cinq métiers de la Caisse des Dépôts. Elle de ses clients et au plus près d’eux. rassemble dans une même structure les exper- tises internes à destination des territoires. Porte d’entrée client unique, elle propose des solu- tions sur mesure de conseil et de financement en prêts et en investissement pour répondre aux besoins des collectivités locales, des orga- nismes de logement social, des entreprises publiques locales et des professions juridiques. Elle s’adresse à tous les territoires, depuis les zones rurales jusqu’aux métropoles, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Créée en 2018, la Banque des Territoires est un")
    thisalinea.textcontent.append("des Dépôts afin d’être mieux identifiée auprès")
    thisalinea.textcontent.append("des cinq métiers de la Caisse des Dépôts. Elle")
    thisalinea.textcontent.append("de ses clients et au plus près d’eux.")
    thisalinea.textcontent.append("rassemble dans une même structure les exper-")
    thisalinea.textcontent.append("tises internes à destination des territoires. Porte")
    thisalinea.textcontent.append("d’entrée client unique, elle propose des solu-")
    thisalinea.textcontent.append("tions sur mesure de conseil et de financement")
    thisalinea.textcontent.append("en prêts et en investissement pour répondre")
    thisalinea.textcontent.append("aux besoins des collectivités locales, des orga-")
    thisalinea.textcontent.append("nismes de logement social, des entreprises")
    thisalinea.textcontent.append("publiques locales et des professions juridiques.")
    thisalinea.textcontent.append("Elle s’adresse à tous les territoires, depuis les")
    thisalinea.textcontent.append("zones rurales jusqu’aux métropoles, avec l’ambi-")
    thisalinea.textcontent.append("tion de lutter contre les inégalités sociales et les")
    thisalinea.textcontent.append("fractures territoriales. La Banque des Territoires")
    thisalinea.textcontent.append("est déployée dans les 16 directions régionales")
    thisalinea.textcontent.append("et les 37 implantations territoriales de la Caisse")
    thisalinea.textcontent.append("Pour des territoires plus attractifs, inclusifs,")
    thisalinea.textcontent.append("durables et connectés.")
    thisalinea.textcontent.append("www.banquedesterritoires.fr")
    thisalinea.textcontent.append("@BanqueDesTerr")
    thisalinea.textcontent.append("Sophie Huet")
    thisalinea.textcontent.append("sophie.huet2@caissedesdepots.fr")
    thisalinea.textcontent.append("M : + 33 6 07 42 14 50")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "À PROPOS DE ECF"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 190
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "The European Climate Foundation (ECF) is a responsible transition to a net-zero economy major philanthropic initiative working to help and sustainable society in Europe and around tackle the climate crisis by fostering the deve- the world. lopment of a net-zero emission society at the national, European, and global level. The ECF supports over 700 partner organisations to carry out activities that drive urgent and ambitious policy in support of the objectives of the Paris Agreement, contribute to the public debate on climate action, and help deliver a socially Agathe Destresse agathe.destresse@Europeanclimate.org Avec le soutien de "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The European Climate Foundation (ECF) is a")
    thisalinea.textcontent.append("responsible transition to a net-zero economy")
    thisalinea.textcontent.append("major philanthropic initiative working to help")
    thisalinea.textcontent.append("and sustainable society in Europe and around")
    thisalinea.textcontent.append("tackle the climate crisis by fostering the deve-")
    thisalinea.textcontent.append("the world.")
    thisalinea.textcontent.append("lopment of a net-zero emission society at the")
    thisalinea.textcontent.append("national, European, and global level. The ECF")
    thisalinea.textcontent.append("supports over 700 partner organisations to carry")
    thisalinea.textcontent.append("out activities that drive urgent and ambitious")
    thisalinea.textcontent.append("policy in support of the objectives of the Paris")
    thisalinea.textcontent.append("Agreement, contribute to the public debate")
    thisalinea.textcontent.append("on climate action, and help deliver a socially")
    thisalinea.textcontent.append("Agathe Destresse")
    thisalinea.textcontent.append("agathe.destresse@Europeanclimate.org")
    thisalinea.textcontent.append("Avec le soutien de")
    thisalinea.textcontent.append("")
    alineas.append(thisalinea)

    return alineas
