import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_eu_space() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document eu_space
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
    thisalinea.texttitle = "eu_space"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Dear reader, climate change is one of the biggest challenges facing humanity today – and overcoming it requires not only an evolution in the way we live our lives, but also a green modification on how we do business. Driving this transformation is the European Green Deal, which strives to drastically reduce carbon emissions, increase sustainable practices and, ultimately, make Europe the world’s first climate-neutral continent by 2050. But achieving these goals requires that companies take a deep look at their internal operations, and supply chains to identify opportunities for reducing their own environmental footprint. It is where the EU "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2023 / ISSUE 1 EU Space for Green Transformation A new tool for companies to monitor their sustainability targets #EUSpace"
    thisalinea.titlefontsize = "15.0"
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
    thisalinea.textlevel = 1
    thisalinea.texttitle = "FOREWORD"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 2
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Dear reader, climate change is one of the biggest challenges facing humanity today – and overcoming it requires not only an evolution in the way we live our lives, but also a green modification on how we do business. Driving this transformation is the European Green Deal, which strives to drastically reduce carbon emissions, increase sustainable practices and, ultimately, make Europe the world’s first climate-neutral continent by 2050. But achieving these goals requires that companies take a deep look at their internal operations, and supply chains to identify opportunities for reducing their own environmental footprint. It is where the EU "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Dear reader,")
    thisalinea.textcontent.append("climate change is one of the biggest challenges facing humanity today – and")
    thisalinea.textcontent.append("overcoming it requires not only an evolution in the way we live our lives, but")
    thisalinea.textcontent.append("also a green modification on how we do business.")
    thisalinea.textcontent.append("Driving this transformation is the European Green Deal, which strives to")
    thisalinea.textcontent.append("drastically reduce carbon emissions, increase sustainable practices and,")
    thisalinea.textcontent.append("ultimately, make Europe the world’s first climate-neutral continent by 2050.")
    thisalinea.textcontent.append("But achieving these goals requires that companies take a deep look at their")
    thisalinea.textcontent.append("internal operations, and supply chains to identify opportunities for reducing")
    thisalinea.textcontent.append("their own environmental footprint.")
    thisalinea.textcontent.append("It is where the EU Space Programme comes into play.")
    thisalinea.textcontent.append("While EU Space data and services are essential assets to supporting the implementation of the Green Deal,")
    thisalinea.textcontent.append("businesses stand to benefit too. For example, Copernicus, Galileo and EGNOS supply the information companies")
    thisalinea.textcontent.append("need to monitor environmental indicators, reduce their environmental impact, become more sustainable and drive")
    thisalinea.textcontent.append("the green transformation. Better yet, much of this data is openly accessible and provided free of charge.")
    thisalinea.textcontent.append("To help companies utilise this data as a means of driving their own sustainability journeys, EUSPA has compiled the")
    thisalinea.textcontent.append("first #EUSpace for the Green Transformation report. In the following pages, we introduce the Green Deal, its")
    thisalinea.textcontent.append("implications for companies and, most importantly, how the EU Space Programme can help businesses become more")
    thisalinea.textcontent.append("sustainable.")
    thisalinea.textcontent.append("Leveraging our team’s collective expertise in #EUSpace, we have created a report that every company can use to")
    thisalinea.textcontent.append("monitor their sustainability targets. The report includes detailed, real-world examples to inspire companies on how")
    thisalinea.textcontent.append("to use #EUSpace for clean industry, construction and renovation, smart and sustainable mobility, a healthier and")
    thisalinea.textcontent.append("green food system, and restoring ecosystems and biodiversity.")
    thisalinea.textcontent.append("Whether it be increasing the efficiency of renewable energy infrastructure, enabling more efficient flightpaths, or")
    thisalinea.textcontent.append("implementing precision agriculture operations, I’m confident that this report will become a go-to-source for your")
    thisalinea.textcontent.append("green transformation and a trusted roadmap in your sustainability journey.")
    thisalinea.textcontent.append("Happy reading!")
    thisalinea.textcontent.append("Rodrigo da Costa")
    thisalinea.textcontent.append("EUSPA Executive Director")
    thisalinea.textcontent.append("Prague, January 2023")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "TABLE OF CONTENTS"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3.2.1 Clean energy production and supply ........................................................................................................ 31 3.2.2 Clean industry boosting a cleaner industry ............................................................................................ 35 3.2.3 Construction and renovation ....................................................................................................................... 39 3.2.4 Smart and sustainable mobility .................................................................................................................. 40 3.2.5 A healthier and greener food system ....................................................................................................... 47 3.2.6 Restored ecosystems and biodiversity ..................................................................................................... 53 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "FOREWORD ................................................................................................................................................................................................... II EXECUTIVE SUMMARY ........................................................................................................................................................................... 1"
    thisalinea.titlefontsize = "11.040000000000077"
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
    thisalinea.texttitle = "1. INTRODUCTION  4"
    thisalinea.titlefontsize = "11.040000000000077"
    thisalinea.nativeID = 5
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
    thisalinea.texttitle = "2. THE GREEN TRANSFORMATION AND EU GREEN DEAL FOR BUSINESS IN EUROPE  7"
    thisalinea.titlefontsize = "11.040000000000077"
    thisalinea.nativeID = 6
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
    thisalinea.texttitle = "3. THE ROLE OF THE EU SPACE PROGRAMME IN SUPPORTING COMPANIES ALONG THEIR SUSTAINABILITY JOURNEY  15"
    thisalinea.titlefontsize = "11.040000000000077"
    thisalinea.nativeID = 7
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3.2.1 Clean energy production and supply ........................................................................................................ 31 3.2.2 Clean industry boosting a cleaner industry ............................................................................................ 35 3.2.3 Construction and renovation ....................................................................................................................... 39 3.2.4 Smart and sustainable mobility .................................................................................................................. 40 3.2.5 A healthier and greener food system ....................................................................................................... 47 3.2.6 Restored ecosystems and biodiversity ..................................................................................................... 53 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3.2.1 Clean energy production and supply ........................................................................................................ 31")
    thisalinea.textcontent.append("3.2.2 Clean industry boosting a cleaner industry ............................................................................................ 35")
    thisalinea.textcontent.append("3.2.3 Construction and renovation ....................................................................................................................... 39")
    thisalinea.textcontent.append("3.2.4 Smart and sustainable mobility .................................................................................................................. 40")
    thisalinea.textcontent.append("3.2.5 A healthier and greener food system ....................................................................................................... 47")
    thisalinea.textcontent.append("3.2.6 Restored ecosystems and biodiversity ..................................................................................................... 53")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. CONCLUSIONS: EU SPACE FOR GREEN TRANSFORMATION  58"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 8
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
    thisalinea.texttitle = "ANNEX 1: ABOUT THE EUROPEAN GLOBAL NAVIGATION SYSTEM AND COPERNICUS  60"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 9
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
    thisalinea.texttitle = "ANNEX 2: ABOUT THE AUTHORS  63"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 10
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
    thisalinea.texttitle = "LIST OF EXHIBITS . 64"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 11
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
    thisalinea.texttitle = "ABBREVIATIONS AND ACRONYMS . 66"
    thisalinea.titlefontsize = "11.039999999999992"
    thisalinea.nativeID = 12
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "EXECUTIVE SUMMARY"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 13
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "In December 2019, the European Commission announced the European Green Deal, a package of policies and initiatives to answer the United Nation’s 2030 Agenda and the Sustainable Development Goals. This ambitious roadmap towards a climate-resilient society aspires to make the European Union’s economy sustainable, turning climate and environmental challenges into opportunities. The Green Deal is designed to transform Europe into the first climate-neutral continent, achieving zero net emissions of greenhouse gases by 2050. As tighter regulation and legislation appear on the horizon and purchasing and investment patterns place ever- higher importance on sustainability, companies embark on their sustainability journey. Not "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In December 2019, the European Commission announced the European Green Deal, a package of policies and")
    thisalinea.textcontent.append("initiatives to answer the United Nation’s 2030 Agenda and the Sustainable Development Goals. This ambitious")
    thisalinea.textcontent.append("roadmap towards a climate-resilient society aspires to make the European Union’s economy sustainable, turning")
    thisalinea.textcontent.append("climate and environmental challenges into opportunities. The Green Deal is designed to transform Europe into the")
    thisalinea.textcontent.append("first climate-neutral continent, achieving zero net emissions of greenhouse gases by 2050.")
    thisalinea.textcontent.append("As tighter regulation and legislation appear on the horizon and purchasing and investment patterns place ever-")
    thisalinea.textcontent.append("higher importance on sustainability, companies embark on their sustainability journey. Not just external factors")
    thisalinea.textcontent.append("(regulation, revenues), but also internal ones, such as talent attraction, employee productivity, motivation and")
    thisalinea.textcontent.append("retention, are growing in significance. This is reflected in the key figures presented below: firstly, the appeal of a")
    thisalinea.textcontent.append("prospective employer to students and young professionals is 25% higher for companies whose green transformation")
    thisalinea.textcontent.append("is already underway1. Secondly, and most crucially, the market for the green transformation itself stands at € 15")
    thisalinea.textcontent.append("billion in 2022 and is expected to grow at a CAGR of 21.9% to 20302. Finally, a staggering 85% majority of Moody’s")
    thisalinea.textcontent.append("debt ratings took ESG into account in 2020 3 – demonstrating clearly that the investment appetite is rising for")
    thisalinea.textcontent.append("companies strong in environmental, social and governance matters. As a matter of fact, the broader impetus for the")
    thisalinea.textcontent.append("green transformation is also born from the need to build climate resilience, as the world’s society and industry")
    thisalinea.textcontent.append("anticipate the transformation climate change will bring to daily lives, livelihoods, consumption, shipping, and all")
    thisalinea.textcontent.append("aspects of life and the market.")
    thisalinea.textcontent.append("Exhibit 1: Why Pursuing the green transformation - key figures")
    thisalinea.textcontent.append("Performing the green transformation requires that a company takes a deep look through their internal operations,")
    thisalinea.textcontent.append("as well as their surrounding supply chain to understand where and how pollution and waste occur. In that regard,")
    thisalinea.textcontent.append("the slew of tools newly-available in the 21st century – including remote sensing, location-based services, artificial")
    thisalinea.textcontent.append("intelligence and many others – makes monitoring, tracking, evaluating and implementing sustainable operations not")
    thisalinea.textcontent.append("just possible, but long-term profitable.")
    thisalinea.textcontent.append("The EU Space Programme is able to provide value to all players across supply and value chains, sectors and activities,")
    thisalinea.textcontent.append("chiefly with its Copernicus (Earth Observation) and EGNSS (positioning, navigation and timing) components. From")
    thisalinea.textcontent.append("renewable energy generation and distribution to industrial waste management, wildlife monitoring, urban planning")
    thisalinea.textcontent.append("and fleet management, the Copernicus and Galileo can offer a host of independent, as well as synergistic services")
    thisalinea.textcontent.append("to aid companies along their sustainability journeys and support them in greening their operations.")
    thisalinea.textcontent.append("EU Space data and services are an important asset to support the implementation of the Green Deal objectives. At")
    thisalinea.textcontent.append("government level, Galileo and Copernicus are essential tools for environmental monitoring, as they provide")
    thisalinea.textcontent.append("reliable and nearly real-time data on positioning and Earth Observation. Policies can be shaped based on reality and")
    thisalinea.textcontent.append("thoughtful corrective actions can be taken, when necessary.")
    thisalinea.textcontent.append("In the context of a more sustainable society and ESG scoring, companies are setting green transformation targets to")
    thisalinea.textcontent.append("reduce greenhouse emissions and environmental footprint of their operations, as well promote their actions to")
    thisalinea.textcontent.append("attract customers and increase their market shares. Business benefit from a myriad of possible applications for")
    thisalinea.textcontent.append("EU space data, which translates into not only greener practices, but also cost reduction and increased efficiency.")
    thisalinea.textcontent.append("For example, a green urban development relies on solid geospatial data. EGNSS has a fundamental role in reducing")
    thisalinea.textcontent.append("greenhouse emissions, consonant to the Green Deal’s ambitions. Aiming a smart and sustainable mobility, Galileo")
    thisalinea.textcontent.append("is a key tool for reducing travel time and fuel consumption. Satellite data provided by Copernicus and Galileo play")
    thisalinea.textcontent.append("a key role in improving the food system, developing sustainable and efficient practices. The EU space data")
    thisalinea.textcontent.append("enables precision agriculture by mapping the evolution of crops and precisely navigating to the intervention areas.")
    thisalinea.textcontent.append("Ecosystems and biodiversity preservation are vital for the maintenance of life on Earth. In this respect, Copernicus")
    thisalinea.textcontent.append("data is especially appropriate for monitoring the environment, providing crucial climate-biodiversity indicators.")
    thisalinea.textcontent.append("Almost all the consulted companies (direct interviews and surveys) stated that they are currently not leveraging")
    thisalinea.textcontent.append("EU Space Data for pursuing their green transformation objectives. Many consulted companies acknowledged")
    thisalinea.textcontent.append("that the potential for EU Space data is enormous and expressed their interest to know more about it and")
    thisalinea.textcontent.append("possibly being engaged by EUSPA in further action.")
    thisalinea.textcontent.append("This study aims to introduce the EU Green Deal, its implications for companies, and how EU Space can help")
    thisalinea.textcontent.append("companies to address their green transformation, presenting current practices of EU-based champions in")
    thisalinea.textcontent.append("sustainability management, and how companies can benefit from the EU Space Programme applications. More")
    thisalinea.textcontent.append("specifically, the study aims to:")
    thisalinea.textcontent.append("During the study, both secondary and primary research have been conducted. In particular, a stakeholder")
    thisalinea.textcontent.append("consultation has been performed through direct industry interviews and a web survey aimed both to space services")
    thisalinea.textcontent.append("providers and user companies. As a result of the consultation, about thirty companies provided useful insights and")
    thisalinea.textcontent.append("inputs used throughout the report.")
    thisalinea.textcontent.append("The participating companies range from listed companies all the way to SMEs, from manufacturing to service sector")
    thisalinea.textcontent.append("companies. Some examples of consulted companies are listed in Exhibit 2.")
    thisalinea.textcontent.append("Exhibit 2: Participating companies who disclosed their name4")
    thisalinea.textcontent.append("The European Union Agency for Space Programme (EUSPA)’s core mission is to implement the EU Space")
    thisalinea.textcontent.append("Programme and to provide reliable, safe and secure space-related services, maximising their socio-economic")
    thisalinea.textcontent.append("benefits for European society and business. The lack of awareness towards the EU Space Programme and its")
    thisalinea.textcontent.append("benefits for companies can only be overcome by fostering the collaboration between the European Commission,")
    thisalinea.textcontent.append("EUSPA, adopters of EU space-based solutions and service providers. The development of innovative and")
    thisalinea.textcontent.append("competitive business models related to the green transformation and in support of the Green Deal objectives cannot")
    thisalinea.textcontent.append("be separated from the effort made by companies willing to contribute to the wellness of EU citizens and the")
    thisalinea.textcontent.append("development of a greener and more inclusive society.")
    thisalinea.textcontent.append("If you are a company and you are interested in having additional information about the EU Space Programme and")
    thisalinea.textcontent.append("how it can support your green transformation do not hesitate in reaching out to EUSPA at market@euspa.europa.eu.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Understand the Green Deal and the implications for companies: The Green Deal comes with ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 14
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Understand the Green Deal and the implications for companies: The Green Deal comes with implications that ripple through the entire corporate ecosystem and provides companies with opportunities as well as the need to react to the changing regulatory and policy framework. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Understand the Green Deal and the implications for companies: The Green Deal comes with implications")
    thisalinea.textcontent.append("that ripple through the entire corporate ecosystem and provides companies with opportunities as well as")
    thisalinea.textcontent.append("the need to react to the changing regulatory and policy framework.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Analyse how companies currently address green transformation: Companies (and investors) are focusing ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 15
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Analyse how companies currently address green transformation: Companies (and investors) are focusing more and more on sustainability. The understanding of the methods, measures, and tools used by the companies for their green transformation is crucial to identify which gaps can be filled by the EU Space Programme. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Analyse how companies currently address green transformation: Companies (and investors) are focusing")
    thisalinea.textcontent.append("more and more on sustainability. The understanding of the methods, measures, and tools used by the")
    thisalinea.textcontent.append("companies for their green transformation is crucial to identify which gaps can be filled by the EU Space")
    thisalinea.textcontent.append("Programme.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Describe the full potential of EU Space data for green transformation: Present the way ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 16
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ Describe the full potential of EU Space data for green transformation: Present the way companies can use EU Space data and services to help them on their path towards sustainability. Provide an analysis to quantify and qualify current and future benefits (e.g., monetary, efficiency related) of using EU Space data and their value-added for green transformation. Show specific practical use cases of currently deployed applications. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Describe the full potential of EU Space data for green transformation: Present the way companies can")
    thisalinea.textcontent.append("use EU Space data and services to help them on their path towards sustainability. Provide an analysis to")
    thisalinea.textcontent.append("quantify and qualify current and future benefits (e.g., monetary, efficiency related) of using EU Space data")
    thisalinea.textcontent.append("and their value-added for green transformation. Show specific practical use cases of currently deployed")
    thisalinea.textcontent.append("applications.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Provide a call for action to companies: present a call for action for companies ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 17
    thisalinea.parentID = 13
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "▪ Provide a call for action to companies: present a call for action for companies that are less aware of the EU Space Programme benefits to engage with EUSPA to understand how to maximise the use of EU Space data and services to support their green transformation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Provide a call for action to companies: present a call for action for companies that are less aware of the")
    thisalinea.textcontent.append("EU Space Programme benefits to engage with EUSPA to understand how to maximise the use of EU Space")
    thisalinea.textcontent.append("data and services to support their green transformation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. INTRODUCTION Study context and approach"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 18
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Climate change is one of the biggest challenges of humanity and its severe impacts to society are just beginning to emerge. Greenhouse gas (GHG) emissions by human activities e.g., manufacturing, transport, energy production and distribution, agriculture are the most accountable to this phenomenon. Exhibit 3: Greenhouse gas emissions global and by sector To overcome climate change in the long term, we must drastically reduce anthropogenic emissions and encourage a strong shift towards sustainability and green transformation. In this context, much importance is given to our transition to a more sustainable way of living and working. This necessitates a shift in "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Climate change is one of the biggest challenges of humanity and its severe impacts to society are just beginning to")
    thisalinea.textcontent.append("emerge. Greenhouse gas (GHG) emissions by human activities e.g., manufacturing, transport, energy production and")
    thisalinea.textcontent.append("distribution, agriculture are the most accountable to this phenomenon.")
    thisalinea.textcontent.append("Exhibit 3: Greenhouse gas emissions global and by sector")
    thisalinea.textcontent.append("To overcome climate change in the long term, we must drastically reduce anthropogenic emissions and encourage")
    thisalinea.textcontent.append("a strong shift towards sustainability and green transformation. In this context, much importance is given to our")
    thisalinea.textcontent.append("transition to a more sustainable way of living and working. This necessitates a shift in thinking and in mode of")
    thisalinea.textcontent.append("operations – away from environmentally-harmful practices and unsustainable resource use and towards")
    thisalinea.textcontent.append("ecological mindfulness.")
    thisalinea.textcontent.append("The EU intends to be at the forefront of this shift and has enabled the European Green Deal that will actively")
    thisalinea.textcontent.append("support the 17 Sustainable Development Goals (SDGs) put forth by the United Nation’s 2030 Agenda5.")
    thisalinea.textcontent.append("The European Green Deal acts as a general directive with multiple targets, namely, supplying clean, affordable, and")
    thisalinea.textcontent.append("secure energy, mobilising industry for a clean circular economy, building and renovating in an energy- and resource-")
    thisalinea.textcontent.append("efficient way, moving to a toxic-free environment, preserving and restoring ecosystems and biodiversity, creating an")
    thisalinea.textcontent.append("environmentally friendly food system, and accelerating the shift to sustainable and smart mobility.")
    thisalinea.textcontent.append("The ultimate goal of the set of policies around the Green Deal is to make Europe the first climate-neutral continent")
    thisalinea.textcontent.append("and to achieve zero net emissions of greenhouse gases by 2050. This will be achieved by employing clean")
    thisalinea.textcontent.append("technologies across different industries to build a green economic model. An important milestone to reach this target")
    thisalinea.textcontent.append("is the reduction of emissions of at least 55% compared to 1990 levels already by 2030.")
    thisalinea.textcontent.append("The mission of the European Union Agency for the Space Programme (EUSPA) is to support the EU’s goal to")
    thisalinea.textcontent.append("achieve the highest return on the EU Space Programme's investment in terms of benefits to users, economic")
    thisalinea.textcontent.append("growth and industry competitiveness. The EU Space Programme, including its flagships Copernicus, Galileo and")
    thisalinea.textcontent.append("EGNOS, can be critical to supply the necessary information for Europe to make it more sustainable, and to support")
    thisalinea.textcontent.append("industry and policy makers to monitor environmental indicators, but also to reduce the environmental impacts.")
    thisalinea.textcontent.append("Copernicus, world’s most advanced Earth Observation system, has been monitoring the Earth’s environment for")
    thisalinea.textcontent.append("years, providing a unique combination of full, free and open data and thematic information services. The Copernicus")
    thisalinea.textcontent.append("Climate Change Service (C3S) provides past, current and future projections on climate and its changes, while the")
    thisalinea.textcontent.append("Copernicus Atmosphere Monitoring Service (CAMS) delivers data and information about air quality and its")
    thisalinea.textcontent.append("corresponding density of pollutants. Copernicus data supports governments and businesses to monitor industrial")
    thisalinea.textcontent.append("emissions sentinel-4 and Sentinel-5/5P have capabilities to acquire atmospheric measurements of the airborne")
    thisalinea.textcontent.append("pollutants such as COx and NOX with a high spatial-temporal resolution.")
    thisalinea.textcontent.append("Galileo and EGNOS contribute to the European Green Deal by providing accurate positioning, navigation and timing.")
    thisalinea.textcontent.append("The positioning signals, often in combination with Copernicus data, enable smart farming or precision agriculture")
    thisalinea.textcontent.append("that allows farmers to save fuel, pesticides and fertilisers, and limit water waste. Its benefits stretch along many")
    thisalinea.textcontent.append("sectors, with e.g., emission reduction for road transport and route optimisation in the maritime and aviation sectors.")
    thisalinea.textcontent.append("As the EU Space Programme is continuously expanding with more data, signals and services, more and more")
    thisalinea.textcontent.append("applications are enabled for governments and businesses, many supporting our common goal of a greener economy.")
    thisalinea.textcontent.append("Additional details about the European Global Navigation System and Copernicus are described in Annex 1.")
    thisalinea.textcontent.append("Exhibit 4: Examples of EU Space contribution to key elements of Green Transformation")
    thisalinea.textcontent.append("The cumulative environmental benefits enabled by the EU Space Programme in energy, road transport, aviation,")
    thisalinea.textcontent.append("agriculture, forestry, and mining are substantial. Tons of polluting emissions can be avoided, and more efficient")
    thisalinea.textcontent.append("use of our resources could save billions to the public and to businesses.")
    thisalinea.textcontent.append("Despite the ample benefits, the EU Space Programme still lacks awareness with industrial stakeholders. Most of")
    thisalinea.textcontent.append("the surveyed companies for this report state that they are currently not leveraging EU Space data in their pursuit")
    thisalinea.textcontent.append("of green transformation, but many are keen to explore how this data and signals can support this.")
    thisalinea.textcontent.append("The purpose of this study is to analyse the contribution of EU Space Programme data and services to the European")
    thisalinea.textcontent.append("Green Deal objectives for sustainability and show case how the EU Space Programme can support companies")
    thisalinea.textcontent.append("towards their green transformation paths.")
    thisalinea.textcontent.append("The overall study approach is based on four-steps, starting from the first two tasks to establish an understanding")
    thisalinea.textcontent.append("of the Green Deal’s objectives and action areas, as they pertain to changes in policy (1), and reflected in companies’")
    thisalinea.textcontent.append("green journeys (2). The third step entails the synthesis of various sustainability metrics to identify EU-based")
    thisalinea.textcontent.append("companies embracing the green transformation, to outline how EU Space can support (3), and interview companies")
    thisalinea.textcontent.append("to gain insights on how they tackled and monitored green transformation and environmental impacts in their")
    thisalinea.textcontent.append("respective sectors, and also on how EU Space Data contributed (if in any way yet) and might contribute in the future.")
    thisalinea.textcontent.append("Finally, the fourth step relates to the generation of informed recommendations (4) for the promotion of EU-Space")
    thisalinea.textcontent.append("to enable the green transformation in industry and help unlock efficiencies in companies’ sustainability and")
    thisalinea.textcontent.append("operations.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. THE GREEN TRANSFORMATION AND EU GREEN DEAL FOR BUSINESS IN EUROPE"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 19
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "The change in thinking observed across industry, policy and society towards more sustainable practices is often framed under the moniker of “green transformation”. In the subject literature, this term is mostly defined as actions aimed at creating equilibrium (agreement) between the economic growth and care for the environment, aimed at guaranteeing a high quality of life for both present and future generations at the level allowed by the civilisational development, and at the same time an effective and rational use of the available resources. This can be applied at individual level, e.g., single companies or at group level, e.g., single "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Green transformation market"
    thisalinea.titlefontsize = "15.959999999999923"
    thisalinea.nativeID = 20
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The change in thinking observed across industry, policy and society towards more sustainable practices is often framed under the moniker of “green transformation”. In the subject literature, this term is mostly defined as actions aimed at creating equilibrium (agreement) between the economic growth and care for the environment, aimed at guaranteeing a high quality of life for both present and future generations at the level allowed by the civilisational development, and at the same time an effective and rational use of the available resources. This can be applied at individual level, e.g., single companies or at group level, e.g., single "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The change in thinking observed across industry, policy and society towards more sustainable practices is often")
    thisalinea.textcontent.append("framed under the moniker of “green transformation”. In the subject literature, this term is mostly defined as actions")
    thisalinea.textcontent.append("aimed at creating equilibrium (agreement) between the economic growth and care for the environment, aimed at")
    thisalinea.textcontent.append("guaranteeing a high quality of life for both present and future generations at the level allowed by the civilisational")
    thisalinea.textcontent.append("development, and at the same time an effective and rational use of the available resources. This can be applied at")
    thisalinea.textcontent.append("individual level, e.g., single companies or at group level, e.g., single countries, continents, world.")
    thisalinea.textcontent.append("The green transformation is a dynamic process involving several sectors and actors of the economy and society,")
    thisalinea.textcontent.append("such as energy production, distribution and storage, agriculture and forestry, natural resource extraction, building")
    thisalinea.textcontent.append("construction and renovation, mobility, water supply and treatment, waste management, and environmental")
    thisalinea.textcontent.append("remediation. However, this process is not meant to be a simple transition to a new model of business, as it influences")
    thisalinea.textcontent.append("and requires changes in many aspects of everyday life, aiming to shift the entire societal cohort towards more")
    thisalinea.textcontent.append("sustainable behaviour, to help abate and mitigate climate change.")
    thisalinea.textcontent.append("The green transformation is not an idealised abstraction of society’s shift to sustainability, but rather a very tangible")
    thisalinea.textcontent.append("concept – one which can create, and boost markets.")
    thisalinea.textcontent.append("The EU itself plans to invest over €1 trillion over the next decade to support the European Green Deal.")
    thisalinea.textcontent.append("Exhibit 5: European Green Deal investment plan and action areas")
    thisalinea.textcontent.append("Exhibit 6: European Green Deal action areas")
    thisalinea.textcontent.append("As shown in Exhibit 7, the market size for the green transformation is expected to grow at an incredible pace")
    thisalinea.textcontent.append("(+21.9% CAGR) from 20202. Companies indeed have started considering pursuing sustainability targets as a key")
    thisalinea.textcontent.append("element of their narrative for their value proposition and competitive advantage.")
    thisalinea.textcontent.append("Exhibit 7: Global green transformation market2")
    thisalinea.textcontent.append("It is increasingly understood across industries that the green transformation stands for the right strategic, financial,")
    thisalinea.textcontent.append("and environmental direction. With a rapidly evolving policy framework exerting more and more pressure on")
    thisalinea.textcontent.append("businesses, building climate resilience through the green transformation is now more a necessity than a strategic")
    thisalinea.textcontent.append("niche. In addition, more stringent regulations imposing fines or trade impediments to avoid polluting practices and")
    thisalinea.textcontent.append("environmental damages (such as for the use of nitrogenous compounds in agriculture) is a clear market enabler for")
    thisalinea.textcontent.append("businesses to consider undergoing their own green transition.")
    thisalinea.textcontent.append("Many sectors have spearheaded the change, especially the ones under the most regulatory scrutiny – namely: energy,")
    thisalinea.textcontent.append("agriculture, and transport.")
    thisalinea.textcontent.append("Among the contributing factors to the success of the green transformation6 in the energy industry is a supportive")
    thisalinea.textcontent.append("regulatory environment. With ever-stricter regulations on the horizon, a funding and innovation framework")
    thisalinea.textcontent.append("conducive to sustainable change, and the complement of a shifting regulatory landscape in the automobile industry,")
    thisalinea.textcontent.append("legacy operators began to perform their transitions earlier than most. This, as discussed, will occur within most (if")
    thisalinea.textcontent.append("not all) other economic sectors, as regulation is rolled out at a fast pace; the period of incremental change is ending.")
    thisalinea.textcontent.append("Furthermore, supply-chain factors, such as the high volatility of input materials (coal, oil and gas) brought a further")
    thisalinea.textcontent.append("impetus to move away from legacy operations. Though not directly transferrable to all sectors, this example is highly")
    thisalinea.textcontent.append("illustrative of the need, and benefits of the green transformation, especially in the industries least adherent to")
    thisalinea.textcontent.append("sustainable practices.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ In energy, decarbonisation is seeing the phasing-out of legacy, carbon-rich energy sources including oil, ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 21
    thisalinea.parentID = 20
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ In energy, decarbonisation is seeing the phasing-out of legacy, carbon-rich energy sources including oil, coal, and natural gas. Large focus is also placed on improving the energy efficiency of distribution grids, housing, and industry "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ In energy, decarbonisation is seeing the phasing-out of legacy, carbon-rich energy sources including oil,")
    thisalinea.textcontent.append("coal, and natural gas. Large focus is also placed on improving the energy efficiency of distribution grids,")
    thisalinea.textcontent.append("housing, and industry")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The agricultural sector is focusing on significant technology-based reductions in land and resource use, ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 22
    thisalinea.parentID = 20
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ The agricultural sector is focusing on significant technology-based reductions in land and resource use, and the redirection of operations toward carbon capture (producing increased added value in net emissions reductions) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The agricultural sector is focusing on significant technology-based reductions in land and resource use,")
    thisalinea.textcontent.append("and the redirection of operations toward carbon capture (producing increased added value in net emissions")
    thisalinea.textcontent.append("reductions)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ In transport, the transition to electric powertrains has originated a now booming segment, with ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 23
    thisalinea.parentID = 20
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ In transport, the transition to electric powertrains has originated a now booming segment, with road vehicles on an exponential adoption path – in reaction to, and anticipation of shifting regulation in the early 2030s. Similarly, efforts on green aviation are growing. Improvements in urban and rural mobility infrastructure are also further integrating the sector into the digital sustainable era. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ In transport, the transition to electric powertrains has originated a now booming segment, with road")
    thisalinea.textcontent.append("vehicles on an exponential adoption path – in reaction to, and anticipation of shifting regulation in the early")
    thisalinea.textcontent.append("2030s. Similarly, efforts on green aviation are growing. Improvements in urban and rural mobility")
    thisalinea.textcontent.append("infrastructure are also further integrating the sector into the digital sustainable era.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Green transformation impact on business"
    thisalinea.titlefontsize = "15.959999999999923"
    thisalinea.nativeID = 24
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Though not expressly necessary, the green transformation is often tied with the use of modern, innovative digital tools. Digitalisation, in turn, supplies tools for optimisation to underpin many efficiencies in resource use and waste reduction, target tracking and monitoring, regulatory compliance, and the generation of decision-making data for long-term planning. Many of these tasks stand to benefit from the range of applications offered by EU Space data and signals. These efficiencies will be discussed to a greater extent in the coming sections, with associated tangible use-cases and, where possible, economic impact analyses. Significant investment is needed for the green transformation, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Though not expressly necessary, the green transformation is often tied with the use of modern, innovative digital")
    thisalinea.textcontent.append("tools. Digitalisation, in turn, supplies tools for optimisation to underpin many efficiencies in resource use and waste")
    thisalinea.textcontent.append("reduction, target tracking and monitoring, regulatory compliance, and the generation of decision-making data for")
    thisalinea.textcontent.append("long-term planning. Many of these tasks stand to benefit from the range of applications offered by EU Space data")
    thisalinea.textcontent.append("and signals. These efficiencies will be discussed to a greater extent in the coming sections, with associated tangible")
    thisalinea.textcontent.append("use-cases and, where possible, economic impact analyses.")
    thisalinea.textcontent.append("Significant investment is needed for the green transformation, covering the cost of the described process")
    thisalinea.textcontent.append("assessment and redesign, modernisation (including digital and other tools, such as space-based products and")
    thisalinea.textcontent.append("services, cloud computing, and others), as well as staff training and reskilling. Furthermore, it is necessary, for a")
    thisalinea.textcontent.append("business to successfully perform their green transformation, to capture and keep employee, stakeholder, and")
    thisalinea.textcontent.append("shareholder buy-in. In the early stages, there is often traction in overcoming the longstanding status quo of")
    thisalinea.textcontent.append("operations. This period is, nevertheless, characterised by exponential growth – slow at first, but very rapid once the")
    thisalinea.textcontent.append("first friction is overcome7.")
    thisalinea.textcontent.append("A conceptual illustration of the overall profits seen by a company over their green transformation is provided in the")
    thisalinea.textcontent.append("Exhibit below. As it has been the case in practice built upon Ørsted’s lessons learned8, it is likely for a company to")
    thisalinea.textcontent.append("undergo a period of losses during the initial investment and restructuring phase. Then comes a period of")
    thisalinea.textcontent.append("technological innovation and scale, diffusing benefits throughout the company (and supply chain), beginning to")
    thisalinea.textcontent.append("bring returns on the initial efforts and investment, on a rapid but steady upward slope, and then showing stabilised")
    thisalinea.textcontent.append("returns after a certain point.")
    thisalinea.textcontent.append("Exhibit 8: The green transformation investment returns curve")
    thisalinea.textcontent.append("In a shifting investor, consumer and employment landscape, the green transformation also brings advantages in")
    thisalinea.textcontent.append("terms of public perception. As described previously, gathering support and providing a sound strategic vision to key")
    thisalinea.textcontent.append("stakeholders around a business is key to the process. These include consumers and/or customers, policymakers,")
    thisalinea.textcontent.append("employees, and other stakeholders (suppliers, shareholders, board members, and others).")
    thisalinea.textcontent.append("Investors’ perspective")
    thisalinea.textcontent.append("From the investor standpoint, as discussed, ESG risks hold an ever more important place in the investment go-")
    thisalinea.textcontent.append("no-go decision process. Indicatively, 85% of Moody’s debt ratings in 2020 considered ESG risks as a material credit")
    thisalinea.textcontent.append("item3. In being such a deeply transformative process, the green transition offers the opportunity for a business to")
    thisalinea.textcontent.append("not only overhaul environmental bottlenecks and weaknesses, but also ones in the governance structure, as well as")
    thisalinea.textcontent.append("internal social standing (and belief). There lie direct benefits, therefore, for companies to appeal more to investors,")
    thisalinea.textcontent.append("thanks to their green transformation.")
    thisalinea.textcontent.append("Customers’ perspective")
    thisalinea.textcontent.append("There are arguably even stronger dynamics at play in consumer/customer perception. Multiple studies have been,")
    thisalinea.textcontent.append("and continue to be conducted on the subject, as it is a rapidly evolving, for reasons already described. Of the most")
    thisalinea.textcontent.append("notable trends is the ongoing shift in perception 9 of sustainable products from a niche category to rather an")
    thisalinea.textcontent.append("important aspect of all product categories, a clear example is provided by the study from Ferguson10 recognising")
    thisalinea.textcontent.append("how more than half of German and British consumers explicitly check for sustainable ingredients on shelf products")
    thisalinea.textcontent.append("in stores; and more than 70% of customers in those countries is aware of brands associated with environmental")
    thisalinea.textcontent.append("concerns. The increasing attention on the ESG and sustainability-related sides of a product or service also offers")
    thisalinea.textcontent.append("businesses the capacity for reduced costs. Thanks to the homogenisation of consumer preference toward")
    thisalinea.textcontent.append("sustainability, that aspect can be used as a singular marketing lever across different markets and regions, offering")
    thisalinea.textcontent.append("scale economies. It is important, nevertheless, to note that current data shows that, in certain sectors such as food,")
    thisalinea.textcontent.append("the traditional factors of price and quality remain more influential in mass consumer decisions than sustainability.11")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Green transformation in regulatory requirements"
    thisalinea.titlefontsize = "15.95999999999998"
    thisalinea.nativeID = 25
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The European Green Deal will have major structural implications for the EU economy in the coming decades, affecting everything from the way we produce and use power, to how we travel, heat our homes, and even how we eat. This is made possible through a series of policies which will be introduced or updated starting from already existing measures. Many of the policies put in place in the context of the European Green Deal will deeply affect business and operations of European companies. Those changes are all focused in improving European environmental conditions and making a greener and fairer society "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The European Green Deal will have major structural implications for the EU economy in the coming decades,")
    thisalinea.textcontent.append("affecting everything from the way we produce and use power, to how we travel, heat our homes, and even how we")
    thisalinea.textcontent.append("eat. This is made possible through a series of policies which will be introduced or updated starting from already")
    thisalinea.textcontent.append("existing measures.")
    thisalinea.textcontent.append("Many of the policies put in place in the context of the European Green Deal will deeply affect business and")
    thisalinea.textcontent.append("operations of European companies. Those changes are all focused in improving European environmental conditions")
    thisalinea.textcontent.append("and making a greener and fairer society")
    thisalinea.textcontent.append("To that end, in addition to the supportive policy environment the Green Deal will bring for the green transformation")
    thisalinea.textcontent.append("and sustainable innovation, disincentives will be put into place as well. Though not expressly defined yet to date, a")
    thisalinea.textcontent.append("comprehensive and cohesive system of fines and penalties will be set up (on top of mechanisms such as the")
    thisalinea.textcontent.append("Emissions Trading System) to define the price of non-compliance.")
    thisalinea.textcontent.append("A summary of the main changes to regulations proposed with the upcoming European Green Deal is shown in")
    thisalinea.textcontent.append("Exhibit 9. For businesses, there lies a great opportunity to synergistically capitalise on the EU Space Programme")
    thisalinea.textcontent.append("for their own sustainable transformation and monitoring, as well as for the improvement of their legal")
    thisalinea.textcontent.append("compliance.")
    thisalinea.textcontent.append("Those considerations are meant to be only indicative to provide with a general idea about potential applications of")
    thisalinea.textcontent.append("the EU Space in relation to Green Deal-related regulatory updates. Detailed use cases underlining how the EU")
    thisalinea.textcontent.append("Space applications are supporting/ can enable the green transformation and the journey of companies towards it,")
    thisalinea.textcontent.append("are provided in the following sections of this document.")
    thisalinea.textcontent.append("Exhibit 9: Summary & mapping of key regulation updates under the Green Deal and examples of EU Space applications12")
    thisalinea.textcontent.append("Examples of EU Space applications")
    thisalinea.textcontent.append("Examples of EU Space applications")
    thisalinea.textcontent.append("Examples of EU Space applications")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. THE ROLE OF THE EU SPACE PROGRAMME IN SUPPORTING COMPANIES ALONG THEIR SUSTAINABILITY JOURNEY"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 26
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "The European Union Space Programme in all its components has already been introduced previously in this report, together with a preliminary discussion about its role for the established Green Deal objectives. As anticipated, due to the higher impact on the topic, this report will focus primarily on the European Global Navigation Satellite Systems (EGNSS), including Galileo and EGNOS and Copernicus. As for the EGNSS, their role in support of the Green Deal’s ambitions for emissions reductions is crucial. A key example is the transport sector 13, including aviation, maritime, road, and rail transport. The sector contributes heavily to emissions in "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The European Union Space Programme in all its components has already been introduced previously in this report,")
    thisalinea.textcontent.append("together with a preliminary discussion about its role for the established Green Deal objectives. As anticipated, due")
    thisalinea.textcontent.append("to the higher impact on the topic, this report will focus primarily on the European Global Navigation Satellite")
    thisalinea.textcontent.append("Systems (EGNSS), including Galileo and EGNOS and Copernicus.")
    thisalinea.textcontent.append("As for the EGNSS, their role in support of the Green Deal’s ambitions for emissions reductions is crucial. A key")
    thisalinea.textcontent.append("example is the transport sector 13, including aviation, maritime, road, and rail transport. The sector contributes")
    thisalinea.textcontent.append("heavily to emissions in Europe. The EU’s goal is to lower them by 90% by 2050, to meet the overall net neutrality")
    thisalinea.textcontent.append("target set by the European Union.")
    thisalinea.textcontent.append("The development of GNSS-enabled Performance-Based Navigation (PBN) for aviation has been a breakthrough in")
    thisalinea.textcontent.append("that regard. Traditional route planning, using Ground-Based Augmentation Systems (GBAS), has required that a")
    thisalinea.textcontent.append("point-by-point path is taken, cruising between navigation data sources (e.g., beacons). Rather than compromising")
    thisalinea.textcontent.append("air routes to meet these requirements, Galileo and EGNOS allow planners to draft more direct paths between")
    thisalinea.textcontent.append("destinations, prioritising performance – and thus, lower fuel use and emissions – by providing a constant stream of")
    thisalinea.textcontent.append("navigation data and reducing (or eliminating) reliance on traditional GBAS. To that end, EGNSS data is also often")
    thisalinea.textcontent.append("more accurate, and safer than ground-based alternatives.")
    thisalinea.textcontent.append("Another use for EGNSS in aviation is Localiser Performance using Vertical guidance (LPV) approaches. Using")
    thisalinea.textcontent.append("EGNSS data, aircraft operators can involve more accurate data (compared to conventional sources) in landing")
    thisalinea.textcontent.append("procedures. That, in turn, allows automated manoeuvres which optimise performance and more closely follow the")
    thisalinea.textcontent.append("ideal landing line, leading directly again to fuel savings, and thus reducing emissions.")
    thisalinea.textcontent.append("In road transport, high-accuracy real-time EGNSS data, and Copernicus-based urban planning applications will")
    thisalinea.textcontent.append("ease the transition into optimised assisted and fully autonomous driving. The network of semi- and fully autonomous")
    thisalinea.textcontent.append("vehicles will then be able to cross-interface between vehicles, as well as with centralised control centres, using")
    thisalinea.textcontent.append("GNSS to regulate and monitor traffic, optimise vehicle inputs (throttle, steering, route planning), as well as make")
    thisalinea.textcontent.append("roads safer to run in.")
    thisalinea.textcontent.append("While EGNSS allow users to improve their operations making them more efficient, Copernicus becomes particularly")
    thisalinea.textcontent.append("useful when it comes to monitoring and having a better understanding of the environment around us. A concrete")
    thisalinea.textcontent.append("example is provided by the use of Copernicus data to precisely position renewable energy infrastructure14.")
    thisalinea.textcontent.append("The energy output in terms of watt-hour produced by sustainable sources like solar panels or wind turbines is highly")
    thisalinea.textcontent.append("dependent on their correct positioning. Not only the right site is fundamental, but even the correct orientation makes")
    thisalinea.textcontent.append("a significant difference. Copernicus services together with historical data provide energy companies with information")
    thisalinea.textcontent.append("about solar radiation and wind behaviours on a world-wide base, allowing them to make informed decisions and")
    thisalinea.textcontent.append("get the best from their infrastructure.")
    thisalinea.textcontent.append("A detailed discussion about EGNSS and Copernicus in support of Green Deal goals will be the core of this section")
    thisalinea.textcontent.append("of the report; it is important to understand that the role of the EU Space Programme for what concerns environmental")
    thisalinea.textcontent.append("matters is not something vague and uncountable, but already effective and tangible. For example, the EU Space")
    thisalinea.textcontent.append("already supports Green Deal aims such as CO2 reduction, smart mobility, cleaner energy production, and others. A")
    thisalinea.textcontent.append("summary of those achievements is provided in a study15 promoted by the European Commission of which some of")
    thisalinea.textcontent.append("the conclusions are reported in Exhibit 10.")
    thisalinea.textcontent.append("Exhibit 10: Estimated impact of the EU Space Programme on selected markets and on the environment15")
    thisalinea.textcontent.append("Since its first roll-out, Copernicus has been actively involved in monitoring pollution, land use, and waste")
    thisalinea.textcontent.append("management, among other applications, for example:")
    thisalinea.textcontent.append("Copernicus with the C3S service is a crucial asset for monitoring climate change as it produces, on a global scale")
    thisalinea.textcontent.append("basic climate variable describing the climate over time. More broadly, with its services and products, Copernicus")
    thisalinea.textcontent.append("directly supports the objectives set up by the European Green Deal.")
    thisalinea.textcontent.append("Exhibit 11: Summary of the most relevant Copernicus services and products for the Green Deal objectives")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("objective")
    thisalinea.textcontent.append("Copernicus data and")
    thisalinea.textcontent.append("information involved")
    thisalinea.textcontent.append("Specific examples of products")
    thisalinea.textcontent.append("Atmosphere Monitoring")
    thisalinea.textcontent.append("(CAMS)")
    thisalinea.textcontent.append("Marine Env. Monitoring")
    thisalinea.textcontent.append("(CMEMS)")
    thisalinea.textcontent.append("Achieve")
    thisalinea.textcontent.append("climate")
    thisalinea.textcontent.append("neutrality")
    thisalinea.textcontent.append("Land Monitoring (CLMS)")
    thisalinea.textcontent.append("Climate Change (C3S) ▪ Climate projections")
    thisalinea.textcontent.append("Copernicus Sentinels")
    thisalinea.textcontent.append("Atmosphere Monitoring")
    thisalinea.textcontent.append("(CAMS)")
    thisalinea.textcontent.append("Land Monitoring (CLMS)")
    thisalinea.textcontent.append("Copernicus Sentinels")
    thisalinea.textcontent.append("Atmosphere Monitoring")
    thisalinea.textcontent.append("(CAMS)")
    thisalinea.textcontent.append("Land Monitoring (CLMS) ▪ Lake water quality")
    thisalinea.textcontent.append("Copernicus Sentinels")
    thisalinea.textcontent.append("Atmosphere Monitoring")
    thisalinea.textcontent.append("(CAMS)")
    thisalinea.textcontent.append("Marine Environment")
    thisalinea.textcontent.append("Monitoring (CMEMS)")
    thisalinea.textcontent.append("Land Monitoring (CLMS)")
    thisalinea.textcontent.append("Clean the")
    thisalinea.textcontent.append("industrial")
    thisalinea.textcontent.append("revolution")
    thisalinea.textcontent.append("Make")
    thisalinea.textcontent.append("transport")
    thisalinea.textcontent.append("sustainable")
    thisalinea.textcontent.append("for all")
    thisalinea.textcontent.append("Restore")
    thisalinea.textcontent.append("ecosystems")
    thisalinea.textcontent.append("and")
    thisalinea.textcontent.append("biodiversity")
    thisalinea.textcontent.append("Copernicus Sentinels ▪ Sentinel-1 and Sentinel-2 for deforestation monitoring")
    thisalinea.textcontent.append("Atmosphere Monitoring")
    thisalinea.textcontent.append("(CAMS)")
    thisalinea.textcontent.append("Marine Environment")
    thisalinea.textcontent.append("Monitoring (CMEMS)")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("objective")
    thisalinea.textcontent.append("Copernicus data and")
    thisalinea.textcontent.append("information involved")
    thisalinea.textcontent.append("Specific examples of products")
    thisalinea.textcontent.append("Renovate")
    thisalinea.textcontent.append("buildings for")
    thisalinea.textcontent.append("greener")
    thisalinea.textcontent.append("lifestyles")
    thisalinea.textcontent.append("Atmosphere Monitoring")
    thisalinea.textcontent.append("(CAMS)")
    thisalinea.textcontent.append("Land Monitoring (CLMS) ▪ Urban Atlas")
    thisalinea.textcontent.append("Climate Change (C3S) ▪ Urban Heat Islands")
    thisalinea.textcontent.append("Copernicus Sentinels")
    thisalinea.textcontent.append("Marine Environment")
    thisalinea.textcontent.append("Monitoring (CMEMS)")
    thisalinea.textcontent.append("Build a")
    thisalinea.textcontent.append("healthier and")
    thisalinea.textcontent.append("greener food")
    thisalinea.textcontent.append("system")
    thisalinea.textcontent.append("Land Monitoring (CLMS)")
    thisalinea.textcontent.append("Climate Change (C3S) ▪ Bioclimatic indicators")
    thisalinea.textcontent.append("The role of the EU Space for Green Deal objectives and companies’ journey in the green transformation can be at")
    thisalinea.textcontent.append("the highest level possible simplified into two macro-categories: environmental monitoring and environmental")
    thisalinea.textcontent.append("footprint reduction, as defined in Exhibit 12. These two topics will be the core of the rest of this chapter and will be")
    thisalinea.textcontent.append("tackled from the perspective of companies.")
    thisalinea.textcontent.append("Exhibit 12: Role of EU Space for green transformation - definitions of environmental monitoring")
    thisalinea.textcontent.append("and footprint reduction")
    thisalinea.textcontent.append("A first good example of the importance and benefit of the EU Space Programme for environmental monitoring is")
    thisalinea.textcontent.append("provided by the insurance sector which relies more and more on space data in case of catastrophic events to")
    thisalinea.textcontent.append("speed up refunding procedures helping affected populations to start reconstruction in the shortest time possible. A")
    thisalinea.textcontent.append("detailed use case is provided in Exhibit below.")
    thisalinea.textcontent.append("Exhibit 13: Use case - EU Space Programme for insurance companies")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Monitoring insured assets")
    thisalinea.textcontent.append("The insurance sector accounts globally for €5 trillion, and it is undergoing a profound evolution")
    thisalinea.textcontent.append("driven by digital transformation. Collaboration between traditional insurers and InsurTech firms")
    thisalinea.textcontent.append("will give rise to newer business models and revenue streams aiming at higher profitability and")
    thisalinea.textcontent.append("reduced operational costs.")
    thisalinea.textcontent.append("In the context of digitalisation, many of the traditional activities performed by insurers are now")
    thisalinea.textcontent.append("highly dependent on the availability of large quantities of reliable data. Players in the sector are")
    thisalinea.textcontent.append("eager to have both more precise risk models, and reliable asset monitoring systems to make their")
    thisalinea.textcontent.append("operations more sustainable and therefore more profitable.")
    thisalinea.textcontent.append("Having access to funds and resources coming from insurance companies' reimbursements in the")
    thisalinea.textcontent.append("shortest possible time can be vital for people. The typical process can be very tricky and")
    thisalinea.textcontent.append("inefficient, especially in cases of areas where access for insurance inspectors can be difficult due")
    thisalinea.textcontent.append("to the occurred phenomena. Using satellite imagery for monitoring the affected areas, not only")
    thisalinea.textcontent.append("can speed up those processes improving the life quality of affected people letting them to go back")
    thisalinea.textcontent.append("to normality and reduce logistic costs for insurance companies. Post-event damage assessment,")
    thisalinea.textcontent.append("asset monitoring and risk modelling driven by satellite data provide a reliable and up-to-date")
    thisalinea.textcontent.append("date tool for insurance companies. In case of catastrophic events, many of the claims issued to")
    thisalinea.textcontent.append("insurance companies can be addressed using space data. Satellite pre-disaster images are")
    thisalinea.textcontent.append("matched with post-event ones to detect changes and highlight the entity of damages and")
    thisalinea.textcontent.append("speed up claims management and funds unlocking.")
    thisalinea.textcontent.append("Companies such as SkyTek are combining Copernicus data with commercially available ones to")
    thisalinea.textcontent.append("address those topics.")
    thisalinea.textcontent.append("Exhibit 14: Value chain and position of EO space data in insurance sector")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU")
    thisalinea.textcontent.append("Space")
    thisalinea.textcontent.append("providers16")
    thisalinea.textcontent.append("As shown in the use case presented above, open and free access to the European Union’s Copernicus Earth")
    thisalinea.textcontent.append("Observation data, analyses, maps, and forecasts stimulated innovation, providing young companies like Skytek, GAF,")
    thisalinea.textcontent.append("Earthpulse and others with the ability to build, test, and deploy value-adding services17.")
    thisalinea.textcontent.append("Now that the general picture and definitions about the EU Space and its role in supporting the objectives of the")
    thisalinea.textcontent.append("Green Deal have been clarified, the next sections of this document will focus on providing the reader with specific")
    thisalinea.textcontent.append("examples and use cases about the two areas defined in the Exhibit 12.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ The Copernicus Atmosphere Monitoring Service (CAMS) provides daily forecasts of global air quality ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 27
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ The Copernicus Atmosphere Monitoring Service (CAMS) provides daily forecasts of global air quality that public and private authorities can use to determine citizens’ exposure to pollutants such as aerosols and particulates. It is also useful for air traffic control in case of volcanic activity. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The Copernicus Atmosphere Monitoring Service (CAMS) provides daily forecasts of global air quality")
    thisalinea.textcontent.append("that public and private authorities can use to determine citizens’ exposure to pollutants such as aerosols")
    thisalinea.textcontent.append("and particulates. It is also useful for air traffic control in case of volcanic activity.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ The Copernicus Marine Service (CMEMS) oversees water quality monitoring and forecasting of pollutants ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 28
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ The Copernicus Marine Service (CMEMS) oversees water quality monitoring and forecasting of pollutants such as nitrates, phosphates, and dissolved iron in the sea from land and especially along the coast, but also monitors organic pollution such as algal blooms, which are increasing with global warming and eutrophication of the water. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The Copernicus Marine Service (CMEMS) oversees water quality monitoring and forecasting of pollutants")
    thisalinea.textcontent.append("such as nitrates, phosphates, and dissolved iron in the sea from land and especially along the coast, but")
    thisalinea.textcontent.append("also monitors organic pollution such as algal blooms, which are increasing with global warming and")
    thisalinea.textcontent.append("eutrophication of the water.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ The European Maritime Safety Agency (EMSA) uses Sentinel satellite imagery to monitor sea pollution ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 29
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ The European Maritime Safety Agency (EMSA) uses Sentinel satellite imagery to monitor sea pollution such as oil spills and other polluters. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The European Maritime Safety Agency (EMSA) uses Sentinel satellite imagery to monitor sea pollution")
    thisalinea.textcontent.append("such as oil spills and other polluters.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ The Copernicus Land Monitoring Service monitors changes in grassland rich Natura2000 hotspots for ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 30
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "▪ The Copernicus Land Monitoring Service monitors changes in grassland rich Natura2000 hotspots for nature conservation, to figure out whether these sites are being effectively preserved or if a decline in loss of biodiversity is halted. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The Copernicus Land Monitoring Service monitors changes in grassland rich Natura2000 hotspots for")
    thisalinea.textcontent.append("nature conservation, to figure out whether these sites are being effectively preserved or if a decline in loss")
    thisalinea.textcontent.append("of biodiversity is halted.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Anthropogenic and natural emissions "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 31
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "▪ Anthropogenic and natural emissions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Anthropogenic and natural emissions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Global ship emissions "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 32
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "▪ Global ship emissions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Global ship emissions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Eutrophication "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 33
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "▪ Eutrophication "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Eutrophication")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Lake water quality "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 34
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "▪ Lake water quality "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Lake water quality")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Natura2000 "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 35
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "▪ Natura2000 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Natura2000")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ CORINE Land Cover "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 36
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "▪ CORINE Land Cover "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ CORINE Land Cover")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-4, Sentinel-5 and Sentinel-5P for monitoring of ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 37
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "▪ Sentinel-4, Sentinel-5 and Sentinel-5P for monitoring of emissions of trace gases and air quality "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-4, Sentinel-5 and Sentinel-5P for monitoring of")
    thisalinea.textcontent.append("emissions of trace gases and air quality")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Air quality analyses and forecasts "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 38
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "▪ Air quality analyses and forecasts "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Air quality analyses and forecasts")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Anthropogenic emissions "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 39
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "▪ Anthropogenic emissions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Anthropogenic emissions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ CORINE Land Cover "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 40
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "▪ CORINE Land Cover "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ CORINE Land Cover")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Natura2000 "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 41
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "▪ Natura2000 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Natura2000")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-2 for evidence supporting the evaluation of green ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 42
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "▪ Sentinel-2 for evidence supporting the evaluation of green claims "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-2 for evidence supporting the evaluation of green")
    thisalinea.textcontent.append("claims")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Anthropogenic emissions "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 43
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = "▪ Anthropogenic emissions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Anthropogenic emissions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Global ship emissions "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 44
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "▪ Global ship emissions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Global ship emissions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-1 for oil spill monitoring at sea, Sentinel-2 for oil spill ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 45
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "▪ Sentinel-1 for oil spill monitoring at sea, Sentinel-2 for oil spill monitoring on land "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-1 for oil spill monitoring at sea, Sentinel-2 for oil spill")
    thisalinea.textcontent.append("monitoring on land")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Air quality analyses and forecasts "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 46
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = "▪ Air quality analyses and forecasts "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Air quality analyses and forecasts")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Primary productivity "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 47
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "▪ Primary productivity "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Primary productivity")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sea surface temperature "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 48
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "▪ Sea surface temperature "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sea surface temperature")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Street tree layer "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 49
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 22
    thisalinea.summary = "▪ Street tree layer "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Street tree layer")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Urban atlas "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 50
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 23
    thisalinea.summary = "▪ Urban atlas "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Urban atlas")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Natura2000 "
    thisalinea.titlefontsize = "8.999999999999972"
    thisalinea.nativeID = 51
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 24
    thisalinea.summary = "▪ Natura2000 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Natura2000")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ High resolution layers "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 52
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 25
    thisalinea.summary = "▪ High resolution layers "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ High resolution layers")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Solar radiation "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 53
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 26
    thisalinea.summary = "▪ Solar radiation "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Solar radiation")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sea surface wave forecasts "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 54
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 27
    thisalinea.summary = "▪ Sea surface wave forecasts "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sea surface wave forecasts")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sea surface wind ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 55
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 28
    thisalinea.summary = "▪ Sea surface wind Supply clean energy "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sea surface wind")
    thisalinea.textcontent.append("Supply clean")
    thisalinea.textcontent.append("energy")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-1 for sea surface waves and wind, wake analysis of ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 56
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 29
    thisalinea.summary = "▪ Sentinel-1 for sea surface waves and wind, wake analysis of Copernicus Sentinels offshore wind farms "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-1 for sea surface waves and wind, wake analysis of")
    thisalinea.textcontent.append("Copernicus Sentinels")
    thisalinea.textcontent.append("offshore wind farms")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-2 for biomass estimation "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 57
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 30
    thisalinea.summary = "▪ Sentinel-2 for biomass estimation "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-2 for biomass estimation")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Anthropogenic emissions "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 58
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 31
    thisalinea.summary = "▪ Anthropogenic emissions "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Anthropogenic emissions")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-3 for urban heat island monitoring "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 59
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 32
    thisalinea.summary = "▪ Sentinel-3 for urban heat island monitoring "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-3 for urban heat island monitoring")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Copernicus expansion mission LSTM for high resolution urban ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 60
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 33
    thisalinea.summary = "▪ Copernicus expansion mission LSTM for high resolution urban heat island monitoring for more precise building heat loss detection "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Copernicus expansion mission LSTM for high resolution urban")
    thisalinea.textcontent.append("heat island monitoring for more precise building heat loss")
    thisalinea.textcontent.append("detection")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Eutrophication "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 61
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 34
    thisalinea.summary = "▪ Eutrophication "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Eutrophication")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Chlorophyll-a "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 62
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 35
    thisalinea.summary = "▪ Chlorophyll-a "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Chlorophyll-a")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Primary production "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 63
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 36
    thisalinea.summary = "▪ Primary production "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Primary production")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Oxygen "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 64
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 37
    thisalinea.summary = "▪ Oxygen "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Oxygen")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Salinity and acidity "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 65
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 38
    thisalinea.summary = "▪ Salinity and acidity "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Salinity and acidity")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ CORINE Land Use/Land Cover "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 66
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 39
    thisalinea.summary = "▪ CORINE Land Use/Land Cover "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ CORINE Land Use/Land Cover")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Lake water quality "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 67
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 40
    thisalinea.summary = "▪ Lake water quality "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Lake water quality")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-1 for detecting illegal, unreported and unregulated ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 68
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 41
    thisalinea.summary = "▪ Sentinel-1 for detecting illegal, unreported and unregulated fishing Copernicus Sentinels "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-1 for detecting illegal, unreported and unregulated")
    thisalinea.textcontent.append("fishing")
    thisalinea.textcontent.append("Copernicus Sentinels")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-2 for deforestation and afforestation monitoring "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 69
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 42
    thisalinea.summary = "▪ Sentinel-2 for deforestation and afforestation monitoring "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-2 for deforestation and afforestation monitoring")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Sentinel-2 for crop growth monitoring for precise fertiliser and ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 70
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 43
    thisalinea.summary = "▪ Sentinel-2 for crop growth monitoring for precise fertiliser and pesticide application in agriculture "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Sentinel-2 for crop growth monitoring for precise fertiliser and")
    thisalinea.textcontent.append("pesticide application in agriculture")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ Climate change is making weather-related catastrophic events more and more common, ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 71
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 44
    thisalinea.summary = "▪ Climate change is making weather-related catastrophic events more and more common, leaving populations affected to deal with reconstruction, massive losses in terms of households and lives "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Climate change is making weather-related catastrophic events more and more common,")
    thisalinea.textcontent.append("leaving populations affected to deal with reconstruction, massive losses in terms of")
    thisalinea.textcontent.append("households and lives")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ The “aftermath” of an extreme event includes reconstruction and damage assessment which ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 72
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 45
    thisalinea.summary = "▪ The “aftermath” of an extreme event includes reconstruction and damage assessment which involve the affected population, governments, civil protection agencies, NGOs, insurance companies and other stakeholders. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The “aftermath” of an extreme event includes reconstruction and damage assessment which")
    thisalinea.textcontent.append("involve the affected population, governments, civil protection agencies, NGOs, insurance")
    thisalinea.textcontent.append("companies and other stakeholders.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "▪ The European Green Deal promotes the shift towards a more just society in which ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 73
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 46
    thisalinea.summary = "▪ The European Green Deal promotes the shift towards a more just society in which economic resources are more easily accessible to the population, especially in case of emergency such as a catastrophic weather-related event "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The European Green Deal promotes the shift towards a more just society in which economic")
    thisalinea.textcontent.append("resources are more easily accessible to the population, especially in case of emergency such")
    thisalinea.textcontent.append("as a catastrophic weather-related event")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Role of the EU Space in monitoring green transformation targets"
    thisalinea.titlefontsize = "15.959999999999923"
    thisalinea.nativeID = 74
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 47
    thisalinea.summary = "Environmental monitoring activities are carried out on soil, atmosphere, and water by companies and institutions with the scope to assess how human activities are interfering with the biosphere. Historically, those activities always involved a first, in-situ sample collection, followed by a specific analysis process, and a final data categorisation and visualisation. All the processes mentioned above are very resource-intensive, requiring personnel on the ground to either conduct sensor maintenance or to physically collect samples. The next paragraphs show how the EU Space Programme, and in particular Copernicus, can be used by institutional and commercial players to make environmental monitoring more "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Environmental monitoring activities are carried out on soil, atmosphere, and water by companies and institutions")
    thisalinea.textcontent.append("with the scope to assess how human activities are interfering with the biosphere.")
    thisalinea.textcontent.append("Historically, those activities always involved a first, in-situ sample collection, followed by a specific analysis")
    thisalinea.textcontent.append("process, and a final data categorisation and visualisation.")
    thisalinea.textcontent.append("All the processes mentioned above are very resource-intensive, requiring personnel on the ground to either")
    thisalinea.textcontent.append("conduct sensor maintenance or to physically collect samples.")
    thisalinea.textcontent.append("The next paragraphs show how the EU Space Programme, and in particular Copernicus, can be used by institutional")
    thisalinea.textcontent.append("and commercial players to make environmental monitoring more efficient and effective. Not only does the use of")
    thisalinea.textcontent.append("space data allows to free up human and economic resources otherwise necessary, but it also makes possible more")
    thisalinea.textcontent.append("frequent monitoring of areas difficult to be reached by human personnel.")
    thisalinea.textcontent.append("Environmental monitoring is mandatory for certain companies, especially in the manufacturing industry. Monitoring")
    thisalinea.textcontent.append("procedures are hard coded in countless regulations and standards; therefore, they are a topic very resistant to")
    thisalinea.textcontent.append("innovation, leaving only limited room for the EU Space Programme, likely to only cover a secondary/support role in")
    thisalinea.textcontent.append("the meaning of for example quickly identify risks and issues in companies’ infrastructure.")
    thisalinea.textcontent.append("ESG is becoming a crucial aspect for modern companies, and it is foreseen to have much higher relevance in light of")
    thisalinea.textcontent.append("the upcoming Green Deal relevant new regulations issued by the European Institutions.")
    thisalinea.textcontent.append("Following the original directive about non-financial reporting issued by the European Union, the European")
    thisalinea.textcontent.append("Commission adopted in 2021 a proposal for the Corporate Sustainability Reporting Directive (CSRD),")
    thisalinea.textcontent.append("encompassing a series of measures issued to ensure that large companies are required to report not only on financial")
    thisalinea.textcontent.append("matters, but also on sustainability issues such as environmental footprint, social rights, human rights and")
    thisalinea.textcontent.append("governance factors (i.e., ESG reporting). Starting in 2024, initially large companies (i.e., more than 500")
    thisalinea.textcontent.append("employees), followed by listed SMEs, will have to embrace the CSRD to continue their operations in the European")
    thisalinea.textcontent.append("Union.")
    thisalinea.textcontent.append("Exhibit 15: ESG main evaluation areas")
    thisalinea.textcontent.append("Pushed by the change in non-financial reporting regulation, environmental monitoring with the purpose of")
    thisalinea.textcontent.append("measuring ESG scores is an emerging and promising topic, yet in its development phases, and so more likely to")
    thisalinea.textcontent.append("embrace innovation and new approaches. Therefore, the use of space data not only can be beneficial, but Copernicus")
    thisalinea.textcontent.append("data might also be considered in the future as a standard for monitoring and measuring environmental indicators. In")
    thisalinea.textcontent.append("this section, we will first provide a general introduction to ESG, and then we will focus on how the EU Space")
    thisalinea.textcontent.append("Programme is currently integrated or can be integrated in the measurement of environmental KPIs.")
    thisalinea.textcontent.append("Through the past half century, as shown in the earlier sections, topics such as global climate change, environment,")
    thisalinea.textcontent.append("and sustainability have gained increasing importance. Companies are more and more sensitive to those topics,")
    thisalinea.textcontent.append("high attention is given to those processes aimed at monitoring emissions and environmental footprint of companies’")
    thisalinea.textcontent.append("operations, and, when possible, reducing them.")
    thisalinea.textcontent.append("Furthermore, in the latest years, we have seen the rise of a social consciousness devoted to “save the planet”")
    thisalinea.textcontent.append("through actions aimed to achieve a more sustainable society and economy. Companies recognised as")
    thisalinea.textcontent.append("environmentally friendly are better placed to get new customers, new investors, and even new employees. On the")
    thisalinea.textcontent.append("other hand, possible investors might find a company unattractive if its brand is linked to poor environmental")
    thisalinea.textcontent.append("practices, and therefore they might prefer not to associate with it.")
    thisalinea.textcontent.append("A good instrument to evaluate the performance of a company in terms of environmental effort and impact is the ESG")
    thisalinea.textcontent.append("scoring. Environmental, social, and corporate governance (ESG) is an approach to evaluate efforts of a company")
    thisalinea.textcontent.append("towards social goals beyond the core business of the organisation itself. More specifically:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ Air monitoring combines emissions, meteorological, and topographic data to detect and predict the ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 75
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Air monitoring combines emissions, meteorological, and topographic data to detect and predict the concentration of air pollutants in a determined aria. Environmental data is typically gathered using specialised sensor networks placed locally in high-risk areas. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Air monitoring combines emissions, meteorological, and topographic data to detect and predict the")
    thisalinea.textcontent.append("concentration of air pollutants in a determined aria. Environmental data is typically gathered using")
    thisalinea.textcontent.append("specialised sensor networks placed locally in high-risk areas.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ Soil monitoring typically requires operators to grab and analyse soil samples to detect phenomena ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 76
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Soil monitoring typically requires operators to grab and analyse soil samples to detect phenomena such as acidification, biodiversity loss, contamination, erosion, organic material loss, salinization, and slope instability. Main parameters on study are salinity, which, if imbalanced, can cause detrimental effects on water quality and plant yield; chemical contaminations coming from toxic elements, such as nuclear waste, coal ash, microplastics, petrochemicals, and acid rain, which can lead to the development of pollution- related diseases if in contact with humans or animals; and erosion due to factors such as rainfall, surface runoff, rivers, streams, floods, wind, mass movement, soil composition "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Soil monitoring typically requires operators to grab and analyse soil samples to detect phenomena such as")
    thisalinea.textcontent.append("acidification, biodiversity loss, contamination, erosion, organic material loss, salinization, and slope")
    thisalinea.textcontent.append("instability. Main parameters on study are salinity, which, if imbalanced, can cause detrimental effects on")
    thisalinea.textcontent.append("water quality and plant yield; chemical contaminations coming from toxic elements, such as nuclear waste,")
    thisalinea.textcontent.append("coal ash, microplastics, petrochemicals, and acid rain, which can lead to the development of pollution-")
    thisalinea.textcontent.append("related diseases if in contact with humans or animals; and erosion due to factors such as rainfall, surface")
    thisalinea.textcontent.append("runoff, rivers, streams, floods, wind, mass movement, soil composition and structure, topography, and lack")
    thisalinea.textcontent.append("of vegetation management.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ Water monitoring, is usually performed through the acquisition of samples from any water source ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 77
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ Water monitoring, is usually performed through the acquisition of samples from any water source (e.g., see, rivers, lakes, drinking water sources, etc.) to measure and monitor parameters such as biological presence, chemical content, and microbiological parameters. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Water monitoring, is usually performed through the acquisition of samples from any water source (e.g.,")
    thisalinea.textcontent.append("see, rivers, lakes, drinking water sources, etc.) to measure and monitor parameters such as biological")
    thisalinea.textcontent.append("presence, chemical content, and microbiological parameters.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The environmental criteria, include factors such as the energy used and wasted by a company, the use of"
    thisalinea.titlefontsize = "11.04000000000002"
    thisalinea.nativeID = 78
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "resources, carbon emissions, and contribution to climate change. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("resources, carbon emissions, and contribution to climate change.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The social criteria, address the relationships the company has and the reputation it fosters with people and"
    thisalinea.titlefontsize = "11.04000000000002"
    thisalinea.nativeID = 79
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "institutions in the communities where the business is active. Factors such as fair treatment of employees, diversity and inclusion are accounted for. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("institutions in the communities where the business is active. Factors such as fair treatment of employees,")
    thisalinea.textcontent.append("diversity and inclusion are accounted for.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The governance criteria are the internal system of practices, controls, and procedures companies adopt to"
    thisalinea.titlefontsize = "11.039999999999992"
    thisalinea.nativeID = 80
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "govern themselves. Companies are nowadays giving significant relevance to ESG – often driven by capital markets creating pressure to achieve progress in this dimension. Shareholders and investors seek reflective and progressive policies in all three of these realms and use it as a tool to weigh up a business’ overall sustainable performance. Customers and channel partners are increasingly weighing in ESG compliance into their purchase decisions. Lastly, employees and recruitment candidates value the sustainability ambition of their (potential) employer. The graph below outlines the ESG framework adopted by Henkel, as an example. Exhibit 16: Example - ESG goals and KPIs "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("govern themselves.")
    thisalinea.textcontent.append("Companies are nowadays giving significant relevance to ESG – often driven by capital markets creating pressure to")
    thisalinea.textcontent.append("achieve progress in this dimension. Shareholders and investors seek reflective and progressive policies in all three")
    thisalinea.textcontent.append("of these realms and use it as a tool to weigh up a business’ overall sustainable performance. Customers and channel")
    thisalinea.textcontent.append("partners are increasingly weighing in ESG compliance into their purchase decisions. Lastly, employees and")
    thisalinea.textcontent.append("recruitment candidates value the sustainability ambition of their (potential) employer.")
    thisalinea.textcontent.append("The graph below outlines the ESG framework adopted by Henkel, as an example.")
    thisalinea.textcontent.append("Exhibit 16: Example - ESG goals and KPIs adopted by Henkel")
    thisalinea.textcontent.append("The increasing importance ESG is acquiring in the modern society and way to do business, is well exemplified by a")
    thisalinea.textcontent.append("recent study estimating that for certain industries the share of profit at stake in case of significant modifications")
    thisalinea.textcontent.append("in environmental and social policies can reach up to 60%18.")
    thisalinea.textcontent.append("Exhibit 17: Estimated share of EBITDA at risk due to ESG negative performance by industry")
    thisalinea.textcontent.append("All these factors together made ESG a predominant topic in companies’ directive boards, and the currently given")
    thisalinea.textcontent.append("attention is only expected to grow in the next years boosted by ambitious targets such as the European Union")
    thisalinea.textcontent.append("climate neutrality in 2050, and new regulations such as from the European Green Deal, committing the Union to")
    thisalinea.textcontent.append("pursue a more sustainable and inclusive society.")
    thisalinea.textcontent.append("In the recent BCG-INSEAD “Board ESG Pulse")
    thisalinea.textcontent.append("Check” found that 70% of directors are only")
    thisalinea.textcontent.append("moderately or not at all effective at")
    thisalinea.textcontent.append("integrating ESG into company strategy and")
    thisalinea.textcontent.append("governance.")
    thisalinea.textcontent.append("Given the importance of ESG role in the modern corporate life, a reliable assessment and scoring system is necessary.")
    thisalinea.textcontent.append("It needs to be objective, accurate and consistent. It should be able to provide comparable scores for businesses")
    thisalinea.textcontent.append("across sectors and geographies. Given the global reach of space assets and their known ability to impact SDGs,")
    thisalinea.textcontent.append("it is high time to investigate systematically space data and services contribution to the corporate ESG world.")
    thisalinea.textcontent.append("Please refer to the following sections showing on how EU Space can contribute to ESG monitoring and reporting, in")
    thisalinea.textcontent.append("particular, Exhibit 21 shows some examples of relevant KPIs to be monitored and how EU Space can be beneficial")
    thisalinea.textcontent.append("in doing that.")
    thisalinea.textcontent.append("ESG Monitoring ecosystems and value chains are still under development. The business world has gone a long way")
    thisalinea.textcontent.append("from initial alibi-reporting and upgraded Corporate Social Responsibility (CSR) reporting. Rightly so, some of these")
    thisalinea.textcontent.append("efforts have and are being criticised by media and Non-Governmental Organisations (NGOs) as greenwashing. The")
    thisalinea.textcontent.append("finance world is gradually adopting ESG products and mechanisms to track this.")
    thisalinea.textcontent.append("Four major drivers of activity can be observed:")
    thisalinea.textcontent.append("In recent years, several ratings and certification schemes have been created to assess organisations’ performance")
    thisalinea.textcontent.append("in those matters. These companies provide information to users by cross-checking input from assessed companies")
    thisalinea.textcontent.append("to avoid misleading practices like the greenwashing19. Among the most relevant are the B Corporation Certification,")
    thisalinea.textcontent.append("the Sustainalytics Risk Index, and the Corporate Knights Rating.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "A) Increasing sophistication of top down ESG rating "
    thisalinea.titlefontsize = "9.479999999999961"
    thisalinea.nativeID = 81
    thisalinea.parentID = 80
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "A) Increasing sophistication of top down ESG rating "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("A) Increasing sophistication of top down ESG rating")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The B Corporation Certification (also B Corp) is issued by B Lab, a non-profit organisation, to those"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 82
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "companies that score a minimum of 80 points (out of 200) in an assessment about social and environmental sustainability. Even though, a B Corp Certification, does not bring any legal significance to the holding companies, it is globally recognised as a powerful branding tool to build trust in consumers, investors, and suppliers and to attract and retain employees. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("companies that score a minimum of 80 points (out of 200) in an assessment about social and environmental")
    thisalinea.textcontent.append("sustainability. Even though, a B Corp Certification, does not bring any legal significance to the holding")
    thisalinea.textcontent.append("companies, it is globally recognised as a powerful branding tool to build trust in consumers, investors, and")
    thisalinea.textcontent.append("suppliers and to attract and retain employees.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The Sustainalytics Risk Index is issued by the Dutch private firm Sustainalytics to assess companies'"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 83
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "exposure to long-term environmental, social, and governance risks. It is useful both for companies themselves for targeted marketing programmes, and investors to find potential risks and opportunities "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("exposure to long-term environmental, social, and governance risks. It is useful both for companies")
    thisalinea.textcontent.append("themselves for targeted marketing programmes, and investors to find potential risks and opportunities")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ The Corporate Knights Ranking is issued by Corporate Knights, a Canadian financial research firm which"
    thisalinea.titlefontsize = "11.04000000000002"
    thisalinea.nativeID = 84
    thisalinea.parentID = 74
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "compiles every year starting from 2005 the “Global 100” ranking, a table showing the 100 best performing companies in terms of ESG based on a set of 43 KPIs. The process behind the compiling of ESG ratings is typically based on data provided by companies on a voluntary basis. ESG data aggregators, therefore, start from data which might be partial or biased by the internal perception of the company supplying them. This first set of information is complemented with additional surveys and sector analysis studies. Altogether, those data allow aggregators to compile a list of KPIs converging into the ESG "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("compiles every year starting from 2005 the “Global 100” ranking, a table showing the 100 best performing")
    thisalinea.textcontent.append("companies in terms of ESG based on a set of 43 KPIs.")
    thisalinea.textcontent.append("The process behind the compiling of ESG ratings is typically based on data provided by companies on a voluntary")
    thisalinea.textcontent.append("basis. ESG data aggregators, therefore, start from data which might be partial or biased by the internal perception")
    thisalinea.textcontent.append("of the company supplying them. This first set of information is complemented with additional surveys and sector")
    thisalinea.textcontent.append("analysis studies. Altogether, those data allow aggregators to compile a list of KPIs converging into the ESG rating.")
    thisalinea.textcontent.append("The chart below reports the correlation between different environmental scorings (part of ESG scoring) of a sample")
    thisalinea.textcontent.append("company issued by different providers. The data are shown on a scale from 1 to 0, in which 1 represents a perfect")
    thisalinea.textcontent.append("correlation (i.e., scores compiled by two different issuers are perfectly identical for a same company) and 0")
    thisalinea.textcontent.append("represents no correlation (i.e., scores compiled by two different ratings have no overlapping consensus for a same")
    thisalinea.textcontent.append("company), it is very evident that the lack of standardisation intrinsic in the described process reduces the")
    thisalinea.textcontent.append("reliability of the rating as a performance indicator.")
    thisalinea.textcontent.append("Exhibit 18: Correlations between environmental scoring issued by different organisations")
    thisalinea.textcontent.append("A process of regulation and standardisation of the environmental monitoring is likely to happen in the next few")
    thisalinea.textcontent.append("years pushed by the already mentioned Corporate Sustainability Reporting Directive (CSRD) bringing relevant")
    thisalinea.textcontent.append("business opportunities to those players able to provide reliable and unbiased data. In this context, a clear opportunity")
    thisalinea.textcontent.append("stands for the use of the EU Space Programme as a data provider, both for companies to have a realistic")
    thisalinea.textcontent.append("understanding of their status-quo, and for regulators to monitor the environment and be able to take informed")
    thisalinea.textcontent.append("decisions on measures to be put in place for environment protection. Numerous companies are pushing in this")
    thisalinea.textcontent.append("direction developing products specifically targeted to the ESG parameters assessment. A typical use case provided")
    thisalinea.textcontent.append("by a European start-up is presented in the following use case.")
    thisalinea.textcontent.append("Exhibit 19: Use case - Copernicus for ESG monitoring")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("GlobeEye monitors ESG parameters through Copernicus")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("With the upcoming regulation about Non-Financial Reporting, ESG rating is now being perceived")
    thisalinea.textcontent.append("as an added factor companies should consider while evaluating their performance. An")
    thisalinea.textcontent.append("independent point of view based on reliable and unbiased data is therefore becoming")
    thisalinea.textcontent.append("fundamental, since there is the need to monitor ESG performance in an impartial way.")
    thisalinea.textcontent.append("The collection of ESG data is usually reliant on in-situ sensors deployed by the companies")
    thisalinea.textcontent.append("themselves and self-reported data.")
    thisalinea.textcontent.append("This is where space data can play a fundamental role. The Copernicus Programme is one of the")
    thisalinea.textcontent.append("leading contributors to this revolution in ESG monitoring. Companies such as GlobeEye are")
    thisalinea.textcontent.append("addressing the growing needs for unbiased ESG data thanks to space assets. GlobeEye leverages")
    thisalinea.textcontent.append("EO data from different providers, aggregating and analysing them through proprietary AI")
    thisalinea.textcontent.append("algorithms; this allows to provide key insights on crucial parameters such as NOx and particulates")
    thisalinea.textcontent.append("in the interested areas. The role of Copernicus for such data is central and it currently hinges on")
    thisalinea.textcontent.append("Sentinel-5P. Launched in 2017, the")
    thisalinea.textcontent.append("Sentinel-5 Precursor relies on its TROPOMI")
    thisalinea.textcontent.append("payload to monitor several pollutants and")
    thisalinea.textcontent.append("greenhouse gases (GHG) in the atmosphere,")
    thisalinea.textcontent.append("such as ozone (O3) and methane (CH4), as")
    thisalinea.textcontent.append("well as carbon, sulphur, and nitrogen oxides")
    thisalinea.textcontent.append("(COx, SOx, NOx). However, the contribution of")
    thisalinea.textcontent.append("Copernicus does not stop here, and it is set to")
    thisalinea.textcontent.append("increase significantly in the coming years")
    thisalinea.textcontent.append("thanks to the upcoming launches of new")
    thisalinea.textcontent.append("satellites. Sentinel-4 and Sentinel-5 are the")
    thisalinea.textcontent.append("first ones and are planned to work in tandem")
    thisalinea.textcontent.append("to complement and expand upon the")
    thisalinea.textcontent.append("capabilities provided by Sentinel-5P. Additionally, further data will be provided by the Expansion")
    thisalinea.textcontent.append("Sentinels, namely the CO2M constellation, which will focus on anthropogenic emissions of CO2.")
    thisalinea.textcontent.append("Exhibit 20: NOX distribution over Europe")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU")
    thisalinea.textcontent.append("Space")
    thisalinea.textcontent.append("providers20")
    thisalinea.textcontent.append("The following Exhibit shows some examples of common Key Performance Indicators (KPIs) used by companies in")
    thisalinea.textcontent.append("the monitoring of the environmental aspects within ESG scoring metrics frameworks. The list has been identified")
    thisalinea.textcontent.append("from industrial examples, Corporate Knights’ open method and other standards, including the 14000-series ISO")
    thisalinea.textcontent.append("family on environmental management.")
    thisalinea.textcontent.append("Exhibit 21: Examples of environmental monitoring KPIs for green transformation")
    thisalinea.textcontent.append("and EU Space contribution")
    thisalinea.textcontent.append("Indicator Unit Description Examples of EU Space contribution")
    thisalinea.textcontent.append("GHG emissions")
    thisalinea.textcontent.append("Tonnes of")
    thisalinea.textcontent.append("CO2 equiv.")
    thisalinea.textcontent.append("Total direct and indirect")
    thisalinea.textcontent.append("CO2-equivalent GHG")
    thisalinea.textcontent.append("emissions produced by")
    thisalinea.textcontent.append("business activity")
    thisalinea.textcontent.append("Copernicus satellites and in particular")
    thisalinea.textcontent.append("Sentinel-4 and Sentinel-5/5P have")
    thisalinea.textcontent.append("capabilities to acquire atmospheric")
    thisalinea.textcontent.append("measurements of the airborne pollutants")
    thisalinea.textcontent.append("Indicator Unit Description Examples of EU Space contribution")
    thisalinea.textcontent.append("NOx emissions Tonnes")
    thisalinea.textcontent.append("SOx emissions Tonnes")
    thisalinea.textcontent.append("Direct nitrogen oxide")
    thisalinea.textcontent.append("emissions across all")
    thisalinea.textcontent.append("operations")
    thisalinea.textcontent.append("Direct sulphur dioxide")
    thisalinea.textcontent.append("emissions across all")
    thisalinea.textcontent.append("operations")
    thisalinea.textcontent.append("Volatile Organic")
    thisalinea.textcontent.append("Compound (VOC)")
    thisalinea.textcontent.append("emissions")
    thisalinea.textcontent.append("Tonnes")
    thisalinea.textcontent.append("Direct VOC emissions")
    thisalinea.textcontent.append("across all operations")
    thisalinea.textcontent.append("Particulate Matter")
    thisalinea.textcontent.append("(PM) emissions")
    thisalinea.textcontent.append("Tonnes")
    thisalinea.textcontent.append("Total particulate matter")
    thisalinea.textcontent.append("emissions")
    thisalinea.textcontent.append("such as COx and NOX with a high spatial-")
    thisalinea.textcontent.append("temporal resolution, to be used for air")
    thisalinea.textcontent.append("quality.")
    thisalinea.textcontent.append("In the future, the CO2M Copernicus")
    thisalinea.textcontent.append("Expansion Mission can support further CO2")
    thisalinea.textcontent.append("emission measurements.")
    thisalinea.textcontent.append("Companies can use open data provided by")
    thisalinea.textcontent.append("Copernicus services, especially CAMS to")
    thisalinea.textcontent.append("assess and act on their environmental")
    thisalinea.textcontent.append("footprint.21")
    thisalinea.textcontent.append("Water withdrawal")
    thisalinea.textcontent.append("Cubic")
    thisalinea.textcontent.append("meters")
    thisalinea.textcontent.append("Ttl")
    thisalinea.textcontent.append("electricity use")
    thisalinea.textcontent.append("MWh")
    thisalinea.textcontent.append("Total volume of water")
    thisalinea.textcontent.append("withdrawn (not include")
    thisalinea.textcontent.append("Total direct and indirect")
    thisalinea.textcontent.append("energy used, including")
    thisalinea.textcontent.append("self-generated energy")
    thisalinea.textcontent.append("reused rainwater) The EU space programme plays relevant")
    thisalinea.textcontent.append("role in renewable energy siting and")
    thisalinea.textcontent.append("maintenance.")
    thisalinea.textcontent.append("Renewable")
    thisalinea.textcontent.append("energy use")
    thisalinea.textcontent.append("MWh")
    thisalinea.textcontent.append("Total purpose-built, self-")
    thisalinea.textcontent.append("generated renewable")
    thisalinea.textcontent.append("energy used")
    thisalinea.textcontent.append("Total waste")
    thisalinea.textcontent.append("generated")
    thisalinea.textcontent.append("Tonnes")
    thisalinea.textcontent.append("Total hazardous and")
    thisalinea.textcontent.append("non-hazardous waste")
    thisalinea.textcontent.append("generated")
    thisalinea.textcontent.append("Waste")
    thisalinea.textcontent.append("recycled")
    thisalinea.textcontent.append("Tonnes")
    thisalinea.textcontent.append("Total recycled waste")
    thisalinea.textcontent.append("across all operations")
    thisalinea.textcontent.append("Good examples are the use of CAMS for")
    thisalinea.textcontent.append("assessing solar irradiance for solar panel")
    thisalinea.textcontent.append("siting, or Sentinel-1 data used for finding")
    thisalinea.textcontent.append("suitable locations for offshore wind farms")
    thisalinea.textcontent.append("Solutions enabled by Galileo can boost")
    thisalinea.textcontent.append("waste collection logistics efficiency.")
    thisalinea.textcontent.append("On the other hand, Copernicus is vastly")
    thisalinea.textcontent.append("used to monitor waste presence in oceans")
    thisalinea.textcontent.append("(Copernicus Marine Service) other than")
    thisalinea.textcontent.append("providing information on ocean, lake, river,")
    thisalinea.textcontent.append("air and soil pollution.")
    thisalinea.textcontent.append("The European Union has been a pioneer and took steps towards enforcing ESG compliance, initially, starting with")
    thisalinea.textcontent.append("the financial markets: The new EU Sustainable Finance Action Plan introduced a number of key measures which")
    thisalinea.textcontent.append("will come into effect in the EU shortly.")
    thisalinea.textcontent.append("From 2 August 2022, sales agents or distributors authorised in the EU under the MiFID regime must take into")
    thisalinea.textcontent.append("account any sustainability preferences of a client (in addition to the client's investment objectives and risk tolerances)")
    thisalinea.textcontent.append("when assessing the suitability of financial services or products for recommendation. Systematically asking")
    thisalinea.textcontent.append("investors at the outset of the sales process to indicate if they have a preference for ESG products, as envisaged,")
    thisalinea.textcontent.append("could cause a radical shift in the demand levels for ESG products. EU-authorised securities management")
    thisalinea.textcontent.append("companies (UCITS) and fund managers (AIFM) must specifically factor the consideration of sustainability risks into")
    thisalinea.textcontent.append("their investment due diligence processes, risk management processes, and conflicts of interest policies. This will")
    thisalinea.textcontent.append("require the integration of sustainability considerations and factors into firms' investment processes and risk")
    thisalinea.textcontent.append("management processes for all funds managed, not just ESG-focussed funds.")
    thisalinea.textcontent.append("The secondary phase of the EU Sustainable Finance Disclosure Regulation (SFDR) will crack down on empty")
    thisalinea.textcontent.append("promises and require EU financial products that seek to promote ESG characteristics or have a sustainable")
    thisalinea.textcontent.append("investment objective to make detailed pre-contractual and financial disclosures from 1 January 2023.")
    thisalinea.textcontent.append("In addition, banks are increasingly using ESG ratings to provide access to finance to their clients. For example,")
    thisalinea.textcontent.append("Deutsche Bank is linking the Henkel AG & Co. KGaA (Henkel) supply chain finance program to the ESG ratings of")
    thisalinea.textcontent.append("Henkel's suppliers. Deutsche Bank is the first bank in Europe to convert an existing supply chain finance program")
    thisalinea.textcontent.append("for its client. Through this program, Henkel creates incentives for its suppliers to be more sustainable.")
    thisalinea.textcontent.append("A Henkel’s supplier can receive payment immediately after Henkel approves its invoice. The financing costs for the")
    thisalinea.textcontent.append("suppliers are based on Henkel's creditworthiness, which means that the suppliers can usually lower their typical")
    thisalinea.textcontent.append("financing costs. By improving their ESG rating, suppliers can further reduce financing costs in the supply chain.")
    thisalinea.textcontent.append("Exhibit 22: Media headlines from the last three months (as of July 2022)")
    thisalinea.textcontent.append("Corporates have realised that their investors, their customers and future employees are increasingly aware of")
    thisalinea.textcontent.append("ESG. Typically, corporates are professionalising what grew out of corporate social responsibility (CSR) activities")
    thisalinea.textcontent.append("which were typically organised under public relations functions. As the strategic relevance increases with a link to")
    thisalinea.textcontent.append("corporate purpose, the responsibility for ESG is moving closer to the C-level, either through a dedicated")
    thisalinea.textcontent.append("sustainability officer under the CEO or reporting to the CFO. Many corporates create proactive bottom-up efforts")
    thisalinea.textcontent.append("of corporates in shaping their ESG data generation capability. BCG has developed a four-stage evolution that")
    thisalinea.textcontent.append("companies typically go through in shaping their ESG capability.")
    thisalinea.textcontent.append("Exhibit 23: Four-stage evolution of companies through ESG capabilities (BCG)")
    thisalinea.textcontent.append("These factors are promoting a more in-depth integration of ESG matters in processes and operations of companies.")
    thisalinea.textcontent.append("From our research and interviews with engaged partners, we found two general archetypes of companies talking")
    thisalinea.textcontent.append("the monitoring of KPIs associated with environment in two different ways. A first group to whom we refer as")
    thisalinea.textcontent.append("“Champions” and a second group here referred as “Second Adopters”. Even though both groups are aware of the")
    thisalinea.textcontent.append("importance of environmental monitoring, they differentiate by the level of integration these have in their operations.")
    thisalinea.textcontent.append("Champions are likely to have full integration of environmental monitoring solutions in their operation, Second")
    thisalinea.textcontent.append("Adopters, usually rely on less pervasive solutions such as emissions mathematical models or surveys to be filled")
    thisalinea.textcontent.append("by responsible people across the organization.")
    thisalinea.textcontent.append("The ESG system landscape is very wide and varied. On the one end of the spectrum the large Enterprise Resource")
    thisalinea.textcontent.append("Planning (ERP) providers with end-to-end solutions promising to link seamlessly into existing corporate systems.")
    thisalinea.textcontent.append("Their promise is range from supply chain risk and reputation, sustainability management systems, ethical business")
    thisalinea.textcontent.append("operations all the way to integrated reporting and performance management. On the other end, there are numerous")
    thisalinea.textcontent.append("simpler survey or workflow solutions which address parts of the information – often software-as-a-service solutions")
    thisalinea.textcontent.append("from start-ups who see themselves as part of the climate tech or fintech scene.")
    thisalinea.textcontent.append("An example of integration of innovative technology for environmental monitoring and ESG rating is the use of space")
    thisalinea.textcontent.append("data by energy companies to monitor methane emissions into the atmosphere. Sentinel-5P data are particularly")
    thisalinea.textcontent.append("suitable for this application. A detailed use case is provided in the following Exhibit.")
    thisalinea.textcontent.append("Exhibit 24: Use case - Copernicus for methane emissions monitoring in the energy sector")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("TotalEnergies to monitor GHG emissions through Copernicus")
    thisalinea.textcontent.append("The energy sector is one of the main contributors to methane emissions, as one-third of the")
    thisalinea.textcontent.append("global anthropogenic ones can be traced back to energy production 22 . Consequently, as")
    thisalinea.textcontent.append("announced in the European methane strategy, the European commission adopted a proposal for")
    thisalinea.textcontent.append("a regulation specifically targeting the reduction of methane emissions in the energy sector. A")
    thisalinea.textcontent.append("central element of this proposal revolves around improved measurement, reporting, and")
    thisalinea.textcontent.append("verification of these emissions. Traditional monitoring techniques for methane emissions are")
    thisalinea.textcontent.append("numerous and each is suitable for specific circumstances23. In case of well-defined origin points,")
    thisalinea.textcontent.append("typical for industrial sites, stack sampling can be used; this involves calibrated bags collecting")
    thisalinea.textcontent.append("samples over time, for them to be later")
    thisalinea.textcontent.append("analysed in laboratories. Tracer gas")
    thisalinea.textcontent.append("dispersion relies on the controlled release")
    thisalinea.textcontent.append("of tracer gases at the point of emission,")
    thisalinea.textcontent.append("with concentration measurements of both")
    thisalinea.textcontent.append("the tracer gas and methane then taken")
    thisalinea.textcontent.append("downwind to monitor methane dispersion;")
    thisalinea.textcontent.append("this technique is often used for livestock")
    thisalinea.textcontent.append("emissions or for wastewater treatment")
    thisalinea.textcontent.append("facilities. Alternatively, enclosure chamber")
    thisalinea.textcontent.append("measurement can be implemented by")
    thisalinea.textcontent.append("deploying either static or dynamic")
    thisalinea.textcontent.append("chamber atop emission points. Finally,")
    thisalinea.textcontent.append("drones equipped with laser beam sensors")
    thisalinea.textcontent.append("can be used for methane monitoring too,")
    thisalinea.textcontent.append("when dealing with pipelines and oil fields.")
    thisalinea.textcontent.append("Exhibit 25: Data visualisation of GHGSat")
    thisalinea.textcontent.append("methane emission measurement for")
    thisalinea.textcontent.append("TotalEnergies")
    thisalinea.textcontent.append("The capabilities of the EU Space Programme are perfectly suited to complement and improve")
    thisalinea.textcontent.append("traditional methane emissions monitoring techniques. Key players in the fossil fuels industry are")
    thisalinea.textcontent.append("aware of it, as proven by TotalEnergies, a French multinational energy and petroleum company,")
    thisalinea.textcontent.append("founded almost 100 years ago and employing more than 100,000 people globally. In line with its")
    thisalinea.textcontent.append("long-standing efforts to identify, quantify and reduce methane emissions from its facilities,")
    thisalinea.textcontent.append("TotalEnergies leveraged Copernicus and partnered with Canadian GHGSat to perform a")
    thisalinea.textcontent.append("controlled methane release and validate the contribution of space data to the effective monitoring")
    thisalinea.textcontent.append("of polluting missions within the context of energy production. Enabled by the atmospheric")
    thisalinea.textcontent.append("measurement data coming from Copernicus Sentinel-5P, GHGSat managed to detect the")
    thisalinea.textcontent.append("smallest ever methane emission via satellite, proving the added value that space data can provide")
    thisalinea.textcontent.append("and paving the way to increased adoption of satellite-based monitoring for atmospheric methane")
    thisalinea.textcontent.append("emissions. This would not have been possible without the state-of-the-art capabilities of the")
    thisalinea.textcontent.append("Copernicus programme. Together with its complementary mission Sentinel-4 and, as a precursor")
    thisalinea.textcontent.append("of Sentinel-5, Sentinel-5P has the aim to perform atmospheric measurements with high spatial-")
    thisalinea.textcontent.append("temporal resolution, to be used for air quality, ozone & UV radiation, and climate monitoring &")
    thisalinea.textcontent.append("forecasting. With Sentinel-5, as well as the upcoming satellites of the second generation of")
    thisalinea.textcontent.append("Copernicus, the EU Space Programme is set to play a pivotal role in the green transition of the")
    thisalinea.textcontent.append("energy sector.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU")
    thisalinea.textcontent.append("Space")
    thisalinea.textcontent.append("providers24")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ ESG reporting is often based on self-assessed and possibly biased data provided by ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 85
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ ESG reporting is often based on self-assessed and possibly biased data provided by companies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ ESG reporting is often based on self-assessed and possibly biased data provided by")
    thisalinea.textcontent.append("companies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Independent assessment is necessary to comply with upcoming more stringent regulation ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 86
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Independent assessment is necessary to comply with upcoming more stringent regulation about non-financial reporting which will affect European companies starting from 2024 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Independent assessment is necessary to comply with upcoming more stringent regulation")
    thisalinea.textcontent.append("about non-financial reporting which will affect European companies starting from 2024")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Green Deal put at its very centre the idea of a more sustainable society ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 87
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ Green Deal put at its very centre the idea of a more sustainable society and therefore it promotes regulations willing to enforce a more rigid control over companies’ environmental performance such as the Corporate Sustainability Reporting Directive destined to underline the importance of a correct non-financial management of business B) Regulators and investors demanding sustainability information in investment & financing activities C) Corporates embracing ESG as a strategic goal and implementing processes D) Growing number of ESG IT solutions – from start-up solutions to fully integrated packages "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Green Deal put at its very centre the idea of a more sustainable society and therefore it")
    thisalinea.textcontent.append("promotes regulations willing to enforce a more rigid control over companies’ environmental")
    thisalinea.textcontent.append("performance such as the Corporate Sustainability Reporting Directive destined to underline")
    thisalinea.textcontent.append("the importance of a correct non-financial management of business")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "B) Regulators and investors demanding sustainability information in investment ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 88
    thisalinea.parentID = 87
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "B) Regulators and investors demanding sustainability information in investment & financing activities "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("B) Regulators and investors demanding sustainability information in investment")
    thisalinea.textcontent.append("& financing activities")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "C) Corporates embracing ESG as a strategic goal and implementing processes "
    thisalinea.titlefontsize = "9.47999999999999"
    thisalinea.nativeID = 89
    thisalinea.parentID = 87
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "C) Corporates embracing ESG as a strategic goal and implementing processes "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("C) Corporates embracing ESG as a strategic goal and implementing processes")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "D) Growing number of ESG IT solutions – from start-up solutions to fully integrated packages "
    thisalinea.titlefontsize = "9.47999999999999"
    thisalinea.nativeID = 90
    thisalinea.parentID = 87
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "D) Growing number of ESG IT solutions – from start-up solutions to fully integrated packages "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("D) Growing number of ESG IT solutions – from start-up solutions to fully integrated packages")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Energy production is one of the highest-impact sectors in terms of greenhouse gasses ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 91
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "▪ Energy production is one of the highest-impact sectors in terms of greenhouse gasses (GHG) production "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Energy production is one of the highest-impact sectors in terms of greenhouse gasses")
    thisalinea.textcontent.append("(GHG) production")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ GHG emissions might be difficult to monitor on a large scale in the area ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 92
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "▪ GHG emissions might be difficult to monitor on a large scale in the area not immediately surrounding the production sites "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ GHG emissions might be difficult to monitor on a large scale in the area not immediately")
    thisalinea.textcontent.append("surrounding the production sites")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ The Green Deal a clean energy transition, and with the goal of achieving a ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 93
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "▪ The Green Deal a clean energy transition, and with the goal of achieving a 32% energy share from renewables "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The Green Deal a clean energy transition, and with the goal of achieving a 32% energy share")
    thisalinea.textcontent.append("from renewables")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Moreover, it sets important goals to ensure a secure and affordable energy supply for ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 94
    thisalinea.parentID = 84
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "▪ Moreover, it sets important goals to ensure a secure and affordable energy supply for EU residences "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Moreover, it sets important goals to ensure a secure and affordable energy supply for EU residences")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "EU Space for reducing environmental footprint of companies"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 95
    thisalinea.parentID = 26
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 48
    thisalinea.summary = "In this section of the document, the positive environmental impact of the EU Space on different industrial sectors will be showcased through conceptual discussion and practical use cases, organised following, when possible, the structure of the Green Deal action areas as described in the following Exhibit. Many initiatives aim to reduce the pollution generated by the constantly increasing power consumption typical in the modern society, especially using renewable sources. In 2021, electricity generated from renewable sources in the EU reached a new high of 1068 TWh, a 1% increase (+12 TWh) year-on-year, and a 9% (+88 TWh) increase compared to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In this section of the document, the positive environmental impact of the EU Space on different industrial sectors")
    thisalinea.textcontent.append("will be showcased through conceptual discussion and practical use cases, organised following, when possible, the")
    thisalinea.textcontent.append("structure of the Green Deal action areas as described in the following Exhibit.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.1 Clean energy production and supply"
    thisalinea.titlefontsize = "14.04000000000002"
    thisalinea.nativeID = 96
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Many initiatives aim to reduce the pollution generated by the constantly increasing power consumption typical in the modern society, especially using renewable sources. In 2021, electricity generated from renewable sources in the EU reached a new high of 1068 TWh, a 1% increase (+12 TWh) year-on-year, and a 9% (+88 TWh) increase compared to 2019. Renewables accounted for 37% of EU electricity production in 2021, up from 34% in 201925. Exhibit 26: Energy generation from solar and wind sources in EU2725 The EU Space Programme can make significant contributions to renewable energy providers’ performance, especially in terms of accessing reliable "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Many initiatives aim to reduce the pollution generated by the constantly increasing power consumption typical in")
    thisalinea.textcontent.append("the modern society, especially using renewable sources. In 2021, electricity generated from renewable sources in")
    thisalinea.textcontent.append("the EU reached a new high of 1068 TWh, a 1% increase (+12 TWh) year-on-year, and a 9% (+88 TWh) increase")
    thisalinea.textcontent.append("compared to 2019. Renewables accounted for 37% of EU electricity production in 2021, up from 34% in 201925.")
    thisalinea.textcontent.append("Exhibit 26: Energy generation from solar and wind sources in EU2725")
    thisalinea.textcontent.append("The EU Space Programme can make significant contributions to renewable energy providers’ performance,")
    thisalinea.textcontent.append("especially in terms of accessing reliable data for decision-making. Examples include the efficient placement of")
    thisalinea.textcontent.append("renewable energy infrastructure, power infrastructure monitoring and maintenance, and time synchronisation for")
    thisalinea.textcontent.append("electricity grids.")
    thisalinea.textcontent.append("Site choice is among the biggest challenges and predictors in the success of the setup and operation of renewable")
    thisalinea.textcontent.append("energy infrastructure. Many factors play into the decision of the best site for each project and energy source, and")
    thisalinea.textcontent.append("therefore into the final output, efficiency and profitability of the programme. Connections to the grid, historical")
    thisalinea.textcontent.append("weather data (solar irradiance, windspeeds and directions, marine currents, etc.), as well as the oro- and")
    thisalinea.textcontent.append("topographical characteristics are all crucial parameters in this process.")
    thisalinea.textcontent.append("In photovoltaic energy, the amount of solar radiation available and solar panel efficiency depends on several")
    thisalinea.textcontent.append("variables, such as the season, the time of day, the temperature and the geographic latitude; however, the total")
    thisalinea.textcontent.append("available radiation is also affected by clouds, aerosol particles, ozone molecules, and water vapour in the")
    thisalinea.textcontent.append("atmosphere. All these elements interact with the solar radiation absorbing and deflecting it, impacting, therefore,")
    thisalinea.textcontent.append("the efficiency of the power plant.26")
    thisalinea.textcontent.append("Using information gathered from Copernicus’ satellites and atmospheric models, the Copernicus Atmosphere")
    thisalinea.textcontent.append("Monitoring Service produces global irradiation models starting from 2004 until now. Using those models, the")
    thisalinea.textcontent.append("renewable energy sector can make sound decisions on where to best place the solar panels for example. With")
    thisalinea.textcontent.append("similar reasoning, considering the capabilities of Copernicus in monitoring wind and marine currents, it is possible")
    thisalinea.textcontent.append("to build similar applications for the siting of wind turbines and tidal power generation plants. It is estimated that")
    thisalinea.textcontent.append("40 TWh of additional electrical power will be generated thanks to Copernicus until 203027.")
    thisalinea.textcontent.append("Renewable energy")
    thisalinea.textcontent.append("Other than the previous mention application about the correct positioning of renewable energy infrastructure, it is")
    thisalinea.textcontent.append("important to remember that solar panels or wind turbines are generally located in difficult-to-reach places or in")
    thisalinea.textcontent.append("remote locations; solar panels, for instance, are usually placed on high roofs or in remote fields, while wind turbines’")
    thisalinea.textcontent.append("rotors have to be placed several dozens of metres high from the ground. The efficiency of these installations is")
    thisalinea.textcontent.append("directly correlated to their correct maintenance. A build-up of debris on a solar panel can limit its energy output,")
    thisalinea.textcontent.append("while unidentified damage to a wind turbine can have disastrous consequences not only on energy production, but")
    thisalinea.textcontent.append("also on human lives. Copernicus historical weather data from the C3S ERA 5 Reanalysis can help perfect the")
    thisalinea.textcontent.append("cleaning of panels or the maintenance of wind turbines28.")
    thisalinea.textcontent.append("The precise positioning services offered by the EGNSS, together with the latest developments in computer vision-")
    thisalinea.textcontent.append("aided navigation, allow the use of unmanned aerial vehicles (UAVs) in inspection operations, making them quick,")
    thisalinea.textcontent.append("cheap, and dramatically less dangerous for human operators. UAVs have seen successful applications in detecting")
    thisalinea.textcontent.append("solar panel hotspots, a common source of reduction in power generation. Precise GNSS, offered by Galileo and its")
    thisalinea.textcontent.append("upcoming High Accuracy Service, is crucial to making this and future applications efficient.")
    thisalinea.textcontent.append("Oil and gas")
    thisalinea.textcontent.append("Copernicus satellite imagery allows monitoring the full length of oil and gas pipelines, therefore, reliably detecting")
    thisalinea.textcontent.append("potential threats and guiding the rapid response of the emergency services. Sentinel-1’s synthetic aperture radar,")
    thisalinea.textcontent.append("for example, can detect major changes in land surface such as a landslide or earthquake that may damage")
    thisalinea.textcontent.append("infrastructure. Biomass production as a feedstock for biofuels can also be monitored and tracked thanks to")
    thisalinea.textcontent.append("Copernicus and EGNSS.")
    thisalinea.textcontent.append("Smart grids")
    thisalinea.textcontent.append("Energy companies are increasingly using smart grids to improve efficiency and reduce costs. By implementing two-")
    thisalinea.textcontent.append("way communication between smart devices in the field and central data structures, and then linking these to")
    thisalinea.textcontent.append("intelligent analytics, operators gain unprecedented insight into consumption patterns, network performance and")
    thisalinea.textcontent.append("other metrics to ensure optimal operating levels at all times.")
    thisalinea.textcontent.append("The key to this operation is accurate synchronisation between data points. Without it, operators have a limited")
    thisalinea.textcontent.append("ability to extract accurate information from the field or make effective changes to network operations29 This is where")
    thisalinea.textcontent.append("the EGNSS come into play.")
    thisalinea.textcontent.append("EGNSS receivers are relatively cheap, reliable and highly accurate time sources that can be used in large numbers")
    thisalinea.textcontent.append("in smart grids to enable automatic real-time monitoring of the grid. Currently, several projects are developing the")
    thisalinea.textcontent.append("proposed concept and improving its resiliency to tampering.")
    thisalinea.textcontent.append("Exhibit 27: Use case - EU Space Programme for boosting clean energy adoption")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("production and the opportunity cost of poor land allocation")
    thisalinea.textcontent.append("The Green Deal involves a clean energy transition, with the goal of achieving a 32% energy share from")
    thisalinea.textcontent.append("renewables")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Copernicus to boost renewable energy growth")
    thisalinea.textcontent.append("A significant amount of the energy produced is assigned to households, which account for around")
    thisalinea.textcontent.append("25% of the total30.")
    thisalinea.textcontent.append("The limited use of roof space over buildings have pushed for the adoption of small solar panel")
    thisalinea.textcontent.append("installations on top of residential buildings. This growth has been very quick, and it forecasted")
    thisalinea.textcontent.append("to continue, with projections showing an increase from 59 GW installed globally in 2021 to almost")
    thisalinea.textcontent.append("95 GW in 202531. However, overall adoption is still limited, with even Italy, one of the leading")
    thisalinea.textcontent.append("European countries, being less than 25%31. One of the reasons for this limited penetration can")
    thisalinea.textcontent.append("be traced back to homeowners simply being unaware of the solar potential of their roofs and")
    thisalinea.textcontent.append("to the challenge in accessing reliable and precise information on the production of solar energy.")
    thisalinea.textcontent.append("NOVELTIS, a French company founded in 1998, found a way to tackle this problem, leveraging")
    thisalinea.textcontent.append("the power of EU Space data. In collaboration with the European Centre for Medium-Range")
    thisalinea.textcontent.append("Weather Forecasts (ECMWF) and Copernicus (through CAMS, its Atmosphere Monitoring")
    thisalinea.textcontent.append("System), NOVELTIS has developed Mon Toit Solaire, a service simulating and calculating the")
    thisalinea.textcontent.append("energy potential of photovoltaic rooftop projects and providing users with reliable technical and")
    thisalinea.textcontent.append("financial information. Moreover, it eases the realisation of installation projects by providing")
    thisalinea.textcontent.append("information about local certified professional installers on its website.")
    thisalinea.textcontent.append("Exhibit 28: The Mon Toit Solaire user interface")
    thisalinea.textcontent.append("The contribution of Copernicus")
    thisalinea.textcontent.append("to this service is of paramount")
    thisalinea.textcontent.append("importance. CAMS collects")
    thisalinea.textcontent.append("information about clouds,")
    thisalinea.textcontent.append("water vapour, aerosols, and")
    thisalinea.textcontent.append("ozone levels, and feeds it into a")
    thisalinea.textcontent.append("radiative transfer model to")
    thisalinea.textcontent.append("calculate the amount of solar")
    thisalinea.textcontent.append("irradiation that reaches the")
    thisalinea.textcontent.append("ground. This is then combined")
    thisalinea.textcontent.append("with 3D modelling and")
    thisalinea.textcontent.append("dedicated algorithms, making it")
    thisalinea.textcontent.append("possible to calculate the actual")
    thisalinea.textcontent.append("available roof surface and thus")
    thisalinea.textcontent.append("extrapolating the predicted energy production. The end result is an accessible service that allows")
    thisalinea.textcontent.append("end users to easily understand the economic benefits of rooftop solar installations, facilitating")
    thisalinea.textcontent.append("household adoption and contributing to the green transition.")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU")
    thisalinea.textcontent.append("Space")
    thisalinea.textcontent.append("providers32")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Inappropriate positioning of clean energy infrastructure results in inefficiencies in energy "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 97
    thisalinea.parentID = 96
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Inappropriate positioning of clean energy infrastructure results in inefficiencies in energy "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Inappropriate positioning of clean energy infrastructure results in inefficiencies in energy")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Costs associated with corrective actions are high "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 98
    thisalinea.parentID = 96
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Costs associated with corrective actions are high "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Costs associated with corrective actions are high")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.2 Clean industry boosting a cleaner industry"
    thisalinea.titlefontsize = "14.040000000000077"
    thisalinea.nativeID = 99
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The transition into a cleaner European industry will require concerted efforts to address product carbon footprint and durability simultaneously. On the former, more robust emissions reduction measures in operations will be needed. Durability, on the other hand, requires proper maintenance and the tools to ensure this is feasible. In this chapter, we will discuss the impacts EU SPACE can have on clean transport, infrastructure, raw materials extraction and waste and pollution. Cleaner industrial operations Galileo-enabled location-based services can be used throughout the industry to track and optimise operations, such as in warehousing, bringing direct emissions reductions, as well as linked "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The transition into a cleaner European industry will require concerted efforts to address product carbon footprint")
    thisalinea.textcontent.append("and durability simultaneously. On the former, more robust emissions reduction measures in operations will be")
    thisalinea.textcontent.append("needed. Durability, on the other hand, requires proper maintenance and the tools to ensure this is feasible. In this")
    thisalinea.textcontent.append("chapter, we will discuss the impacts EU SPACE can have on clean transport, infrastructure, raw materials extraction")
    thisalinea.textcontent.append("and waste and pollution.")
    thisalinea.textcontent.append("Cleaner industrial operations")
    thisalinea.textcontent.append("Galileo-enabled location-based services can be used throughout the industry to track and optimise operations, such")
    thisalinea.textcontent.append("as in warehousing, bringing direct emissions reductions, as well as linked cost savings.")
    thisalinea.textcontent.append("Galileo will also be instrumental in delivering the electronic product passport – a consumer information tool,")
    thisalinea.textcontent.append("designed to provide valuable information about the origin, composition and durability of a product, based on its")
    thisalinea.textcontent.append("path from sourcing, to production, to retail. Similar principles may be applied in enabling the circular economy, by")
    thisalinea.textcontent.append("providing manufacturers with more reliable and accurate information on the history and quality of recycled materials.")
    thisalinea.textcontent.append("The EU Space Programme is especially well-suited to help unlock fuel efficiencies for the maritime industry,")
    thisalinea.textcontent.append("especially for large vessels such as tanker ships and bulk carriers. Indeed, EGNSS can provide ships with information")
    thisalinea.textcontent.append("for accurate manoeuvring in congested areas, increasing their energy and fuel efficiency. In addition, Earth")
    thisalinea.textcontent.append("observation data and information on currents as well as other factors (e.g., movement of sea ice) can help to optimise")
    thisalinea.textcontent.append("the maritime industry’s fuel efficiency through better routing, thus decreasing emissions and saving costs. Similarly,")
    thisalinea.textcontent.append("the aviation industry can also strongly benefit from the utilisation of EU Space Programme assets for fuel efficiencies")
    thisalinea.textcontent.append("and reduction in emissions. While aviation is the second largest source of greenhouse gases from transport (after")
    thisalinea.textcontent.append("road), the use of EGNOS for safe landing procedures in critical conditions such as fog can enable significant")
    thisalinea.textcontent.append("reductions in the frequency of aborted landings, in turn helping to limit fuel expenditures and emissions.")
    thisalinea.textcontent.append("Lastly, a combination of Copernicus-based planning, and Galileo-enabled operations will facilitate the increased")
    thisalinea.textcontent.append("adoption of the sharing economy. A pertinent example of this is the optimisation of ride-hailing vehicle routes –")
    thisalinea.textcontent.append("including on Uber, Bolt, and many other services33 which help drivers through cost savings, riders through time-")
    thisalinea.textcontent.append("effectiveness, and the greater economy through the resulting reduction in fuel use and emissions. Further resource")
    thisalinea.textcontent.append("reductions are achieved thanks to the optimised fleet management meaning the correct number and type of vehicles,")
    thisalinea.textcontent.append("incorporating traffic congestion and other factors for ideal routes, and checked driving behaviour.")
    thisalinea.textcontent.append("Infrastructure construction and maintenance")
    thisalinea.textcontent.append("Galileo and Copernicus together can help with infrastructure mapping and monitoring and therefore making them")
    thisalinea.textcontent.append("more robust. This can be especially useful for maintaining road infrastructure in rural areas. Disrupted supply chains")
    thisalinea.textcontent.append("can cause loss of products and resources like fuel. Lack of monitoring also makes route optimisation harder, resulting")
    thisalinea.textcontent.append("in inefficiencies. Another use case includes remote sensing in telecommunications industry. Digital elevation")
    thisalinea.textcontent.append("models and land use/land cover can be used to build predictive models for network planning to achieve optimal")
    thisalinea.textcontent.append("network capacity. The presence of necessary data and its quality is critical for accuracy of such models. This is a")
    thisalinea.textcontent.append("relatively cheaper way of satisfying capacity requirements.")
    thisalinea.textcontent.append("Lone workers are employed in a range of industries, but they are at relatively higher risk because of not having")
    thisalinea.textcontent.append("someone to assist or supervise them. In case of an accident, notification of emergency services by a co-worker is")
    thisalinea.textcontent.append("normally necessary. In this context, GNSS is used by different applications to decrease the risk by measuring impacts")
    thisalinea.textcontent.append("and durations of inactivity. Depending on the situation, emergency services are informed of the accident location by")
    thisalinea.textcontent.append("those applications.")
    thisalinea.textcontent.append("Raw materials")
    thisalinea.textcontent.append("It is important, within the context of clean industry, to consider the impacts of raw material extraction, as they are a")
    thisalinea.textcontent.append("highly polluting part of the greater supply chain. Mining, and quarrying, in particular, lie among the most")
    thisalinea.textcontent.append("environmentally harmful activities in this cycle, directly impacting land, water, and air.")
    thisalinea.textcontent.append("Air quality is especially affected by mining operations. Unrefined materials are released when mineral deposits")
    thisalinea.textcontent.append("are exposed to the surface through mining. Wind and vehicular traffic due to mining equipment cause such materials")
    thisalinea.textcontent.append("to become airborne. Lead, arsenic, cadmium, are a non-negligible component of these particulates. These pollutants")
    thisalinea.textcontent.append("can damage the health of people living near the mining site. Diseases of the respiratory system and allergies can be")
    thisalinea.textcontent.append("triggered by the inhalation of such airborne particles.")
    thisalinea.textcontent.append("The modification of the landscape, such as creating open pits and waste deposits can lead to the physical destruction")
    thisalinea.textcontent.append("of the land at the mining site. Furthermore, it can contribute to the deterioration of the area's flora and fauna. There")
    thisalinea.textcontent.append("is also a huge possibility that many of the surface features that were present before mining activities cannot be")
    thisalinea.textcontent.append("replaced after the process has ended. The removal of soil layers and deep underground digging can destabilize the")
    thisalinea.textcontent.append("ground which threatens the future of roads and buildings in the area.")
    thisalinea.textcontent.append("This extreme change in the environment can have a catastrophic impact on the biodiversity of the area. Mining")
    thisalinea.textcontent.append("leads to a massive habitat loss for a diversity of flora and fauna ranging from soil microorganisms to large")
    thisalinea.textcontent.append("mammals34. Considering the current policies for biodiversity preservation, it is vital for companies to understand")
    thisalinea.textcontent.append("the impact of their mining activities to remain competitive.")
    thisalinea.textcontent.append("As of today, the EU accounts for 6% of the world’s population, yet consumes up to 30% of metals produced globally.")
    thisalinea.textcontent.append("This trend is expected to rise to a 63% increase per capita by 206035.")
    thisalinea.textcontent.append("Exhibit 29: Carbon and energy intensity per tonne of metal produced in EU36")
    thisalinea.textcontent.append("Another of the areas in which the EU Space Programme can be beneficial is in the optimisation of fleet management")
    thisalinea.textcontent.append("during mining operations.")
    thisalinea.textcontent.append("It is estimated that the use of precise navigation services can improve the efficiency of mining equipment,")
    thisalinea.textcontent.append("especially trucks, in terms of fuel consumption from 1.8 to 2.3%37.")
    thisalinea.textcontent.append("Furthermore, Galileo-enabled location-based services can be similarly used throughout industry to track and")
    thisalinea.textcontent.append("optimise operations, such as warehousing, bringing direct emissions reductions, leading to cost savings.")
    thisalinea.textcontent.append("Exhibit 30: Use case - EU Space Programme for mining")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Correct management and extraction of resources is needed for ecosystems and biodiversity")
    thisalinea.textcontent.append("preservation")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("EGNSS to improve mining operations")
    thisalinea.textcontent.append("GNSS positioning data is used for example to provide drill monitoring, control and guidance,")
    thisalinea.textcontent.append("allowing to navigate drill rigs with centimetre-level precision without the need for traditional,")
    thisalinea.textcontent.append("time-consuming manual surveys. As a result, optimal fragmentation of rock can be achieved,")
    thisalinea.textcontent.append("which facilitates the subsequent stone extraction and removal activities. Furthermore, accurate")
    thisalinea.textcontent.append("positioning allows to overlap the planned design for the overall mine structure with real-time")
    thisalinea.textcontent.append("vehicles’ position, which can for example be used to offer precise guidance on where ore blocks")
    thisalinea.textcontent.append("are located.")
    thisalinea.textcontent.append("Accurate positioning, however, is not enough. Robustness and resiliency are critical too,")
    thisalinea.textcontent.append("especially in challenging areas.")
    thisalinea.textcontent.append("Companies such as Septentrio, a Belgian manufacturer of GNSS components and receivers")
    thisalinea.textcontent.append("focused on industrial applications such as construction, surveying, robotics, logistics, and")
    thisalinea.textcontent.append("maritime. Septentrio has more than two decades of experience in providing top-of-the-line")
    thisalinea.textcontent.append("products for accurate positioning, and its expertise extends to the mining industry as well.")
    thisalinea.textcontent.append("Septentrio has specifically developed the ARDVAC control system 38 , relying on proprietary")
    thisalinea.textcontent.append("algorithms to improve positioning robustness and resilience during operations. In particular, the")
    thisalinea.textcontent.append("IONO+ algorithm reduces the impact of ionospheric oscillations, while LOCK+ targets signal")
    thisalinea.textcontent.append("robustness during vibrations or shocks and AIM+ protects from radiofrequency interference.")
    thisalinea.textcontent.append("Thanks to the performance of Septentrio’s product line enabled by the capabilities of EGNSS,")
    thisalinea.textcontent.append("mining players relying on these products can ensure maximised efficiency even in the harshest of")
    thisalinea.textcontent.append("environments, achieving not only the highest levels of safety for all operators involved, but also")
    thisalinea.textcontent.append("optimising the utilisation of natural resources and thus safeguarding the integrity of surrounding")
    thisalinea.textcontent.append("ecosystems.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers39")
    thisalinea.textcontent.append("Waste and pollution")
    thisalinea.textcontent.append("The increasing quantities of waste generated in European countries are another challenge to be addressed within")
    thisalinea.textcontent.append("the green transition of industry. It is estimated that Europe produces annually over 800 million of tonnes of waste")
    thisalinea.textcontent.append("per year40. The annual average rate of increase of this waste since 1985 in the OECD European area is estimated at")
    thisalinea.textcontent.append("around 3 per cent. Present disposal and processing capacity is probably not sufficient to deal with the expected")
    thisalinea.textcontent.append("growth, furthermore, existing facilities are often not adequate to ensure acceptable environmental standards41. The")
    thisalinea.textcontent.append("waste related to industries represents 30% of the total European, which results in unnecessary costs to companies.")
    thisalinea.textcontent.append("Since the 1970s, European countries have achieved important progress in reducing emissions into air and water")
    thisalinea.textcontent.append("from production processes by imposing strict emissions standards on conventional pollutants. However, because")
    thisalinea.textcontent.append("of their single-media mandate, environmental")
    thisalinea.textcontent.append("regulations have addressed air and water pollution")
    thisalinea.textcontent.append("problems separately. The result has been to move")
    thisalinea.textcontent.append("pollution problems to the least regulated")
    thisalinea.textcontent.append("environmental medium and the least controlled form")
    thisalinea.textcontent.append("of pollution. The implementation of emission")
    thisalinea.textcontent.append("control technologies has often resulted in")
    thisalinea.textcontent.append("increased amounts of solid waste from production")
    thisalinea.textcontent.append("processes. In addition, the concentration of")
    thisalinea.textcontent.append("hazardous substances in solid residues has increased.")
    thisalinea.textcontent.append("Exhibit 31: Share of waste generated in EU40")
    thisalinea.textcontent.append("One of the most significant impacts of the EU Space")
    thisalinea.textcontent.append("Programme on waste management is the use of")
    thisalinea.textcontent.append("Copernicus in monitoring waste in the oceans. It is")
    thisalinea.textcontent.append("estimated that 4 to 10% of all the recovered waste")
    thisalinea.textcontent.append("from the ocean in operations such as The Ocean")
    thisalinea.textcontent.append("Cleanup 42 or Clean Oceans Project 43 , is directly")
    thisalinea.textcontent.append("accountable to Copernicus44.")
    thisalinea.textcontent.append("Not only reducing waste, but also recycling is a key")
    thisalinea.textcontent.append("measurement for a greener industry. The circular")
    thisalinea.textcontent.append("economy provides a holistic model for reusing, repairing and recycling existing materials and products as long as")
    thisalinea.textcontent.append("possible. The circular economy can benefit from Galileo similarly as with the electronic product passport – a")
    thisalinea.textcontent.append("consumer information tool, designed to provide valuable information about the origin, composition and durability of")
    thisalinea.textcontent.append("a product, based on its path from sourcing, to production, to retail. By providing manufacturers with more reliable")
    thisalinea.textcontent.append("and accurate information on the history and quality of recycled materials, Galileo can be an important benefit for")
    thisalinea.textcontent.append("industries.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Companies face several challenges during raw material production, from exploration to ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 100
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Companies face several challenges during raw material production, from exploration to mine closure and restoration "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Companies face several challenges during raw material production, from exploration to")
    thisalinea.textcontent.append("mine closure and restoration")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Biodiversity and human health can be severely harmed if mining activities are not cautiously ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 101
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Biodiversity and human health can be severely harmed if mining activities are not cautiously monitored "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Biodiversity and human health can be severely harmed if mining activities are not cautiously")
    thisalinea.textcontent.append("monitored")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.3 Construction and renovation"
    thisalinea.titlefontsize = "14.040000000000077"
    thisalinea.nativeID = 102
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The EU Space Programme, and Copernicus in particular, are particularly well-placed to offer high-value products and services to urban planners. The CLMS, providing its land use and land cover capabilities in tandem with the Copernicus space component, can be complemented with in situ data – including demographic statistics, historical information, and other layers as pertinent to the application – to enhance informed decision-making in the urban planning process. In conjunction with EGNSS, Copernicus may be used to create precise location-based action in urban and rural environments. A number of the potential applications of Copernicus urban planning data include: Exhibit 32: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU Space Programme, and Copernicus in particular, are particularly well-placed to offer high-value products")
    thisalinea.textcontent.append("and services to urban planners. The CLMS, providing its land use and land cover capabilities in tandem with the")
    thisalinea.textcontent.append("Copernicus space component, can be complemented with in situ data – including demographic statistics, historical")
    thisalinea.textcontent.append("information, and other layers as pertinent to the application – to enhance informed decision-making in the urban")
    thisalinea.textcontent.append("planning process. In conjunction with EGNSS, Copernicus may be used to create precise location-based action in")
    thisalinea.textcontent.append("urban and rural environments.")
    thisalinea.textcontent.append("A number of the potential applications of Copernicus urban planning data include:")
    thisalinea.textcontent.append("Exhibit 32: Use case – EU Space Programme for urban planning and maintenance")
    thisalinea.textcontent.append("The Green Deal supports the development of more sustainable cities, vegetation")
    thisalinea.textcontent.append("management and life quality for citizens")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Copernicus for construction monitoring")
    thisalinea.textcontent.append("An important role in the sustainable development of urban environments is related to pre-")
    thisalinea.textcontent.append("emptive maintenance. By timely noticing maintenance needs, the lifespan of buildings can be")
    thisalinea.textcontent.append("increased. While day-to-day servicing can be predicted more easily, the effect of the")
    thisalinea.textcontent.append("surroundings is more difficult to anticipate. An example of a disruptive factor in an environment,")
    thisalinea.textcontent.append("is the construction of the Fereggiano tunnel in Italy (2017). The development of this")
    thisalinea.textcontent.append("infrastructure induces vibrations in the ground that are felt by surrounding buildings. Detektia is a")
    thisalinea.textcontent.append("company that created a tool to assess external effects on existing infrastructure using DinSAR -")
    thisalinea.textcontent.append("essentially combining multiple SAR measurements taken at different times to estimate the")
    thisalinea.textcontent.append("movement of buildings. They then")
    thisalinea.textcontent.append("cluster the movements in categories")
    thisalinea.textcontent.append("to warn the building owners of")
    thisalinea.textcontent.append("potential maintenance requirements.")
    thisalinea.textcontent.append("Exhibit 33: Map of Genova area produced")
    thisalinea.textcontent.append("by Detektia")
    thisalinea.textcontent.append("Detektia uses Copernicus satellite")
    thisalinea.textcontent.append("(Sentinel-1) measurements as")
    thisalinea.textcontent.append("input in their tool, showing the utility")
    thisalinea.textcontent.append("of the current space assets of the EU")
    thisalinea.textcontent.append("in the commercial service sector.")
    thisalinea.textcontent.append("Detektia has received interest from")
    thisalinea.textcontent.append("numerous customers such as ICA,")
    thisalinea.textcontent.append("Sacyr, and Acciona Energia which")
    thisalinea.textcontent.append("plan to leverage the prediction tool")
    thisalinea.textcontent.append("in their projects. Tools such as the")
    thisalinea.textcontent.append("one developed by Detektia, convert")
    thisalinea.textcontent.append("the vast array of data collected by")
    thisalinea.textcontent.append("Copernicus into, potential live-")
    thisalinea.textcontent.append("saving, commercially viable tools")
    thisalinea.textcontent.append("touching a variety of sectors such as energy, and chemical industries to name a few.")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers45")
    thisalinea.textcontent.append("Further business uses of urban planning data include the location-based augmentation of marketing campaigns with")
    thisalinea.textcontent.append("geotargeted advertising, by way of Copernicus-derived maps used in conjunction with EGNSS signals received on")
    thisalinea.textcontent.append("personal devices.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Infrastructure placement and distribution, such as for the allocation of 5G towers – according ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 103
    thisalinea.parentID = 102
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Infrastructure placement and distribution, such as for the allocation of 5G towers – according to land use/land cover (CLMS) and in situ internet traffic and demographic data "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Infrastructure placement and distribution, such as for the allocation of 5G towers – according to land")
    thisalinea.textcontent.append("use/land cover (CLMS) and in situ internet traffic and demographic data")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Atmospheric pollution monitoring and management, through CAMS, which may be employed to better- ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 104
    thisalinea.parentID = 102
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Atmospheric pollution monitoring and management, through CAMS, which may be employed to better- distribute green spaces and prioritise areas for public transport infrastructure or traffic restrictions (e.g., low-emission zones) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Atmospheric pollution monitoring and management, through CAMS, which may be employed to better-")
    thisalinea.textcontent.append("distribute green spaces and prioritise areas for public transport infrastructure or traffic restrictions (e.g.,")
    thisalinea.textcontent.append("low-emission zones)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Urban heat management, in the identification and remediation of heat islands (e.g., in industrial ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 105
    thisalinea.parentID = 102
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ Urban heat management, in the identification and remediation of heat islands (e.g., in industrial or business zones) and providing tools for the design of ventilation and heat absorbing areas "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Urban heat management, in the identification and remediation of heat islands (e.g., in industrial or business")
    thisalinea.textcontent.append("zones) and providing tools for the design of ventilation and heat absorbing areas")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Green space allotment, including for public and business use, to abate the effects of ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 106
    thisalinea.parentID = 102
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "▪ Green space allotment, including for public and business use, to abate the effects of urban pollution, as well as to improve everyday conditions for citizens and employees "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Green space allotment, including for public and business use, to abate the effects of urban pollution, as")
    thisalinea.textcontent.append("well as to improve everyday conditions for citizens and employees")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Urban planning, resource management and green infrastructures require extensive and ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 107
    thisalinea.parentID = 102
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "▪ Urban planning, resource management and green infrastructures require extensive and reliable data to be effective "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Urban planning, resource management and green infrastructures require extensive and")
    thisalinea.textcontent.append("reliable data to be effective")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Furthermore, solid data can support risk assessment and preventive maintenance on buildings ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 108
    thisalinea.parentID = 102
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "▪ Furthermore, solid data can support risk assessment and preventive maintenance on buildings making less likely high environmental impact corrective maintenance operations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Furthermore, solid data can support risk assessment and preventive maintenance on buildings")
    thisalinea.textcontent.append("making less likely high environmental impact corrective maintenance operations")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.4 Smart and sustainable mobility"
    thisalinea.titlefontsize = "14.039999999999992"
    thisalinea.nativeID = 109
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The EU Space Programme offers a host of solutions for greener transport and mobility in roads, railways, waterways and airways. Indeed, space-enabled smart mobility has already taken centre stage in Europe’s transport management system. EU space assets, in particular EGNSS, allow for monitoring of mobility in different networks, thus contributing to reducing emissions as well as optimising resource usage. Transportation sector, including land, maritime, and air transport of both passengers and freights, is estimated to account for 27% of total greenhouse emissions in Europe46. While cars generate the most emissions, aviation has been responsible for the largest percentage increase in "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU Space Programme offers a host of solutions for greener transport and mobility in roads, railways, waterways")
    thisalinea.textcontent.append("and airways. Indeed, space-enabled smart mobility has already taken centre stage in Europe’s transport")
    thisalinea.textcontent.append("management system. EU space assets, in particular EGNSS, allow for monitoring of mobility in different networks,")
    thisalinea.textcontent.append("thus contributing to reducing emissions as well as optimising resource usage.")
    thisalinea.textcontent.append("Transportation sector, including land, maritime, and air transport of both passengers and freights, is estimated to")
    thisalinea.textcontent.append("account for 27% of total greenhouse emissions in Europe46. While cars generate the most emissions, aviation has")
    thisalinea.textcontent.append("been responsible for the largest percentage increase in greenhouse gas emissions over 1990 levels (+129 %),")
    thisalinea.textcontent.append("followed by international shipping (+32%) and road transport (+23%)46.")
    thisalinea.textcontent.append("Exhibit 34: Share of transport greenhouse gas emissions in Europe47")
    thisalinea.textcontent.append("Road transport forms the highest proportion of overall transport emissions (72% in 2019 of all EU transport GHG).")
    thisalinea.textcontent.append("However, most of the existing and planned environmental measures in the Member States agenda focus on road")
    thisalinea.textcontent.append("transport, therefore, this share is expected to decrease as road transport decarbonises faster than other transport")
    thisalinea.textcontent.append("modes. The largest increases up to 2030 are projected in the aviation sector, followed by international maritime")
    thisalinea.textcontent.append("transport, as they are not prioritised by national policies. These sub-sectors are therefore expected to constitute a")
    thisalinea.textcontent.append("higher proportion of transport sector emissions in the coming years47.")
    thisalinea.textcontent.append("The road transport sector is already highly populated by GNSS applications which are consistently improving the")
    thisalinea.textcontent.append("performance of vehicles in terms of safety, cost of operation, and sustainability. Galileo information for roads,")
    thisalinea.textcontent.append("such as their geodetic height 48 , can be employed to unlock fuel savings, thus ensuring greener solutions for")
    thisalinea.textcontent.append("transportation vehicles. One such instance is provided by the Galileo-Ecodrive solution, in which actual and")
    thisalinea.textcontent.append("prospective information on road’s geodetic height profile to optimise the operation of auxiliary devices of vehicles.")
    thisalinea.textcontent.append("ESA estimated that for a typical mileage, fuel savings could be in the range of 3-5%, potentially saving up to two")
    thisalinea.textcontent.append("billion litres of fuel per year throughout Europe. Additionally, the use of satellite navigation systems such as Galileo")
    thisalinea.textcontent.append("for vehicles can reduce journey times by more than 10%, which clearly significantly contributes reducing emissions49.")
    thisalinea.textcontent.append("Exhibit 35: Use case - EU Space Programme for autonomous mobility")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Earth Observation in support of autonomous vehicles")
    thisalinea.textcontent.append("The city of Copenhagen, plans to achieve carbon neutrality by 2025 through a combination of")
    thisalinea.textcontent.append("intelligent public transit systems, electric car-sharing services, and improved city infrastructure for")
    thisalinea.textcontent.append("cycling and walking.50 Indeed, as recognised by Copenhagen as well as many other communities,")
    thisalinea.textcontent.append("smart mobility can provide a very significant push for green transportation and green cities at")
    thisalinea.textcontent.append("large. Transportation systems are estimated to account for 64% of global oil consumption and")
    thisalinea.textcontent.append("27% of global energy use.51")
    thisalinea.textcontent.append("Space data, including both remote sensing and navigation, is essential to unlock the great")
    thisalinea.textcontent.append("benefits deriving from smart mobility solutions. Several examples of (European) companies")
    thisalinea.textcontent.append("supporting the development of the smart mobility industries exist. One such instance is TernowAI.")
    thisalinea.textcontent.append("The company extensively employs remote sensing data from various sources including SAR")
    thisalinea.textcontent.append("imagery from Sentinel-1 in support of autonomous driving solutions. TernowAI develops various")
    thisalinea.textcontent.append("products highly relevant to autonomous vehicles through the processing of remote sensing data:")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Through a novel approach, the company can integrate SAR and optical imagery from satellites,")
    thisalinea.textcontent.append("enabling the measuring of GCPs with cm-level accuracy. This is an integral and fundamental part")
    thisalinea.textcontent.append("of both AeroSat Vector and HD maps. The former is based upon the processing of remote sensing")
    thisalinea.textcontent.append("data through proprietary algorithms to generate vector-based maps in lower resolution. In")
    thisalinea.textcontent.append("contrast, for the latter the company processes Earth observation images with artificial intelligence")
    thisalinea.textcontent.append("processes to entirely avoid the need for in-situ images. HD maps are amongst the key components")
    thisalinea.textcontent.append("of the infrastructure supporting widespread autonomous driving; these include information")
    thisalinea.textcontent.append("about the exact positions of various significant features of the urban landscape such as")
    thisalinea.textcontent.append("pedestrian crossing, traffic lights and signs, barriers and several others. In essence, most if not")
    thisalinea.textcontent.append("all autonomous car manufacturers have recognised the need for onboard HD maps for any")
    thisalinea.textcontent.append("autonomous vehicle for both safety reasons as well as for driver and passenger comfort.")
    thisalinea.textcontent.append("Companies such as TernowAI, integrating Earth observation imagery with AI processes, are well-")
    thisalinea.textcontent.append("positioned to meet this market need.")
    thisalinea.textcontent.append("Exhibit 36: TernowAI AeroSat HD Map product, provided in the OpenDRIVE format")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers52")
    thisalinea.textcontent.append("Copernicus can make electricity more affordable by facilitating renewable energy generation, making electric cars")
    thisalinea.textcontent.append("more common. Coupled with increasing fuel prices this year, lower electricity prices will attract more people to")
    thisalinea.textcontent.append("switch to electric cars. Self-driving cars and vehicles which are in development can benefit from more accurate")
    thisalinea.textcontent.append("positioning services provided by Galileo.")
    thisalinea.textcontent.append("The use of the EU Space Programme not only serves the road transport sector making it greener and more efficient,")
    thisalinea.textcontent.append("but it also helps in improving infrastructure management.")
    thisalinea.textcontent.append("Exhibit 37: Use case - EU Space Programme for highway management")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("must be put in place in order to do it")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers53")
    thisalinea.textcontent.append("Copernicus for road infrastructure management")
    thisalinea.textcontent.append("The traditional approach for road infrastructure building and maintenance does not rely on space")
    thisalinea.textcontent.append("data, being instead based on in-situ observations.")
    thisalinea.textcontent.append("Space data can help addressing road maintenance, making road assessments cheaper and")
    thisalinea.textcontent.append("easier to perform on a large scale thanks to regular observations allowing the development")
    thisalinea.textcontent.append("of periodically updated, country wide InSAR (Interferometric Synthetic Aperture Radar) maps")
    thisalinea.textcontent.append("including Sentinel-1 data. In turn, these analyses can then be already leveraged in the planning")
    thisalinea.textcontent.append("phases, optimising route design and reducing associated costs. The economic benefits of this")
    thisalinea.textcontent.append("paradigm shift enabled by Earth Observation satellites are estimated at almost €20 million for")
    thisalinea.textcontent.append("example for the Italian company ANAS alone.")
    thisalinea.textcontent.append("These benefits, however, are not merely economic. More efficient highway management reflects")
    thisalinea.textcontent.append("on the surrounding environment as well. On the one hand, not having to repeatedly modify")
    thisalinea.textcontent.append("designs and routes limits the impact of construction works, both in terms of the emission")
    thisalinea.textcontent.append("generated by construction activities as well as the modifications introduced in the")
    thisalinea.textcontent.append("geomorphological landscape. On the other, periodic monitoring using InSAR can help in")
    thisalinea.textcontent.append("identifying and mitigating any impact on, for example, local farms caused by induced changes in")
    thisalinea.textcontent.append("underground water flows and aquifer levels.")
    thisalinea.textcontent.append("In the future, the creation of larger archives of data thanks to InSAR will allow to analyse sites")
    thisalinea.textcontent.append("retrospectively. Additionally, the launch of new SAR satellites will increase both the resolution")
    thisalinea.textcontent.append("and the revisit times. This will make it possible to offer semi real-time monitoring that could be")
    thisalinea.textcontent.append("very useful during extreme-meteorological events, for faster response and for failure prediction")
    thisalinea.textcontent.append("purposes.")
    thisalinea.textcontent.append("As for the aviation sector, one of the main challenges is traffic management. Delays in planes' schedules create the")
    thisalinea.textcontent.append("necessity of prolonging the effective time planes have their engines running idle on the ground. In this context,")
    thisalinea.textcontent.append("EGNSS can come to help. There are projects aimed at using satellite navigation to reduce these delays through")
    thisalinea.textcontent.append("artificial intelligence algorithms analysing ground traffic data54.")
    thisalinea.textcontent.append("Exhibit 38: Use case - EU Space Programme for airport management")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("The EU wants to reduce greenhouse gas emissions in transport by 90% before 2050")
    thisalinea.textcontent.append("EGNSS for airport ground equipment management")
    thisalinea.textcontent.append("Large airports are complex hubs where logistics and consumer experience come together. The")
    thisalinea.textcontent.append("logistical challenges faced by airport staff and airliners are highly complex and require advanced")
    thisalinea.textcontent.append("tools to deal with these adequately. On the other hand, airports must consider the consumer")
    thisalinea.textcontent.append("experience: the walking distance from a gate to another, waiting time between flights, etc.")
    thisalinea.textcontent.append("From an environmental perspective, delays induce increased air pollution due to aeroplanes")
    thisalinea.textcontent.append("having to idle for longer at the gate with running engines while waiting for ground equipment")
    thisalinea.textcontent.append("to arrive. Since jet engines require some time to warm up prior to flight, it is common practice to")
    thisalinea.textcontent.append("keep engines running at gates. This is a wasteful practice to be able to clear the gate as soon as")
    thisalinea.textcontent.append("on-boarding is finished, and clearance is granted.")
    thisalinea.textcontent.append("Blue Dot Solutions is a company that developed a service focusing on reducing the occurrence of")
    thisalinea.textcontent.append("delays and limit the consequent additional air pollution and passenger frustrations. Their Ground")
    thisalinea.textcontent.append("Eye solution is composed of multiple layers (e.g., IoT devices, satellite data, statistics, data")
    thisalinea.textcontent.append("integration, mobile App) that work seamlessly together to provide situational awareness to")
    thisalinea.textcontent.append("operators on the ground.")
    thisalinea.textcontent.append("Exhibit 39: GroundEye interface")
    thisalinea.textcontent.append("Ground Eye uses accurate location of ground assets and aircraft at the airport to optimally")
    thisalinea.textcontent.append("utilise these resources and, as such, reduce delays. Galileo and SBAS are tools from the EU Space")
    thisalinea.textcontent.append("Programme that have proven increasingly useful in the provision of location data with the required")
    thisalinea.textcontent.append("accuracy to be used in tools like Ground Eye. More specifically, the location accuracy of EGNSS")
    thisalinea.textcontent.append("in difficult environments such as airports has been praised by the company as a contributing")
    thisalinea.textcontent.append("factor of the success for the Ground Eye tool.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers55")
    thisalinea.textcontent.append("In maritime operations, Earth Observation data from Copernicus can be used to determine the strength and direction")
    thisalinea.textcontent.append("of ocean streams, combing this data with precise navigation through Galileo and EGNOS to optimise routes, reducing")
    thisalinea.textcontent.append("fuel consumption and consequently emissions.")
    thisalinea.textcontent.append("Clean waters are critical for ocean life and humans, but some maritime accidents can lead to big amounts of oil")
    thisalinea.textcontent.append("spillage to waters and threaten life. Integrated maritime data can be used to counter these accidents. A good")
    thisalinea.textcontent.append("example of this is CleanSeaNet programme which is a European satellite-based oil spill monitoring and vessel")
    thisalinea.textcontent.append("detection service.")
    thisalinea.textcontent.append("Exhibit 40: Use case – EU Space Programme for safer maritime navigation56")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Green Deal is committed to drastically reducing the emissions from the transport sector")
    thisalinea.textcontent.append("and making operations safer for the human personnel")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("EU Space for navigation in Greenland")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Greenland is the largest non-continental island with many of its settlements being on smaller")
    thisalinea.textcontent.append("islands as well. As a result, almost all transport, of both goods and people, happens by sea.")
    thisalinea.textcontent.append("Navigating highly dynamic environment of Greenland can be dangerous and all the potential")
    thisalinea.textcontent.append("route changes can not only cause accidents with significant damage, but also be responsible")
    thisalinea.textcontent.append("for significant environmental impact.")
    thisalinea.textcontent.append("This situation has led to an ice-service provided by the Danish Meteorological Institute (DMI)")
    thisalinea.textcontent.append("located in Copenhagen which has evolved over the years to use data coming from the Sentinel")
    thisalinea.textcontent.append("satellites. DMI relies on both optical and radar imagery, as well as thermal infrared satellite")
    thisalinea.textcontent.append("data (e.g., AVHRR) and microwave radiometers (e.g., AMSR2) and altimeters. The main benefits")
    thisalinea.textcontent.append("of Copernicus data are the result of the satellite’s capability to capture large areas in very short")
    thisalinea.textcontent.append("time, providing higher and faster coverage than traditional in-situ measurements. The constant")
    thisalinea.textcontent.append("monitoring allows to identify evolving ice dynamics and, therefore, to optimise ship’s routes")
    thisalinea.textcontent.append("around ice formations and identify when new, better lanes become available.")
    thisalinea.textcontent.append("While this service provides important economic benefit to Greenland, around €10 million per year,")
    thisalinea.textcontent.append("a crucial contribution pertains to environmental benefits. Route optimisation allows to save fuel")
    thisalinea.textcontent.append("and even in the event of having to resort to longer routes, being able to avoid changing travel")
    thisalinea.textcontent.append("plans at the last-minute results in a net positive impact, thus making sea transport more")
    thisalinea.textcontent.append("sustainable. Furthermore, reliable and frequent satellite data can help prevent accidents and oil")
    thisalinea.textcontent.append("spills, safeguarding the integrity of the Arctic ecosystem. It is crucial to note that these benefits")
    thisalinea.textcontent.append("are compounded by the importance of Greenland and of polar ice in the overall context of")
    thisalinea.textcontent.append("climate change. The melting of frozen water reservoirs captured by the thick ice covering")
    thisalinea.textcontent.append("Greenland’s landmass will have a profound effect on global sea levels, endangering millions of")
    thisalinea.textcontent.append("people across the globe. Moreover, the island’s ice sheets are trapping significant amounts of")
    thisalinea.textcontent.append("methane: the release of this gas in the atmosphere because of increasing global temperatures")
    thisalinea.textcontent.append("would further compound the greenhouse effect, exacerbating an already critical situation.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers57")
    thisalinea.textcontent.append("Another use case for maritime is weather forecasting in the maritime environment. This is supported by collecting")
    thisalinea.textcontent.append("meteorological data and location data from the ships on the move. More accurate knowledge of the real conditions")
    thisalinea.textcontent.append("that this system will provide can lead to improvements to safety and fuel usage.")
    thisalinea.textcontent.append("EUSPA has actively funded the Prepare-Ships Project to support the development of a robust navigation application,")
    thisalinea.textcontent.append("integrating EGNSS and EO data through machine-learning processes to accurately predict the future positioning of")
    thisalinea.textcontent.append("nearby vessels. Besides ensuring safety at sea by decreasing collision risks, applications such as those developed")
    thisalinea.textcontent.append("within the scope of Prepare-Ships will facilitate energy-effective manoeuvring and route-optimisation, significantly")
    thisalinea.textcontent.append("reducing the environmental impact of maritime transportation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ The future of mobility is strongly depended on highly accurate location "
    thisalinea.titlefontsize = "9.47999999999999"
    thisalinea.nativeID = 110
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ The future of mobility is strongly depended on highly accurate location "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The future of mobility is strongly depended on highly accurate location")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Additionally, traffic can be optimised through better routing to reduce travelling time and fuel ..."
    thisalinea.titlefontsize = "9.47999999999999"
    thisalinea.nativeID = 111
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Additionally, traffic can be optimised through better routing to reduce travelling time and fuel consumption "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Additionally, traffic can be optimised through better routing to reduce travelling time and fuel")
    thisalinea.textcontent.append("consumption")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Reduction of CO₂ emissions is crucial for the maintenance of life on Earth "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 112
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ Reduction of CO₂ emissions is crucial for the maintenance of life on Earth "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Reduction of CO₂ emissions is crucial for the maintenance of life on Earth")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ The Green Deal sets important targets to decrease the emission of greenhouse gases "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 113
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "▪ The Green Deal sets important targets to decrease the emission of greenhouse gases "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The Green Deal sets important targets to decrease the emission of greenhouse gases")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Global cm-level Ground Control Points (GCPs) "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 114
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "▪ Global cm-level Ground Control Points (GCPs) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Global cm-level Ground Control Points (GCPs)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ AeroSat Vector Maps "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 115
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "▪ AeroSat Vector Maps "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ AeroSat Vector Maps")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Aerosat HD Maps "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 116
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "▪ Aerosat HD Maps "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Aerosat HD Maps")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Extensive road network is challenging to manage, high human and economic resources "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 117
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "▪ Extensive road network is challenging to manage, high human and economic resources "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Extensive road network is challenging to manage, high human and economic resources")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ In-situ observations are inefficient and characterise by high environmental footprint "
    thisalinea.titlefontsize = "9.47999999999999"
    thisalinea.nativeID = 118
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "▪ In-situ observations are inefficient and characterise by high environmental footprint "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ In-situ observations are inefficient and characterise by high environmental footprint")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ The European Green Deal pushes for a more efficient transport industry which can be ..."
    thisalinea.titlefontsize = "9.47999999999999"
    thisalinea.nativeID = 119
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "▪ The European Green Deal pushes for a more efficient transport industry which can be enabled by a better road network "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The European Green Deal pushes for a more efficient transport industry which can be")
    thisalinea.textcontent.append("enabled by a better road network")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Poor fleet coordination in airports can lead to higher emissions due to additional travel ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 120
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "▪ Poor fleet coordination in airports can lead to higher emissions due to additional travel Challenge time and/or congestion "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Poor fleet coordination in airports can lead to higher emissions due to additional travel")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("time and/or congestion")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Congestions in airports can lead aircrafts to prolong their time in the air "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 121
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "▪ Congestions in airports can lead aircrafts to prolong their time in the air "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Congestions in airports can lead aircrafts to prolong their time in the air")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Navigation in challenging environment might be difficult due to the fast-changing ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 122
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "▪ Navigation in challenging environment might be difficult due to the fast-changing conditions which can force crews to unexpected deviations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Navigation in challenging environment might be difficult due to the fast-changing")
    thisalinea.textcontent.append("conditions which can force crews to unexpected deviations")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Such deviations increase fuel consumption of ships and therefore the environmental ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 123
    thisalinea.parentID = 109
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "▪ Such deviations increase fuel consumption of ships and therefore the environmental footprint of maritime operations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Such deviations increase fuel consumption of ships and therefore the environmental")
    thisalinea.textcontent.append("footprint of maritime operations")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.5 A healthier and greener food system"
    thisalinea.titlefontsize = "14.04000000000002"
    thisalinea.nativeID = 124
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Tackling green agriculture is a task on many fronts. Precision agriculture and better enforcement of agro- environmental policies underpin the response that is meant to lead the sector into a 50% reduction of chemicals used, and climate neutrality by 2035. The use of digital technologies in agriculture is helping the whole sector improve its performance and become greener. The necessity for efficiency and sustainability of agricultural production is growing. Companies are highly aware of the importance of enhancing productivity without harming the environment, and, therefore, are continually looking for means to achieve this. In this context, the EU Space Programme "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Tackling green agriculture is a task on many fronts. Precision agriculture and better enforcement of agro-")
    thisalinea.textcontent.append("environmental policies underpin the response that is meant to lead the sector into a 50% reduction of chemicals")
    thisalinea.textcontent.append("used, and climate neutrality by 2035. The use of digital technologies in agriculture is helping the whole sector")
    thisalinea.textcontent.append("improve its performance and become greener.")
    thisalinea.textcontent.append("The necessity for efficiency and sustainability of agricultural production is growing. Companies are highly aware of")
    thisalinea.textcontent.append("the importance of enhancing productivity without harming the environment, and, therefore, are continually looking")
    thisalinea.textcontent.append("for means to achieve this. In this context, the EU Space Programme is a key asset in supporting agricultural")
    thisalinea.textcontent.append("businesses to reduce costs and improve quality of goods, while ensuring sustainable practices.")
    thisalinea.textcontent.append("The synergy between Galileo signals, Copernicus data and Artificial Intelligence (AI) based techniques facilitates")
    thisalinea.textcontent.append("the operation of both crewed and uncrewed vehicles – aerial and land-based – for optimised farming. Copernicus")
    thisalinea.textcontent.append("imagery provides the foundations for digital field models, including the identification of boundaries with other plots,")
    thisalinea.textcontent.append("the mapping and evolution of crops and invasive species. These may then be fed into AI algorithms to determine")
    thisalinea.textcontent.append("optimal intervention points, fertiliser and pesticide quantities and distribution, and efficient weed-removal")
    thisalinea.textcontent.append("methods. Galileo enables the implementation of these models, by efficiently and accurately guiding agri-vehicles")
    thisalinea.textcontent.append("Exhibit 41: Use case - EU Space Programme for smart agri-resource management")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– most commonly tractors and drones – in optimal patterns with accurate location. "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 125
    thisalinea.parentID = 124
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– most commonly tractors and drones – in optimal patterns with accurate location. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– most commonly tractors and drones – in optimal patterns with accurate location.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Challenge"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 126
    thisalinea.parentID = 124
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Crop management and monitoring in situ can be costly and not efficient. Resources as water, fertilisers and pesticides are often used extensively, generating costs to farmers and polluting soils, air and water ▪ Moreover, crops can suffer from diseases, pests and nutrient deficiencies, which, if late diagnosed, can harm the whole field "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Crop management and monitoring in situ can be costly and not efficient. Resources as ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 127
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Crop management and monitoring in situ can be costly and not efficient. Resources as water, fertilisers and pesticides are often used extensively, generating costs to farmers and polluting soils, air and water "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Crop management and monitoring in situ can be costly and not efficient. Resources as")
    thisalinea.textcontent.append("water, fertilisers and pesticides are often used extensively, generating costs to farmers and")
    thisalinea.textcontent.append("polluting soils, air and water")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Moreover, crops can suffer from diseases, pests and nutrient deficiencies, which, if late ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 128
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Moreover, crops can suffer from diseases, pests and nutrient deficiencies, which, if late diagnosed, can harm the whole field "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Moreover, crops can suffer from diseases, pests and nutrient deficiencies, which, if late")
    thisalinea.textcontent.append("diagnosed, can harm the whole field")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Role of the Green Deal"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 129
    thisalinea.parentID = 124
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ The Green Deal sets important goals on water, pesticides and fertiliser usage, aiming to improve the health of soil and people. It is important to highlight that overuse of pesticides may result in contamination of soil, water and non-target plants and animals that can decrease biodiversity and, in some cases, reduce crop yield "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ The Green Deal sets important goals on water, pesticides and fertiliser usage, aiming to ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 130
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ The Green Deal sets important goals on water, pesticides and fertiliser usage, aiming to improve the health of soil and people. It is important to highlight that overuse of pesticides may result in contamination of soil, water and non-target plants and animals that can decrease biodiversity and, in some cases, reduce crop yield "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ The Green Deal sets important goals on water, pesticides and fertiliser usage, aiming to")
    thisalinea.textcontent.append("improve the health of soil and people. It is important to highlight that overuse of pesticides")
    thisalinea.textcontent.append("may result in contamination of soil, water and non-target plants and animals that can")
    thisalinea.textcontent.append("decrease biodiversity and, in some cases, reduce crop yield")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ ₂ "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 131
    thisalinea.parentID = 129
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ ₂")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "Solution offered by EU Space"
    thisalinea.titlefontsize = "11.039999999999964"
    thisalinea.nativeID = 132
    thisalinea.parentID = 124
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Example of real-life use case Copernicus for crop monitoring in BelgiumPotato cultivation in central Europe has enlarged to such an extent over the last decades that any further switch from any crop to potatoes is very likely to result in soil degradation and soil depletion. Thus, a higher output and growth can only be reached through an improvement in the efficiency of agricultural land utilisation. Potato fields in Belgium today achieve an output around 50 tonnes per hectare, but maximum output is expected to be double than that, around 100 tonnes/ha. This higher supply can only result from better, more "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life use")
    thisalinea.textcontent.append("case")
    thisalinea.textcontent.append("Copernicus for crop monitoring in BelgiumPotato cultivation in central Europe has enlarged to")
    thisalinea.textcontent.append("such an extent over the last decades that any further switch from any crop to potatoes is very")
    thisalinea.textcontent.append("likely to result in soil degradation and soil depletion. Thus, a higher output and growth can only")
    thisalinea.textcontent.append("be reached through an improvement in the efficiency of agricultural land utilisation. Potato fields")
    thisalinea.textcontent.append("in Belgium today achieve an output around 50 tonnes per hectare, but maximum output is")
    thisalinea.textcontent.append("expected to be double than that, around 100 tonnes/ha. This higher supply can only result from")
    thisalinea.textcontent.append("better, more sustainable and more effective farm management practices. An ulterior factor playing")
    thisalinea.textcontent.append("a significant role is climate and the consequent weather: unexpected changes in the weather")
    thisalinea.textcontent.append("Space data can play a central role in potato industry, both in helping it become more efficient to")
    thisalinea.textcontent.append("meet upcoming challenges as well as in providing it with the necessary tools to face the effects")
    thisalinea.textcontent.append("of climate change. As a matter of fact, it is already doing so. VITO, a Flemish independent research")
    thisalinea.textcontent.append("organization in the field of cleantech and sustainable development, has developed in cooperation")
    thisalinea.textcontent.append("with Belgapom a Copernicus-based service called WatchITgrow58, entirely dedicated to the")
    thisalinea.textcontent.append("Belgian potato industry. WatchITgrow is a geo-information platform relying on data from both")
    thisalinea.textcontent.append("Sentinel-1 and Sentinel-2 which can provide potato farmers, agronomists, traders and processors")
    thisalinea.textcontent.append("with data and information on the growth of different potato varieties. Complementing this space-")
    thisalinea.textcontent.append("based dataset with information from other satellites, drones, weather and soil measurements, this")
    thisalinea.textcontent.append("service offers extensive support to the potato sector, including information on the state and")
    thisalinea.textcontent.append("growth of crops, yields and harvest dates estimates, as well as enabling the improvement of")
    thisalinea.textcontent.append("yields and reducing production and quality losses.")
    thisalinea.textcontent.append("Exhibit 42: WatchITgrow interface for")
    thisalinea.textcontent.append("crop management")
    thisalinea.textcontent.append("Future developments are set to provide even")
    thisalinea.textcontent.append("more benefits. Thanks to an increase in the")
    thisalinea.textcontent.append("quantity and quality of data available,")
    thisalinea.textcontent.append("together with the capabilities introduced by")
    thisalinea.textcontent.append("new generation of satellites, it will be possible")
    thisalinea.textcontent.append("to provide farmers with recommendations on")
    thisalinea.textcontent.append("nitrogen fertilisation – thus also generating")
    thisalinea.textcontent.append("positive environmental impact –, as well as")
    thisalinea.textcontent.append("warnings for irrigation scheduling and even")
    thisalinea.textcontent.append("major diseases such as late blight. Not only")
    thisalinea.textcontent.append("will this unlock new economic benefits, but")
    thisalinea.textcontent.append("also it will provide significant environmental")
    thisalinea.textcontent.append("impact: Copernicus will enable greener and")
    thisalinea.textcontent.append("healthier food by optimising the use of")
    thisalinea.textcontent.append("pesticides, making sure they are used only when and where necessary and thus reducing the")
    thisalinea.textcontent.append("excess fertilizer not taken up by the plants and, therefore, the excess nutrients which run-off into")
    thisalinea.textcontent.append("surface-water channels contaminating water supplies.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers59")
    thisalinea.textcontent.append("Enabled by the large availability of space data, especially EGNSS, precision agriculture is helping to support")
    thisalinea.textcontent.append("improvement of production of crops and the green transformation. The first benefit of this practice is the water saved")
    thisalinea.textcontent.append("in agriculture, which accounts for 4% of water saved per year60. Moreover, thanks to precision agriculture and space")
    thisalinea.textcontent.append("data in general, it is possible to save up to 9% of pesticides and 7% of fertilisers60. Another important factor to")
    thisalinea.textcontent.append("consider is the fuel consumption for all the activities related to agriculture, which precision agriculture is estimated")
    thisalinea.textcontent.append("to reduce by 6%60. As a result of those improvements, in 2022, precision agriculture is estimated to have a huge")
    thisalinea.textcontent.append("economic and sustainable impact on the sector, growing considerably in the next years.")
    thisalinea.textcontent.append("Exhibit 43: Use case - Copernicus for more efficient use of water in the food industry")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Use of water in the food industry is subjected to strict regulation both to preserve the")
    thisalinea.textcontent.append("environment and consumers’ health")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Green Deal aims to establish a more sustainable food chain in which a responsible use of")
    thisalinea.textcontent.append("natural resources leads to reduced waste and increased quality of products")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers61")
    thisalinea.textcontent.append("Copernicus for water management in the food industry Space data can play a pivotal role in")
    thisalinea.textcontent.append("addressing the water challenges of the beer industry, as proven by Heineken, the number one")
    thisalinea.textcontent.append("brewer in Europe and one of the largest in the world. Heineken’s brewery in Zoeterwoude, a")
    thisalinea.textcontent.append("municipality in the Netherlands, uses local river water for its needs. The water is stored and purified")
    thisalinea.textcontent.append("by the dunes in South Holland before reaching the facility where it can be used in the brewing")
    thisalinea.textcontent.append("process. To improve the water management in its area, this Heineken brewery partnered with the")
    thisalinea.textcontent.append("University of Wageningen creating the Green Circles cooperative.")
    thisalinea.textcontent.append("Thanks to this collaboration, Heineken can combine satellite observations with meteorological data")
    thisalinea.textcontent.append("and the results of other biophysical analyses to forecasts floods and droughts, thus obtaining")
    thisalinea.textcontent.append("valuable information to improve water resource management. Wageningen Environmental")
    thisalinea.textcontent.append('Research and Climate Adaptation Services leveraged a wide range of data to create "story maps",')
    thisalinea.textcontent.append("combining GIS maps and artist impressions.")
    thisalinea.textcontent.append("Using these, the Green Circles partners can easily plan a more responsible approach to business")
    thisalinea.textcontent.append("and environmental development. The Copernicus Climate Change Service proved extremely")
    thisalinea.textcontent.append("valuable in providing prototype water indicators, one of the most comprehensive and up-to-date")
    thisalinea.textcontent.append("climate change resources. These data can be mapped graphically, thus helping the wider")
    thisalinea.textcontent.append("community to understand the impact at a pan-European level, and are a critical add-on to local")
    thisalinea.textcontent.append("data, such as meteorological information and observation from in situ stations. It is important to")
    thisalinea.textcontent.append("note that, with this data, Wageningen Environmental Research has been able to develop accurate")
    thisalinea.textcontent.append("forecasts of water flows, which allowed Heineken Netherlands to act, improving its water")
    thisalinea.textcontent.append("management and reducing its environmental impact. Furthermore, it also fostered the birth of new")
    thisalinea.textcontent.append("spin-off projects. For example, Heineken invested in the creation of marshland to naturally")
    thisalinea.textcontent.append("purify the wastewater from the brewery, as natural purification costs less, has ecological benefits,")
    thisalinea.textcontent.append("creates a pleasant environment, and will provide a store of water in times of drought.")
    thisalinea.textcontent.append("Copernicus can also be used to then monitor and enforce performance-based agriculture. Farmers are provided")
    thisalinea.textcontent.append("with a measure of how their crops are performing, while also having access to historical data as well as forecasts")
    thisalinea.textcontent.append("on how the future performance is likely to be. Rewarding systems – such as the one enforced by the Agoro Carbon")
    thisalinea.textcontent.append("Alliance 62 are enabled by satellite imagery. Previously, aerial or manual, land-based surveying was necessary,")
    thisalinea.textcontent.append("rendering these systems very costly, and in certain instances infeasible in the more sparsely populated countryside.")
    thisalinea.textcontent.append("The open and free nature of Copernicus data allows for these systems to be put in place to more easily and")
    thisalinea.textcontent.append("effectively enforce the agricultural policy. The monitoring of the growth and evolution of invasive alien species, as")
    thisalinea.textcontent.append("well as illegal practices in agriculture, is also directly enabled by similar systems.")
    thisalinea.textcontent.append("Soil is of course of critical importance for the health and sustainability of crops and their products, and in addition")
    thisalinea.textcontent.append("provides invaluable ecosystem services such as ensuring the cleanliness of water, supporting biodiversity and")
    thisalinea.textcontent.append("helping to regulate climate. EO data from Copernicus in conjunction with ground measurements (e.g., from the Land")
    thisalinea.textcontent.append("Use/Cover Area frame Survey (LUCAS) soil monitoring system) provide key data and information for")
    thisalinea.textcontent.append("the monitoring and verification of soil conditions, which in turn can support analyses on the health of crops and")
    thisalinea.textcontent.append("food. Also, EGNSS and Copernicus can provide early warnings for natural disasters and increase food security")
    thisalinea.textcontent.append("further.")
    thisalinea.textcontent.append("Copernicus data and products developed by CAMS and C3S can not only benefit climate action within the")
    thisalinea.textcontent.append("agricultural sector but can also be used to ensure food security. Indeed, CAMS monitors the concentration of")
    thisalinea.textcontent.append("carbon dioxide, nitrous oxide and methane among other greenhouse gases, 23% of which are estimated to be")
    thisalinea.textcontent.append("emitted as a result of human activities in agriculture and forestry. Agriculture is a particular case for climate action")
    thisalinea.textcontent.append("as it not only contributes to emissions of greenhouse gases, but also helps their mitigation and their uptake as crops")
    thisalinea.textcontent.append("and other vegetation act as sinks. As such, C3S created the Sectoral Information System for Global Agriculture to")
    thisalinea.textcontent.append("allow the sector to adapt to the changes brought by climate change, ensuring that crop yields in critical areas remain")
    thisalinea.textcontent.append("consistent as well as allowing for efficiencies to be unlocked, thus helping to reduce the impact of the agricultural")
    thisalinea.textcontent.append("sector on the environment.63")
    thisalinea.textcontent.append("Livestock management is another dimension that EO and GNSS can improve. Selecting an ideal grazing area is")
    thisalinea.textcontent.append("important. Likewise, sustainable livestock reproduction is facilitated by GNSS and EO.")
    thisalinea.textcontent.append("Galileo is also to be further used in a similar fashion to the electronic product passport, to establish a food passport.")
    thisalinea.textcontent.append("This would provide consumers with reliable, traceable information about the origin and path of a food product from")
    thisalinea.textcontent.append("‘Farm to Fork’, adding another beneficial food safety dimension to the existing system, and promoting more")
    thisalinea.textcontent.append("nutritious food, for healthier lifestyles. At the same time, from the farmer's perspective, this adds value to the")
    thisalinea.textcontent.append("product being produced. Furthermore, data and information from EO and GNSS can be coupled with innovative")
    thisalinea.textcontent.append("technologies such as blockchain and Distributed Ledger Technology (DLT), both of which are considered to have")
    thisalinea.textcontent.append("great potential in the agricultural sector. The application of these technologies can ensure the traceability of foods")
    thisalinea.textcontent.append("from source to consumer, ensuring their immutability and auditability.")
    thisalinea.textcontent.append("Exhibit 44: Use case - Copernicus for more efficient use of water resources")
    thisalinea.textcontent.append("Green Deal aims to more sustainable and responsible use of natural resources")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Copernicus for aquifer monitoring")
    thisalinea.textcontent.append("The term “aquifer” 64 refers to an underground layer of rock or sediment capable to absorb and")
    thisalinea.textcontent.append("hold water permeating through the soil. Groundwater extracted from aquifers is an invaluable")
    thisalinea.textcontent.append("resource, with demand growing due to the need for potable water and households, irrigation for")
    thisalinea.textcontent.append("agriculture, and industry. When this demand exceeds available supply, the resulting")
    thisalinea.textcontent.append("environmental damage can be extremely serious and can lead to land subsidence (i.e., the gradual")
    thisalinea.textcontent.append("settling or sudden sinking of land surface due to underground movements). Furthermore, the")
    thisalinea.textcontent.append("extensive exploitation and the resulting pollution make it so that only 1% of all freshwaters")
    thisalinea.textcontent.append("(including both aquifers and surface sources) is available for direct use.It is therefore evident that")
    thisalinea.textcontent.append("effective and appropriate management of aquifers is indispensable for sustainable use and long-")
    thisalinea.textcontent.append("term availability of groundwater. This is the case, for example, for the Spanish region of Murcia")
    thisalinea.textcontent.append("where the policies related to groundwater are impacted by the European Water Framework")
    thisalinea.textcontent.append("Directive (WFD) and implemented by CHS, the regional River Basin Authority. Leveraging")
    thisalinea.textcontent.append("traditional methods, CHS has deployed over the years an extensive network of ground stations to")
    thisalinea.textcontent.append("measure piezometric levels of water pressure and estimate water levels in aquifers. EU Space")
    thisalinea.textcontent.append("Data has played a role in this field for several years now, thanks to the use of GNSS-enabled")
    thisalinea.textcontent.append("ground stations. This has widely improved the data collection process, making it more reliable")
    thisalinea.textcontent.append("and more easily performed than in the past.")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Copernicus Sentinel-1 SAR data can provide all-weather, day-night capability to accurately")
    thisalinea.textcontent.append("detect and measure ground observations. The observation allows to compare the images at")
    thisalinea.textcontent.append("different points in time and thus compute ground deformations up to a few millimetres.")
    thisalinea.textcontent.append("Additionally, the European Ground Motion Service (EGMS) can provide consistent data regarding")
    thisalinea.textcontent.append("ground displacements.")
    thisalinea.textcontent.append("Exhibit 45: Satellite map of ground")
    thisalinea.textcontent.append("deformation")
    thisalinea.textcontent.append("As a result, aquifer management becomes")
    thisalinea.textcontent.append("more efficient, with a plethora of")
    thisalinea.textcontent.append("environmental benefits as a consequence.")
    thisalinea.textcontent.append("Optimising water extraction can help prevent")
    thisalinea.textcontent.append("ground subsidence and reduce, or even avoid,")
    thisalinea.textcontent.append("aquifer depletion. Additionally, space data-")
    thisalinea.textcontent.append("based decision-making can play a central role")
    thisalinea.textcontent.append("in maintaining river levels above those")
    thisalinea.textcontent.append("thresholds that would impact ecosystems")
    thisalinea.textcontent.append("and protected natural spaces. Moreover,")
    thisalinea.textcontent.append("satellite data can also contribute to quickly")
    thisalinea.textcontent.append("identifying and thus preventing saltwater")
    thisalinea.textcontent.append("infiltration in the aquifer, which degrades the")
    thisalinea.textcontent.append("quality of the water and affects agricultural soil. Furthermore, satellite monitoring can even go")
    thisalinea.textcontent.append("beyond, for example allowing to track the stability of mining waste dumps and playing a role in")
    thisalinea.textcontent.append("preventing the contamination of groundwater from polluting chemicals.")
    thisalinea.textcontent.append("Companies, such as Detektia monitor ground water dynamics and slope stability using DInSAR")
    thisalinea.textcontent.append("and InSAR technology. Detektia transforms the information provided by satellites into digital")
    thisalinea.textcontent.append("solutions for infrastructure management.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers65")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Water is one of the most precious resources we have, and it must be ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 133
    thisalinea.parentID = 132
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Water is one of the most precious resources we have, and it must be managed with the maximum attention "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Water is one of the most precious resources we have, and it must be managed with the")
    thisalinea.textcontent.append("maximum attention")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "▪ Aquifers must be strictly monitored to preserve their integrity and the safety of ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 134
    thisalinea.parentID = 132
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Aquifers must be strictly monitored to preserve their integrity and the safety of surrounding areas "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Aquifers must be strictly monitored to preserve their integrity and the safety of")
    thisalinea.textcontent.append("surrounding areas")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.6 Restored ecosystems and biodiversity"
    thisalinea.titlefontsize = "14.040000000000077"
    thisalinea.nativeID = 135
    thisalinea.parentID = 95
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Climate change has impacted global biodiversity as well as ecosystems and will continue to be one of the leading drivers of biodiversity loss in the 21st century. Such a threat to the natural environment requires proportionate action in the management of ecosystems through conservation and restoration. The Copernicus Climate Change Service (C3S) provides operational climate indicators that help properly assess and manage biodiversity loss. Implemented by the European Centre for Medium-Range Weather Forecasts (ECMWF) on behalf of the European Commission, the centre provides climate data and information on a range of sectoral areas affecting ecosystems and biodiversity (i.e., climate change, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Climate change has impacted global biodiversity as well as ecosystems and will continue to be one of the leading")
    thisalinea.textcontent.append("drivers of biodiversity loss in the 21st century. Such a threat to the natural environment requires proportionate action")
    thisalinea.textcontent.append("in the management of ecosystems through conservation and restoration.")
    thisalinea.textcontent.append("The Copernicus Climate Change Service (C3S) provides operational climate indicators that help properly assess")
    thisalinea.textcontent.append("and manage biodiversity loss. Implemented by the European Centre for Medium-Range Weather Forecasts")
    thisalinea.textcontent.append("(ECMWF) on behalf of the European Commission, the centre provides climate data and information on a range of")
    thisalinea.textcontent.append("sectoral areas affecting ecosystems and biodiversity (i.e., climate change, marine and land conditions).")
    thisalinea.textcontent.append("In particular, there are climate-biodiversity indicators developed within the Sectoral Information System (SIS),")
    thisalinea.textcontent.append("which assist in assessing the impact of temperature, rainfall and other atmospheric, terrestrial or oceanic variables")
    thisalinea.textcontent.append("on habitat suitability, species distribution and species fitness and reproduction. The indicators can be used for")
    thisalinea.textcontent.append("biodiversity and ecosystem service assessments for both fauna and flora, in the terrestrial as well as the marine")
    thisalinea.textcontent.append("biosphere, for different climatic zones around the globe. The SIS for Global Biodiversity offers a flexible, generic")
    thisalinea.textcontent.append("platform providing global users with access to key information. Importantly, SIS can provide support for decision-")
    thisalinea.textcontent.append("makers mitigating the current lack of relevant climate data. Indeed, policymakers, scientists, nature conservation")
    thisalinea.textcontent.append("agencies, landowners, private companies etc. all over the world are currently using this data to inform their decision-")
    thisalinea.textcontent.append("making process on issues impacting their direct business and society at large.")
    thisalinea.textcontent.append("As a tangible example of data-driven change, a country renowned for its pristine nature and sustainability is Costa")
    thisalinea.textcontent.append("Rica, whose development goals are directly linked to biodiversity. Because of the scarcity of consistent and reliable")
    thisalinea.textcontent.append("national data, the country relies on data from the C3S Climate Data Store which is used in conjunction with local")
    thisalinea.textcontent.append("station data to provide a baseline for downscaled and calibrated climate data and basic biodiversity indicators")
    thisalinea.textcontent.append("that could be projected into the future.")
    thisalinea.textcontent.append("The results pulled from the data showed that the temperature and precipitation will likely increase by 2040 along")
    thisalinea.textcontent.append("with a potential shift in biodiversity resulting from the rise in temperature. Moreover, it helped facilitate the Costa")
    thisalinea.textcontent.append("Rican government’s decision-making regarding a crucial policy topic. All in all, this use case showcases the central")
    thisalinea.textcontent.append("role that Copernicus data can play in monitoring, assessing, managing and mitigating biodiversity and ecosystem")
    thisalinea.textcontent.append("services. Additionally, the results can be used to inform adaptive measures which will increase the resilience of the")
    thisalinea.textcontent.append("country’s ecosystems.")
    thisalinea.textcontent.append("Support for biodiversity protection policies is also provided by the Copernicus Marine Environment Monitoring")
    thisalinea.textcontent.append("Service (CMEMS), working to preserve marine biodiversity worldwide. Once again, the data offered to decision-")
    thisalinea.textcontent.append("makers allows for data-driven, holistic strategies to be implemented. Within the European frameworks, CMEMS")
    thisalinea.textcontent.append("data is used to support the EU Marine Strategy Framework Directive, the EU Biodiversity Strategy and the EU Habitat")
    thisalinea.textcontent.append("Directive. Concrete examples of the use of Copernicus data for the Marine Strategy Framework Directive are the")
    thisalinea.textcontent.append("improvement of eutrophication assessments through the leveraging of ocean colour data, as well as data on ocean")
    thisalinea.textcontent.append("currents allowing the tracking of and response operations for oil spill drifts. Furthermore, EU decision-makers, as")
    thisalinea.textcontent.append("well as national and local administrators, use several different variables monitored by CMEMS (e.g., low and mid")
    thisalinea.textcontent.append("trophic levels biomass, ocean colour, ocean temperature, etc.) in order to implement the EU’s Biodiversity Strategy")
    thisalinea.textcontent.append("as set out in the European Green Deal.")
    thisalinea.textcontent.append("Many relevant examples can be found in the industry. Leading companies in the renewable energy segment – wind,")
    thisalinea.textcontent.append("due to the risk of bird strikes, and solar due to high land take, in particular – are beginning to integrate biodiversity")
    thisalinea.textcontent.append("action into their ESG strategy. This may involve targets for biodiversity loss minimisation, and even species")
    thisalinea.textcontent.append("reintroduction in harmony with the developed energy projects. In agriculture, also, increases in efficiencies allow for")
    thisalinea.textcontent.append("cooperatives and associations to engage in similar initiatives, thanks to the subsequently decreased land take and")
    thisalinea.textcontent.append("thus more areas available for biodiversity preservation. A combination of EGNSS-based tracking (e.g., for protected")
    thisalinea.textcontent.append("aviary species or similar), and Copernicus data and information used for vegetation/forestry planning and monitoring,")
    thisalinea.textcontent.append("as well as habitat management can enable such initiatives. Use cases of tracking also include predicting conservation")
    thisalinea.textcontent.append("hot-spots, identifying human-animal interaction zones, sustaining productive fisheries and understanding spread of")
    thisalinea.textcontent.append("diseases.")
    thisalinea.textcontent.append("Another relevant application to which Copernicus contributes is the monitoring of pipelines. In general, early")
    thisalinea.textcontent.append("pipeline leak detection tends to be difficult due to the vast geographic area affected, if not quickly contained they")
    thisalinea.textcontent.append("can lead to severe environmental impacts ranging from oil pollution to unwanted methane gas emissions.")
    thisalinea.textcontent.append("Forests are another key asset and host of biodiversity for Europe, not only for resource generation, but also as a")
    thisalinea.textcontent.append("green lung for the European population. In 2020, the EU had an estimated 159 million hectares of forests. This")
    thisalinea.textcontent.append("area has increased by almost 10% since 1990 (145 million hectares). In five EU Member States, more than half of")
    thisalinea.textcontent.append("the land area was covered with forests: Finland (66%), Sweden (63%), Slovenia (61%), Estonia (54%) and Latvia")
    thisalinea.textcontent.append("(53%)66.")
    thisalinea.textcontent.append("Earth Observation data provide forest authorities with accurate forest mapping, usable for storm damages")
    thisalinea.textcontent.append("assessment, inventory and validation of forest strands for wood purchasers. Thanks to time series of satellite images")
    thisalinea.textcontent.append("forest authorities are also able to detect a change in the land cover/land use in forest areas like illegal clear cut for")
    thisalinea.textcontent.append("example, or urban areas expansion threatening the ecosystem. These instruments appear to be even more important")
    thisalinea.textcontent.append("if considering that in the EU more than 60% of forests are privately owned67.")
    thisalinea.textcontent.append("Exhibit 45: Use case – Copernicus for deforestation and forest management")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("natural resources and protect the biosphere")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("The Green Deal poses as one of its objectives the preservation of biodiversity and of the")
    thisalinea.textcontent.append("natural environment")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Copernicus for deforestation monitoring")
    thisalinea.textcontent.append("Forests account for most of Earth’s terrestrial biodiversity, covering 31% of the global land area;")
    thisalinea.textcontent.append("they supply water, provide livelihoods (over 90% of those living in extreme poverty are dependent")
    thisalinea.textcontent.append("on forests), help mitigate climate change and are key to the production of sustainable food.")
    thisalinea.textcontent.append("However, the health of forests has been and continues to be threatened by deforestation and")
    thisalinea.textcontent.append("degradation. Between 2015 and 2020, approximately 10 million hectares per year were lost due")
    thisalinea.textcontent.append("to deforestation, about 0.25% of the total forest land area. In this context, the EU agreed law to")
    thisalinea.textcontent.append("fight global deforestation and forest degradation driven by EU production and")
    thisalinea.textcontent.append("consumption through the provisional political agreement just reached between the European")
    thisalinea.textcontent.append("Parliament and the Council on an EU Regulation on deforestation-free supply chains.68")
    thisalinea.textcontent.append("For instance, Satelligence uses optical and radar satellite data from Sentinel-1 and Sentinel-")
    thisalinea.textcontent.append("2, both archived and recent, to generate the Forest Loss Risk Index. This incorporates accurate")
    thisalinea.textcontent.append("forest and other land cover and deforestation information, enabling the identification of risks in")
    thisalinea.textcontent.append("the entire landscape, supporting and informing programmatic intervention. 69 Furthermore,")
    thisalinea.textcontent.append("satellite data is integrated with supply chain data stored in an up-to-date database of million so")
    thisalinea.textcontent.append("geolocated farms, concessions, factories, and other key locations. Satelligence can thus provide")
    thisalinea.textcontent.append("key insights on performance of agricultural production and supply chain risks linked with")
    thisalinea.textcontent.append("deforestation.")
    thisalinea.textcontent.append("Exhibit 46: Sample Satelligence")
    thisalinea.textcontent.append("deforestation product")
    thisalinea.textcontent.append("In essence, Satelligence’s use of")
    thisalinea.textcontent.append("satellite data from Copernicus")
    thisalinea.textcontent.append("allows real-time notifications on")
    thisalinea.textcontent.append("deforestation trends and events")
    thisalinea.textcontent.append("inside and outside its customers’")
    thisalinea.textcontent.append("supply chains, as well as")
    thisalinea.textcontent.append("supporting progress towards")
    thisalinea.textcontent.append("sustainability commitments")
    thisalinea.textcontent.append("through historical and current")
    thisalinea.textcontent.append("deforestation risk analysis. One")
    thisalinea.textcontent.append("further example of this is the")
    thisalinea.textcontent.append("company’s service in support of")
    thisalinea.textcontent.append("carbon monitoring, allowing its")
    thisalinea.textcontent.append("customers to reduce and offset")
    thisalinea.textcontent.append("their carbon emissions to meet commitments and net-zero targets. Using a combination of")
    thisalinea.textcontent.append("satellite data from Copernicus, spaceborne LiDAR and machine learning, Satelligence monitors")
    thisalinea.textcontent.append("carbon stocks and sequestration from deforestation, as well as tracking the carbon emissions")
    thisalinea.textcontent.append("resulting from continued deforestation activities.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers70")
    thisalinea.textcontent.append("Assuming data from the European Association of Remote Sensing Companies (EARSC) to be consistent in all of")
    thisalinea.textcontent.append("Europe71, 10% of all the clear-cut areas (i.e., areas in which cutting activities is allowed following specific restrictions)")
    thisalinea.textcontent.append("were not complying with the boundaries of the cut area or were not as they were supposed to be. Clear-cut areas")
    thisalinea.textcontent.append("in Europe account for about 10% of the total forest area 72 (i.e., 16 million hectares). Copernicus is expected to")
    thisalinea.textcontent.append("contribute from 2% to 10% of the spotted non-compliant areas. This in the worst-case scenario means that")
    thisalinea.textcontent.append("Copernicus contributed to saving 32 k hectares of forest only in 2022. Considering that each hectare of forest")
    thisalinea.textcontent.append("stores 750 tonnes of CO2 and contributes to absorbing 90 tonnes of CO2 per year, Copernicus is directly accountable")
    thisalinea.textcontent.append("for saving about 27 million tonnes of CO2 per year. On a global scale, Copernicus is already a crucial tool for")
    thisalinea.textcontent.append("innovation happening in the voluntary carbon market’s monitoring, reporting, and verification.")
    thisalinea.textcontent.append("Exhibit 47: Use case - EU Space Programme for tourism")
    thisalinea.textcontent.append("Challenge")
    thisalinea.textcontent.append("Role of the")
    thisalinea.textcontent.append("Green Deal")
    thisalinea.textcontent.append("The EU through the Green Deal commits to shift the economy towards a greener direction")
    thisalinea.textcontent.append("characterised by a more responsible [touristic] industry")
    thisalinea.textcontent.append("Solution")
    thisalinea.textcontent.append("offered by")
    thisalinea.textcontent.append("EU Space")
    thisalinea.textcontent.append("Example of")
    thisalinea.textcontent.append("real-life")
    thisalinea.textcontent.append("use case")
    thisalinea.textcontent.append("Copernicus for tourism impact assessment")
    thisalinea.textcontent.append("Tourism is a crucial sector in today’s world, and it plays a central role both at EU and global level.")
    thisalinea.textcontent.append("Considering the economics behind it, 3.9% of EU’s GDP in 2018 can be traced back to tourism,")
    thisalinea.textcontent.append("and this figure rises significantly (10.3%) when also considering its impact on adjacent sectors.73")
    thisalinea.textcontent.append("However, this increase in tourism is also related to negative environmental impact. Potential")
    thisalinea.textcontent.append("adverse effects of tourism development relate to three main areas: strain on natural resources,")
    thisalinea.textcontent.append("pollution, and physical impacts, typically involving the degradation of ecosystems.")
    thisalinea.textcontent.append("Reducing the impact of tourism-related activities and making the whole sector more resilient is")
    thisalinea.textcontent.append("therefore imperative, and EU space data can play a central role in this regard. One of the many")
    thisalinea.textcontent.append("companies aware of the enabling role of satellite data is Murmuration, a Toulouse-based")
    thisalinea.textcontent.append("company focusing on providing services in the domains of tourism, green tech, and renewable")
    thisalinea.textcontent.append("energies. Its STI project in particular aims to create an industrial system to measure and assess")
    thisalinea.textcontent.append("in detail the environmental impact of tourism, and it hinges on observation data provided by")
    thisalinea.textcontent.append("Copernicus through WEkEO, one of the Copernicus DIASs. The key contribution of space data")
    thisalinea.textcontent.append("pertains to the development of the key indicators underpinning this assessment system, indicators")
    thisalinea.textcontent.append("that span five different categories. Air indicators consider the effect on Earth’s atmosphere and")
    thisalinea.textcontent.append("include Aggregate Air Quality, Super Resolution Air Quality, and Air Pollutants. Biodiversity")
    thisalinea.textcontent.append("indicators focus instead on the health of ecosystems and consider vegetation health, vegetation")
    thisalinea.textcontent.append("classification, forest cover, protected areas, and endangered species. Human activities indicators")
    thisalinea.textcontent.append("focus specifically on the effect of tourism on the environment, considering tourism and road")
    thisalinea.textcontent.append("infrastructure as well as tourist flows. Finally, ground indicators include soil sealing, land")
    thisalinea.textcontent.append("occupation and urban heat, while water indicators consider both water quality and aquatic")
    thisalinea.textcontent.append("coverage.")
    thisalinea.textcontent.append("Exhibit 48: The contribution of Copernicus to the Murmuration")
    thisalinea.textcontent.append("environmental KPIs")
    thisalinea.textcontent.append("Thanks to these KPIs enabled by Copernicus (in particular by CAMS, CLMS, and CMEMS), tourism")
    thisalinea.textcontent.append("providers and the")
    thisalinea.textcontent.append("entities regulating")
    thisalinea.textcontent.append("and managing")
    thisalinea.textcontent.append("tourism can benefit")
    thisalinea.textcontent.append("from clear")
    thisalinea.textcontent.append("information on the")
    thisalinea.textcontent.append("subject and thus")
    thisalinea.textcontent.append("integrate ecological")
    thisalinea.textcontent.append("considerations into")
    thisalinea.textcontent.append("the tourism sector.")
    thisalinea.textcontent.append("Without")
    thisalinea.textcontent.append("Copernicus and its")
    thisalinea.textcontent.append("free, full, and open")
    thisalinea.textcontent.append("data policy, it would not be possible for businesses and institutions to track these KPIs and")
    thisalinea.textcontent.append("therefore act towards positive environmental impact.")
    thisalinea.textcontent.append("Examples")
    thisalinea.textcontent.append("of EU space")
    thisalinea.textcontent.append("providers74")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Deforestation is a significant issue to be monitored in order to guarantee correct use ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 136
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Deforestation is a significant issue to be monitored in order to guarantee correct use of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Deforestation is a significant issue to be monitored in order to guarantee correct use of")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Large surfaces involved make in-situ inspections difficult "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 137
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ Large surfaces involved make in-situ inspections difficult "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Large surfaces involved make in-situ inspections difficult")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Tourism is a key economic sector in Europe involving large volumes of moving people ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 138
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "▪ Tourism is a key economic sector in Europe involving large volumes of moving people and therefore characterised by a significant environmental footprint "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Tourism is a key economic sector in Europe involving large volumes of moving people and")
    thisalinea.textcontent.append("therefore characterised by a significant environmental footprint")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "▪ Impact of tourist activities must be monitored to allow companies and institutions to act ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 139
    thisalinea.parentID = 135
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "▪ Impact of tourist activities must be monitored to allow companies and institutions to act with corrective measures when needed "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Impact of tourist activities must be monitored to allow companies and institutions to act")
    thisalinea.textcontent.append("with corrective measures when needed")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "4. CONCLUSIONS: EU SPACE FOR GREEN TRANSFORMATION"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 140
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "In the context of a more sustainable society and ESG scoring, companies are setting green transformation targets to reduce greenhouse emissions and environmental footprint of their operations, as well promote their actions to attract customers and increase their market shares. Business benefit from a myriad of possible applications for EU space data, which translates into not only greener practices, but also cost reduction and increased efficiency. In a path to decarbonisation of energy resources, the Green Deal proposes a transition to renewable sources. Such businesses can be significantly supported by Galileo and Copernicus data, especially in decision-making. First, the evaluation "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In the context of a more sustainable society and ESG scoring, companies are setting green transformation targets to")
    thisalinea.textcontent.append("reduce greenhouse emissions and environmental footprint of their operations, as well promote their actions to")
    thisalinea.textcontent.append("attract customers and increase their market shares. Business benefit from a myriad of possible applications for")
    thisalinea.textcontent.append("EU space data, which translates into not only greener practices, but also cost reduction and increased efficiency.")
    thisalinea.textcontent.append("In a path to decarbonisation of energy resources, the Green Deal proposes a transition to renewable sources. Such")
    thisalinea.textcontent.append("businesses can be significantly supported by Galileo and Copernicus data, especially in decision-making. First, the")
    thisalinea.textcontent.append("evaluation of infrastructure placement can be enhanced by Copernicus data on wind velocity and direction, solar")
    thisalinea.textcontent.append("radiation and more. Moreover, EGNSS offers precise positioning, useful in inspection operations to save time and")
    thisalinea.textcontent.append("costs, as well as reliable timing and synchronisation to tune smart electricity grids.")
    thisalinea.textcontent.append("The Green Deal goal of a greener industry can be supported by the EU space programme. Galileo devices enables")
    thisalinea.textcontent.append("tracking of products and optimisation of operations throughout their life cycle, resulting in reduced emissions.")
    thisalinea.textcontent.append("Moreover, it supports the creation of an electronic product passport, containing relevant information for the")
    thisalinea.textcontent.append("consumer. As regards to raw materials, Copernicus provides essential data on availability, geology, biology and")
    thisalinea.textcontent.append("ecology. In special for mining operations, Copernicus Earth Observation images supports activities from mining")
    thisalinea.textcontent.append("survey to site clean-up, rehabilitation and waste management. In the matter of waste production reduction and")
    thisalinea.textcontent.append("management, EO can monitor water, creating significant insights into plastic production and recycling.")
    thisalinea.textcontent.append("A green urban development relies on solid data. Infrastructure placement, atmospheric pollution monitoring,")
    thisalinea.textcontent.append("urban heat management and green place allotment are some of the many applications of Copernicus imagery in")
    thisalinea.textcontent.append("urban planning that reinforce the goals of the EU Green Deal.")
    thisalinea.textcontent.append("EGNSS has a fundamental role in reducing greenhouse emissions, consonant to the Green Deal’s ambitions. Aiming")
    thisalinea.textcontent.append("a smart and sustainable mobility, Galileo is a key tool for reducing travel time and fuel consumption, leading to")
    thisalinea.textcontent.append("lower costs and lower emissions. It can be used for path optimising in several transportation sectors, as route,")
    thisalinea.textcontent.append("aviation and marine, bringing important profits to companies. Moreover, Copernicus produces information on ocean")
    thisalinea.textcontent.append("streams strength and direction, as well as weather forecasting, improving safety and fuel usage.")
    thisalinea.textcontent.append("Satellite data provided by Copernicus and Galileo play a key role in improving the food system, developing")
    thisalinea.textcontent.append("sustainable and efficient practices. The EU space data enables precision agriculture by mapping the evolution of")
    thisalinea.textcontent.append("crops and precisely navigating to the intervention areas. Copernicus information on soil moisture and crop")
    thisalinea.textcontent.append("development improves irrigation efficiency, fertilisation and pesticide usage, detection and localisation of crop health")
    thisalinea.textcontent.append("issues and more. Moreover, EGNSS data is imperative for automatic steering of agriculture machinery, enabling rout")
    thisalinea.textcontent.append("planning and optimisation, which results in reduced soil damage and fuel consumption.")
    thisalinea.textcontent.append("Ecosystems and biodiversity preservation are vital for the maintenance of life on Earth. In this respect, Copernicus")
    thisalinea.textcontent.append("data is especially appropriate for monitoring the environment, providing crucial climate-biodiversity indicators.")
    thisalinea.textcontent.append("To fight against biodiversity loss, Copernicus data may be also used for early identification of maintenance issues in")
    thisalinea.textcontent.append("oil and gas pipelines, preventing harmful consequences to the environment of a late leak detection. Further")
    thisalinea.textcontent.append("applications for biodiversity and ecosystem monitoring are broad; Copernicus gives users a better understanding of")
    thisalinea.textcontent.append("deforestation, forest fires, soil degradation, floods, coral reef bleaching and more.")
    thisalinea.textcontent.append("The exhibit below contextualises the contribution of EU Space for green transformation from a business model")
    thisalinea.textcontent.append("perspective with a focus on supporting environmental monitoring and impact reduction.")
    thisalinea.textcontent.append("Exhibit 49: Business model canvas")
    thisalinea.textcontent.append("Despite this enormous potential of EU Space data use for Green Transformation, the industry consultation showed")
    thisalinea.textcontent.append("a clear lack of awareness of this applicability.")
    thisalinea.textcontent.append("Exhibit 50: Summary of the results of stakeholder consultations (interviews and survey)")
    thisalinea.textcontent.append("Almost all the consulted companies (direct interviews and surveys) stated that they are currently not leveraging EU")
    thisalinea.textcontent.append("Space Data for pursuing their green transformation objectives. However, many expressed their interest to know")
    thisalinea.textcontent.append("more about it and possibly being engaged by EUSPA in further action. The European Commission and EUSPA are")
    thisalinea.textcontent.append("committed to support the small businesses and corporates in understanding and implementation of the Space data")
    thisalinea.textcontent.append("in their process of green transformation. This report is the first step in this journey.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "ANNEX 1: ABOUT THE EUROPEAN GLOBAL NAVIGATION SYSTEM AND COPERNICUS"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 141
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "The EGNSS component of the EU Space Programme has been the cornerstone of positioning and timing operations since its introduction, supporting activities spanning from transport, to search and rescue, and trading. It consists of two components: The strengths of Galileo lie in its high accuracy, its reliability for timing and positioning, as well as its advanced authentication system. While the EGNSS provides global positioning and timing, it is a particularly important tool for Europe’s long-term strategic non-dependence from services provided by non-European assets like the US GPS, as well as control over its space-based infrastructure. Galileo stands out as the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "A.1 About the European Global Navigation Satellite System (EGNSS)"
    thisalinea.titlefontsize = "15.959999999999923"
    thisalinea.nativeID = 142
    thisalinea.parentID = 141
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The EGNSS component of the EU Space Programme has been the cornerstone of positioning and timing operations since its introduction, supporting activities spanning from transport, to search and rescue, and trading. It consists of two components: The strengths of Galileo lie in its high accuracy, its reliability for timing and positioning, as well as its advanced authentication system. While the EGNSS provides global positioning and timing, it is a particularly important tool for Europe’s long-term strategic non-dependence from services provided by non-European assets like the US GPS, as well as control over its space-based infrastructure. Galileo stands out as the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EGNSS component of the EU Space Programme has been the cornerstone of positioning and timing operations")
    thisalinea.textcontent.append("since its introduction, supporting activities spanning from transport, to search and rescue, and trading. It consists of")
    thisalinea.textcontent.append("two components:")
    thisalinea.textcontent.append("The strengths of Galileo lie in its high accuracy, its reliability for timing and positioning, as well as its advanced")
    thisalinea.textcontent.append("authentication system. While the EGNSS provides global positioning and timing, it is a particularly important tool")
    thisalinea.textcontent.append("for Europe’s long-term strategic non-dependence from services provided by non-European assets like the US GPS,")
    thisalinea.textcontent.append("as well as control over its space-based infrastructure. Galileo stands out as the only civilian GNSS service in the")
    thisalinea.textcontent.append("world.")
    thisalinea.textcontent.append("Galileo currently offers three services: the Open Service (OS), a free mass-market service for positioning, navigation")
    thisalinea.textcontent.append("and timing, the Search and Rescue (SAR) service, Europe’s contribution to the international distress beacon locating")
    thisalinea.textcontent.append("organisation COSPAS-SARSAT both operational since 2016, and the Public Regulated Service (PRS), a fully")
    thisalinea.textcontent.append("encrypted and robust service for authorised security and governmental users in EU Member States. In addition,")
    thisalinea.textcontent.append("Galileo is set to offer other major service lines including the Galileo Open Service Navigation Message")
    thisalinea.textcontent.append("Authentication (OSNMA) – free and open with authentication capabilities, the High Accuracy Service (HAS) –")
    thisalinea.textcontent.append("designed to deliver further signal, encryption and value-added services to commercial users75.")
    thisalinea.textcontent.append("Exhibit 51: Galileo services")
    thisalinea.textcontent.append("EGNOS is a satellite-based augmentation system, originally designed to enhance the Global Positioning System")
    thisalinea.textcontent.append("(GPS) signal for safety-of-life operations. EGNOS provides across all EU Member States high-accuracy, high-")
    thisalinea.textcontent.append("integrity services for aviation, maritime and land-based users where raw GNSS information is insufficient.")
    thisalinea.textcontent.append("Specifically, as of 2022, EGNOS uses three geostationary satellites and an extensive ground station network to")
    thisalinea.textcontent.append("provide three services: the Open Service (OS) – used for non-safety-critical applications; the Safety of Life Service")
    thisalinea.textcontent.append("(SOLS) – for navigation where human lives are at stake; and the EGNOS Data Access Service (EDAS) – a ground-")
    thisalinea.textcontent.append("based data access point for information collected by EGNOS.")
    thisalinea.textcontent.append("The EGNSS value chain comprises three major segments: space- and ground-based infrastructure in the upstream")
    thisalinea.textcontent.append("(1), system integrators (2), and devices and value-added service providers in the downstream (3). Downstream")
    thisalinea.textcontent.append("actors vary more widely, with the primary differentiators being their area of specialisation and expertise in specific")
    thisalinea.textcontent.append("verticals, such for instance agriculture, energy, transport, etc., all of which have a different operating landscape.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ Galileo, the European Global Navigation Satellite System (GNSS), operational since December 2016 when it ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 143
    thisalinea.parentID = 142
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "▪ Galileo, the European Global Navigation Satellite System (GNSS), operational since December 2016 when it started offering initial services to public authorities, businesses, and citizens. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ Galileo, the European Global Navigation Satellite System (GNSS), operational since December 2016 when it")
    thisalinea.textcontent.append("started offering initial services to public authorities, businesses, and citizens.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "▪ EGNOS, the European Satellite-Based Augmentation System (SBAS), that improves the accuracy of GNSS ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 144
    thisalinea.parentID = 142
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "▪ EGNOS, the European Satellite-Based Augmentation System (SBAS), that improves the accuracy of GNSS signals. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("▪ EGNOS, the European Satellite-Based Augmentation System (SBAS), that improves the accuracy of GNSS")
    thisalinea.textcontent.append("signals.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "A.2 About Copernicus – the EU Earth Observation programme"
    thisalinea.titlefontsize = "15.959999999999923"
    thisalinea.nativeID = 145
    thisalinea.parentID = 141
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Copernicus is the EU’s Earth Observation (EO) programme that provides satellite data and information freely and openly to users. The Sentinel satellites consist of a series of different missions providing global coverage of radar, multispectral, atmospheric chemistry and altimetry data, with additional missions to follow. What started as the Global Monitoring for Environment and Security (GMES) programme in 1999 is now an operational system, seen by many observers as one of the world’s largest EO providers and an enormous utility for the benefit of Europe and the world. The Copernicus programme features six primary service lines including atmosphere, marine environment, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Copernicus is the EU’s Earth Observation (EO) programme that provides satellite data and information freely")
    thisalinea.textcontent.append("and openly to users. The Sentinel satellites consist of a series of different missions providing global coverage of")
    thisalinea.textcontent.append("radar, multispectral, atmospheric chemistry and altimetry data, with additional missions to follow. What started as")
    thisalinea.textcontent.append("the Global Monitoring for Environment and Security (GMES) programme in 1999 is now an operational system, seen")
    thisalinea.textcontent.append("by many observers as one of the world’s largest EO providers and an enormous utility for the benefit of Europe and")
    thisalinea.textcontent.append("the world.")
    thisalinea.textcontent.append("The Copernicus programme features six primary service lines including atmosphere, marine environment, land")
    thisalinea.textcontent.append("monitoring, climate change, security and emergency management, which provide ready-to-use Copernicus-based")
    thisalinea.textcontent.append("analyses and information in a variety of domains, in Europe and abroad. Copernicus services are based on")
    thisalinea.textcontent.append("information from the Sentinels (core Copernicus satellites) as well as tens of third-party satellites known as")
    thisalinea.textcontent.append("Contributing Missions, complemented by in-situ (meaning on-site non-space) data.")
    thisalinea.textcontent.append("Exhibit 52: Copernicus services")
    thisalinea.textcontent.append("The combined capabilities of Copernicus data and information ensure European autonomous access to")
    thisalinea.textcontent.append("environmental knowledge and technologies, supporting the Union’s decision-making in areas such as")
    thisalinea.textcontent.append("environmental policy, climate change, maritime, agriculture, rural development, the preservation of cultural heritage,")
    thisalinea.textcontent.append("civil protection, land and infrastructure monitoring, security as well as the digital economy, among others76.")
    thisalinea.textcontent.append("A key component of the Copernicus system is its data policy that makes most of its satellite data and services")
    thisalinea.textcontent.append("available on a full, open, and free-of-charge basis.")
    thisalinea.textcontent.append("Copernicus data are delivered to their users through a variety of online data access platforms77, such as the ESA-")
    thisalinea.textcontent.append("managed Copernicus Data Space Ecosystem which was inaugurated in January 2023, and the EUMETSAT-managed")
    thisalinea.textcontent.append("EUMETCast platform78. In addition to the above platforms, several Copernicus Services have developed their own")
    thisalinea.textcontent.append("online platform, which provide users with access to information and forecasting products, associated documentation")
    thisalinea.textcontent.append("and support services for their use (1000+ Copernicus products are available to users in total).")
    thisalinea.textcontent.append("To fully tap the potential of Copernicus data, in 2017, the European Commission launched the development of five")
    thisalinea.textcontent.append("cloud-based platforms: the Copernicus Data and Information Access Services (DIAS). Each DIAS provided access")
    thisalinea.textcontent.append("in a virtual environment to all Copernicus data and information, as well as tools and utilities to process them in the")
    thisalinea.textcontent.append("cloud without having to download massive amounts of data. Building on the experience gained with the launch of")
    thisalinea.textcontent.append("the DIASes, a new Copernicus data access service, referred to as the Copernicus Data Space Ecosystem79, has been")
    thisalinea.textcontent.append("launched in January 2023. Such service is part of part of the Copernicus activities delegated by the European")
    thisalinea.textcontent.append("Commission to the European Space Agency and aim at harmonising and streamlining the Copernicus Data Access")
    thisalinea.textcontent.append("framework through a single platform to better access and exploit the Copernicus Data. The new service will be fully")
    thisalinea.textcontent.append("operational in July 2023 after a progressive phase-in period corresponding to the phasing out of the current data")
    thisalinea.textcontent.append("distribution service, leaving time for users to migrate and familiarise themselves with the new service interfaces 80.")
    thisalinea.textcontent.append("In parallel, Eumetsat, ECMWF, Mercator Ocean International and EEA operate the WEkEO cloud-based platform81")
    thisalinea.textcontent.append("which provides access to a variety of Sentinel data and to products and information from the Copernicus")
    thisalinea.textcontent.append("Atmosphere, Ocean and Land Monitoring and Climate Change Services.")
    thisalinea.textcontent.append("This policy is already stimulating the application of digital technology and geospatial intelligence in institutions and")
    thisalinea.textcontent.append("businesses and helps to foster the role of “soft power” of the EU internationally.")
    thisalinea.textcontent.append("Copernicus provides about 8 Petabytes of open and free data per year to citizens, businesses and governments")
    thisalinea.textcontent.append("across Europe. As with EGNSS, a significant part of Copernicus’s value chain lies with added-value service")
    thisalinea.textcontent.append("providers, who adapt, process and redistribute specialised data from the full, open set. Information from Copernicus")
    thisalinea.textcontent.append("is also often augmented with in-situ observation, such as from aerial, water-based or ground-based sensor")
    thisalinea.textcontent.append("information, providing further, higher-fidelity and higher-value information to end-users. Other added-value")
    thisalinea.textcontent.append("services include data analysis, integration with supplemental sources, and validation.")
    thisalinea.textcontent.append("Future evolutions of the Copernicus Programme include six Sentinel Expansion missions especially designed to")
    thisalinea.textcontent.append("address EU policy and gaps in Copernicus user needs and to expand the current capabilities of the Copernicus Space")
    thisalinea.textcontent.append("Component82. The Copernicus Sentinel expansion missions will provide new and enhanced information helping to")
    thisalinea.textcontent.append("tackle challenges such as food security, water management, sea level, polar ice, urbanization and climate change82.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "ANNEX 2: ABOUT THE AUTHORS"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 146
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "The European Commission The European Commission (EC) and more specifically the DirectorateGeneral for Defence Industry and Space (DG DEFIS) has overall responsibility for the implementation of the Union Space Programme and its components (Galileo, EGNOS, Copernicus, GOVSATCOM and SSA). This includes: DG DEFIS further contributes to shaping the EU space policy and fostering a strong, innovative and resilient EU space ecosystem. It supports the emergence of New Space in the EU, including SMEs and new entrants, fosters entrepreneurship and access to finance, and contributes to the growth of the EU space industry. DG DEFIS promotes EU space research fostering a "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The European Commission")
    thisalinea.textcontent.append("The European Commission (EC) and more specifically the DirectorateGeneral for")
    thisalinea.textcontent.append("Defence Industry and Space (DG DEFIS) has overall responsibility for the")
    thisalinea.textcontent.append("implementation of the Union Space Programme and its components (Galileo,")
    thisalinea.textcontent.append("EGNOS, Copernicus, GOVSATCOM and SSA).")
    thisalinea.textcontent.append("This includes:")
    thisalinea.textcontent.append("DG DEFIS further contributes to shaping the EU space policy and fostering a strong, innovative and resilient EU space")
    thisalinea.textcontent.append("ecosystem. It supports the emergence of New Space in the EU, including SMEs and new entrants, fosters entrepreneurship")
    thisalinea.textcontent.append("and access to finance, and contributes to the growth of the EU space industry. DG DEFIS promotes EU space research")
    thisalinea.textcontent.append("fostering a cost-effective, competitive and innovative space industry and research community. It ensures that space")
    thisalinea.textcontent.append("technology, services and applications meet EU policy needs, and the R&I needs of the EU Space Programme. It also ensures")
    thisalinea.textcontent.append("that the EU can access and use space with a high level of autonomy.")
    thisalinea.textcontent.append("The EU space policy addresses some of the most pressing challenges facing the EU today, such as fighting climate change,")
    thisalinea.textcontent.append("supporting EU’s priorities, whilst strongly contributing to the green and digital transitions and to the resilience of the Union.")
    thisalinea.textcontent.append("The European Union Agency for the Space Programme")
    thisalinea.textcontent.append("As a European Union Agency, EUSPA’s mission is to implement the first")
    thisalinea.textcontent.append("integrated EU Space Programme and multiply the benefits generated by space")
    thisalinea.textcontent.append("data and services for citizens, businesses and governments.")
    thisalinea.textcontent.append("As a European Union Agency, EUSPA’s mission is to implement the first")
    thisalinea.textcontent.append("integrated EU Space Programme and multiply the benefits generated by space")
    thisalinea.textcontent.append("data and services for citizens, businesses and governments.")
    thisalinea.textcontent.append("As a body of the EU, the Agency contributes to EU´s priorities: Green Deal and digital transition, the safety and security of")
    thisalinea.textcontent.append("the Union and its citizens, while reinforcing its autonomy and resilience.")
    thisalinea.textcontent.append("EUSPA:")
    thisalinea.textcontent.append("The authors would like to convey special thanks to the contributor of this report SpaceTec Partners.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Overseeing the implementation of all activities related to the programme; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 147
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "• Overseeing the implementation of all activities related to the programme; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Overseeing the implementation of all activities related to the programme;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Defining its priorities and long-term evolution; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 148
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "• Defining its priorities and long-term evolution; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Defining its priorities and long-term evolution;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Managing the funds allocated to the programme; "
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 149
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "• Managing the funds allocated to the programme; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Managing the funds allocated to the programme;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Ensuring a clear division of responsibilities and tasks, in particular between the EU Agency ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 150
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "• Ensuring a clear division of responsibilities and tasks, in particular between the EU Agency for the Space Programme and the European Space Agency; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Ensuring a clear division of responsibilities and tasks, in particular between the EU Agency for the Space")
    thisalinea.textcontent.append("Programme and the European Space Agency;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Ensuring proper reporting on the programme to the Member States of the EU, the ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 151
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "• Ensuring proper reporting on the programme to the Member States of the EU, the European Parliament and the Council of the European Union. The EU Space Programme is fully financed by the European Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Ensuring proper reporting on the programme to the Member States of the EU, the European Parliament and the")
    thisalinea.textcontent.append("Council of the European Union.")
    thisalinea.textcontent.append("The EU Space Programme is fully financed by the European Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Delivers safe, state-of-the-art, European satellite-based services to a growing group of users in Europe ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 152
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "• Delivers safe, state-of-the-art, European satellite-based services to a growing group of users in Europe and around the world. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Delivers safe, state-of-the-art, European satellite-based services to a growing group of users in Europe and")
    thisalinea.textcontent.append("around the world.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Promotes the use of space data and services from Galileo, EGNOS, Copernicus and GOVSATCOM. "
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 153
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "• Promotes the use of space data and services from Galileo, EGNOS, Copernicus and GOVSATCOM. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Promotes the use of space data and services from Galileo, EGNOS, Copernicus and GOVSATCOM.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Ensures the safety and security of the EU Space Programme assets both in space ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 154
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "• Ensures the safety and security of the EU Space Programme assets both in space and on the ground. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Ensures the safety and security of the EU Space Programme assets both in space and on the ground.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Supports innovation along the whole value chain of business development for companies, start-ups, ..."
    thisalinea.titlefontsize = "9.480000000000018"
    thisalinea.nativeID = 155
    thisalinea.parentID = 146
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "• Supports innovation along the whole value chain of business development for companies, start-ups, innovators and academia. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Supports innovation along the whole value chain of business development for companies, start-ups,")
    thisalinea.textcontent.append("innovators and academia.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "LIST OF EXHIBITS"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 156
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "Exhibit 1: Why Pursuing the green transformation - key figures .................................................................................................. 1 Exhibit 2: Participating companies who disclosed their name ....................................................................................................... 3 Exhibit 3: Greenhouse gas emissions global and by sector .......................................................................................................... 4 Exhibit 4: Examples of EU Space contribution to key elements of Green Transformation ................................................... 5 Exhibit 5: European Green Deal investment plan and action areas .............................................................................................. 7 Exhibit 6: European Green Deal action areas ....................................................................................................................................... 8 Exhibit 7: Global green transformation market2 .................................................................................................................................. 9 Exhibit 8: The green transformation investment returns curve .................................................................................................... 10 Exhibit 9: Summary & mapping of key regulation updates under the Green Deal "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Exhibit 1: Why Pursuing the green transformation - key figures .................................................................................................. 1")
    thisalinea.textcontent.append("Exhibit 2: Participating companies who disclosed their name ....................................................................................................... 3")
    thisalinea.textcontent.append("Exhibit 3: Greenhouse gas emissions global and by sector .......................................................................................................... 4")
    thisalinea.textcontent.append("Exhibit 4: Examples of EU Space contribution to key elements of Green Transformation ................................................... 5")
    thisalinea.textcontent.append("Exhibit 5: European Green Deal investment plan and action areas .............................................................................................. 7")
    thisalinea.textcontent.append("Exhibit 6: European Green Deal action areas ....................................................................................................................................... 8")
    thisalinea.textcontent.append("Exhibit 7: Global green transformation market2 .................................................................................................................................. 9")
    thisalinea.textcontent.append("Exhibit 8: The green transformation investment returns curve .................................................................................................... 10")
    thisalinea.textcontent.append("Exhibit 9: Summary & mapping of key regulation updates under the Green Deal")
    thisalinea.textcontent.append("and examples of EU Space applications .......................................................................................................................... 12")
    thisalinea.textcontent.append("Exhibit 10: Estimated impact of the EU Space Programme on selected markets and on the environment .................. 16")
    thisalinea.textcontent.append("Exhibit 11: Summary of the most relevant Copernicus services and products for the Green Deal objectives ............ 17")
    thisalinea.textcontent.append("Exhibit 12: Role of EU Space for green transformation - definitions of environmental monitoring")
    thisalinea.textcontent.append("and footprint reduction ......................................................................................................................................................... 18")
    thisalinea.textcontent.append("Exhibit 13: Use case - EU Space Programme for insurance companies .................................................................................... 19")
    thisalinea.textcontent.append("Exhibit 14: Value chain and position of EO space data in insurance sector ............................................................................. 20")
    thisalinea.textcontent.append("Exhibit 15: ESG main evaluation areas ................................................................................................................................................. 22")
    thisalinea.textcontent.append("Exhibit 16: Example - ESG goals and KPIs adopted by Henkel ................................................................................................... 23")
    thisalinea.textcontent.append("Exhibit 17: Estimated share of EBITDA at risk due to ESG negative performance by industry ........................................ 23")
    thisalinea.textcontent.append("Exhibit 18: Correlations between environmental scoring issued by different organisations ............................................. 25")
    thisalinea.textcontent.append("Exhibit 19: Use case - Copernicus for ESG monitoring ................................................................................................................... 25")
    thisalinea.textcontent.append("Exhibit 20: NOX distribution over Europe ............................................................................................................................................ 26")
    thisalinea.textcontent.append("Exhibit 21: Examples of environmental monitoring KPIs for green transformation and EU Space contribution ....... 26")
    thisalinea.textcontent.append("Exhibit 22: Media headlines from the last three months (as of July 2022) .............................................................................. 28")
    thisalinea.textcontent.append("Exhibit 23: Four-stage evolution of companies through ESG capabilities (BCG) .................................................................. 29")
    thisalinea.textcontent.append("Exhibit 24: Use case - Copernicus for methane emissions monitoring in the energy sector.............................................. 30")
    thisalinea.textcontent.append("Exhibit 25: Data visualisation of GHGSat methane emission measurement for TotalEnergies ........................................ 30")
    thisalinea.textcontent.append("Exhibit 26: Energy generation from solar and wind sources in EU2725 ..................................................................................... 32")
    thisalinea.textcontent.append("Exhibit 27: Use case - EU Space Programme for boosting clean energy adoption ............................................................... 33")
    thisalinea.textcontent.append("Exhibit 28: The Mon Toit Solaire user interface ................................................................................................................................. 34")
    thisalinea.textcontent.append("Exhibit 29: Carbon and energy intensity per tonne of metal produced in EU ......................................................................... 36")
    thisalinea.textcontent.append("Exhibit 30: Use case - EU Space Programme for mining................................................................................................................ 37")
    thisalinea.textcontent.append("Exhibit 31: Share of waste generated in EU40 .................................................................................................................................... 38")
    thisalinea.textcontent.append("Exhibit 32: Use case – EU Space Programme for urban planning and maintenance ............................................................ 39")
    thisalinea.textcontent.append("Exhibit 33: Map of Genova area produced by Detektia ................................................................................................................. 40")
    thisalinea.textcontent.append("Exhibit 34: Share of transport greenhouse gas emissions in Europe47 ...................................................................................... 41")
    thisalinea.textcontent.append("Exhibit 35: Use case - EU Space Programme for autonomous mobility ................................................................................... 41")
    thisalinea.textcontent.append("Exhibit 36: TernowAI AeroSat HD Map product, provided in the OpenDRIVE format ........................................................ 43")
    thisalinea.textcontent.append("Exhibit 37: Use case - EU Space Programme for highway management ................................................................................. 43")
    thisalinea.textcontent.append("Exhibit 38: Use case - EU Space Programme for airport management ..................................................................................... 45")
    thisalinea.textcontent.append("Exhibit 39: GroundEye interface ............................................................................................................................................................. 45")
    thisalinea.textcontent.append("Exhibit 40: Use case – EU Space Programme for safer maritime navigation ........................................................................... 46")
    thisalinea.textcontent.append("Exhibit 41: Use case - EU Space Programme for smart agri-resource management ........................................................... 48")
    thisalinea.textcontent.append("Exhibit 42: WatchITgrow interface for crop management ............................................................................................................ 49")
    thisalinea.textcontent.append("Exhibit 43: Use case - Copernicus for more efficient use of water in the food industry ...................................................... 49")
    thisalinea.textcontent.append("Exhibit 44: Use case - Copernicus for more efficient use of water resources ......................................................................... 51")
    thisalinea.textcontent.append("Exhibit 45: Use case – Copernicus for deforestation and forest management ....................................................................... 54")
    thisalinea.textcontent.append("Exhibit 46: Sample Satelligence deforestation product ................................................................................................................ 55")
    thisalinea.textcontent.append("Exhibit 47: Use case - EU Space Programme for tourism .............................................................................................................. 56")
    thisalinea.textcontent.append("Exhibit 48: The contribution of Copernicus to the Murmuration environmental KPIs .......................................................... 57")
    thisalinea.textcontent.append("Exhibit 49: Business model canvas ........................................................................................................................................................ 59")
    thisalinea.textcontent.append("Exhibit 50: Summary of the results of stakeholder consultations (interviews and survey) ................................................ 59")
    thisalinea.textcontent.append("Exhibit 51: Galileo services ....................................................................................................................................................................... 60")
    thisalinea.textcontent.append("Exhibit 52: Copernicus services ............................................................................................................................................................... 61")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "ABBREVIATIONS AND ACRONYMS"
    thisalinea.titlefontsize = "24.0"
    thisalinea.nativeID = 157
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "Acronym Description AFIR Alternative Fuels Infrastructure Regulation AI Artificial Intelligence AUM Assets Under Management C3S Copernicus Climate Change Service CAMS Copernicus Atmosphere Monitoring Service CBAM Carbon Border Adjustment Mechanism CLMS Copernicus Land Monitoring Service CMEMS Copernicus Marine Environment Monitoring Service CO2 Carbon Dioxide CORSIA Carbon Offset and Reduction Scheme for International Aviation CSR Corporate Social Responsibility CSRD Corporate Sustainability Reporting Directive EBPD Energy Performance of Buildings Directive ECMWF European Centre for Medium-Range Weather Forecasts EDAS EGNOS Data Access Service EEA European Economic Area EGDIP European Green Deal Investment Plan EGNOS European Geostationary Navigation Overlay Service EGNSS European Global Navigation Satellite "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Acronym Description")
    thisalinea.textcontent.append("AFIR Alternative Fuels Infrastructure Regulation")
    thisalinea.textcontent.append("AI Artificial Intelligence")
    thisalinea.textcontent.append("AUM Assets Under Management")
    thisalinea.textcontent.append("C3S Copernicus Climate Change Service")
    thisalinea.textcontent.append("CAMS Copernicus Atmosphere Monitoring Service")
    thisalinea.textcontent.append("CBAM Carbon Border Adjustment Mechanism")
    thisalinea.textcontent.append("CLMS Copernicus Land Monitoring Service")
    thisalinea.textcontent.append("CMEMS Copernicus Marine Environment Monitoring Service")
    thisalinea.textcontent.append("CO2 Carbon Dioxide")
    thisalinea.textcontent.append("CORSIA Carbon Offset and Reduction Scheme for International Aviation")
    thisalinea.textcontent.append("CSR Corporate Social Responsibility")
    thisalinea.textcontent.append("CSRD Corporate Sustainability Reporting Directive")
    thisalinea.textcontent.append("EBPD Energy Performance of Buildings Directive")
    thisalinea.textcontent.append("ECMWF European Centre for Medium-Range Weather Forecasts")
    thisalinea.textcontent.append("EDAS EGNOS Data Access Service")
    thisalinea.textcontent.append("EEA European Economic Area")
    thisalinea.textcontent.append("EGDIP European Green Deal Investment Plan")
    thisalinea.textcontent.append("EGNOS European Geostationary Navigation Overlay Service")
    thisalinea.textcontent.append("EGNSS European Global Navigation Satellite System")
    thisalinea.textcontent.append("EIB European Investment Bank")
    thisalinea.textcontent.append("EMFF European Maritime and Fisheries Fund")
    thisalinea.textcontent.append("EMS Emergency Management Service")
    thisalinea.textcontent.append("EMSA European Maritime Safety Agency")
    thisalinea.textcontent.append("EO Earth Observation")
    thisalinea.textcontent.append("ESA European Space Agency")
    thisalinea.textcontent.append("ESG Environmental, Social, Governance")
    thisalinea.textcontent.append("ESR Effort Sharing Regulation")
    thisalinea.textcontent.append("ETD Energy Taxation Directive")
    thisalinea.textcontent.append("ETS Emissions Trading System")
    thisalinea.textcontent.append("EU European Union")
    thisalinea.textcontent.append("EUSD European Union Space Data")
    thisalinea.textcontent.append("EUSPA European Union Agency for the Space Programme")
    thisalinea.textcontent.append("FAO Food and Agriculture Organization of the United Nations")
    thisalinea.textcontent.append("GBAS Ground-Based Augmentation Systems")
    thisalinea.textcontent.append("GHG Greenhouse Gas")
    thisalinea.textcontent.append("GNSS Global Navigation Satellite System")
    thisalinea.textcontent.append("GPS Global Positioning System")
    thisalinea.textcontent.append("HAS High Accuracy Service")
    thisalinea.textcontent.append("Acronym Description")
    thisalinea.textcontent.append("IARC")
    thisalinea.textcontent.append("ICAO")
    thisalinea.textcontent.append("IMO")
    thisalinea.textcontent.append("IoT")
    thisalinea.textcontent.append("JTF")
    thisalinea.textcontent.append("JTM")
    thisalinea.textcontent.append("JTM")
    thisalinea.textcontent.append("International Agency for Research on Cancer")
    thisalinea.textcontent.append("International Civil Aviation Organization")
    thisalinea.textcontent.append("International Maritime Organization")
    thisalinea.textcontent.append("Internet of Things")
    thisalinea.textcontent.append("Just Transition Fund")
    thisalinea.textcontent.append("Just Transition Mechanism")
    thisalinea.textcontent.append("Just Transition Mechanism")
    thisalinea.textcontent.append("LBS Location-Based Services")
    thisalinea.textcontent.append("LPV Localiser Performance using Vertical guidance")
    thisalinea.textcontent.append("LULUCF Regulation on Land Use, Land Use Change and Forestry")
    thisalinea.textcontent.append("MSCI Morgan Stanley Capital International")
    thisalinea.textcontent.append("NOx Nitrogen Oxides")
    thisalinea.textcontent.append("OMR Outermost Region")
    thisalinea.textcontent.append("OS Open Service")
    thisalinea.textcontent.append("OSNMA Open Service Navigation Message Authentication")
    thisalinea.textcontent.append("PBN Performance-Based Navigation")
    thisalinea.textcontent.append("PM Particulate Matter")
    thisalinea.textcontent.append("PRS Public Regulated Service")
    thisalinea.textcontent.append("REDII Renewable Energy Directive")
    thisalinea.textcontent.append("SAR Search and Rescue")
    thisalinea.textcontent.append("SBAS Satellite-Based Augmentation System")
    thisalinea.textcontent.append("SDG Sustainable Development Goal")
    thisalinea.textcontent.append("SME Small to Medium Enterprise")
    thisalinea.textcontent.append("SOLS Safety of Life Service")
    thisalinea.textcontent.append("SOx Sulphur Oxides")
    thisalinea.textcontent.append("SSA Space Situational Awareness")
    thisalinea.textcontent.append("UAV Uncrewed Aerial Vehicle")
    thisalinea.textcontent.append("UN United Nations")
    thisalinea.textcontent.append("UNFCCC United Nations Framework Convention on Climate Change")
    thisalinea.textcontent.append("VOC Volatile Organic Compound")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "EUSPA Mission Statement"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 158
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The mission of the European Union Agency for the Space Programme (EUSPA) is defined by the EU Space Programme Regulation. EUSPA’s mission is to be the user-oriented operational Agency of the EU Space Programme, contributing to sustainable growth, security and safety of the European Union. Its goal is to: The European Union Agency for the Space Programme: linking space to user needs. www.euspa.europa.eu • Provide long-term, state-of-the-art safe and secure Galileo and EGNOS positioning, navigation and timing services and cost-effective satellite communications services for GOVSATCOM, whilst ensuring service continuity and robustness; • Communicate, promote, and develop the market for data, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The mission of the European Union Agency for the Space Programme (EUSPA) is defined by the EU Space")
    thisalinea.textcontent.append("Programme Regulation. EUSPA’s mission is to be the user-oriented operational Agency of the EU Space Programme,")
    thisalinea.textcontent.append("contributing to sustainable growth, security and safety of the European Union.")
    thisalinea.textcontent.append("Its goal is to:")
    thisalinea.textcontent.append("The European Union Agency for the Space Programme: linking space to user needs.")
    thisalinea.textcontent.append("www.euspa.europa.eu")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Provide long-term, state-of-the-art safe and secure Galileo and EGNOS positioning, navigation and timing ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 159
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "• Provide long-term, state-of-the-art safe and secure Galileo and EGNOS positioning, navigation and timing services and cost-effective satellite communications services for GOVSATCOM, whilst ensuring service continuity and robustness; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Provide long-term, state-of-the-art safe and secure Galileo and EGNOS positioning, navigation and timing")
    thisalinea.textcontent.append("services and cost-effective satellite communications services for GOVSATCOM, whilst ensuring service")
    thisalinea.textcontent.append("continuity and robustness;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Communicate, promote, and develop the market for data, information and services offered by Galileo, ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 160
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "• Communicate, promote, and develop the market for data, information and services offered by Galileo, EGNOS, Copernicus and GOVSATCOM; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Communicate, promote, and develop the market for data, information and services offered by Galileo, EGNOS,")
    thisalinea.textcontent.append("Copernicus and GOVSATCOM;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Provide space-based tools and services to enhance the safety of the Union and its ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 161
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "• Provide space-based tools and services to enhance the safety of the Union and its Member States. In particular, to support PRS usage across the EU; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Provide space-based tools and services to enhance the safety of the Union and its Member States. In particular,")
    thisalinea.textcontent.append("to support PRS usage across the EU;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Implement and monitor the security of the EU Space Programme and to assist in ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 162
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "• Implement and monitor the security of the EU Space Programme and to assist in and be the reference for the use of the secured services, enhancing the security of the Union and its Member States; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Implement and monitor the security of the EU Space Programme and to assist in and be the reference for the")
    thisalinea.textcontent.append("use of the secured services, enhancing the security of the Union and its Member States;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Contribute to fostering a competitive European industry for Galileo, EGNOS, and GOVSATCOM, reinforcing ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 163
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "• Contribute to fostering a competitive European industry for Galileo, EGNOS, and GOVSATCOM, reinforcing the autonomy, including technological autonomy, of the Union and its Member States; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Contribute to fostering a competitive European industry for Galileo, EGNOS, and GOVSATCOM, reinforcing")
    thisalinea.textcontent.append("the autonomy, including technological autonomy, of the Union and its Member States;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Contribute to maximising the socio-economic benefits of the EU Space Programme by fostering the ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 164
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "• Contribute to maximising the socio-economic benefits of the EU Space Programme by fostering the development of a competitive and innovative downstream industry for Galileo, EGNOS, and Copernicus, leveraging also Horizon Europe, other EU funding mechanisms and innovative procurement mechanisms; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Contribute to maximising the socio-economic benefits of the EU Space Programme by fostering the")
    thisalinea.textcontent.append("development of a competitive and innovative downstream industry for Galileo, EGNOS, and Copernicus,")
    thisalinea.textcontent.append("leveraging also Horizon Europe, other EU funding mechanisms and innovative procurement mechanisms;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• Contribute to fostering the development of a wider European space ecosystem, with a particular ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 165
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "• Contribute to fostering the development of a wider European space ecosystem, with a particular focus on innovation, entrepreneurship and start-ups, and reinforcing know-how in Member States and Union regions. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• Contribute to fostering the development of a wider European space ecosystem, with a particular focus on")
    thisalinea.textcontent.append("innovation, entrepreneurship and start-ups, and reinforcing know-how in Member States and Union regions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "• As of July 2023, EUSPA will take the responsibility for the Programme’s Space Surveillance ..."
    thisalinea.titlefontsize = "9.0"
    thisalinea.nativeID = 166
    thisalinea.parentID = 158
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "• As of July 2023, EUSPA will take the responsibility for the Programme’s Space Surveillance Tracking Front Desk operations service. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("• As of July 2023, EUSPA will take the responsibility for the Programme’s Space Surveillance Tracking Front")
    thisalinea.textcontent.append("Desk operations service.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "#EUSpace"
    thisalinea.titlefontsize = "13.715000000000003"
    thisalinea.nativeID = 167
    thisalinea.parentID = 157
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    return alineas
