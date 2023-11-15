import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_STEP() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document STEP
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
    thisalinea.texttitle = "STEP"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The EU is an attractive destination for sustainable investments. The European Single Market has over the last 30 years delivered very significant economic benefits, delivering to the EU a GDP that is up to 9% higher in the long run, than would have been the case without the Single Market.1 The European business model is based on openness and the EU offers a business- friendly environment. The European social model provides high quality and inclusive education and training, well-functioning social protection systems, as well as public health and environmental protection. Together with fair competition and an unparalleled regulatory framework geared "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "EXPLANATORY MEMORANDUM"
    thisalinea.titlefontsize = "12.0"
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
    thisalinea.texttitle = "1. CONTEXT OF THE PROPOSAL"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 2
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The EU is an attractive destination for sustainable investments. The European Single Market has over the last 30 years delivered very significant economic benefits, delivering to the EU a GDP that is up to 9% higher in the long run, than would have been the case without the Single Market.1 The European business model is based on openness and the EU offers a business- friendly environment. The European social model provides high quality and inclusive education and training, well-functioning social protection systems, as well as public health and environmental protection. Together with fair competition and an unparalleled regulatory framework geared "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Reasons for and objectives of the proposal The EU’s long-term commitment to a green and digital transition and the impact on industry in the EU."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The EU is an attractive destination for sustainable investments. The European Single Market has over the last 30 years delivered very significant economic benefits, delivering to the EU a GDP that is up to 9% higher in the long run, than would have been the case without the Single Market.1 The European business model is based on openness and the EU offers a business- friendly environment. The European social model provides high quality and inclusive education and training, well-functioning social protection systems, as well as public health and environmental protection. Together with fair competition and an unparalleled regulatory framework geared "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU is an attractive destination for sustainable investments. The European Single Market")
    thisalinea.textcontent.append("has over the last 30 years delivered very significant economic benefits, delivering to the EU a")
    thisalinea.textcontent.append("GDP that is up to 9% higher in the long run, than would have been the case without the Single")
    thisalinea.textcontent.append("Market.1 The European business model is based on openness and the EU offers a business-")
    thisalinea.textcontent.append("friendly environment. The European social model provides high quality and inclusive")
    thisalinea.textcontent.append("education and training, well-functioning social protection systems, as well as public health")
    thisalinea.textcontent.append("and environmental protection. Together with fair competition and an unparalleled regulatory")
    thisalinea.textcontent.append("framework geared towards the twin digital and green transitions and resilience, this is helping")
    thisalinea.textcontent.append("to provide the necessary predictability for investors.")
    thisalinea.textcontent.append("Strengthening the competitiveness and resilience in strategic sectors and reducing the")
    thisalinea.textcontent.append("dependencies of the European economy through the green and digital transformations has")
    thisalinea.textcontent.append("been the EU compass over the last years. With NextGenerationEU,2 the EU’s flagship")
    thisalinea.textcontent.append("economic recovery programme, the EU has closed the gap with pre-pandemic output levels")
    thisalinea.textcontent.append("already in the summer of 2021. The funds directed to the twin green and digital transition are")
    thisalinea.textcontent.append("making our economy more competitive. The unprecedented efforts by Member States to")
    thisalinea.textcontent.append("implement crucial reforms increase the EU’s resilience.")
    thisalinea.textcontent.append("The EU industry has proven its inbuilt resilience but is being challenged. High inflation,")
    thisalinea.textcontent.append("labour and skills shortages, demographic change, post-COVID supply chains disruptions,")
    thisalinea.textcontent.append("rising interest rates, and spikes in energy costs and input prices are weighing on the")
    thisalinea.textcontent.append("competitiveness of the EU industry. This is paired with strong, but not always fair,")
    thisalinea.textcontent.append("competition on the fragmented global market. The uptake and scaling up of certain critical")
    thisalinea.textcontent.append("and emerging technologies in strategic sectors within the Union will be essential to seize the")
    thisalinea.textcontent.append("opportunities and meet the objectives of the green and digital transitions to reduce strategic")
    thisalinea.textcontent.append("dependencies and to facilitate cross-border investments across the Single Market. Therefore,")
    thisalinea.textcontent.append("immediate action is required to support the development or manufacturing in the Union, or")
    thisalinea.textcontent.append("safeguarding and strengthening their value chains, of critical technologies in the following")
    thisalinea.textcontent.append("fields: deep and digital technologies, clean technologies, and biotechnologies. The Union also")
    thisalinea.textcontent.append("needs to address labour and skills shortages in those strategic sectors.")
    thisalinea.textcontent.append("The EU has already put forward several initiatives to support its industry. The Green Deal")
    thisalinea.textcontent.append("Industrial Plan3 seeks to enhance the competitiveness of Europe's net-zero industry, secure the")
    thisalinea.textcontent.append("volumes needed for critical raw materials and support the fast transition to climate neutrality.")
    thisalinea.textcontent.append("It provides a more supportive environment for the scaling up of the EU's manufacturing")
    thisalinea.textcontent.append("capacity in clean-tech. The plan is based on four pillars: a predictable and simplified")
    thisalinea.textcontent.append("regulatory environment, speeding up access to finance, enhancing skills, and open trade for")
    thisalinea.textcontent.append("resilient supply chains. With the European Innovation Agenda,4 the EU has sought to position")
    thisalinea.textcontent.append("Europe at the forefront of the new wave of deep tech innovation and start-ups. One of its main")
    thisalinea.textcontent.append("objectives is to improve access to finance for European start-ups and scale-ups, for example,")
    thisalinea.textcontent.append("1")
    thisalinea.textcontent.append("by mobilising untapped sources of private capital and simplifying listing rules. Moreover, the")
    thisalinea.textcontent.append("Commission has in March 2023 adopted a new Temporary Crisis and Transition Framework")
    thisalinea.textcontent.append("for State aid.5 Member States have more flexibility to design and implement support measures")
    thisalinea.textcontent.append("in sectors that are key for the transition to climate neutrality. Member States are also currently")
    thisalinea.textcontent.append("amending their national recovery and resilience plans to include REPowerEU Chapters,6")
    thisalinea.textcontent.append("which is a crucial opportunity to provide immediate support to companies and boost their")
    thisalinea.textcontent.append("competitiveness, without creating unnecessary strategic dependencies.")
    thisalinea.textcontent.append("While these solutions provide fast and targeted support, the EU needs a more structural")
    thisalinea.textcontent.append("answer to the investment needs of its industries. As indicated by President von der Leyen in")
    thisalinea.textcontent.append("the State of the Union address of 14 September 2022,7 there is a need to ensure that the future")
    thisalinea.textcontent.append("of industry is made in Europe. Moreover, a common European industrial policy requires")
    thisalinea.textcontent.append("common European funding.8 Hence, the need to set up a Strategic Technologies for")
    thisalinea.textcontent.append("Europe Platform (‘STEP’).")
    thisalinea.textcontent.append("The Platform should help preserve a European edge on critical and emerging technologies")
    thisalinea.textcontent.append("relevant to the green and digital transitions, from computing-related technologies, including")
    thisalinea.textcontent.append("microelectronics, quantum computing, and artificial intelligence; to biotechnology and")
    thisalinea.textcontent.append("biomanufacturing, and net-zero technologies. The European Council recognised the need to")
    thisalinea.textcontent.append("address the issue and recommended to ‘ensure full mobilisation of available funding and")
    thisalinea.textcontent.append("existing financial instruments and deploy them in a more flexible manner, so as to provide")
    thisalinea.textcontent.append("timely and targeted support in strategic sectors without affecting the cohesion policy")
    thisalinea.textcontent.append("objectives’.9 This way, the STEP should also help to mobilise private capital to support the")
    thisalinea.textcontent.append("competitiveness of European businesses in these technologies in the global arena, which in")
    thisalinea.textcontent.append("turn will lead to domestic capacity building.")
    thisalinea.textcontent.append("Placing the STEP at the heart of the EU budget is the most effective solution. The transition to")
    thisalinea.textcontent.append("climate neutrality, resilience and digital technologies are already guiding principles of the")
    thisalinea.textcontent.append("multiannual financial framework: 30% of the EUR 2 trillion 2021-2027 MFF which includes")
    thisalinea.textcontent.append("the NextGenerationEU recovery programmes are being spent on climate actions and more")
    thisalinea.textcontent.append("than 20% of the Recovery and Resilience Facility is dedicated to digital policies. Besides, the")
    thisalinea.textcontent.append("Digital Europe Programme supports bringing digital technology to businesses, citizens and")
    thisalinea.textcontent.append("public administrations. The EU budget is also the ultimate EU tool to underpin the Single")
    thisalinea.textcontent.append("Market and common action with value-added at EU level, securing economies of scale,")
    thisalinea.textcontent.append("effectiveness, solidarity and passing a clear political message that the EU stands together in")
    thisalinea.textcontent.append("the face of challenges.")
    thisalinea.textcontent.append("The creation of the STEP is fully aligned with the ambitions set by Europe’s partners. The")
    thisalinea.textcontent.append("United States’ Inflation Reduction Act will mobilise over USD 360 billion by 2032")
    thisalinea.textcontent.append("(approximately EUR 330 billion). Japan's green transformation plans aim to raise up to JPY")
    thisalinea.textcontent.append("20 trillion (approximately EUR 140 billion).10 India has put forward the Production Linked")
    thisalinea.textcontent.append("Incentive Scheme to enhance competitiveness in sectors like solar photovoltaics and batteries.")
    thisalinea.textcontent.append("The United Kingdom, Canada and many others have also put forward their investment plans")
    thisalinea.textcontent.append("in clean technologies. It is important for all actors to ensure that funding be designed and")
    thisalinea.textcontent.append("implemented in the least distortive manner practicable. Reinforcing transparency and")
    thisalinea.textcontent.append("2")
    thisalinea.textcontent.append("deliberation on industrial subsidies internationally is equally key to safeguard and improve the")
    thisalinea.textcontent.append("existing – but incomplete - level playing field on which the EU’s and global prosperity has")
    thisalinea.textcontent.append("been built.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Overview of the EU budget to the green and digital transition"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 4
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The EU has several funds and programmes on- and off-budget to provide support to deep and digital technologies, clean technologies, and biotechnologies. These instruments include in particular cohesion policy funds, the Recovery and Resilience Facility, the Innovation Fund, InvestEU, the European Defence Fund and Horizon Europe: While the EU has been providing steady financing both to the green and digital transitions, the funds are generally spread across various spending programmes and following different rules. Leveraging on existing instruments and governance frameworks will speed-up the 3 implementation and allow to mobilise higher amounts of financial support. This is the aim of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU has several funds and programmes on- and off-budget to provide support to deep and")
    thisalinea.textcontent.append("digital technologies, clean technologies, and biotechnologies. These instruments include in")
    thisalinea.textcontent.append("particular cohesion policy funds, the Recovery and Resilience Facility, the Innovation Fund,")
    thisalinea.textcontent.append("InvestEU, the European Defence Fund and Horizon Europe:")
    thisalinea.textcontent.append("While the EU has been providing steady financing both to the green and digital transitions,")
    thisalinea.textcontent.append("the funds are generally spread across various spending programmes and following different")
    thisalinea.textcontent.append("rules. Leveraging on existing instruments and governance frameworks will speed-up the")
    thisalinea.textcontent.append("3")
    thisalinea.textcontent.append("implementation and allow to mobilise higher amounts of financial support. This is the aim of")
    thisalinea.textcontent.append("the STEP.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– Cohesion policy supports the green (EUR 110 billion) and digital (EUR 36.6 billion) ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 5
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– Cohesion policy supports the green (EUR 110 billion) and digital (EUR 36.6 billion) transition in Member States and regions, including a total of EUR 85 billion under the European Regional Development Fund (ERDF), the Cohesion Fund (CF) and the Just Transition Fund (JTF) – the EU’s main funds under regional development policy "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Cohesion policy supports the green (EUR 110 billion) and digital (EUR 36.6 billion)")
    thisalinea.textcontent.append("transition in Member States and regions, including a total of EUR 85 billion under")
    thisalinea.textcontent.append("the European Regional Development Fund (ERDF), the Cohesion Fund (CF) and the")
    thisalinea.textcontent.append("Just Transition Fund (JTF) – the EU’s main funds under regional development policy")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– to support the EU energy transition. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 6
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– to support the EU energy transition. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– to support the EU energy transition.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– The Recovery and Resilience Facility and REPowerEU, the EU's plan to make ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 7
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– The Recovery and Resilience Facility and REPowerEU, the EU's plan to make Europe independent from Russian fossil fuels, offer unprecedented opportunities to Member States to finance green and digital investments and reforms. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Recovery and Resilience Facility and REPowerEU, the EU's plan to make")
    thisalinea.textcontent.append("Europe independent from Russian fossil fuels, offer unprecedented opportunities to")
    thisalinea.textcontent.append("Member States to finance green and digital investments and reforms.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– Drawing on the revenues from the EU Emission Trading System (ETS)11 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 8
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– Drawing on the revenues from the EU Emission Trading System (ETS)11 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Drawing on the revenues from the EU Emission Trading System (ETS)11")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– The Modernisation Fund (EUR 60 billion) provides substantial support to 13 ..."
    thisalinea.titlefontsize = "11.999999999999943"
    thisalinea.nativeID = 9
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "– The Modernisation Fund (EUR 60 billion) provides substantial support to 13 beneficiary Member States to accelerate their energy transition. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Modernisation Fund (EUR 60 billion) provides substantial support to 13")
    thisalinea.textcontent.append("beneficiary Member States to accelerate their energy transition.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– The Social Climate Fund (EUR 86 billion) will provide substantial support to ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 10
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "– The Social Climate Fund (EUR 86 billion) will provide substantial support to Member States to help addressing for vulnerable groups the consequences of the green transition. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Social Climate Fund (EUR 86 billion) will provide substantial support to")
    thisalinea.textcontent.append("Member States to help addressing for vulnerable groups the consequences of")
    thisalinea.textcontent.append("the green transition.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– The Innovation Fund (EUR 43 billion) will provide until 2030 funding for ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 11
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "– The Innovation Fund (EUR 43 billion) will provide until 2030 funding for innovative low-carbon technologies, including for the manufacturing of these technologies, for instance to help energy-intensive industries, develop carbon capture and storage, innovative renewable energy generation or energy storage. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Innovation Fund (EUR 43 billion) will provide until 2030 funding for")
    thisalinea.textcontent.append("innovative low-carbon technologies, including for the manufacturing of these")
    thisalinea.textcontent.append("technologies, for instance to help energy-intensive industries, develop carbon")
    thisalinea.textcontent.append("capture and storage, innovative renewable energy generation or energy")
    thisalinea.textcontent.append("storage.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– InvestEU contributes both to the green transition and to digitisation. Overall 30% of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 12
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "– InvestEU contributes both to the green transition and to digitisation. Overall 30% of the InvestEU guarantee (i.e. EUR 7.8 billion) and 60% of the Sustainable Infrastructure Window (EUR 5.9 billion) contribute to climate objectives. Further, it is expected that more than EUR 2 billion could contribute to digital objectives and over EUR 1 billion to biotech and medicines related investments. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– InvestEU contributes both to the green transition and to digitisation. Overall 30% of")
    thisalinea.textcontent.append("the InvestEU guarantee (i.e. EUR 7.8 billion) and 60% of the Sustainable")
    thisalinea.textcontent.append("Infrastructure Window (EUR 5.9 billion) contribute to climate objectives. Further, it")
    thisalinea.textcontent.append("is expected that more than EUR 2 billion could contribute to digital objectives and")
    thisalinea.textcontent.append("over EUR 1 billion to biotech and medicines related investments.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– Horizon Europe, the EU's main research and innovation programme, will dedicate ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 13
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "– Horizon Europe, the EU's main research and innovation programme, will dedicate EUR 20.2 billion to research and development of clean tech; EUR 11.5 billion to biotech and medicines, and EUR 19.3 billion to digital technologies. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Horizon Europe, the EU's main research and innovation programme, will dedicate")
    thisalinea.textcontent.append("EUR 20.2 billion to research and development of clean tech; EUR 11.5 billion to")
    thisalinea.textcontent.append("biotech and medicines, and EUR 19.3 billion to digital technologies.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– The Digital Europe Programme, with a total budget allocation of EUR 7.6 billion, is ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 14
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "– The Digital Europe Programme, with a total budget allocation of EUR 7.6 billion, is providing support to digital technologies. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Digital Europe Programme, with a total budget allocation of EUR 7.6 billion, is")
    thisalinea.textcontent.append("providing support to digital technologies.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "– The European Defence Fund, with a budget of EUR 8 billion, supports research and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 15
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "– The European Defence Fund, with a budget of EUR 8 billion, supports research and development of state-of-the-art and interoperable defence technology and equipment. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The European Defence Fund, with a budget of EUR 8 billion, supports research and")
    thisalinea.textcontent.append("development of state-of-the-art and interoperable defence technology and equipment.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Strategic Technologies for Europe Platform (STEP)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 16
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The STEP will create the necessary conditions for a more effective, efficient and targeted use of existing EU funds while contributing to achieving a level playing field in the Single Market and thereby safeguarding cohesion. It will also help to direct existing funding towards the relevant projects and speed up implementation on a subset of areas which will be identified as crucial for Europe’s leadership. The choice of streamlining and making a better use of existing instruments over creating a brand-new instrument responds to the call by the European Council and has three main advantages. First, timing. With the creation "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The STEP will create the necessary conditions for a more effective, efficient and targeted use")
    thisalinea.textcontent.append("of existing EU funds while contributing to achieving a level playing field in the Single Market")
    thisalinea.textcontent.append("and thereby safeguarding cohesion. It will also help to direct existing funding towards the")
    thisalinea.textcontent.append("relevant projects and speed up implementation on a subset of areas which will be identified as")
    thisalinea.textcontent.append("crucial for Europe’s leadership. The choice of streamlining and making a better use of")
    thisalinea.textcontent.append("existing instruments over creating a brand-new instrument responds to the call by the")
    thisalinea.textcontent.append("European Council and has three main advantages. First, timing. With the creation of a new")
    thisalinea.textcontent.append("instrument taking at least 12 to 18 months, bringing existing instruments together can be done")
    thisalinea.textcontent.append("much more quickly. This would be an indisputable advantage for the beneficiaries of EU")
    thisalinea.textcontent.append("funding as they would have the chance to reap the benefits of EU funding more swiftly.")
    thisalinea.textcontent.append("Second, adapting the existing instruments would increase the possibilities of blending")
    thisalinea.textcontent.append("different sources of financing – under both direct and shared management – thereby leading to")
    thisalinea.textcontent.append("a more efficient use of resources. And finally, building on those existing instruments will also")
    thisalinea.textcontent.append("be simpler for project promoters and programme managers. With the help of the Sovereignty")
    thisalinea.textcontent.append("Portal, all the information about funding opportunities will be centralised. Moreover, it will")
    thisalinea.textcontent.append("limit the administrative burden for project promoters and programme managers and minimise")
    thisalinea.textcontent.append("the risk of overlaps amongst instruments.")
    thisalinea.textcontent.append("The STEP would allow the Union to react quickly in the face of risks for companies critical")
    thisalinea.textcontent.append("for Union’s value chains and to develop a top up for multi country projects, such as Important")
    thisalinea.textcontent.append("Projects of Common European Interest (IPCEIs), to enhance all Member State’s access to")
    thisalinea.textcontent.append("such projects, thereby safeguarding cohesion, and to strengthen the Single Market and counter")
    thisalinea.textcontent.append("unequal availability of State Aid.")
    thisalinea.textcontent.append("On that basis, the objective of the STEP is three-fold:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "1. Providing flexibility in existing instruments "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 17
    thisalinea.parentID = 16
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Providing flexibility in existing instruments "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Providing flexibility in existing instruments")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2. Reinforcing the firepower of existing instruments "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 18
    thisalinea.parentID = 16
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Reinforcing the firepower of existing instruments "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Reinforcing the firepower of existing instruments")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3. Creating synergies among existing instruments "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 19
    thisalinea.parentID = 16
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Creating synergies among existing instruments "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Creating synergies among existing instruments")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Providing flexibility in existing instruments to better support relevant investments"
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 20
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Cohesion funds represent the largest single EU policy financed through the EU budget. To incentivise Member States, the Commission proposes a new priority across all major funds - 4 the European Regional Development Fund (ERDF), Cohesion Fund (CF), and the Just Transition Fund (JTF). The Commission also proposes to open up those funds for large companies in less developed and transition regions, as well as in more developed regions of Member States with a GDP per capita below the EU average, to unleash greater investments in the target areas of the STEP. By providing financial incentives in the form of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Cohesion funds represent the largest single EU policy financed through the EU budget. To")
    thisalinea.textcontent.append("incentivise Member States, the Commission proposes a new priority across all major funds -")
    thisalinea.textcontent.append("4")
    thisalinea.textcontent.append("the European Regional Development Fund (ERDF), Cohesion Fund (CF), and the Just")
    thisalinea.textcontent.append("Transition Fund (JTF). The Commission also proposes to open up those funds for large")
    thisalinea.textcontent.append("companies in less developed and transition regions, as well as in more developed regions of")
    thisalinea.textcontent.append("Member States with a GDP per capita below the EU average, to unleash greater investments")
    thisalinea.textcontent.append("in the target areas of the STEP. By providing financial incentives in the form of higher pre-")
    thisalinea.textcontent.append("financing and EU financing, Member States are encouraged to reprioritise their programmes.")
    thisalinea.textcontent.append("Under those funds, the Commission also proposes a 30% pre-financing in 2024 to incentivise")
    thisalinea.textcontent.append("uptake and an increase the EU financing to 100% for STEP projects.")
    thisalinea.textcontent.append("Moreover, it is proposed to provide additional flexibilities for Member States to be able to")
    thisalinea.textcontent.append("implement the 2014-2020 cohesion policy programmes. The regulatory framework for the")
    thisalinea.textcontent.append("implementation of the 2014-2020 programmes for cohesion policy and the Fund for European")
    thisalinea.textcontent.append("Aid to the Most Deprived (FEAD) has already been adapted to provide Member States and")
    thisalinea.textcontent.append("regions with additional flexibility in terms of implementation rules of cohesion policy and")
    thisalinea.textcontent.append("more liquidity to tackle the effects of the COVID-19 pandemic and the war or aggression")
    thisalinea.textcontent.append("against Ukraine.12 These measures, introduced at the end of the programming period, require")
    thisalinea.textcontent.append("sufficient time and administrative resources to be fully exploited and implemented. Therefore,")
    thisalinea.textcontent.append("it is proposed to extend the deadlines for the submission of the closure documentation under")
    thisalinea.textcontent.append("the 2014-2020 period by 12 months. This should help the Member States that will face")
    thisalinea.textcontent.append("additional workload linked to the revision of the operational programmes for the purpose of")
    thisalinea.textcontent.append("the STEP.")
    thisalinea.textcontent.append("To incentivise Member States to provide resources to InvestEU, the EU flagship programme")
    thisalinea.textcontent.append("to boost investments in critical industries, the Commission proposes to increase the transfers")
    thisalinea.textcontent.append("to InvestEU from the recovery and resilience plans from 4% to 10%. This additional")
    thisalinea.textcontent.append("flexibility to use Member States’ resources under InvestEU will help them to benefit from the")
    thisalinea.textcontent.append("established structures and market expertise of the InvestEU implementing partners, to select")
    thisalinea.textcontent.append("and finance the most promising companies. In this respect, where a Member State decides to")
    thisalinea.textcontent.append("transfer resources to InvestEU national compartments for implementing an existing InvestEU")
    thisalinea.textcontent.append("financial product developed for the EU compartment by the Commission with Union")
    thisalinea.textcontent.append("implementing partners and international implementing partners, such as the European")
    thisalinea.textcontent.append("Investment Bank Group and the European Bank for Reconstruction and Development,")
    thisalinea.textcontent.append("meaning that the Member State has no discretionary input into the design of the financial")
    thisalinea.textcontent.append("product, such a decision does not render the design of the financial product imputable to the")
    thisalinea.textcontent.append("State and hence such a decision does not in itself entail State aid. This is without prejudice to")
    thisalinea.textcontent.append("the obligation of Union financial instruments and budgetary guarantees to be consistent with")
    thisalinea.textcontent.append("State aid rules pursuant to Article 209(2)(c) of the Financial Regulation.")
    thisalinea.textcontent.append("Moreover, to facilitate the RRF related contributions to the Member State compartment of")
    thisalinea.textcontent.append("InvestEU and its uptake, the Commission will adapt the Technical guidance on the application")
    thisalinea.textcontent.append("of ‘do no significant harm’ under Regulation (EU) 2021/241 to ensure that financial products")
    thisalinea.textcontent.append("implemented under the InvestEU Fund can indicate, where applicable the absence of")
    thisalinea.textcontent.append("significant harm to the six environmental objectives set out in Article 17 of Regulation (EU)")
    thisalinea.textcontent.append("5")
    thisalinea.textcontent.append("2020/852 by applying InvestEU rules in combination with the relevant implementing")
    thisalinea.textcontent.append("partner’s policies.")
    thisalinea.textcontent.append("In addition, new STEP priorities will be included in the Innovation Fund, which is a funding")
    thisalinea.textcontent.append("programme for the deployment of net-zero and innovative technologies; the European")
    thisalinea.textcontent.append("Defence Fund, which is a funding programme for the research and development of defence")
    thisalinea.textcontent.append("technology, and the European Innovation Council (EIC) under Horizon Europe, which is")
    thisalinea.textcontent.append("Europe’s flagship innovation programme to identify, develop and scale up breakthrough")
    thisalinea.textcontent.append("technologies. Moreover, it will be possible for the EIC to provide equity-only support to non-")
    thisalinea.textcontent.append("bankable small mid-caps.")
    thisalinea.textcontent.append("Equity support for STEP sectors")
    thisalinea.textcontent.append("Companies looking for investments to start up or scale must overcome a series of")
    thisalinea.textcontent.append("interconnected problems from securing patient capital to accessing critical networks and")
    thisalinea.textcontent.append("capabilities if they are to remain in Europe and compete effectively in the current wave of")
    thisalinea.textcontent.append("innovation.")
    thisalinea.textcontent.append("Figure: Venture capital by destination and by stage (2020-Q1 2023).")
    thisalinea.textcontent.append("The EU has two main instruments providing equity support for European companies, namely")
    thisalinea.textcontent.append("the InvestEU Programme and the European Innovation Council. InvestEU is the EU flagship")
    thisalinea.textcontent.append("programme to catalyse private investments in the EU economy. The InvestEU Fund is")
    thisalinea.textcontent.append("delivered through implementing partners, including the European Investment Bank (EIB) and")
    thisalinea.textcontent.append("the European Investment Fund (EIF), which deploy financial products providing debt")
    thisalinea.textcontent.append("(including guarantee), equity and quasi-equity support to companies and projects operating in")
    thisalinea.textcontent.append("sectors relevant for the European sovereignty.")
    thisalinea.textcontent.append("In particular, the EIF deploys two equity products with the total EU guarantee allocation of")
    thisalinea.textcontent.append("EUR 5.2 billion and an indicative portfolio of EUR 8.7 billion, targeting research,")
    thisalinea.textcontent.append("development, commercialisation and scaling of clean technologies or environmental")
    thisalinea.textcontent.append("sustainability solutions and digital and sustainable infrastructure projects. As of mid-2023, the")
    thisalinea.textcontent.append("EIF has approved more than 100 investments in funds expected to mobilise close to EUR 30")
    thisalinea.textcontent.append("billion of investment. The EIB provides equity-type support under high-risk thematic and")
    thisalinea.textcontent.append("venture debt products, focusing inter alia on green transition, strategic digital technologies")
    thisalinea.textcontent.append("and key enabling technologies.")
    thisalinea.textcontent.append("6")
    thisalinea.textcontent.append("The types of support that can be provided through the EIC involve blended finance, grant-")
    thisalinea.textcontent.append("only and equity-only under certain conditions. In accordance with the existing legislation,")
    thisalinea.textcontent.append("equity-only support can be provided to non-bankable SMEs, including start-ups, which have")
    thisalinea.textcontent.append("already received a grant-only support. This initiative expands that definition by allowing to")
    thisalinea.textcontent.append("provide equity-only to non-bankable SMEs and small mid-caps carrying out breakthrough and")
    thisalinea.textcontent.append("disruptive innovation in critical technologies and regardless of whether they previously")
    thisalinea.textcontent.append("received other types of support from the EIC Accelerator. The proposed extension would")
    thisalinea.textcontent.append("provide equity-only support to high risk, high potential companies targeting investments in")
    thisalinea.textcontent.append("the range of EUR 15 to 50 million and catalysing financing rounds with co-investors in the")
    thisalinea.textcontent.append("range of EUR 50 to 250 million.")
    thisalinea.textcontent.append("The EIC was established under Horizon Europe to identify and provide scale up support for")
    thisalinea.textcontent.append("breakthrough technologies and innovations, with a focus on higher risk, earlier stage")
    thisalinea.textcontent.append("companies. A key component of the EIC is the EIC Fund, which is designed to take risks that")
    thisalinea.textcontent.append("the market will not take alone and bridges a critical financing gap for deep tech companies.")
    thisalinea.textcontent.append("The EIC Fund has been fully operational since Autumn 2022 and has already made over 130")
    thisalinea.textcontent.append("investment decisions. However, the EIC Fund cannot accommodate the needs of an increasing")
    thisalinea.textcontent.append("number of companies that require follow-on financing rounds or larger investment amounts.")
    thisalinea.textcontent.append("This is particularly the case for critical and emerging technologies that remain high risk but")
    thisalinea.textcontent.append("also require large amounts of capital to reach the market. The new EIC Fund compartment")
    thisalinea.textcontent.append("would meet the needs for larger investment amounts (above EUR 15 million), as well as")
    thisalinea.textcontent.append("complementing other EU financial instruments and products, including those under Invest")
    thisalinea.textcontent.append("EU.")
    thisalinea.textcontent.append("Demand for investments in deep tech in Europe remains strong, with over 5000 applications")
    thisalinea.textcontent.append("received in the first two years of EIC operation resulting in support for over 400 companies.")
    thisalinea.textcontent.append("Of these, 245 companies have been recommended for the unique blend of non-dilutive grant")
    thisalinea.textcontent.append("alongside investment through the EIC and 131 of these companies have received an")
    thisalinea.textcontent.append("investment recommendation of EUR 5 million or above. It is estimated that approximately")
    thisalinea.textcontent.append("25% of the companies that have been awarded investment of over EUR 5 million from the")
    thisalinea.textcontent.append("EIC will require follow-on funding of on average EUR 25-35 million: representing a pipeline")
    thisalinea.textcontent.append("of 20-30 companies a year13 requiring EUR 0.5 to 1 bn per year.")
    thisalinea.textcontent.append("Based on current experience from the EIC, this EU-backed investment would leverage")
    thisalinea.textcontent.append("additional private investment of up to five times and therefore significantly address the market")
    thisalinea.textcontent.append("gap. Without additional support, many of these companies could relocate outside of Europe to")
    thisalinea.textcontent.append("access larger financing rounds or could be overtaken by third country competitors that are")
    thisalinea.textcontent.append("better financed.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Reinforcing the firepower of existing instruments to speed up relevant investments"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 21
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "In terms of resources, it is proposed that an additional total amount of EUR 10 billion is allocated to support existing and well-proven EU investment schemes aimed at strengthening STEP investments, while preserving the cohesion objectives and contributing to a level playing field in the Single Market by ensuring a geographically balanced distribution of projects financed under the STEP via the respective mandates of the participating programmes, taking into account the demand-driven nature of certain implementing programmes. InvestEU 7 The deployment is well on track with 85% of the initial guarantee already contracted with implementing partners, representing EUR 22.3 billion. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In terms of resources, it is proposed that an additional total amount of EUR 10 billion is")
    thisalinea.textcontent.append("allocated to support existing and well-proven EU investment schemes aimed at strengthening")
    thisalinea.textcontent.append("STEP investments, while preserving the cohesion objectives and contributing to a level")
    thisalinea.textcontent.append("playing field in the Single Market by ensuring a geographically balanced distribution of")
    thisalinea.textcontent.append("projects financed under the STEP via the respective mandates of the participating")
    thisalinea.textcontent.append("programmes, taking into account the demand-driven nature of certain implementing")
    thisalinea.textcontent.append("programmes.")
    thisalinea.textcontent.append("InvestEU")
    thisalinea.textcontent.append("7")
    thisalinea.textcontent.append("The deployment is well on track with 85% of the initial guarantee already contracted with")
    thisalinea.textcontent.append("implementing partners, representing EUR 22.3 billion. The fast absorption of the EU")
    thisalinea.textcontent.append("guarantee reveals the large market interest for the funding opportunities offered by InvestEU.")
    thisalinea.textcontent.append("This calls for reinforcing the EU guarantee by an additional EUR7.5 billion; requiring a")
    thisalinea.textcontent.append("financial top-up of EUR 3 billion with a 40% provisioning rate. This additional guarantee")
    thisalinea.textcontent.append("should be exclusively used for project contributing to STEP priorities and has the potential to")
    thisalinea.textcontent.append("trigger up to EUR 75 billion of investments with an average multiplier of 10.")
    thisalinea.textcontent.append("A new STEP policy window will be set under InvestEU to provide an additional volume of")
    thisalinea.textcontent.append("budgetary guarantee to the implementing partners, which will deploy debt (including")
    thisalinea.textcontent.append("guarantees) and equity financial products for companies, including SMEs, and projects in the")
    thisalinea.textcontent.append("sectors supported by the STEP, including investment in manufacturing and supply chains.")
    thisalinea.textcontent.append("InvestEU will leverage additional investment, particularly from the private sector, by")
    thisalinea.textcontent.append("addressing market failures and sub-optimal investment situations experienced in the sectors")
    thisalinea.textcontent.append("targeted by the STEP. InvestEU is already able to support projects falling within Important")
    thisalinea.textcontent.append("Projects of Common European Interest (IPCEIs) within the meaning of Article 107(3)(b)")
    thisalinea.textcontent.append("TFEU and its reinforcement through the fifth window will therefore enhance its possibility to")
    thisalinea.textcontent.append("do so for critical projects within the scope of application of STEP.")
    thisalinea.textcontent.append("The European Innovation Council")
    thisalinea.textcontent.append("The EIC is the leading mean for providing seed capital to fast growing start-ups. Given its")
    thisalinea.textcontent.append("expertise, the EIC is well suited to reinforce the funding in companies seeking scale-up capital")
    thisalinea.textcontent.append("beyond the first innovation phase. A EUR 0.5 billion budgetary reinforcements combined")
    thisalinea.textcontent.append("with EUR 2.13 billion from redeployment and de-commitments will enable the EIC to")
    thisalinea.textcontent.append("provide unprecedented equity investments for tickets between EUR 15 million and EUR 50")
    thisalinea.textcontent.append("million. With an average multiplier of 5, this can lead to EUR 13 billion of fresh equity")
    thisalinea.textcontent.append("support to non-bankable SMEs and small mid-caps.")
    thisalinea.textcontent.append("Innovation Fund")
    thisalinea.textcontent.append("The Innovation Fund, financed from the auctioning of allowances under the EU Emissions")
    thisalinea.textcontent.append("Trading System, is one of the world’s largest funding programmes for the deployment of net-")
    thisalinea.textcontent.append("zero and innovative technologies. It aims to bring to market industrial solutions to")
    thisalinea.textcontent.append("decarbonise Europe and focuses on highly innovative technologies and processes. The goal to")
    thisalinea.textcontent.append("create the right financial incentives for companies to invest in clean tech and to empower")
    thisalinea.textcontent.append("them to become global clean tech leaders is fully aligned with the STEP objectives. To")
    thisalinea.textcontent.append("respond to the growing needs for innovation to maintain the EU’s competitiveness on global")
    thisalinea.textcontent.append("markets, the size of the Innovation Fund should be increased by EUR 5 billion. In line with")
    thisalinea.textcontent.append("the objectives of ensuring cohesion and promoting the Single Market, and in order to support")
    thisalinea.textcontent.append("the green transition and the development of clean technologies throughout the Union, the")
    thisalinea.textcontent.append("additional financial envelope shall be made available through calls for proposals open to")
    thisalinea.textcontent.append("entities from Member States whose average GDP per capita is below the EU average of the")
    thisalinea.textcontent.append("EU-27 measured in purchasing power standards (PPS) and calculated on the basis of Union")
    thisalinea.textcontent.append("figures for the period 2015-2017. Taking into account experience to date, this should result in")
    thisalinea.textcontent.append("overall investments of around EUR 20 billion.")
    thisalinea.textcontent.append("European Defence Fund")
    thisalinea.textcontent.append("The European Defence Fund is critical to enhance the competitiveness, innovation, efficiency")
    thisalinea.textcontent.append("and technological autonomy of the Union’s defence industry, thereby contributing to the")
    thisalinea.textcontent.append("Union’s open strategic autonomy. It also supports the cross-border cooperation between")
    thisalinea.textcontent.append("Member States as well as cooperation between enterprises, research centres, national")
    thisalinea.textcontent.append("administrations, international organisations and universities throughout the Union, both in the")
    thisalinea.textcontent.append("8")
    thisalinea.textcontent.append("research and in the development phases of defence products and technologies. To respond to")
    thisalinea.textcontent.append("growing needs, the European Defence Fund should be increased by EUR 1.5 billion. Taking")
    thisalinea.textcontent.append("into account the limited experience to date, this could result in overall investments of around")
    thisalinea.textcontent.append("EUR 2 billion.")
    thisalinea.textcontent.append("Taken together, the reinforcements of the foregoing four programmes and instruments")
    thisalinea.textcontent.append("(InvestEU, European Innovation Council, Innovation Fund, European Defence Fund) can be")
    thisalinea.textcontent.append("expected to lead to additional investments in the critical technologies covered by STEP of")
    thisalinea.textcontent.append("around EUR 110 billion.")
    thisalinea.textcontent.append("By providing financial incentives in cohesion policy funds in the form of higher pre-financing")
    thisalinea.textcontent.append("and co-financing, Member States are encouraged to reprioritise their programmes. Every 5%")
    thisalinea.textcontent.append("of reprogramming towards STEP priorities leads to EUR 18.9 billion of resources made")
    thisalinea.textcontent.append("available, in addition to EUR 6 billion to be paid out from the Just Transition Fund. The")
    thisalinea.textcontent.append("increase of the ceiling under the RRF to use resources for InvestEU products via its national")
    thisalinea.textcontent.append("compartments represents an additional flexibility for Member States of EUR 30 billion")
    thisalinea.textcontent.append("potentially available for such sovereignty investments.")
    thisalinea.textcontent.append("Altogether, the total estimated amount of new investments through STEP could reach up to")
    thisalinea.textcontent.append("EUR 160 billion.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Creating synergies among instruments to better support relevant investments"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 22
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "To access those funds, companies and project promoters will be able to consult a new publicly available website (the ‘Sovereignty Portal’). This Portal will provide information about relevant funding opportunities with the ongoing and upcoming calls under the EU programmes contributing to the STEP objectives as well as guidance and contacts to the existing advisory hubs. Moreover, a ‘Sovereignty Seal’ will be awarded to projects contributing to the STEP objectives, provided that the project has been assessed and complies with the minimum quality requirements, in particular eligibility, exclusion and award criteria, provided by a call for proposals under Horizon Europe, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("To access those funds, companies and project promoters will be able to consult a new publicly")
    thisalinea.textcontent.append("available website (the ‘Sovereignty Portal’). This Portal will provide information about")
    thisalinea.textcontent.append("relevant funding opportunities with the ongoing and upcoming calls under the EU")
    thisalinea.textcontent.append("programmes contributing to the STEP objectives as well as guidance and contacts to the")
    thisalinea.textcontent.append("existing advisory hubs.")
    thisalinea.textcontent.append("Moreover, a ‘Sovereignty Seal’ will be awarded to projects contributing to the STEP")
    thisalinea.textcontent.append("objectives, provided that the project has been assessed and complies with the minimum")
    thisalinea.textcontent.append("quality requirements, in particular eligibility, exclusion and award criteria, provided by a call")
    thisalinea.textcontent.append("for proposals under Horizon Europe, the Digital Europe programme, the EU4Health")
    thisalinea.textcontent.append("programme, the European Defence Fund or the Innovation Fund, and regardless of whether")
    thisalinea.textcontent.append("the project has received funds under those instruments. These minimum quality requirements")
    thisalinea.textcontent.append("will be established with a view to identify high quality projects. This Seal offers a unique")
    thisalinea.textcontent.append("opportunity to build on the applicable high-quality evaluation processes under those")
    thisalinea.textcontent.append("instruments. This Seal will be used as a quality label and will help projects attract public and")
    thisalinea.textcontent.append("private investments by certifying its contribution to the objectives of the STEP and therefore")
    thisalinea.textcontent.append("guiding market participants in their investment decisions. Moreover, the Seal will promote")
    thisalinea.textcontent.append("better access to EU funding and financing, notably by facilitating cumulative or combined")
    thisalinea.textcontent.append("funding from several Union instruments. This would, for instance, allow Member States to")
    thisalinea.textcontent.append("grant support from ERDF and ESF+ to projects having been awarded a Sovereignty Seal")
    thisalinea.textcontent.append("directly, subject to compliance with applicable State aid rules.")
    thisalinea.textcontent.append("The Commission is also working to ensure synergies between the rules of the Innovation")
    thisalinea.textcontent.append("Fund and the State aid rules to ensure a more streamlined process. The Commission will")
    thisalinea.textcontent.append("further align criteria and streamline processes to ensure that the decision on State aid is taken")
    thisalinea.textcontent.append("at the same time as the funding decision from the Innovation Fund, provided a complete")
    thisalinea.textcontent.append("notification by the Member State occurs in due time. Such synergies are also being assessed")
    thisalinea.textcontent.append("for other selected EU instruments, including the EIC Fund.")
    thisalinea.textcontent.append("The Commission will also consult Member States on a proposal to enable higher rates of aid")
    thisalinea.textcontent.append("via a bonus for projects within the scope of STEP in assisted regions to spur further economic")
    thisalinea.textcontent.append("development, while preserving cohesion objectives.")
    thisalinea.textcontent.append("9")
    thisalinea.textcontent.append("Authorities in charge of programmes falling under STEP should also be encouraged to")
    thisalinea.textcontent.append("consider support for strategic projects identified in accordance with the Net Zero Industry and")
    thisalinea.textcontent.append("the Critical Raw Materials Acts that fall under the scope of Article 2 of the Regulation,")
    thisalinea.textcontent.append("subject to compliance with applicable State aid rules.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "STEP– focus on investments"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 23
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "To be successful, the STEP should focus on few but well-targeted investment areas. The Platform should ensure and preserve a European edge on critical and emerging technologies and related manufacturing in the following fields:14 deep and digital technologies, clean technologies, and biotechnologies. The scope of the STEP would therefore focus on leading edge technologies to advance the green and digital transitions, supporting both the manufacturing side and the value chains. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("To be successful, the STEP should focus on few but well-targeted investment areas. The")
    thisalinea.textcontent.append("Platform should ensure and preserve a European edge on critical and emerging technologies")
    thisalinea.textcontent.append("and related manufacturing in the following fields:14 deep and digital technologies, clean")
    thisalinea.textcontent.append("technologies, and biotechnologies. The scope of the STEP would therefore focus on leading")
    thisalinea.textcontent.append("edge technologies to advance the green and digital transitions, supporting both the")
    thisalinea.textcontent.append("manufacturing side and the value chains.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Deep and digital technologies"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 24
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "Innovation, and in particular its new wave of deep-tech innovation, is the European reply to bring down greenhouse gas emissions, to make our economies more digital and to guarantee Europe’s food, energy and secure raw materials supply and security. Deep tech innovation, which is rooted in cutting edge science, technology and engineering, often combining advances in the physical, biological and digital spheres and with the potential to deliver transformative solutions in the face of global challenges. Those innovations have the potential to drive innovation across the economy and society, thus transforming the EU’s business landscape. The European Innovation Agenda already "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Innovation, and in particular its new wave of deep-tech innovation, is the European reply to")
    thisalinea.textcontent.append("bring down greenhouse gas emissions, to make our economies more digital and to guarantee")
    thisalinea.textcontent.append("Europe’s food, energy and secure raw materials supply and security. Deep tech innovation,")
    thisalinea.textcontent.append("which is rooted in cutting edge science, technology and engineering, often combining")
    thisalinea.textcontent.append("advances in the physical, biological and digital spheres and with the potential to deliver")
    thisalinea.textcontent.append("transformative solutions in the face of global challenges. Those innovations have the potential")
    thisalinea.textcontent.append("to drive innovation across the economy and society, thus transforming the EU’s business")
    thisalinea.textcontent.append("landscape.")
    thisalinea.textcontent.append("The European Innovation Agenda already aims to position Europe at the forefront of the new")
    thisalinea.textcontent.append("wave of deep tech innovation and start-ups. One of its main objectives is to improve access to")
    thisalinea.textcontent.append("finance for European start-ups and scale-ups, for example, by mobilising untapped sources of")
    thisalinea.textcontent.append("private capital and simplifying listing rules.")
    thisalinea.textcontent.append("The STEP would add another dimension to the EU commitment to the delivery on this")
    thisalinea.textcontent.append("agenda. The EU will steer further funding, and also define a clear investment direction. This")
    thisalinea.textcontent.append("will further support deep tech investments in Europe, to the benefit of the EU economies and")
    thisalinea.textcontent.append("the society as a whole.")
    thisalinea.textcontent.append("Digital technologies have a profound impact on the competitiveness of the EU economy as a")
    thisalinea.textcontent.append("whole, boosting efficiency and innovation. Their adoption and integration across the economy")
    thisalinea.textcontent.append("will be vital to the overall competitiveness and productivity.15 To maintain its industrial")
    thisalinea.textcontent.append("leadership, the EU needs to attain a leading role in key digital technology.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Clean technologies"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 25
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "EU’s competitiveness in the clean energy sector entails the capacity to produce and use affordable, reliable and accessible clean energy and compete in the global clean energy markets, with the overall aim of supporting the transition to climate neutrality and bringing benefits to the EU economy and people. The EU is currently facing technological and non- technological challenges, such as high energy prices, critical raw materials supply chain disruptions and skills shortages. Strengthening the competitiveness of the EU clean energy sector will contribute to increasing the EU's technology leadership, and shape a more resilient, 10 independent, secure and affordable energy "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("EU’s competitiveness in the clean energy sector entails the capacity to produce and use")
    thisalinea.textcontent.append("affordable, reliable and accessible clean energy and compete in the global clean energy")
    thisalinea.textcontent.append("markets, with the overall aim of supporting the transition to climate neutrality and bringing")
    thisalinea.textcontent.append("benefits to the EU economy and people. The EU is currently facing technological and non-")
    thisalinea.textcontent.append("technological challenges, such as high energy prices, critical raw materials supply chain")
    thisalinea.textcontent.append("disruptions and skills shortages. Strengthening the competitiveness of the EU clean energy")
    thisalinea.textcontent.append("sector will contribute to increasing the EU's technology leadership, and shape a more resilient,")
    thisalinea.textcontent.append("10")
    thisalinea.textcontent.append("independent, secure and affordable energy system needed to meet these challenges. In that")
    thisalinea.textcontent.append("context, the Commission’s communication on the Green Deal Industrial Plan presented a")
    thisalinea.textcontent.append("comprehensive plan for enhancing the competitiveness of Europe’s net-zero industry and")
    thisalinea.textcontent.append("supporting the fast transition to climate neutrality; and the Net-Zero Industry Act16 establishes")
    thisalinea.textcontent.append("a framework of measures for strengthening Europe’s net-zero energy technologies")
    thisalinea.textcontent.append("manufacturing ecosystem.")
    thisalinea.textcontent.append("Since 2020, the European Commission has published yearly progress reports on")
    thisalinea.textcontent.append("competitiveness of clean energy technologies that present the current and projected state of")
    thisalinea.textcontent.append("play for different clean and low-carbon energy technologies and solutions. According to the")
    thisalinea.textcontent.append("2022 Competitiveness Progress Report,17 which the Commission publishes in the context of")
    thisalinea.textcontent.append("the Governance of the Energy Union and Climate Action framework, ‘The rapid development")
    thisalinea.textcontent.append("and deployment of home-grown clean energy technologies in the EU is key to a cost-")
    thisalinea.textcontent.append("effective, climate friendly and socially fair response to the current energy crisis’. The report")
    thisalinea.textcontent.append("also confirms that more public and private investments in clean energy research and")
    thisalinea.textcontent.append("innovation, scale-up and affordable deployment are of pivotal importance. The EU’s")
    thisalinea.textcontent.append("regulatory and financial frameworks have a crucial role to play here. Together with the")
    thisalinea.textcontent.append("implementation of the New European Innovation Agenda, EU funding programmes, enhanced")
    thisalinea.textcontent.append("cooperation between Member States, and a continuous monitoring of national R&I activities,")
    thisalinea.textcontent.append("are crucial to design an impactful EU R&I ecosystem, and to bridge the gap between research")
    thisalinea.textcontent.append("and innovation and market uptake, thus reinforcing EU competitiveness.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Biotechnologies"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 26
    thisalinea.parentID = 3
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "Biotechnology and biomanufacturing are key for the modernisation of the European industry. They are used in a variety of industrial sectors such as healthcare and pharmaceuticals, agriculture, materials, and bioeconomy. Reaping the full benefits of biotechnology can help the EU economy grow and provides new jobs, while also supporting sustainable development, public health, and environmental protection. The coronavirus pandemic has proven the importance of biotech with vaccine manufacturers having played a key role in reversing the course of the pandemic. And while Europe continues to be a leader in life science innovation, its biotech industry remains approximately a quarter of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Biotechnology and biomanufacturing are key for the modernisation of the European industry.")
    thisalinea.textcontent.append("They are used in a variety of industrial sectors such as healthcare and pharmaceuticals,")
    thisalinea.textcontent.append("agriculture, materials, and bioeconomy. Reaping the full benefits of biotechnology can help")
    thisalinea.textcontent.append("the EU economy grow and provides new jobs, while also supporting sustainable development,")
    thisalinea.textcontent.append("public health, and environmental protection.")
    thisalinea.textcontent.append("The coronavirus pandemic has proven the importance of biotech with vaccine manufacturers")
    thisalinea.textcontent.append("having played a key role in reversing the course of the pandemic. And while Europe continues")
    thisalinea.textcontent.append("to be a leader in life science innovation, its biotech industry remains approximately a quarter")
    thisalinea.textcontent.append("of the size of the US in terms of both the number of companies and the value of venture")
    thisalinea.textcontent.append("financing.18 In addition, financing – both at the earliest stages and later on – is deemed more")
    thisalinea.textcontent.append("limited in Europe than in the US. This constrains companies’ ability to invest in larger")
    thisalinea.textcontent.append("diversified pipelines and leaves them reliant on their initial investors.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Consistency with existing policy provisions in the policy area"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 27
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The Green Deal Industrial Plan is the EU’s roadmap to secure the long-term competitiveness of Europe's industry and support the fast transition to climate neutrality. The Net-Zero Industry Act represents its regulatory arm. The act seeks to ensure a simpler and fast-track permitting, promoting European strategic projects, and developing standards to support the scale-up of technologies across the Single Market. It is complemented by the Critical Raw Materials Act,19 to ensure sufficient access to those materials, like rare earths, that are vital for 11 manufacturing technologies that are key for the twin transition. Another key instrument to support the competitiveness "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The Green Deal Industrial Plan is the EU’s roadmap to secure the long-term competitiveness")
    thisalinea.textcontent.append("of Europe's industry and support the fast transition to climate neutrality. The Net-Zero")
    thisalinea.textcontent.append("Industry Act represents its regulatory arm. The act seeks to ensure a simpler and fast-track")
    thisalinea.textcontent.append("permitting, promoting European strategic projects, and developing standards to support the")
    thisalinea.textcontent.append("scale-up of technologies across the Single Market. It is complemented by the Critical Raw")
    thisalinea.textcontent.append("Materials Act,19 to ensure sufficient access to those materials, like rare earths, that are vital for")
    thisalinea.textcontent.append("11")
    thisalinea.textcontent.append("manufacturing technologies that are key for the twin transition. Another key instrument to")
    thisalinea.textcontent.append("support the competitiveness of the European industry is the European Chips Act.20 It seeks to")
    thisalinea.textcontent.append("bolster Europe’s resilience in semiconductor technologies and applications, and boost the")
    thisalinea.textcontent.append("EU's share of the global microchips market.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "• Consistency with other Union policies"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 28
    thisalinea.parentID = 27
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The proposal falls within the EU’s overall efforts to secure the green and digital transformation of its economy. It contributes to the objectives of parts of the Fit for 55 package21 that focus on decarbonising EU industry. The proposal will also contribute to the EU’s resilience and open strategic autonomy by strengthening the EU’s capacity as regards critical technologies, including key energy-related technologies, which is crucial for supporting the development of other sectors of the economy. It relies on existing EU policies that seek to achieve the same objective – from cohesion, through recovery investments to research and innovation financing "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal falls within the EU’s overall efforts to secure the green and digital")
    thisalinea.textcontent.append("transformation of its economy. It contributes to the objectives of parts of the Fit for 55")
    thisalinea.textcontent.append("package21 that focus on decarbonising EU industry.")
    thisalinea.textcontent.append("The proposal will also contribute to the EU’s resilience and open strategic autonomy by")
    thisalinea.textcontent.append("strengthening the EU’s capacity as regards critical technologies, including key energy-related")
    thisalinea.textcontent.append("technologies, which is crucial for supporting the development of other sectors of the")
    thisalinea.textcontent.append("economy.")
    thisalinea.textcontent.append("It relies on existing EU policies that seek to achieve the same objective – from cohesion,")
    thisalinea.textcontent.append("through recovery investments to research and innovation financing – which seek to support")
    thisalinea.textcontent.append("European economy and channel EU funds towards the green and digital transformation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. LEGAL BASIS, SUBSIDIARITY AND PROPORTIONALITY"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 29
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "This Regulation pursues the general objective of setting up a legal framework which supports the channelling of EU funds towards STEP projects. The objectives of the STEP will be achieved through the following programmes: 12 Therefore, considering the above, Article 164, Article 173, Article 175(3), Article 176, Article 177, Article 178, Article 182(1) and Article 192(1) are the relevant legal bases for the implementation of this Regulation. – European Regional Development Fund (ERDF) and Cohesion Fund (CF), established under Regulation (EU) 2021/1058;22 the Just Transition Fund (JTF), established under Regulation (EU) 2021/1056;23 the European Social Fund Plus (ESF+), established under "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Legal basis"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 30
    thisalinea.parentID = 29
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "This Regulation pursues the general objective of setting up a legal framework which supports the channelling of EU funds towards STEP projects. The objectives of the STEP will be achieved through the following programmes: 12 Therefore, considering the above, Article 164, Article 173, Article 175(3), Article 176, Article 177, Article 178, Article 182(1) and Article 192(1) are the relevant legal bases for the implementation of this Regulation. – European Regional Development Fund (ERDF) and Cohesion Fund (CF), established under Regulation (EU) 2021/1058;22 the Just Transition Fund (JTF), established under Regulation (EU) 2021/1056;23 the European Social Fund Plus (ESF+), established under "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Regulation pursues the general objective of setting up a legal framework which supports")
    thisalinea.textcontent.append("the channelling of EU funds towards STEP projects. The objectives of the STEP will be")
    thisalinea.textcontent.append("achieved through the following programmes:")
    thisalinea.textcontent.append("12")
    thisalinea.textcontent.append("Therefore, considering the above, Article 164, Article 173, Article 175(3), Article 176, Article")
    thisalinea.textcontent.append("177, Article 178, Article 182(1) and Article 192(1) are the relevant legal bases for the")
    thisalinea.textcontent.append("implementation of this Regulation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– European Regional Development Fund (ERDF) and Cohesion Fund (CF), established ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 31
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– European Regional Development Fund (ERDF) and Cohesion Fund (CF), established under Regulation (EU) 2021/1058;22 the Just Transition Fund (JTF), established under Regulation (EU) 2021/1056;23 the European Social Fund Plus (ESF+), established under Regulation 2021/1057;24 the Common Provisions Regulation (EU) 2021/1060.25 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– European Regional Development Fund (ERDF) and Cohesion Fund (CF), established")
    thisalinea.textcontent.append("under Regulation (EU) 2021/1058;22 the Just Transition Fund (JTF), established")
    thisalinea.textcontent.append("under Regulation (EU) 2021/1056;23 the European Social Fund Plus (ESF+),")
    thisalinea.textcontent.append("established under Regulation 2021/1057;24 the Common Provisions Regulation (EU)")
    thisalinea.textcontent.append("2021/1060.25")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Recovery and Resilience Facility, established under Regulation (EU) 2021/241.26 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 32
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– Recovery and Resilience Facility, established under Regulation (EU) 2021/241.26 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Recovery and Resilience Facility, established under Regulation (EU) 2021/241.26")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– InvestEU, established under Regulation (EU) 2021/52327 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 33
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– InvestEU, established under Regulation (EU) 2021/52327 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– InvestEU, established under Regulation (EU) 2021/52327")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Digital Europe, established under Regulation 2021/694;28 Horizon Europe, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 34
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– Digital Europe, established under Regulation 2021/694;28 Horizon Europe, established under Regulation 2021/695;29 European Defence Fund, established under Regulation (EU) 2021/69730 and the Innovation Fund, established under Directive 2003/87/EC.31 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Digital Europe, established under Regulation 2021/694;28 Horizon Europe,")
    thisalinea.textcontent.append("established under Regulation 2021/695;29 European Defence Fund, established under")
    thisalinea.textcontent.append("Regulation (EU) 2021/69730 and the Innovation Fund, established under Directive")
    thisalinea.textcontent.append("2003/87/EC.31")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– The STEP will also be implemented within the EU4Health programme, established ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 35
    thisalinea.parentID = 30
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "– The STEP will also be implemented within the EU4Health programme, established under Regulation (EU) 2021/52232, concerning the objective to reinforce the development of biotechnologies in the Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The STEP will also be implemented within the EU4Health programme, established")
    thisalinea.textcontent.append("under Regulation (EU) 2021/52232, concerning the objective to reinforce the")
    thisalinea.textcontent.append("development of biotechnologies in the Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Subsidiarity (for non-exclusive competence)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 36
    thisalinea.parentID = 29
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The objectives of the proposal cannot be achieved by Member States acting alone, as the problems are of a cross-border nature, and not limited to single Member States or to a subset of Member States. The proposed actions focus on areas where there is a demonstrable value added in acting at Union level due to the scale, speed and scope of the efforts needed within the Single Market. Given the challenges for accelerating the deployment of net-zero and digital technologies, intervention at the level of the Union helps coordinate responses to address the Union’s needs for additional manufacturing capacities and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The objectives of the proposal cannot be achieved by Member States acting alone, as the")
    thisalinea.textcontent.append("problems are of a cross-border nature, and not limited to single Member States or to a subset")
    thisalinea.textcontent.append("of Member States. The proposed actions focus on areas where there is a demonstrable value")
    thisalinea.textcontent.append("added in acting at Union level due to the scale, speed and scope of the efforts needed within")
    thisalinea.textcontent.append("the Single Market.")
    thisalinea.textcontent.append("Given the challenges for accelerating the deployment of net-zero and digital technologies,")
    thisalinea.textcontent.append("intervention at the level of the Union helps coordinate responses to address the Union’s needs")
    thisalinea.textcontent.append("for additional manufacturing capacities and to prevent structural dependencies. Action at")
    thisalinea.textcontent.append("Union level can clearly drive European actors towards a common vision and implementation")
    thisalinea.textcontent.append("strategy. This is key to generate economies of scale and of scope and to generate critical mass")
    thisalinea.textcontent.append("necessary for scaling up green and digital technologies manufacturing in the EU, while")
    thisalinea.textcontent.append("limiting fragmentation of efforts, deepening of regional imbalances and self-harming subsidy")
    thisalinea.textcontent.append("races between the Member States.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Proportionality"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 37
    thisalinea.parentID = 29
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The proposal is designed to help developing a manufacturing ecosystem via measures to facilitate investments. The objective is to support the longer-term competitiveness and innovation capacity of European industry via manufacturing capabilities, de-risking of investments into strategic projects, as well as by start-ups, scale-ups and SMEs. The measures do not go beyond what is necessary to achieve these goals. The STEP does not consist of a new fund structure but relies on existing EU funding instruments and the proposed additional resources are proportionate to the need to accelerate Platform investments in the short term. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal is designed to help developing a manufacturing ecosystem via measures to")
    thisalinea.textcontent.append("facilitate investments. The objective is to support the longer-term competitiveness and")
    thisalinea.textcontent.append("innovation capacity of European industry via manufacturing capabilities, de-risking of")
    thisalinea.textcontent.append("investments into strategic projects, as well as by start-ups, scale-ups and SMEs.")
    thisalinea.textcontent.append("The measures do not go beyond what is necessary to achieve these goals. The STEP does not")
    thisalinea.textcontent.append("consist of a new fund structure but relies on existing EU funding instruments and the")
    thisalinea.textcontent.append("proposed additional resources are proportionate to the need to accelerate Platform investments")
    thisalinea.textcontent.append("in the short term.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Choice of the instrument"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 38
    thisalinea.parentID = 29
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "A Regulation is the appropriate instrument as it provides directly applicable rules for the support. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("A Regulation is the appropriate instrument as it provides directly applicable rules for the")
    thisalinea.textcontent.append("support.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. RESULTS OF EX-POST EVALUATIONS, STAKEHOLDER CONSULTATIONS AND IMPACT ASSESSMENTS"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 39
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "No stakeholder consultation was carried out specifically. This initiative takes into account stakeholder consultations conducted for the preparation of other related initiatives, such as the Critical Raw Materials Act, the Net-Zero Industry Act, the European Innovation Agenda, the Fit for 55 package, the European Chips Act, and the Digital Decade Compass. Moreover, the European Commission has long-standing and regular contacts with industry stakeholders, 13 Member States and trade associations, which enabled the collection of feedback relevant to the proposal. This proposal does not create a new instrument but is implemented through existing tools under the EU budget, which are amended "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Stakeholder consultations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 40
    thisalinea.parentID = 39
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "No stakeholder consultation was carried out specifically. This initiative takes into account stakeholder consultations conducted for the preparation of other related initiatives, such as the Critical Raw Materials Act, the Net-Zero Industry Act, the European Innovation Agenda, the Fit for 55 package, the European Chips Act, and the Digital Decade Compass. Moreover, the European Commission has long-standing and regular contacts with industry stakeholders, 13 Member States and trade associations, which enabled the collection of feedback relevant to the proposal. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("No stakeholder consultation was carried out specifically. This initiative takes into account")
    thisalinea.textcontent.append("stakeholder consultations conducted for the preparation of other related initiatives, such as the")
    thisalinea.textcontent.append("Critical Raw Materials Act, the Net-Zero Industry Act, the European Innovation Agenda, the")
    thisalinea.textcontent.append("Fit for 55 package, the European Chips Act, and the Digital Decade Compass. Moreover, the")
    thisalinea.textcontent.append("European Commission has long-standing and regular contacts with industry stakeholders,")
    thisalinea.textcontent.append("13")
    thisalinea.textcontent.append("Member States and trade associations, which enabled the collection of feedback relevant to")
    thisalinea.textcontent.append("the proposal.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Impact assessment"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 41
    thisalinea.parentID = 39
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "This proposal does not create a new instrument but is implemented through existing tools under the EU budget, which are amended to be able to better mobilise investment resources into critical technologies. Those existing tools, such as cohesion funds, InvestEU and Horizon Europe, have been subject to an impact assessment.33 Moreover, the proposal builds on existing proposals which have been subject to impact analysis, such as the Critical Raw Materials Act, the European Innovation Agenda, the Fitfor55 package, the European Chips Act, and the Digital Decade Compass as well as the investment needs assessment published on 23 March 2023. This "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This proposal does not create a new instrument but is implemented through existing tools")
    thisalinea.textcontent.append("under the EU budget, which are amended to be able to better mobilise investment resources")
    thisalinea.textcontent.append("into critical technologies. Those existing tools, such as cohesion funds, InvestEU and Horizon")
    thisalinea.textcontent.append("Europe, have been subject to an impact assessment.33 Moreover, the proposal builds on")
    thisalinea.textcontent.append("existing proposals which have been subject to impact analysis, such as the Critical Raw")
    thisalinea.textcontent.append("Materials Act, the European Innovation Agenda, the Fitfor55 package, the European Chips")
    thisalinea.textcontent.append("Act, and the Digital Decade Compass as well as the investment needs assessment published")
    thisalinea.textcontent.append("on 23 March 2023. This analysis, carried out in impact assessments or analytical staff")
    thisalinea.textcontent.append("working documents,34 covers the most significant impacts of this proposal. For those reason,")
    thisalinea.textcontent.append("another impact assessment is not needed. The explanatory memorandum also reflects the ex-")
    thisalinea.textcontent.append("ante assessment carried out by the Commission in relation to the equity-only support to be")
    thisalinea.textcontent.append("provided under the EIC for non-bankable SMEs and small mid-caps.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Regulatory fitness and simplification"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 42
    thisalinea.parentID = 39
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The proposal is not linked to regulatory fitness and simplification but contains a number of provisions to simplify the implementation of existing EU instruments. The reporting requirements have been kept to a minimum to limit the administrative burden on Member States’ authorities and companies, while not undermining the sound financial management principles. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal is not linked to regulatory fitness and simplification but contains a number of")
    thisalinea.textcontent.append("provisions to simplify the implementation of existing EU instruments. The reporting")
    thisalinea.textcontent.append("requirements have been kept to a minimum to limit the administrative burden on Member")
    thisalinea.textcontent.append("States’ authorities and companies, while not undermining the sound financial management")
    thisalinea.textcontent.append("principles.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Fundamental rights"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 43
    thisalinea.parentID = 39
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Article 15 of the Charter provides for the freedom to choose an occupation and the right to engage in work. Supporting the competitiveness of the European industry will ensure economic growth and make sure it continues to offer job opportunities to citizens and residents of the Union. Article 16 of the Charter of Fundamental Rights of the European Union (‘the Charter’) provides for the freedom to conduct a business. The measures under this proposal support the creation of innovation capacity and the deployment of clean energy technologies, which can reinforce the freedom to conduct a business in accordance with Union "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 15 of the Charter provides for the freedom to choose an occupation and the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 44
    thisalinea.parentID = 43
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Article 15 of the Charter provides for the freedom to choose an occupation and the right to engage in work. Supporting the competitiveness of the European industry will ensure economic growth and make sure it continues to offer job opportunities to citizens and residents of the Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 15 of the Charter provides for the freedom to choose an occupation and the right to")
    thisalinea.textcontent.append("engage in work. Supporting the competitiveness of the European industry will ensure")
    thisalinea.textcontent.append("economic growth and make sure it continues to offer job opportunities to citizens and")
    thisalinea.textcontent.append("residents of the Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 16 of the Charter of Fundamental Rights of the European Union (‘the Charter’) ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 45
    thisalinea.parentID = 43
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Article 16 of the Charter of Fundamental Rights of the European Union (‘the Charter’) provides for the freedom to conduct a business. The measures under this proposal support the creation of innovation capacity and the deployment of clean energy technologies, which can reinforce the freedom to conduct a business in accordance with Union law and national laws and practices. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 16 of the Charter of Fundamental Rights of the European Union (‘the Charter’)")
    thisalinea.textcontent.append("provides for the freedom to conduct a business. The measures under this proposal support the")
    thisalinea.textcontent.append("creation of innovation capacity and the deployment of clean energy technologies, which can")
    thisalinea.textcontent.append("reinforce the freedom to conduct a business in accordance with Union law and national laws")
    thisalinea.textcontent.append("and practices.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "BUDGETARY IMPLICATIONS"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 46
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The proposal will result in additional pre-financing to be paid under JTF in 2024, financed by the European Recovery Instrument NextGenerationEU. It will also result in additional pre- financing to be paid under the ERDF, CF and ESF+ in 2024 for amounts programmed under priorities dedicated to operations contributing to strengthening STEP objectives. The additional pre-financing payments for the JTF in 2024 will be financed only from external assigned revenues and will result in a frontloading of NGEU payment appropriations from year 2026 to year 2024. All amounts will be available as external assigned revenues, within 14 the meaning of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal will result in additional pre-financing to be paid under JTF in 2024, financed by")
    thisalinea.textcontent.append("the European Recovery Instrument NextGenerationEU. It will also result in additional pre-")
    thisalinea.textcontent.append("financing to be paid under the ERDF, CF and ESF+ in 2024 for amounts programmed under")
    thisalinea.textcontent.append("priorities dedicated to operations contributing to strengthening STEP objectives. The")
    thisalinea.textcontent.append("additional pre-financing payments for the JTF in 2024 will be financed only from external")
    thisalinea.textcontent.append("assigned revenues and will result in a frontloading of NGEU payment appropriations from")
    thisalinea.textcontent.append("year 2026 to year 2024. All amounts will be available as external assigned revenues, within")
    thisalinea.textcontent.append("14")
    thisalinea.textcontent.append("the meaning of Article 21(5) of Regulation (EU, Euratom) 2018/1046 stemming from the")
    thisalinea.textcontent.append("Next GenerationEU borrowing operations.")
    thisalinea.textcontent.append("The additional pre-financing payments for the ERDF, CF and ESF+ in 2024 will result in a")
    thisalinea.textcontent.append("frontloading of payment appropriations to 2024 and is budgetary neutral over the 2021-2027")
    thisalinea.textcontent.append("period. This additional pre-financing was not envisaged in the draft budget. The Commission")
    thisalinea.textcontent.append("will monitor the amounts programmed by Member States under priorities dedicated to")
    thisalinea.textcontent.append("operations contributing to STEP objectives and assess their impact on the payment needs in")
    thisalinea.textcontent.append("the context of the global transfer exercise in 2024. The amount paid as additional pre-")
    thisalinea.textcontent.append("financing shall be totally cleared from the Commission accounts not later than closure of the")
    thisalinea.textcontent.append("respective programmes, such that the total amount of payments made under the concerned")
    thisalinea.textcontent.append("Funds will remain unchanged with this proposal. The proposed modification does not require")
    thisalinea.textcontent.append("changes in the Multiannual Financial Framework annual ceilings for commitments and")
    thisalinea.textcontent.append("payments as per Annex I to Council Regulation (EU, Euratom) 2020/2093, and does not")
    thisalinea.textcontent.append("imply changes to the overall payment needs over the 2021-27 programming period.")
    thisalinea.textcontent.append("As for Horizon Europe, the proposal consists in reinforcing the envelope of the EIC by EUR")
    thisalinea.textcontent.append("2.63 billion in total:")
    thisalinea.textcontent.append("In addition, the Innovation Fund should be reinforced by EUR 5 billion, the European")
    thisalinea.textcontent.append("Defence Fund by EUR 1.5 billion and the InvestEU should benefit from a reinforcement of")
    thisalinea.textcontent.append("EUR 3 billion resulting in a guarantee of EUR 7.5 billion.")
    thisalinea.textcontent.append("The total budgetary implications for the MFF is therefore EUR 10 billion.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "– EUR 0.8 billion are proposed to be redeployed from the resources allocated to Pillar ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 47
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– EUR 0.8 billion are proposed to be redeployed from the resources allocated to Pillar II 'Global Challenges and European Industrial Competitiveness' for the period 202[x] to 2027; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– EUR 0.8 billion are proposed to be redeployed from the resources allocated to Pillar")
    thisalinea.textcontent.append("II 'Global Challenges and European Industrial Competitiveness' for the period 202[x]")
    thisalinea.textcontent.append("to 2027;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "– EUR 0.13 billion from the reflows of the EIC pilot of Horizon 2020 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 48
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– EUR 0.13 billion from the reflows of the EIC pilot of Horizon 2020 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– EUR 0.13 billion from the reflows of the EIC pilot of Horizon 2020")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "– EUR 1.2 billion resulting from total or partial non-implementation of research ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 49
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– EUR 1.2 billion resulting from total or partial non-implementation of research projects supported by Horizon Europe and its predecessors, are proposed to be made available again, in line with Article 15(3) of the Financial Regulation, to the benefit of the EIC strand of Horizon Europe; and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– EUR 1.2 billion resulting from total or partial non-implementation of research")
    thisalinea.textcontent.append("projects supported by Horizon Europe and its predecessors, are proposed to be made")
    thisalinea.textcontent.append("available again, in line with Article 15(3) of the Financial Regulation, to the benefit")
    thisalinea.textcontent.append("of the EIC strand of Horizon Europe; and")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "– EUR 0.5 billion budgetary reinforcement "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 50
    thisalinea.parentID = 46
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– EUR 0.5 billion budgetary reinforcement "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– EUR 0.5 billion budgetary reinforcement")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "5. OTHER ELEMENTS"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 51
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "The Commission will monitor the implementation of the Platform and measure the achievement of the objectives under this Regulation in a targeted and proportionate manner. The Commission will ensure that data for monitoring the implementation of the activities and results are collected efficiently, effectively and in a timely manner. To monitor the implementation of the Platform, the Commission will compile the expenditures related to the STEP from the relevant programmes. The respective climate spending targets under the relevant programmes continue to apply. This requires the following: 15 To monitor and assess the performance of the programme, the Commission will compile "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Implementation plans and monitoring, evaluation and reporting arrangements"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 52
    thisalinea.parentID = 51
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The Commission will monitor the implementation of the Platform and measure the achievement of the objectives under this Regulation in a targeted and proportionate manner. The Commission will ensure that data for monitoring the implementation of the activities and results are collected efficiently, effectively and in a timely manner. To monitor the implementation of the Platform, the Commission will compile the expenditures related to the STEP from the relevant programmes. The respective climate spending targets under the relevant programmes continue to apply. This requires the following: 15 To monitor and assess the performance of the programme, the Commission will compile "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The Commission will monitor the implementation of the Platform and measure the")
    thisalinea.textcontent.append("achievement of the objectives under this Regulation in a targeted and proportionate manner.")
    thisalinea.textcontent.append("The Commission will ensure that data for monitoring the implementation of the activities and")
    thisalinea.textcontent.append("results are collected efficiently, effectively and in a timely manner.")
    thisalinea.textcontent.append("To monitor the implementation of the Platform, the Commission will compile the")
    thisalinea.textcontent.append("expenditures related to the STEP from the relevant programmes. The respective climate")
    thisalinea.textcontent.append("spending targets under the relevant programmes continue to apply. This requires the")
    thisalinea.textcontent.append("following:")
    thisalinea.textcontent.append("15")
    thisalinea.textcontent.append("To monitor and assess the performance of the programme, the Commission will compile the")
    thisalinea.textcontent.append("results of performance indicators related to the STEP from the relevant programmes.")
    thisalinea.textcontent.append("The implementation of the performance indicators related to the STEP requires:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Common Provisions Regulation: updating Annex I of the Regulation to include ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 53
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– Common Provisions Regulation: updating Annex I of the Regulation to include additional intervention fields; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Common Provisions Regulation: updating Annex I of the Regulation to include")
    thisalinea.textcontent.append("additional intervention fields;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Recovery and Resilience Facility: tagging and reporting based on a break-down of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 54
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– Recovery and Resilience Facility: tagging and reporting based on a break-down of the estimated expenditure by the Commission in accordance with article 29(3) of that Regulation of investments related to the STEP objectives; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Recovery and Resilience Facility: tagging and reporting based on a break-down of")
    thisalinea.textcontent.append("the estimated expenditure by the Commission in accordance with article 29(3) of that")
    thisalinea.textcontent.append("Regulation of investments related to the STEP objectives;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– InvestEU: tracking of expenditures by the Commission. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 55
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– InvestEU: tracking of expenditures by the Commission. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– InvestEU: tracking of expenditures by the Commission.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Direct management programmes (Horizon Europe, Innovation Fund, European ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 56
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– Direct management programmes (Horizon Europe, Innovation Fund, European Defence Fund, Digital Europe Programme, EU4Health Programme): tracking of expenditures by the Commission. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Direct management programmes (Horizon Europe, Innovation Fund, European")
    thisalinea.textcontent.append("Defence Fund, Digital Europe Programme, EU4Health Programme): tracking of")
    thisalinea.textcontent.append("expenditures by the Commission.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Cohesion instruments: amending of the annexes of the fund-specific regulation ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 57
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "– Cohesion instruments: amending of the annexes of the fund-specific regulation containing the performance indicators; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Cohesion instruments: amending of the annexes of the fund-specific regulation")
    thisalinea.textcontent.append("containing the performance indicators;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– InvestEU: amending Annex III of the InvestEU Regulation containing the key ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 58
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "– InvestEU: amending Annex III of the InvestEU Regulation containing the key performance and monitoring indicators; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– InvestEU: amending Annex III of the InvestEU Regulation containing the key")
    thisalinea.textcontent.append("performance and monitoring indicators;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Recovery and Resilience Facility: relying on the existing reporting framework "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 59
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "– Recovery and Resilience Facility: relying on the existing reporting framework "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Recovery and Resilience Facility: relying on the existing reporting framework")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Direct management programmes (Horizon Europe, Innovation Fund, European ..."
    thisalinea.titlefontsize = "11.999999999999943"
    thisalinea.nativeID = 60
    thisalinea.parentID = 52
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "– Direct management programmes (Horizon Europe, Innovation Fund, European Defence Fund, Digital Europe Programme, EU4Health Programme): information to be gathered by the Commission. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Direct management programmes (Horizon Europe, Innovation Fund, European")
    thisalinea.textcontent.append("Defence Fund, Digital Europe Programme, EU4Health Programme): information to")
    thisalinea.textcontent.append("be gathered by the Commission.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Detailed explanation of the specific provisions of the proposal"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 61
    thisalinea.parentID = 51
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Chapter 1 of this Regulation (Articles 1 to 8) sets out the common provisions necessary for the creation of the STEP, while Chapter 2 contains the amendments to other relevant pieces of EU legislation (Articles 9 to 19). Subject matter and Platform objectives (Articles 1 and 2) Financial support (Article 3) This provision lays down the additional EU funding which is used to reinforce the firepower of several instruments, namely InvestEU, Horizon Europe, European Defence Fund and the Innovation Fund. Sovereignty Seal and cumulative funding (Article 4) 16 Article 4 creates a ‘Sovereignty Seal’, which is a new label intended "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Chapter 1 of this Regulation (Articles 1 to 8) sets out the common provisions necessary for")
    thisalinea.textcontent.append("the creation of the STEP, while Chapter 2 contains the amendments to other relevant pieces of")
    thisalinea.textcontent.append("EU legislation (Articles 9 to 19).")
    thisalinea.textcontent.append("Subject matter and Platform objectives (Articles 1 and 2)")
    thisalinea.textcontent.append("Financial support (Article 3)")
    thisalinea.textcontent.append("This provision lays down the additional EU funding which is used to reinforce the firepower")
    thisalinea.textcontent.append("of several instruments, namely InvestEU, Horizon Europe, European Defence Fund and the")
    thisalinea.textcontent.append("Innovation Fund.")
    thisalinea.textcontent.append("Sovereignty Seal and cumulative funding (Article 4)")
    thisalinea.textcontent.append("16")
    thisalinea.textcontent.append("Article 4 creates a ‘Sovereignty Seal’, which is a new label intended to help project promoters")
    thisalinea.textcontent.append("attract public and private investments by certifying its contribution to the STEP objectives.")
    thisalinea.textcontent.append("The Sovereignty Seal would be awarded under directly managed programmes, namely")
    thisalinea.textcontent.append("Horizon Europe, the Innovation Fund, the Digital Europe programme, the EU4Health")
    thisalinea.textcontent.append("programme, and the European Defence Fund. The Seal builds on the existing ‘Seal of")
    thisalinea.textcontent.append("Excellence’, which is a quality label for eligible projects that could not be funded due to lack")
    thisalinea.textcontent.append("of budget available. Unlike the Seal of Excellence, the Sovereignty Seal is defined only by")
    thisalinea.textcontent.append("reference to the objectives pursued by the projects to which it has been awarded, and")
    thisalinea.textcontent.append("regardless of whether the project has been able to receive EU funding as long as it has been")
    thisalinea.textcontent.append("successfully evaluated under Horizon Europe, the Innovation Fund, the Digital Europe")
    thisalinea.textcontent.append("programme, the EU4Health programme or the European Defence Fund. This is a way to")
    thisalinea.textcontent.append("promote that projects which have been partly funded can also receive cumulative or combined")
    thisalinea.textcontent.append("funding with another Union instrument (Article 4(1)(b)). Moreover, the Sovereignty Seal")
    thisalinea.textcontent.append("would also apply to cases where a project has not been able to receive EU funds under one")
    thisalinea.textcontent.append("programme, in order to promote that it receives support under another programme (Article")
    thisalinea.textcontent.append("4(1)(a)).")
    thisalinea.textcontent.append("This provision also indicates that projects having been awarded a Sovereignty Seal should be")
    thisalinea.textcontent.append("prioritised by Member States when proposing their Recovery and Resilience Plans and when")
    thisalinea.textcontent.append("deciding on investment projects to be financed from its share of the Modernisation Fund. As")
    thisalinea.textcontent.append("regards the InvestEU Programme (see also Article 15), the Sovereignty Seal should be taken")
    thisalinea.textcontent.append("into account by the Commission in the context of the procedure provided for in Article 19 of")
    thisalinea.textcontent.append("the EIB Statute and of the policy check laid down in Article 23 of Regulation (EU) 2021/523.")
    thisalinea.textcontent.append("In addition, the implementing partners should be requested to examine projects having been")
    thisalinea.textcontent.append("awarded the Sovereignty Seal in case they fall within their geographic and activity scope.")
    thisalinea.textcontent.append("Concerning cohesion policy, it is proposed that managing authorities are able to grant support")
    thisalinea.textcontent.append("from the ERDF or the ESF+ directly, subject to compliance with applicable State aid rules,")
    thisalinea.textcontent.append("for operations attributed a Sovereignty Seal (see Article 13).")
    thisalinea.textcontent.append("Strategic projects identified in accordance with the Net Zero Industry and the Critical Raw")
    thisalinea.textcontent.append("Materials Acts that fall under the scope of Article 2 of the Regulation may benefit from")
    thisalinea.textcontent.append("cumulative funding across relevant Programmes.")
    thisalinea.textcontent.append("Monitoring and implementation (Article 5)")
    thisalinea.textcontent.append("Sovereignty Portal (Article 6)")
    thisalinea.textcontent.append("17")
    thisalinea.textcontent.append("act as the main point of contact for those priorities, with the objective to ensure the consistent")
    thisalinea.textcontent.append("application of the STEP throughout the Union, and in order to facilitate the combination of")
    thisalinea.textcontent.append("available funding for Platform projects, notably under directly managed programmes and")
    thisalinea.textcontent.append("shared management programmes.")
    thisalinea.textcontent.append("Annual report and evaluation (Articles 7 and 8).")
    thisalinea.textcontent.append("Articles 7 sets out the obligation for the Commission to provide an annual report to the")
    thisalinea.textcontent.append("European Parliament and the Council on the progress made in implementing the STEP")
    thisalinea.textcontent.append("objectives.")
    thisalinea.textcontent.append("Amendments to Directive 2003/87/EC (EU ETS Directive) (Article 9)")
    thisalinea.textcontent.append("Amendments to Regulation (EU) 2021/1058, Regulation on the European Regional")
    thisalinea.textcontent.append("Development Fund and on the Cohesion Fund (Article 10), Regulation on the Just Transition")
    thisalinea.textcontent.append("Fund (Article 11), and to Regulation (EU) 2021/1057, Regulation establishing the European")
    thisalinea.textcontent.append("Social Fund Plus (Article 12)")
    thisalinea.textcontent.append("Moreover, in order to help accelerate those investments and providing the necessary liquidity,")
    thisalinea.textcontent.append("an exceptional pre-financing of 30% will be available for the year 2024. It is also set out that")
    thisalinea.textcontent.append("Member States should be able to apply an increased EU financing rate of up to 100%. This is")
    thisalinea.textcontent.append("reflected for the three Regulations above, by including the same provisions under Articles 10,")
    thisalinea.textcontent.append("11, and 12.")
    thisalinea.textcontent.append("Annexes I and II of the ERDF and CF regulation are amended to include the indicators related")
    thisalinea.textcontent.append("to the new STEP objectives.")
    thisalinea.textcontent.append("18")
    thisalinea.textcontent.append("Amendments to Regulation (EU) 2021/1060, Regulation laying down common provisions")
    thisalinea.textcontent.append("applicable amongst others to the ERDF, CF, JTF and ESF+ (Article 13)")
    thisalinea.textcontent.append("This Regulation is also amended to allow that projects having been awarded a Sovereignty")
    thisalinea.textcontent.append("Seal could benefit from better access to EU funding, notably by facilitating cumulative or")
    thisalinea.textcontent.append("combined funding from several Union instruments. To that end, managing authorities will be")
    thisalinea.textcontent.append("able to grant support from the ERDF or the ESF+ directly, for operations attributed a")
    thisalinea.textcontent.append("Sovereignty Seal. It is also set out that Member States should be able to apply an increased")
    thisalinea.textcontent.append("EU financing rate of up to 100%.")
    thisalinea.textcontent.append("The amendment to Annex I of the CPR Regulation incorporates supplementary intervention")
    thisalinea.textcontent.append("fields that will allow to track the expenditure related to the new Platform objectives.")
    thisalinea.textcontent.append("Amendments to Regulation (EU) No 1303/2013 (Article 14) and Regulation (EU) No")
    thisalinea.textcontent.append("223/2014 (Article 15)")
    thisalinea.textcontent.append("This amendment to provide with additional flexibilities for Member States to be able to")
    thisalinea.textcontent.append("implement the 2014-2020 cohesion policy programmes, the EMFF and the Fund for European")
    thisalinea.textcontent.append("Aid to the Most Deprived (FEAD). The regulatory framework for the implementation of the")
    thisalinea.textcontent.append("2014-2020 programmes has already been adapted to provide Member States and regions with")
    thisalinea.textcontent.append("additional flexibility in terms of implementation rules and more liquidity to tackle the effects")
    thisalinea.textcontent.append("of the COVID-19 pandemic and the war or aggression against Ukraine.35 These measures,")
    thisalinea.textcontent.append("introduced at the end of the programming period, require sufficient time and administrative")
    thisalinea.textcontent.append("resources to be fully exploited and implemented. This is linked to the need for the Member")
    thisalinea.textcontent.append("States to focus administrative resources on the revision of the operational programmes")
    thisalinea.textcontent.append("towards the STEP.")
    thisalinea.textcontent.append("Therefore, the deadline for the submission of that final payment application should be")
    thisalinea.textcontent.append("extended by 12 months. Furthermore, the deadline for the submission of the closure")
    thisalinea.textcontent.append("documents should also be extended by 12 months so that the necessary controls and audits")
    thisalinea.textcontent.append("allowing for an orderly closure of programmes under the 2014-2020 programming period can")
    thisalinea.textcontent.append("be carried out. In order to ensure a sound implementation of the EU budget and respect for the")
    thisalinea.textcontent.append("payment ceilings, payments to be made in 2025 should be capped at 1 % of the financial")
    thisalinea.textcontent.append("appropriations from resources under the Multiannual Financial Framework per programme. It")
    thisalinea.textcontent.append("should be clarified that amounts due exceeding the ceiling of 1% of programme")
    thisalinea.textcontent.append("appropriations per fund for 2025 would not be paid in 2025 nor in subsequent years but only")
    thisalinea.textcontent.append("used for the clearance of pre-financing. Unused amounts shall be decommitted in accordance")
    thisalinea.textcontent.append("with the general rules for decommitment at closure.")
    thisalinea.textcontent.append("19")
    thisalinea.textcontent.append("Amendments to Regulation (EU) 2021/523, establishing the InvestEU Programme (Article")
    thisalinea.textcontent.append("16)")
    thisalinea.textcontent.append("This provision creates a new policy area (fifth window) aimed at supporting STEP")
    thisalinea.textcontent.append("investments under InvestEU, and it accommodates the additional amount of EUR [...] billion")
    thisalinea.textcontent.append("proposed in the context of the MFF review by amending the amounts of the EU guarantee for")
    thisalinea.textcontent.append("the purposes of the STEP. Amendments are also made to reflect the Sovereignty Seal")
    thisalinea.textcontent.append("dimension into InvestEU, as explained under Article 4.")
    thisalinea.textcontent.append("It also proposes additional flexibilities and clarifications to better pursue the objectives of this")
    thisalinea.textcontent.append("initiative. In relation to the combination of portfolios, it is specified that when support from")
    thisalinea.textcontent.append("the financial instruments referred to in Article 7(1) is combined in a financial product in a")
    thisalinea.textcontent.append("subordinated position to the EU guarantee under this Regulation and/or EU guarantee")
    thisalinea.textcontent.append("established by Regulation (EU) 2015/1017, the losses, revenues and repayments as well as")
    thisalinea.textcontent.append("potential recoveries may also be attributed on a non pro rata basis. This amendment aims at")
    thisalinea.textcontent.append("facilitating synergies between the InvestEU and other Union programmes by increasing the")
    thisalinea.textcontent.append("flexibility on the design of blending operations.")
    thisalinea.textcontent.append("To facilitate the uptake of the Member State compartment, it is proposed to slightly increase")
    thisalinea.textcontent.append("the time period available to conclude a guarantee agreement from nine to twelve months from")
    thisalinea.textcontent.append("the conclusion of the contribution agreement. The rules on the membership of the Investment")
    thisalinea.textcontent.append("Committee are also amended to clarify that a non-permanent member may be assigned to a")
    thisalinea.textcontent.append("maximum of two configurations to apply a selection process that allows to constitute the")
    thisalinea.textcontent.append("Investment Committee for the new fifth window in a swift manner.")
    thisalinea.textcontent.append("Annex III of InvestEU Regulation is amended to include the indicators related to the new")
    thisalinea.textcontent.append("STEP window.")
    thisalinea.textcontent.append("Amendments to Regulation (EU) 2021/695, establishing Horizon Europe (Article 17)")
    thisalinea.textcontent.append("This provision aims at providing additional flexibility and funding for the EIC Accelerator.")
    thisalinea.textcontent.append("The Accelerator under Horizon Europe should be able to provide equity-only support to non-")
    thisalinea.textcontent.append("bankable SMEs, including start-ups, and non-bankable small mid-caps, carrying out")
    thisalinea.textcontent.append("innovation in the technologies supported by STEP. Moreover, the unused funds committed for")
    thisalinea.textcontent.append("the EIC Pilot under Horizon2020 should be made available for the purposes of the EIC")
    thisalinea.textcontent.append("Accelerator under Horizon Europe.")
    thisalinea.textcontent.append("Amendments to Regulation (EU) 2021/697, establishing the European Defence Fund (Article")
    thisalinea.textcontent.append("18)")
    thisalinea.textcontent.append("Amendments to Regulation (EU) 2021/241, establishing the Recovery and Resilience Facility")
    thisalinea.textcontent.append("(Article 19)")
    thisalinea.textcontent.append("This Regulation is amended to increase the ceiling for the amount of estimated costs of the")
    thisalinea.textcontent.append("recovery and resilience plans that Member States can use for the Member State compartment")
    thisalinea.textcontent.append("of InvestEU. In addition to the applicable ceiling of 4% of the recovery and resilience plan’s")
    thisalinea.textcontent.append("financial allocation, Member States can decide to allocate a further 6% to support STEP")
    thisalinea.textcontent.append("investments, therefore up to a total of 10%. Article 29 is amended to ensure the Member")
    thisalinea.textcontent.append("20")
    thisalinea.textcontent.append("States identify and submit to the Commission the planned calls for proposals related to the")
    thisalinea.textcontent.append("Platform objectives in order to publish them on the Sovereignty portal.")
    thisalinea.textcontent.append("Entry into force and application (Article 20)")
    thisalinea.textcontent.append("It is proposed that this Regulation, which is directly applicable in all Member States, enters")
    thisalinea.textcontent.append("into force on the day following that of its publication.")
    thisalinea.textcontent.append("21")
    thisalinea.textcontent.append("2023/0199 (COD)")
    thisalinea.textcontent.append("Proposal for a")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 1 explains the subject matter of the Regulation, and Article 2 defines the objectives ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 62
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Article 1 explains the subject matter of the Regulation, and Article 2 defines the objectives and scope of the instrument. In accordance with Article 2, the STEP has a twofold objective: (i) to support the development or manufacturing of critical technologies in the Union or safeguarding and strengthening their value chains; and (ii) reducing labour and skills shortages in those strategic sectors. Article 2 also defines the fields for those critical technologies, namely deep and digital technologies, clean technologies, and biotechnologies. This provision further specifies that, in order for a technology to be deemed as critical for the purposes of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 1 explains the subject matter of the Regulation, and Article 2 defines the objectives")
    thisalinea.textcontent.append("and scope of the instrument. In accordance with Article 2, the STEP has a twofold objective:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(i) to support the development or manufacturing of critical technologies in the Union or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 63
    thisalinea.parentID = 62
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) to support the development or manufacturing of critical technologies in the Union or safeguarding and strengthening their value chains; and (ii) reducing labour and skills shortages in those strategic sectors. Article 2 also defines the fields for those critical technologies, namely deep and digital technologies, clean technologies, and biotechnologies. This provision further specifies that, in order for a technology to be deemed as critical for the purposes of the Platform, it should meet the following conditions: (i) bring an innovative, element with significant economic potential to the Single Market; or (ii) contribute to reduce or prevent the strategic dependencies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) to support the development or manufacturing of critical technologies in the Union or")
    thisalinea.textcontent.append("safeguarding and strengthening their value chains; and (ii) reducing labour and skills")
    thisalinea.textcontent.append("shortages in those strategic sectors. Article 2 also defines the fields for those critical")
    thisalinea.textcontent.append("technologies, namely deep and digital technologies, clean technologies, and biotechnologies.")
    thisalinea.textcontent.append("This provision further specifies that, in order for a technology to be deemed as critical for the")
    thisalinea.textcontent.append("purposes of the Platform, it should meet the following conditions: (i) bring an innovative,")
    thisalinea.textcontent.append("element with significant economic potential to the Single Market; or (ii) contribute to reduce")
    thisalinea.textcontent.append("or prevent the strategic dependencies of the Union. It is also clarified that, where an IPCEI")
    thisalinea.textcontent.append("approved pursuant to Article 107(3)(b) TFEU relates to any of the technology fields referred")
    thisalinea.textcontent.append("to in Article 2(1)(a), the relevant technologies should be deemed to be critical. Article 2 also")
    thisalinea.textcontent.append("provides with further guidance as to the meaning of ‘value chain’.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 5 defines how the Commission shall monitor the implementation of the STEP, the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 64
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Article 5 defines how the Commission shall monitor the implementation of the STEP, the results and progress towards the achievement of its objectives. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 5 defines how the Commission shall monitor the implementation of the STEP, the")
    thisalinea.textcontent.append("results and progress towards the achievement of its objectives.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 6 sets out the obligation for the Commission to set up a new publicly ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 65
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Article 6 sets out the obligation for the Commission to set up a new publicly available website (the Sovereignty Portal) to provide support to companies and project promoters seeking funds for STEP investments. To that end, the Portal is required to display in particular the following information: ongoing and upcoming calls for proposals linked to the STEP objectives (Article 6(1)(a)) and contacts to the national competent authorities designated to act as the main point of contact for the implementation of the STEP at national level (Article 6(1)(d)). Moreover, the Portal should inform about the projects which have been awarded a "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 6 sets out the obligation for the Commission to set up a new publicly available website")
    thisalinea.textcontent.append("(the Sovereignty Portal) to provide support to companies and project promoters seeking funds")
    thisalinea.textcontent.append("for STEP investments. To that end, the Portal is required to display in particular the following")
    thisalinea.textcontent.append("information: ongoing and upcoming calls for proposals linked to the STEP objectives (Article")
    thisalinea.textcontent.append("6(1)(a)) and contacts to the national competent authorities designated to act as the main point")
    thisalinea.textcontent.append("of contact for the implementation of the STEP at national level (Article 6(1)(d)). Moreover,")
    thisalinea.textcontent.append("the Portal should inform about the projects which have been awarded a Sovereignty Seal")
    thisalinea.textcontent.append("label, in order to give them visibility towards potential investors (Article 6(1)(b)), as well as")
    thisalinea.textcontent.append("strategic projects identified under the NZIA and the CRMA (Article 6(1)(c)). Moreover, the")
    thisalinea.textcontent.append("Platform should present the information about the implementation of the Platform (Article")
    thisalinea.textcontent.append("6(2)). Article 6(4) requires Member States to designate one national competent authority to")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 8 lays down the rules on the evaluation of the Platform. The Commission is ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 66
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Article 8 lays down the rules on the evaluation of the Platform. The Commission is required to provide an evaluation report to the European Parliament and the Council by 31 December 2025. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 8 lays down the rules on the evaluation of the Platform. The Commission is required")
    thisalinea.textcontent.append("to provide an evaluation report to the European Parliament and the Council by 31 December")
    thisalinea.textcontent.append("2025.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 9 amends the EU ETS Directive to specify the amount of additional funds to ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 67
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Article 9 amends the EU ETS Directive to specify the amount of additional funds to be implemented through the Innovation Fund for projects aimed at supporting the development or manufacturing in the Union of clean technologies. This additional support is made available only to Member States whose average GDP per capita is below the EU average of the EU-27 measured in purchasing power standards (PPS) and calculated on the basis of Union figures for the period 2015-2017. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 9 amends the EU ETS Directive to specify the amount of additional funds to be")
    thisalinea.textcontent.append("implemented through the Innovation Fund for projects aimed at supporting the development")
    thisalinea.textcontent.append("or manufacturing in the Union of clean technologies. This additional support is made")
    thisalinea.textcontent.append("available only to Member States whose average GDP per capita is below the EU average of")
    thisalinea.textcontent.append("the EU-27 measured in purchasing power standards (PPS) and calculated on the basis of")
    thisalinea.textcontent.append("Union figures for the period 2015-2017.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 10 amends the Regulation on the European Regional Development Fund (ERDF) and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 68
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Article 10 amends the Regulation on the European Regional Development Fund (ERDF) and on the Cohesion Fund (CF) to create new specific objectives under Policy Objective 1 (a more competitive and smarter Europe by promoting innovative and smart economic transformation and regional ICT connectivity) and Policy Objective 2 (a greener, low-carbon transitioning towards a net zero carbon economy and resilient Europe by promoting clean and fair energy transition, green and blue investment, the circular economy, climate change mitigation and adaptation, risk prevention and management, and sustainable urban mobility). It is also made possible to support productive investments in enterprises other "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 10 amends the Regulation on the European Regional Development Fund (ERDF) and")
    thisalinea.textcontent.append("on the Cohesion Fund (CF) to create new specific objectives under Policy Objective 1 (a more")
    thisalinea.textcontent.append("competitive and smarter Europe by promoting innovative and smart economic transformation")
    thisalinea.textcontent.append("and regional ICT connectivity) and Policy Objective 2 (a greener, low-carbon transitioning")
    thisalinea.textcontent.append("towards a net zero carbon economy and resilient Europe by promoting clean and fair energy")
    thisalinea.textcontent.append("transition, green and blue investment, the circular economy, climate change mitigation and")
    thisalinea.textcontent.append("adaptation, risk prevention and management, and sustainable urban mobility). It is also made")
    thisalinea.textcontent.append("possible to support productive investments in enterprises other than SMEs, in less developed")
    thisalinea.textcontent.append("and transition regions, as well as in more developed regions in Member States whose average")
    thisalinea.textcontent.append("GDP per capita is below the EU average of the EU-27 measured in purchasing power")
    thisalinea.textcontent.append("standards (PPS) and calculated on the basis of Union figures for the period 2015-2017.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 11 amends the Regulation on the Just Transition Fund (JTF) to indicate that such ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 69
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "Article 11 amends the Regulation on the Just Transition Fund (JTF) to indicate that such a programme can support investments linked to the STEP objectives. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 11 amends the Regulation on the Just Transition Fund (JTF) to indicate that such a")
    thisalinea.textcontent.append("programme can support investments linked to the STEP objectives.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 49 of the CPR Regulation is amended to ensure that the managing authorities identify ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 70
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Article 49 of the CPR Regulation is amended to ensure that the managing authorities identify and submit to the Commission the planned calls for proposals related to the STEP objectives in order to publish them on the Sovereignty portal, as well as a dedicated secondary theme for the ESF +. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 49 of the CPR Regulation is amended to ensure that the managing authorities identify")
    thisalinea.textcontent.append("and submit to the Commission the planned calls for proposals related to the STEP objectives")
    thisalinea.textcontent.append("in order to publish them on the Sovereignty portal, as well as a dedicated secondary theme for")
    thisalinea.textcontent.append("the ESF +.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 18 amends the Regulation on the European Defence Fund to specify the amount of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 71
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "Article 18 amends the Regulation on the European Defence Fund to specify the amount of additional funds to be implemented through the European Defence Fund. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 18 amends the Regulation on the European Defence Fund to specify the amount of")
    thisalinea.textcontent.append("additional funds to be implemented through the European Defence Fund.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL establishing the Strategic Technologies for Europe Platform (‘STEP’) and amending"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 72
    thisalinea.parentID = 61
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "Directive 2003/87/EC, Regulations (EU) 2021/1058, (EU) 2021/1056, (EU) 2021/1057, (EU) No 1303/2013, (EU) No 223/2014, (EU) 2021/1060, (EU) 2021/523, (EU) 2021/695, (EU) 2021/697 and (EU) 2021/241 THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION, Having regard to the Treaty on the Functioning of the European Union, and in particular Article 164, Article 173, Article 175, third paragraph, Article 176, Article 177, Article 178, Article 182(1) and Article 192(1) thereof, Having regard to the proposal from the European Commission, After transmission of the draft legislative act to the national parliaments, Having regard to the opinion of the European Economic "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Directive 2003/87/EC, Regulations (EU) 2021/1058, (EU) 2021/1056, (EU) 2021/1057,")
    thisalinea.textcontent.append("(EU) No 1303/2013, (EU) No 223/2014, (EU) 2021/1060, (EU) 2021/523, (EU) 2021/695,")
    thisalinea.textcontent.append("(EU) 2021/697 and (EU) 2021/241")
    thisalinea.textcontent.append("THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION,")
    thisalinea.textcontent.append("Having regard to the Treaty on the Functioning of the European Union, and in particular")
    thisalinea.textcontent.append("Article 164, Article 173, Article 175, third paragraph, Article 176, Article 177, Article 178,")
    thisalinea.textcontent.append("Article 182(1) and Article 192(1) thereof,")
    thisalinea.textcontent.append("Having regard to the proposal from the European Commission,")
    thisalinea.textcontent.append("After transmission of the draft legislative act to the national parliaments,")
    thisalinea.textcontent.append("Having regard to the opinion of the European Economic and Social Committee36,")
    thisalinea.textcontent.append("Having regard to the opinion of the Committee of the Regions37,")
    thisalinea.textcontent.append("Acting in accordance with the ordinary legislative procedure,")
    thisalinea.textcontent.append("Whereas:")
    thisalinea.textcontent.append("22")
    thisalinea.textcontent.append("support its industry, such as the Green Deal Industrial Plan,40 the Critical Raw")
    thisalinea.textcontent.append("Materials Act41, the Net Zero Industry Act42, the new Temporary Crisis and Transition")
    thisalinea.textcontent.append("Framework for State aid,43 and REPowerEU.44 While these solutions provide fast and")
    thisalinea.textcontent.append("targeted support, the EU needs a more structural answer to the investment needs of its")
    thisalinea.textcontent.append("industries, safeguarding cohesion and the level playing field in the Single Market and")
    thisalinea.textcontent.append("to reduce the EU’s strategic dependencies.")
    thisalinea.textcontent.append("23")
    thisalinea.textcontent.append("for funding, in accordance with the respective programme rules, to the extent that the")
    thisalinea.textcontent.append("identified funding gap and the eligible costs have not yet been completely covered.")
    thisalinea.textcontent.append("24")
    thisalinea.textcontent.append("programme,51 the European Defence Fund or the Innovation Fund, and regardless of")
    thisalinea.textcontent.append("whether the project has received funding under those instruments. These minimum")
    thisalinea.textcontent.append("quality requirements will be established with a view to identify high quality projects.")
    thisalinea.textcontent.append("This Seal should be used as a quality label, to help projects attract public and private")
    thisalinea.textcontent.append("investments by certifying its contribution to the STEP objectives. Moreover, the Seal")
    thisalinea.textcontent.append("will promote better access to EU funding, notably by facilitating cumulative or")
    thisalinea.textcontent.append("combined funding from several Union instruments.")
    thisalinea.textcontent.append("25")
    thisalinea.textcontent.append("actions undertaken and serve as basis for assessing the need for an upscaling of the")
    thisalinea.textcontent.append("support towards strategic sectors.")
    thisalinea.textcontent.append("26")
    thisalinea.textcontent.append("investments aimed at achieving a skilled and resilient workforce ready for the future")
    thisalinea.textcontent.append("world of work.")
    thisalinea.textcontent.append("27")
    thisalinea.textcontent.append("(end-2023) may continue after that date. In order to ensure a sound implementation of")
    thisalinea.textcontent.append("the EU budget and respect for the payment ceilings, payments to be made in 2025")
    thisalinea.textcontent.append("should be capped at 1 % of the financial appropriations from resources under the")
    thisalinea.textcontent.append("Multiannual Financial Framework per programme. Amounts due exceeding the ceiling")
    thisalinea.textcontent.append("of 1% of programme appropriations per fund for 2025 would not be paid in 2025 nor")
    thisalinea.textcontent.append("in subsequent years but only used for the clearance of pre-financing. Unused amounts")
    thisalinea.textcontent.append("shall be decommitted in accordance with the general rules for decommitment at")
    thisalinea.textcontent.append("closure.")
    thisalinea.textcontent.append("28")
    thisalinea.textcontent.append("HAVE ADOPTED THIS REGULATION:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(1) Strengthening the competitiveness and resilience of the European economy through ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 73
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) Strengthening the competitiveness and resilience of the European economy through the green and digital transformations has been the EU compass over the last years. The green and digital transitions anchored in the European Grean Deal38 and the Digital Decade,39 spurs growth and the modernisation of the EU economy, opening up new business opportunities and helping gain a competitive advantage on the global markets. The European Green Deal sets out the roadmap for making the Union’s economy climate neutral and sustainable in a fair and inclusive manner, tackling climate and environmental-related challenges. Moreover, the Digital Decade Policy Programme 2030 sets "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) Strengthening the competitiveness and resilience of the European economy through")
    thisalinea.textcontent.append("the green and digital transformations has been the EU compass over the last years. The")
    thisalinea.textcontent.append("green and digital transitions anchored in the European Grean Deal38 and the Digital")
    thisalinea.textcontent.append("Decade,39 spurs growth and the modernisation of the EU economy, opening up new")
    thisalinea.textcontent.append("business opportunities and helping gain a competitive advantage on the global")
    thisalinea.textcontent.append("markets. The European Green Deal sets out the roadmap for making the Union’s")
    thisalinea.textcontent.append("economy climate neutral and sustainable in a fair and inclusive manner, tackling")
    thisalinea.textcontent.append("climate and environmental-related challenges. Moreover, the Digital Decade Policy")
    thisalinea.textcontent.append("Programme 2030 sets out a clear direction for the digital transformation of the Union")
    thisalinea.textcontent.append("and for the delivery of digital targets at Union level by 2030, notably concerning")
    thisalinea.textcontent.append("digital skills, digital infrastructures, and the digital transformation of businesses and")
    thisalinea.textcontent.append("public services.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(2) The EU industry has proven its inbuilt resilience but is being challenged. High ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 74
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) The EU industry has proven its inbuilt resilience but is being challenged. High inflation, labour shortages, post-COVID supply chains disruptions, rising interest rates, and spikes in energy costs and input prices are weighing on the competitiveness of the EU industry. This is paired with strong, but not always fair, competition on the fragmented global market. The EU has already put forward several initiatives to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) The EU industry has proven its inbuilt resilience but is being challenged. High")
    thisalinea.textcontent.append("inflation, labour shortages, post-COVID supply chains disruptions, rising interest")
    thisalinea.textcontent.append("rates, and spikes in energy costs and input prices are weighing on the competitiveness")
    thisalinea.textcontent.append("of the EU industry. This is paired with strong, but not always fair, competition on the")
    thisalinea.textcontent.append("fragmented global market. The EU has already put forward several initiatives to")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(3) The uptake and scaling up in the Union of deep and digital technologies, clean ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 75
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) The uptake and scaling up in the Union of deep and digital technologies, clean technologies, and biotechnologies will be essential to seize the opportunities and meet the objectives of the green and digital transitions, thus promoting the competitiveness of the European industry and its sustainability. Therefore, immediate action is required to support the development or manufacturing in the Union of such technologies, safeguarding and strengthening their value chains thereby reducing the Union’s strategic dependencies, and addressing existing labour and skills shortages in those sectors through trainings and apprenticeships and the creation of attractive, quality jobs accessible to all. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) The uptake and scaling up in the Union of deep and digital technologies, clean")
    thisalinea.textcontent.append("technologies, and biotechnologies will be essential to seize the opportunities and meet")
    thisalinea.textcontent.append("the objectives of the green and digital transitions, thus promoting the competitiveness")
    thisalinea.textcontent.append("of the European industry and its sustainability. Therefore, immediate action is required")
    thisalinea.textcontent.append("to support the development or manufacturing in the Union of such technologies,")
    thisalinea.textcontent.append("safeguarding and strengthening their value chains thereby reducing the Union’s")
    thisalinea.textcontent.append("strategic dependencies, and addressing existing labour and skills shortages in those")
    thisalinea.textcontent.append("sectors through trainings and apprenticeships and the creation of attractive, quality")
    thisalinea.textcontent.append("jobs accessible to all.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(4) There is a need to support critical technologies in the following fields: deep and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 76
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) There is a need to support critical technologies in the following fields: deep and digital technologies, clean technologies, and biotechnologies (including the respective critical raw materials value chains), in particular projects, companies and sectors with a critical role for EU’s competitiveness and resilience and its value chains. By way of example, deep technologies and digital technologies should include microelectronics, high-performance computing, quantum technologies (i.e., computing, communication and sensing technologies), cloud computing, edge computing, and artificial intelligence, cybersecurity technologies, robotics, 5G and advanced connectivity and virtual realities, including actions related to deep and digital technologies for the development of defence "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) There is a need to support critical technologies in the following fields: deep and digital")
    thisalinea.textcontent.append("technologies, clean technologies, and biotechnologies (including the respective critical")
    thisalinea.textcontent.append("raw materials value chains), in particular projects, companies and sectors with a")
    thisalinea.textcontent.append("critical role for EU’s competitiveness and resilience and its value chains. By way of")
    thisalinea.textcontent.append("example, deep technologies and digital technologies should include microelectronics,")
    thisalinea.textcontent.append("high-performance computing, quantum technologies (i.e., computing, communication")
    thisalinea.textcontent.append("and sensing technologies), cloud computing, edge computing, and artificial")
    thisalinea.textcontent.append("intelligence, cybersecurity technologies, robotics, 5G and advanced connectivity and")
    thisalinea.textcontent.append("virtual realities, including actions related to deep and digital technologies for the")
    thisalinea.textcontent.append("development of defence and aerospace applications. Clean technologies should")
    thisalinea.textcontent.append("include, among others, renewable energy; electricity and heat storage; heat pumps;")
    thisalinea.textcontent.append("electricity grid; renewable fuels of non-biological origin; sustainable alternative fuels;")
    thisalinea.textcontent.append("electrolysers and fuel cells; carbon capture, utilisation and storage; energy efficiency;")
    thisalinea.textcontent.append("hydrogen and its related infratructure; smart energy solutions; technologies vital to")
    thisalinea.textcontent.append("sustainability such as water purification and desalination; advanced materials such as")
    thisalinea.textcontent.append("nanomaterials, composites and future clean construction materials, and technologies")
    thisalinea.textcontent.append("for the sustainable extraction and processing of critical raw materials. Biotechnology")
    thisalinea.textcontent.append("should be considered to include technologies such as biomolecules and its")
    thisalinea.textcontent.append("applications, pharmaceuticals and medical technologies vital for health security, crop")
    thisalinea.textcontent.append("biotechnology, and industrial biotechnology, such as for waste disposal, and")
    thisalinea.textcontent.append("biomanufacturing. The Commission may issue guidance to further specify the scope of")
    thisalinea.textcontent.append("the technologies in these three fields considered to be critical in accordance with this")
    thisalinea.textcontent.append("Regulation, in order to promote a common interpretation of the projects, companies")
    thisalinea.textcontent.append("and sectors to be supported under the respective programmes in light of the common")
    thisalinea.textcontent.append("strategic objective. Moreover, technologies in any of these three fields which are")
    thisalinea.textcontent.append("subjects of an Important Project of Common European Interest (IPCEI) approved by")
    thisalinea.textcontent.append("the Commission pursuant to Article 107(3), point (b) TFEU should be deemed to be")
    thisalinea.textcontent.append("critical, and individual projects within the scope of such an IPCEI should be eligible")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(5) Strengthening the manufacturing capacity of key technologies in the Union will not be ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 77
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) Strengthening the manufacturing capacity of key technologies in the Union will not be possible without a sizeable skilled workforce. However, labour and skills shortages have increased in all sectors including those considered key for the green and digital transition and endanger the rise of key technologies, also in the context of demographic change. Therefore, it is necessary to boost the activation of more people to the labour market relevant for strategic sectors, in particular through the creation of jobs and apprenticeships for young, disadvantaged persons, in particular, young people not in employment, education or training. Such support will complement "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) Strengthening the manufacturing capacity of key technologies in the Union will not be")
    thisalinea.textcontent.append("possible without a sizeable skilled workforce. However, labour and skills shortages")
    thisalinea.textcontent.append("have increased in all sectors including those considered key for the green and digital")
    thisalinea.textcontent.append("transition and endanger the rise of key technologies, also in the context of")
    thisalinea.textcontent.append("demographic change. Therefore, it is necessary to boost the activation of more people")
    thisalinea.textcontent.append("to the labour market relevant for strategic sectors, in particular through the creation of")
    thisalinea.textcontent.append("jobs and apprenticeships for young, disadvantaged persons, in particular, young people")
    thisalinea.textcontent.append("not in employment, education or training. Such support will complement a number of")
    thisalinea.textcontent.append("other actions aimed at meeting the skills needs stemming from the transition, outlined")
    thisalinea.textcontent.append("in the EU Skills Agenda.45")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(6) The scale of investments needed for the transition require a full mobilisation of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 78
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(6) The scale of investments needed for the transition require a full mobilisation of funding available under existing EU programmes and funds, inclusive those granting a budgetary guarantee for financing and investment operations and implementation of financial instruments and blending operations. Such funding should be deployed in a more flexible manner, to provide timely and targeted support for critical technologies in strategic sectors. Therefore, a Strategic Technologies for Europe Platform (‘STEP’) should give a structural answer to the Union investment needs by helping to better channel the existing EU funds towards critical investments aimed at supporting the development or manufacturing "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(6) The scale of investments needed for the transition require a full mobilisation of")
    thisalinea.textcontent.append("funding available under existing EU programmes and funds, inclusive those granting a")
    thisalinea.textcontent.append("budgetary guarantee for financing and investment operations and implementation of")
    thisalinea.textcontent.append("financial instruments and blending operations. Such funding should be deployed in a")
    thisalinea.textcontent.append("more flexible manner, to provide timely and targeted support for critical technologies")
    thisalinea.textcontent.append("in strategic sectors. Therefore, a Strategic Technologies for Europe Platform (‘STEP’)")
    thisalinea.textcontent.append("should give a structural answer to the Union investment needs by helping to better")
    thisalinea.textcontent.append("channel the existing EU funds towards critical investments aimed at supporting the")
    thisalinea.textcontent.append("development or manufacturing of critical technologies, while preserving a level")
    thisalinea.textcontent.append("playing field in the Single Market, thereby preserving cohesion and aiming at a")
    thisalinea.textcontent.append("geographically balanced distribution of projects financed under the STEP in")
    thisalinea.textcontent.append("accordance with the respective programme mandates.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(7) The STEP should identify resources which should be implemented within the existing ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 79
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(7) The STEP should identify resources which should be implemented within the existing Union programmes and funds, the InvestEU, Horizon Europe, European Defence Fund and Innovation Fund. This should be accompanied by providing additional funding of EUR 10 billion. Of this, EUR 5 billion should be used to increase the endowment of the Innovation Fund46 and EUR 3 billion to increase the total amount of the EU guarantee available for the EU compartment under the InvestEU Regulation to EUR 7,5 billion,47 taking into account the relevant provisioning rate. EUR 0.5 billion should be made available to increase the financial envelope "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(7) The STEP should identify resources which should be implemented within the existing")
    thisalinea.textcontent.append("Union programmes and funds, the InvestEU, Horizon Europe, European Defence Fund")
    thisalinea.textcontent.append("and Innovation Fund. This should be accompanied by providing additional funding of")
    thisalinea.textcontent.append("EUR 10 billion. Of this, EUR 5 billion should be used to increase the endowment of")
    thisalinea.textcontent.append("the Innovation Fund46 and EUR 3 billion to increase the total amount of the EU")
    thisalinea.textcontent.append("guarantee available for the EU compartment under the InvestEU Regulation to EUR")
    thisalinea.textcontent.append("7,5 billion,47 taking into account the relevant provisioning rate. EUR 0.5 billion should")
    thisalinea.textcontent.append("be made available to increase the financial envelope under the Horizon Europe")
    thisalinea.textcontent.append("Regulation,48 which should be amended accordingly; and EUR 1.5 billion to the")
    thisalinea.textcontent.append("European Defence Fund.49")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(8) A Sovereignty Seal should be awarded to projects contributing to the STEP objectives, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 80
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "(8) A Sovereignty Seal should be awarded to projects contributing to the STEP objectives, provided that the project has been assessed and complies with the minimum quality requirements, in particular eligibility, exclusion and award criteria, provided by a call for proposals under Horizon Europe, the Digital Europe programme,50 the EU4Health "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(8) A Sovereignty Seal should be awarded to projects contributing to the STEP objectives,")
    thisalinea.textcontent.append("provided that the project has been assessed and complies with the minimum quality")
    thisalinea.textcontent.append("requirements, in particular eligibility, exclusion and award criteria, provided by a call")
    thisalinea.textcontent.append("for proposals under Horizon Europe, the Digital Europe programme,50 the EU4Health")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(9) To that end, it should be possible to rely on assessments made for the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 81
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "(9) To that end, it should be possible to rely on assessments made for the purposes of other Union programmes in accordance with Articles 126 and 127 of Regulation (EU, Euratom) 2018/1046,52 in order to reduce administrative burden for beneficiaries of Union funds and encourage investment in priority technologies. Provided they comply with the provisions of the RRF Regulation,53 Member States should consider including actions awarded the Sovereignty Seal when preparing their recovery and resilience plans and when proposing their Recovering and Resilience Plans and when deciding on investment projects to be financed from its share of the Modernisation Fund. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(9) To that end, it should be possible to rely on assessments made for the purposes of")
    thisalinea.textcontent.append("other Union programmes in accordance with Articles 126 and 127 of Regulation (EU,")
    thisalinea.textcontent.append("Euratom) 2018/1046,52 in order to reduce administrative burden for beneficiaries of")
    thisalinea.textcontent.append("Union funds and encourage investment in priority technologies. Provided they comply")
    thisalinea.textcontent.append("with the provisions of the RRF Regulation,53 Member States should consider including")
    thisalinea.textcontent.append("actions awarded the Sovereignty Seal when preparing their recovery and resilience")
    thisalinea.textcontent.append("plans and when proposing their Recovering and Resilience Plans and when deciding")
    thisalinea.textcontent.append("on investment projects to be financed from its share of the Modernisation Fund. The")
    thisalinea.textcontent.append("Sovereignty Seal should also be taken into account by the Commission in the context")
    thisalinea.textcontent.append("of the procedure provided for in Article 19 of the EIB Statute and of the policy check")
    thisalinea.textcontent.append("laid down in Article 23 of the InvestEU Regulation. In addition, the implementing")
    thisalinea.textcontent.append("partners should be required to examine projects having been awarded the Sovereignty")
    thisalinea.textcontent.append("Seal in case they fall within their geographic and activity scope in accordance with")
    thisalinea.textcontent.append("Article 26(5) of that Regulation. Authorities in charge of programmes falling under")
    thisalinea.textcontent.append("STEP should also be encouraged to consider support for strategic projects identified in")
    thisalinea.textcontent.append("accordance with the Net Zero Industry and the Critical Raw Materials Acts that are")
    thisalinea.textcontent.append("within the scope of Article 2 of the Regulation and for which rules on cumulative")
    thisalinea.textcontent.append("funding may apply.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(10) A new publicly available website (the ‘Sovereignty Portal’) should be set up by the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 82
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "(10) A new publicly available website (the ‘Sovereignty Portal’) should be set up by the Commission to provide information on available support to companies and project promoters seeking funds for STEP investments. To that end, it should display in an accessible and user-friendly manner the funding opportunities for STEP investments available under the EU budget. This should include information about directly managed programmes, such as Horizon Europe, the Digital Europe programme, the EU4Health programme, and the Innovation Fund, and also other programmes such as InvestEU, the RRF, and cohesion policy funds. Moreover, the Sovereignty Portal should help increase the visibility "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(10) A new publicly available website (the ‘Sovereignty Portal’) should be set up by the")
    thisalinea.textcontent.append("Commission to provide information on available support to companies and project")
    thisalinea.textcontent.append("promoters seeking funds for STEP investments. To that end, it should display in an")
    thisalinea.textcontent.append("accessible and user-friendly manner the funding opportunities for STEP investments")
    thisalinea.textcontent.append("available under the EU budget. This should include information about directly")
    thisalinea.textcontent.append("managed programmes, such as Horizon Europe, the Digital Europe programme, the")
    thisalinea.textcontent.append("EU4Health programme, and the Innovation Fund, and also other programmes such as")
    thisalinea.textcontent.append("InvestEU, the RRF, and cohesion policy funds. Moreover, the Sovereignty Portal")
    thisalinea.textcontent.append("should help increase the visibility for STEP investments towards investors, by listing")
    thisalinea.textcontent.append("the projects that have been awarded a Sovereignty Seal. The Portal should also list the")
    thisalinea.textcontent.append("national competent authorities responsible for acting as contact points for the")
    thisalinea.textcontent.append("implementation of the STEP at national level.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(11) While the STEP relies on the reprogramming and reinforcement of existing ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 83
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "(11) While the STEP relies on the reprogramming and reinforcement of existing programmes for supporting strategic investments, it is also an important element for testing the feasibility and preparation of new interventions as a step towards a European Sovereignty Fund. The evaluation in 2025 will assess the relevance of the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(11) While the STEP relies on the reprogramming and reinforcement of existing")
    thisalinea.textcontent.append("programmes for supporting strategic investments, it is also an important element for")
    thisalinea.textcontent.append("testing the feasibility and preparation of new interventions as a step towards a")
    thisalinea.textcontent.append("European Sovereignty Fund. The evaluation in 2025 will assess the relevance of the")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(12) Directive 2003/87/EC54 should be amended to allow for additional financing with a ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 84
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "(12) Directive 2003/87/EC54 should be amended to allow for additional financing with a financial envelope for the period 2024-2027 of EUR 5 billion. The Innovation Fund supports investments in innovative low-carbon technologies, which is a scope that is to be covered by the STEP. The increase in volume of the Innovation Fund should therefore allow to provide financing responding to the objective of supporting the development or manufacturing in the Union of critical clean technologies. In line with the objectives of ensuring cohesion and promoting the Single Market, and in order to support the green transition and the development of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(12) Directive 2003/87/EC54 should be amended to allow for additional financing with a")
    thisalinea.textcontent.append("financial envelope for the period 2024-2027 of EUR 5 billion. The Innovation Fund")
    thisalinea.textcontent.append("supports investments in innovative low-carbon technologies, which is a scope that is to")
    thisalinea.textcontent.append("be covered by the STEP. The increase in volume of the Innovation Fund should")
    thisalinea.textcontent.append("therefore allow to provide financing responding to the objective of supporting the")
    thisalinea.textcontent.append("development or manufacturing in the Union of critical clean technologies. In line with")
    thisalinea.textcontent.append("the objectives of ensuring cohesion and promoting the Single Market, and in order to")
    thisalinea.textcontent.append("support the green transition and the development of clean technologies throughout the")
    thisalinea.textcontent.append("Union, the additional financial envelope should be made available through calls for")
    thisalinea.textcontent.append("proposals open to entities from Member States whose average GDP per capita is")
    thisalinea.textcontent.append("below the EU average of the EU-27 measured in purchasing power standards (PPS)")
    thisalinea.textcontent.append("and calculated on the basis of Union figures for the period 2015-2017.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(13) In order to extend support possibilities for investments aimed at strengthening ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 85
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "(13) In order to extend support possibilities for investments aimed at strengthening industrial development and reinforcement of value chains in strategic sectors, the scope of support from the ERDF should be extended by providing for new specific objectives under the ERDF, without prejudice to the rules on eligibility of expenditure and climate spending as set out in Regulation (EU) 2021/106055 and Regulation (EU) 2021/105856. In strategic sectors, it should also be possible to support productive investments in enterprises other than SMEs, which can make a significant contribution to the development of less developed and transition regions, as well as in "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(13) In order to extend support possibilities for investments aimed at strengthening")
    thisalinea.textcontent.append("industrial development and reinforcement of value chains in strategic sectors, the")
    thisalinea.textcontent.append("scope of support from the ERDF should be extended by providing for new specific")
    thisalinea.textcontent.append("objectives under the ERDF, without prejudice to the rules on eligibility of expenditure")
    thisalinea.textcontent.append("and climate spending as set out in Regulation (EU) 2021/106055 and Regulation (EU)")
    thisalinea.textcontent.append("2021/105856. In strategic sectors, it should also be possible to support productive")
    thisalinea.textcontent.append("investments in enterprises other than SMEs, which can make a significant contribution")
    thisalinea.textcontent.append("to the development of less developed and transition regions, as well as in more")
    thisalinea.textcontent.append("developed regions of Member States with a GDP per capita below the EU average.")
    thisalinea.textcontent.append("Managing authorities are encouraged to promote the collaboration between large")
    thisalinea.textcontent.append("enterprises and local SMEs, supply chains, innovation and technology ecosystems.")
    thisalinea.textcontent.append("This would allow reinforcing Europe’s overall capacity to strengthen its position in")
    thisalinea.textcontent.append("those sectors through providing access to all Member States for such investments, thus")
    thisalinea.textcontent.append("counteracting the risk of increasing disparities.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(14) The scope of support of the JTF, laid down in Regulation (EU) 2021/1056,57 should ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 86
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "(14) The scope of support of the JTF, laid down in Regulation (EU) 2021/1056,57 should also be extended to cover investments in clean technologies contributing to the objectives of the STEP by large enterprises, provided that they are compatible with the expected contribution to the transition to climate neutrality as set out in the territorial just transition plans. The support provided for such investments should not require a revision of the territorial just transition plan where that revision would be exclusively linked to the gap analysis justifying the investment from the perspective of job creation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(14) The scope of support of the JTF, laid down in Regulation (EU) 2021/1056,57 should")
    thisalinea.textcontent.append("also be extended to cover investments in clean technologies contributing to the")
    thisalinea.textcontent.append("objectives of the STEP by large enterprises, provided that they are compatible with the")
    thisalinea.textcontent.append("expected contribution to the transition to climate neutrality as set out in the territorial")
    thisalinea.textcontent.append("just transition plans. The support provided for such investments should not require a")
    thisalinea.textcontent.append("revision of the territorial just transition plan where that revision would be exclusively")
    thisalinea.textcontent.append("linked to the gap analysis justifying the investment from the perspective of job")
    thisalinea.textcontent.append("creation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(15) The ESF+,58 being the main EU Fund for investment in people, provides a key ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 87
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "(15) The ESF+,58 being the main EU Fund for investment in people, provides a key contribution to promote the development of skills. In order to facilitate the use of that Fund for the STEP objectives, it should be possible to use the ESF+ to cover "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(15) The ESF+,58 being the main EU Fund for investment in people, provides a key")
    thisalinea.textcontent.append("contribution to promote the development of skills. In order to facilitate the use of that")
    thisalinea.textcontent.append("Fund for the STEP objectives, it should be possible to use the ESF+ to cover")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(16) In order to help accelerate investments and provide immediate liquidity for ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 88
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "(16) In order to help accelerate investments and provide immediate liquidity for investments supporting the STEP objectives under the ERDF, the ESF+59 and the JTF, an additional amount of exceptional pre-financing should be provided in the form of a one-off payment with respect to the priorities dedicated to investments supporting the STEP objectives. The additional pre-financing should apply to the whole of the JTF allocation given the need to accelerate its implementation and the strong links of the JTF to support Member States towards the STEP objectives. The rules applying for those amounts of exceptional pre-financing should be consistent with "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(16) In order to help accelerate investments and provide immediate liquidity for")
    thisalinea.textcontent.append("investments supporting the STEP objectives under the ERDF, the ESF+59 and the JTF,")
    thisalinea.textcontent.append("an additional amount of exceptional pre-financing should be provided in the form of a")
    thisalinea.textcontent.append("one-off payment with respect to the priorities dedicated to investments supporting the")
    thisalinea.textcontent.append("STEP objectives. The additional pre-financing should apply to the whole of the JTF")
    thisalinea.textcontent.append("allocation given the need to accelerate its implementation and the strong links of the")
    thisalinea.textcontent.append("JTF to support Member States towards the STEP objectives. The rules applying for")
    thisalinea.textcontent.append("those amounts of exceptional pre-financing should be consistent with the rules")
    thisalinea.textcontent.append("applicable to pre-financing set out in Regulation (EU) 2021/1060. Moreover, to further")
    thisalinea.textcontent.append("incentivise the uptake of such investments and ensure its faster implementation, the")
    thisalinea.textcontent.append("possibility for an increased EU financing rate of 100% for the STEP priorities should")
    thisalinea.textcontent.append("be available. When implementing the new STEP objectives, managing authorities are")
    thisalinea.textcontent.append("encouraged to apply certain social criteria or promote social positive outcomes, such")
    thisalinea.textcontent.append("as creating apprenticeships and jobs for young disadvantaged persons, in particular")
    thisalinea.textcontent.append("young persons not in employment, education or training, applying the social award")
    thisalinea.textcontent.append("criteria in the Directives on public procurement when a project is implemented by a")
    thisalinea.textcontent.append("body subject to public procurement, and paying the applicable wages as agreed")
    thisalinea.textcontent.append("through collective bargaining.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(17) The Common Provisions Regulation60 should be amended to allow that projects ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 89
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = "(17) The Common Provisions Regulation60 should be amended to allow that projects having been awarded a Sovereignty Seal could benefit from better access to EU funding, notably by facilitating cumulative or combined funding from several Union instruments. To that end, it should be possible for managing authorities to grant support from the ERDF or the ESF+ directly, for operations attributed a Sovereignty Seal. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(17) The Common Provisions Regulation60 should be amended to allow that projects")
    thisalinea.textcontent.append("having been awarded a Sovereignty Seal could benefit from better access to EU")
    thisalinea.textcontent.append("funding, notably by facilitating cumulative or combined funding from several Union")
    thisalinea.textcontent.append("instruments. To that end, it should be possible for managing authorities to grant")
    thisalinea.textcontent.append("support from the ERDF or the ESF+ directly, for operations attributed a Sovereignty")
    thisalinea.textcontent.append("Seal.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(18) The regulatory framework for the implementation of the 2014-2020 programmes has ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 90
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "(18) The regulatory framework for the implementation of the 2014-2020 programmes has been adapted over the past years to provide Member States and regions with additional with additional flexibility in terms of implementation rules and more liquidity to tackle the effects of the COVID-19 pandemic and the war or aggression against Ukraine. These measures, introduced at the end of the programming period, require sufficient time and administrative resources to be fully exploited and implemented; also at a time where Member States will focus resources on revising the 2021-2027 operational programmes linked to the STEP objectives. With a view to alleviate "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(18) The regulatory framework for the implementation of the 2014-2020 programmes has")
    thisalinea.textcontent.append("been adapted over the past years to provide Member States and regions with additional")
    thisalinea.textcontent.append("with additional flexibility in terms of implementation rules and more liquidity to tackle")
    thisalinea.textcontent.append("the effects of the COVID-19 pandemic and the war or aggression against Ukraine.")
    thisalinea.textcontent.append("These measures, introduced at the end of the programming period, require sufficient")
    thisalinea.textcontent.append("time and administrative resources to be fully exploited and implemented; also at a time")
    thisalinea.textcontent.append("where Member States will focus resources on revising the 2021-2027 operational")
    thisalinea.textcontent.append("programmes linked to the STEP objectives. With a view to alleviate the administrative")
    thisalinea.textcontent.append("burden on programme authorities and to prevent possible loss of funds at closure for")
    thisalinea.textcontent.append("purely administrative reasons, the deadlines for the administrative closure of the")
    thisalinea.textcontent.append("programmes under the 2014-2020 period should be extended in Regulation (EU) No")
    thisalinea.textcontent.append("1303/201361 and Regulation (EU) No 223/201462. More specifically, the deadline for")
    thisalinea.textcontent.append("the submission of that final payment application should be extended by 12 months.")
    thisalinea.textcontent.append("Furthermore, the deadline for the submission of the closure documents should also be")
    thisalinea.textcontent.append("extended by 12 months. In the context of this amendment, it is appropriate to clarify")
    thisalinea.textcontent.append("that distribution of food and material bought until the end of the eligibility period")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(19) InvestEU is the EU flagship programme to boost investment, especially the green and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 91
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "(19) InvestEU is the EU flagship programme to boost investment, especially the green and digital transition, by providing demand-driven financing, including through blending mechanisms, and technical assistance. Such approach contributes to crowd in additional public and private capital. Given the high market demand of InvestEU guarantee, the EU compartment of InvestEU should be reinforced to correspond to the objectives of the STEP. This will, among other things, reinforce InvestEU’s existing possibility to invest in projects forming part of an IPCEI, within the identified critical technology sectors. In addition, Member States are encouraged to contribute to the InvestEU Member State compartment "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(19) InvestEU is the EU flagship programme to boost investment, especially the green and")
    thisalinea.textcontent.append("digital transition, by providing demand-driven financing, including through blending")
    thisalinea.textcontent.append("mechanisms, and technical assistance. Such approach contributes to crowd in")
    thisalinea.textcontent.append("additional public and private capital. Given the high market demand of InvestEU")
    thisalinea.textcontent.append("guarantee, the EU compartment of InvestEU should be reinforced to correspond to the")
    thisalinea.textcontent.append("objectives of the STEP. This will, among other things, reinforce InvestEU’s existing")
    thisalinea.textcontent.append("possibility to invest in projects forming part of an IPCEI, within the identified critical")
    thisalinea.textcontent.append("technology sectors. In addition, Member States are encouraged to contribute to the")
    thisalinea.textcontent.append("InvestEU Member State compartment to support financial products in line with the")
    thisalinea.textcontent.append("STEP objectives, without prejudice to applicable State aid rules. It should be possible")
    thisalinea.textcontent.append("for Member States to include as a measure in their recovery and resilience plans a cash")
    thisalinea.textcontent.append("contribution for the purpose of the Member State compartment of InvestEU to support")
    thisalinea.textcontent.append("objectives of the STEP. That additional contribution to support objectives of the STEP")
    thisalinea.textcontent.append("could reach up to 6% of their recovery and resilience plan’s total financial allocation")
    thisalinea.textcontent.append("to the Member State compartment of InvestEU. Additional flexibility and")
    thisalinea.textcontent.append("clarifications should also be introduced to better pursue the objectives of the STEP.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(20) Horizon Europe is the EU’s key funding programme for research and innovation, and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 92
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = "(20) Horizon Europe is the EU’s key funding programme for research and innovation, and its European Innovation Council (EIC) provides for support for innovations with potential breakthrough and disruptive nature with scale-up potential that may be too risky for private investors. Additional flexibility should be provided for under Horizon Europe, so that the EIC Accelerator can provide equity-only support to non-bankable SMEs, including start-ups, and non-bankable SMEs and small mid-caps, carrying out innovation in the technologies supported by the STEP and regardless of whether they previously received other types of support from the EIC Accelerator. The implementation of the EIC "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(20) Horizon Europe is the EU’s key funding programme for research and innovation, and")
    thisalinea.textcontent.append("its European Innovation Council (EIC) provides for support for innovations with")
    thisalinea.textcontent.append("potential breakthrough and disruptive nature with scale-up potential that may be too")
    thisalinea.textcontent.append("risky for private investors. Additional flexibility should be provided for under Horizon")
    thisalinea.textcontent.append("Europe, so that the EIC Accelerator can provide equity-only support to non-bankable")
    thisalinea.textcontent.append("SMEs, including start-ups, and non-bankable SMEs and small mid-caps, carrying out")
    thisalinea.textcontent.append("innovation in the technologies supported by the STEP and regardless of whether they")
    thisalinea.textcontent.append("previously received other types of support from the EIC Accelerator. The")
    thisalinea.textcontent.append("implementation of the EIC Fund is currently limited to a maximum investment amount")
    thisalinea.textcontent.append("of EUR 15 million except in exceptional cases and cannot accommodate follow-on")
    thisalinea.textcontent.append("financing rounds or larger investment amounts. Allowing for equity-only support for")
    thisalinea.textcontent.append("non-bankable SMEs and small mid-caps would address the existing market gap with")
    thisalinea.textcontent.append("investments needs in the range of EUR 15 to 50 million. Moreover, experience has")
    thisalinea.textcontent.append("shown that the amounts committed for the EIC Pilot under Horizon2020 are not fully")
    thisalinea.textcontent.append("used. These unused funds should be made available for the purposes of the EIC")
    thisalinea.textcontent.append("Accelerator under Horizon Europe. The Horizon Europe Regulation should also be")
    thisalinea.textcontent.append("amended to reflect the increased envelope for the European Defence Fund.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(21) The European Defence Fund is the leading programme for enhancing the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 93
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "(21) The European Defence Fund is the leading programme for enhancing the competitiveness, innovation, efficiency and technological autonomy of the Union’s defence industry, thereby contributing to the Union’s open strategic autonomy. The development of defence capabilities is crucial, as it underpins the capacity and the autonomy of the European industry to develop defence products and the independence of Member States as the end-users of such products. The additional envelope should therefore be made available to support actions in the field of deep and digital technologies contributing to the development of defence applications. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(21) The European Defence Fund is the leading programme for enhancing the")
    thisalinea.textcontent.append("competitiveness, innovation, efficiency and technological autonomy of the Union’s")
    thisalinea.textcontent.append("defence industry, thereby contributing to the Union’s open strategic autonomy. The")
    thisalinea.textcontent.append("development of defence capabilities is crucial, as it underpins the capacity and the")
    thisalinea.textcontent.append("autonomy of the European industry to develop defence products and the independence")
    thisalinea.textcontent.append("of Member States as the end-users of such products. The additional envelope should")
    thisalinea.textcontent.append("therefore be made available to support actions in the field of deep and digital")
    thisalinea.textcontent.append("technologies contributing to the development of defence applications.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(22) Since the objectives of this Regulation, namely to strengthen European sovereignty, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 94
    thisalinea.parentID = 72
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "(22) Since the objectives of this Regulation, namely to strengthen European sovereignty, accelerate the Union’s green and digital transitions and enhance its competitiveness, and reduce its strategic dependencies cannot be sufficiently achieved by the Member States, but can rather be better achieved at Union level, the Union may adopt measures in accordance with the principle of subsidiarity as set out in Article 5 of the Treaty on European Union. In accordance with the principle of proportionality as set out in that Article, this Regulation does not go beyond what is necessary to achieve those objectives. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(22) Since the objectives of this Regulation, namely to strengthen European sovereignty,")
    thisalinea.textcontent.append("accelerate the Union’s green and digital transitions and enhance its competitiveness,")
    thisalinea.textcontent.append("and reduce its strategic dependencies cannot be sufficiently achieved by the Member")
    thisalinea.textcontent.append("States, but can rather be better achieved at Union level, the Union may adopt measures")
    thisalinea.textcontent.append("in accordance with the principle of subsidiarity as set out in Article 5 of the Treaty on")
    thisalinea.textcontent.append("European Union. In accordance with the principle of proportionality as set out in that")
    thisalinea.textcontent.append("Article, this Regulation does not go beyond what is necessary to achieve those")
    thisalinea.textcontent.append("objectives.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "CHAPTER 1 STEP"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 95
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 1 Subject matter"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 96
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "This Regulation establishes a Strategic Technologies for Europe Platform (‘STEP’ or ‘the Platform’) to support critical and emerging strategic technologies . It lays down the objectives of the Platform, the amount of financial support available under the Platform, and rules for the implementation of the Sovereignty Seal and Sovereignty portal and for reporting on the Platform objectives. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Regulation establishes a Strategic Technologies for Europe Platform (‘STEP’ or ‘the")
    thisalinea.textcontent.append("Platform’) to support critical and emerging strategic technologies .")
    thisalinea.textcontent.append("It lays down the objectives of the Platform, the amount of financial support available under")
    thisalinea.textcontent.append("the Platform, and rules for the implementation of the Sovereignty Seal and Sovereignty portal")
    thisalinea.textcontent.append("and for reporting on the Platform objectives.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 2 STEP objectives"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 97
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "29 technology fields referred to in point (a) of paragraph 1, the relevant technologies shall be deemed to be critical. 1. To strengthen European sovereignty and security, accelerate the Union’s green and digital transitions and enhance its competitiveness, reduce its strategic dependencies, favour a level playing field in the Single Market for investments throughout the Union, and promote inclusive access to attractive, quality jobs, the Platform shall pursue the following objectives: (a) supporting the development or manufacturing throughout the Union, or safeguarding and strengthening the respective value chains, of critical technologies in the following fields: (i) deep and digital technologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("29")
    thisalinea.textcontent.append("technology fields referred to in point (a) of paragraph 1, the relevant technologies")
    thisalinea.textcontent.append("shall be deemed to be critical.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "1. To strengthen European sovereignty and security, accelerate the Union’s green and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 98
    thisalinea.parentID = 97
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. To strengthen European sovereignty and security, accelerate the Union’s green and digital transitions and enhance its competitiveness, reduce its strategic dependencies, favour a level playing field in the Single Market for investments throughout the Union, and promote inclusive access to attractive, quality jobs, the Platform shall pursue the following objectives: (a) supporting the development or manufacturing throughout the Union, or safeguarding and strengthening the respective value chains, of critical technologies in the following fields: (i) deep and digital technologies (ii) clean technologies (iii) biotechnologies (b) addressing shortages of labour and skills critical to all kinds of quality jobs in "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. To strengthen European sovereignty and security, accelerate the Union’s green and")
    thisalinea.textcontent.append("digital transitions and enhance its competitiveness, reduce its strategic dependencies,")
    thisalinea.textcontent.append("favour a level playing field in the Single Market for investments throughout the")
    thisalinea.textcontent.append("Union, and promote inclusive access to attractive, quality jobs, the Platform shall")
    thisalinea.textcontent.append("pursue the following objectives:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(a) supporting the development or manufacturing throughout the Union, or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 99
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) supporting the development or manufacturing throughout the Union, or safeguarding and strengthening the respective value chains, of critical technologies in the following fields: (i) deep and digital technologies (ii) clean technologies (iii) biotechnologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) supporting the development or manufacturing throughout the Union, or")
    thisalinea.textcontent.append("safeguarding and strengthening the respective value chains, of critical")
    thisalinea.textcontent.append("technologies in the following fields:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "(i) deep and digital technologies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 100
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) deep and digital technologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) deep and digital technologies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "(ii) clean technologies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 101
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) clean technologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) clean technologies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 6
    thisalinea.texttitle = "(iii) biotechnologies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 102
    thisalinea.parentID = 99
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(iii) biotechnologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iii) biotechnologies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(b) addressing shortages of labour and skills critical to all kinds of quality jobs in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 103
    thisalinea.parentID = 98
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) addressing shortages of labour and skills critical to all kinds of quality jobs in support of the objective under point (a). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) addressing shortages of labour and skills critical to all kinds of quality jobs in")
    thisalinea.textcontent.append("support of the objective under point (a).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2. The technologies referred to in point (a) of the first paragraph, shall be deemed ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 104
    thisalinea.parentID = 97
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The technologies referred to in point (a) of the first paragraph, shall be deemed to be critical where they meet at least one of the following conditions: (a) bring an innovative, cutting-edge element with significant economic potential to the Single Market; (b) contribute to reduce or prevent strategic dependencies of the Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The technologies referred to in point (a) of the first paragraph, shall be deemed to be")
    thisalinea.textcontent.append("critical where they meet at least one of the following conditions:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(a) bring an innovative, cutting-edge element with significant economic potential ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 105
    thisalinea.parentID = 104
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) bring an innovative, cutting-edge element with significant economic potential to the Single Market; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) bring an innovative, cutting-edge element with significant economic potential")
    thisalinea.textcontent.append("to the Single Market;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(b) contribute to reduce or prevent strategic dependencies of the Union. "
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 106
    thisalinea.parentID = 104
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) contribute to reduce or prevent strategic dependencies of the Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) contribute to reduce or prevent strategic dependencies of the Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3. Where an Important Project of Common European Interest (IPCEI) approved by the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 107
    thisalinea.parentID = 97
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Where an Important Project of Common European Interest (IPCEI) approved by the Commission pursuant to Article 107(3), point (b) TFEU relates to any of the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Where an Important Project of Common European Interest (IPCEI) approved by the")
    thisalinea.textcontent.append("Commission pursuant to Article 107(3), point (b) TFEU relates to any of the")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4. The value chain for the manufacturing of critical technologies referred to in the first ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 108
    thisalinea.parentID = 97
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. The value chain for the manufacturing of critical technologies referred to in the first paragraph relates to final products, as well as key components, specific machinery and critical raw materials primarily used for the production of those products. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. The value chain for the manufacturing of critical technologies referred to in the first")
    thisalinea.textcontent.append("paragraph relates to final products, as well as key components, specific machinery")
    thisalinea.textcontent.append("and critical raw materials primarily used for the production of those products.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "1. Implementation of the Platform shall be supported, in particular, through: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 109
    thisalinea.parentID = 97
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "1. Implementation of the Platform shall be supported, in particular, through: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Implementation of the Platform shall be supported, in particular, through:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 3 Financial Support"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 110
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "(a) a Union guarantee referred to in Article 4(1) of Regulation (EU) 2021/523 with the indicative amount of EUR 7 500 000 000 That guarantee shall be implemented in accordance with Regulation (EU) 2021/523; (b) an amount of EUR 500 000 000 in current prices of the financial envelope referred to in point (i) of Article 12(2)(c) of Regulation (EU) 2021/695. That amount shall be implemented in accordance with Regulation (EU) 2021/695; (c) an amount of EUR 5 000 000 000 in current prices of the financial envelope referred to in the sixth subparagraph of Article 10a(8) of Directive 2003/87/EC. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(a) a Union guarantee referred to in Article 4(1) of Regulation (EU) 2021/523 with ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 111
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) a Union guarantee referred to in Article 4(1) of Regulation (EU) 2021/523 with the indicative amount of EUR 7 500 000 000 That guarantee shall be implemented in accordance with Regulation (EU) 2021/523; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) a Union guarantee referred to in Article 4(1) of Regulation (EU) 2021/523 with")
    thisalinea.textcontent.append("the indicative amount of EUR 7 500 000 000 That guarantee shall be")
    thisalinea.textcontent.append("implemented in accordance with Regulation (EU) 2021/523;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(b) an amount of EUR 500 000 000 in current prices of the financial envelope ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 112
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) an amount of EUR 500 000 000 in current prices of the financial envelope referred to in point (i) of Article 12(2)(c) of Regulation (EU) 2021/695. That amount shall be implemented in accordance with Regulation (EU) 2021/695; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) an amount of EUR 500 000 000 in current prices of the financial envelope")
    thisalinea.textcontent.append("referred to in point (i) of Article 12(2)(c) of Regulation (EU) 2021/695. That")
    thisalinea.textcontent.append("amount shall be implemented in accordance with Regulation (EU) 2021/695;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(c) an amount of EUR 5 000 000 000 in current prices of the financial ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 113
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) an amount of EUR 5 000 000 000 in current prices of the financial envelope referred to in the sixth subparagraph of Article 10a(8) of Directive 2003/87/EC. That amount shall be implemented within the Innovation Fund in accordance with the rules of Article 10a(8) of Directive 2003/87/EC and Commission Delegated Regulation [2019/856]. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) an amount of EUR 5 000 000 000 in current prices of the financial envelope")
    thisalinea.textcontent.append("referred to in the sixth subparagraph of Article 10a(8) of Directive 2003/87/EC.")
    thisalinea.textcontent.append("That amount shall be implemented within the Innovation Fund in accordance")
    thisalinea.textcontent.append("with the rules of Article 10a(8) of Directive 2003/87/EC and Commission")
    thisalinea.textcontent.append("Delegated Regulation [2019/856].")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(d) An amount of EUR 1 500 000 000 in current prices of the financial ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 114
    thisalinea.parentID = 110
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) An amount of EUR 1 500 000 000 in current prices of the financial envelope refered to in Article 4(1) of Regulation (EU) 2021/697. That amount shall be implemented in accordance with Regulation (EU) 2021/697. 2. The amounts referred to in the paragraph 1 shall be used with the aim of achieving the objectives referred to in Article 2. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) An amount of EUR 1 500 000 000 in current prices of the financial envelope")
    thisalinea.textcontent.append("refered to in Article 4(1) of Regulation (EU) 2021/697. That amount shall be")
    thisalinea.textcontent.append("implemented in accordance with Regulation (EU) 2021/697.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2. The amounts referred to in the paragraph 1 shall be used with the aim ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 115
    thisalinea.parentID = 114
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "2. The amounts referred to in the paragraph 1 shall be used with the aim of achieving the objectives referred to in Article 2. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The amounts referred to in the paragraph 1 shall be used with the aim of achieving")
    thisalinea.textcontent.append("the objectives referred to in Article 2.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 4 Sovereignty Seal and cumulative funding"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 116
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "30 1. The Commission shall award a Sovereignty Seal to any action contributing to any of the Platform objectives, provided the action has been assessed and complies with the minimum quality requirements, in particular eligibility, exclusion and award criteria, provided by a call for proposals under Regulation (EU) 2021/695, Regulation (EU) 2021/694, Regulation (EU) 2021/697, Regulation (EU) 2021/522, or Commission Delegated Regulation (EU) 2019/856. 2. The Sovereignty Seal may be used as a quality label, in particular for the purposes of: (a) receiving support for the action under another Union fund or programme in accordance with the rules applicable to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("30")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The Commission shall award a Sovereignty Seal to any action contributing to any of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 117
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The Commission shall award a Sovereignty Seal to any action contributing to any of the Platform objectives, provided the action has been assessed and complies with the minimum quality requirements, in particular eligibility, exclusion and award criteria, provided by a call for proposals under Regulation (EU) 2021/695, Regulation (EU) 2021/694, Regulation (EU) 2021/697, Regulation (EU) 2021/522, or Commission Delegated Regulation (EU) 2019/856. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The Commission shall award a Sovereignty Seal to any action contributing to any of")
    thisalinea.textcontent.append("the Platform objectives, provided the action has been assessed and complies with the")
    thisalinea.textcontent.append("minimum quality requirements, in particular eligibility, exclusion and award criteria,")
    thisalinea.textcontent.append("provided by a call for proposals under Regulation (EU) 2021/695, Regulation (EU)")
    thisalinea.textcontent.append("2021/694, Regulation (EU) 2021/697, Regulation (EU) 2021/522, or Commission")
    thisalinea.textcontent.append("Delegated Regulation (EU) 2019/856.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The Sovereignty Seal may be used as a quality label, in particular for the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 118
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The Sovereignty Seal may be used as a quality label, in particular for the purposes of: (a) receiving support for the action under another Union fund or programme in accordance with the rules applicable to that fund or programme, or (b) financing the action through cumulative or combined funding with another Union instrument in line with the rules of the applicable basic acts. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The Sovereignty Seal may be used as a quality label, in particular for the purposes")
    thisalinea.textcontent.append("of:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) receiving support for the action under another Union fund or programme in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 119
    thisalinea.parentID = 118
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) receiving support for the action under another Union fund or programme in accordance with the rules applicable to that fund or programme, or "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) receiving support for the action under another Union fund or programme in")
    thisalinea.textcontent.append("accordance with the rules applicable to that fund or programme, or")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) financing the action through cumulative or combined funding with another ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 120
    thisalinea.parentID = 118
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) financing the action through cumulative or combined funding with another Union instrument in line with the rules of the applicable basic acts. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) financing the action through cumulative or combined funding with another")
    thisalinea.textcontent.append("Union instrument in line with the rules of the applicable basic acts.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. When revising their recovery and resilience plans in accordance with Regulation ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 121
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. When revising their recovery and resilience plans in accordance with Regulation (EU) 2021/241, Member States shall, without prejudice to the provisions of that Regulation, consider as a priority action which have been awarded a Sovereignty Seal in accordance with paragraph 1. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. When revising their recovery and resilience plans in accordance with Regulation")
    thisalinea.textcontent.append("(EU) 2021/241, Member States shall, without prejudice to the provisions of that")
    thisalinea.textcontent.append("Regulation, consider as a priority action which have been awarded a Sovereignty")
    thisalinea.textcontent.append("Seal in accordance with paragraph 1.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. When deciding on investment projects to finance from their respective shares of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 122
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. When deciding on investment projects to finance from their respective shares of the Modernisation Fund in accordance with Article 10d of Directive 2003/87/EC, Member States shall consider as a priority project for critical clean technologies which have received the Sovereignty Seal in accordance with paragraph 1. In addition, Member States may decide to grant national support to projects with a Sovereignty Seal contributing to the Platform objective referred to in Article 2(1), point (a)(ii). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. When deciding on investment projects to finance from their respective shares of the")
    thisalinea.textcontent.append("Modernisation Fund in accordance with Article 10d of Directive 2003/87/EC,")
    thisalinea.textcontent.append("Member States shall consider as a priority project for critical clean technologies")
    thisalinea.textcontent.append("which have received the Sovereignty Seal in accordance with paragraph 1. In")
    thisalinea.textcontent.append("addition, Member States may decide to grant national support to projects with a")
    thisalinea.textcontent.append("Sovereignty Seal contributing to the Platform objective referred to in Article 2(1),")
    thisalinea.textcontent.append("point (a)(ii).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. Under Regulation (EU) 2021/523, the Sovereignty Seal shall be taken into account in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 123
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. Under Regulation (EU) 2021/523, the Sovereignty Seal shall be taken into account in the context of the procedure provided for in Article 19 of the European Investment Bank Statute and of the policy check as laid down in Article 23(3) of that Regulation. In addition, the implementing partners shall examine projects having been awarded the Sovereignty Seal in case they fall within their geographic and activity scope as laid down in Article 26(5) of that Regulation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. Under Regulation (EU) 2021/523, the Sovereignty Seal shall be taken into account in")
    thisalinea.textcontent.append("the context of the procedure provided for in Article 19 of the European Investment")
    thisalinea.textcontent.append("Bank Statute and of the policy check as laid down in Article 23(3) of that Regulation.")
    thisalinea.textcontent.append("In addition, the implementing partners shall examine projects having been awarded")
    thisalinea.textcontent.append("the Sovereignty Seal in case they fall within their geographic and activity scope as")
    thisalinea.textcontent.append("laid down in Article 26(5) of that Regulation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. Strategic projects identified in accordance with the [Net Zero Industry Act] and the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 124
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. Strategic projects identified in accordance with the [Net Zero Industry Act] and the [Critical Raw Materials Act] within the scope of Article 2 that receive a contribution under the Programmes refered to in Article 3 may also receive a contribution from any other Union programme, including Funds under shared management, provided that the contributions do not cover the same costs. The rules of the relevant Union programme shall apply to the corresponding contribution to the strategic project. The cumulative funding shall not exceed the total eligible costs of the strategic project. The support from the different Union programmes may "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. Strategic projects identified in accordance with the [Net Zero Industry Act] and the")
    thisalinea.textcontent.append("[Critical Raw Materials Act] within the scope of Article 2 that receive a contribution")
    thisalinea.textcontent.append("under the Programmes refered to in Article 3 may also receive a contribution from")
    thisalinea.textcontent.append("any other Union programme, including Funds under shared management, provided")
    thisalinea.textcontent.append("that the contributions do not cover the same costs. The rules of the relevant Union")
    thisalinea.textcontent.append("programme shall apply to the corresponding contribution to the strategic project. The")
    thisalinea.textcontent.append("cumulative funding shall not exceed the total eligible costs of the strategic project.")
    thisalinea.textcontent.append("The support from the different Union programmes may be calculated on a pro-rata")
    thisalinea.textcontent.append("basis in accordance with the documents setting out the conditions for support.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "7. The award of a Sovereignty Seal and provision of cumulative funding is without ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 125
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "7. The award of a Sovereignty Seal and provision of cumulative funding is without prejudice to applicable State aid rules and to the Union’s international obligations. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("7. The award of a Sovereignty Seal and provision of cumulative funding is without")
    thisalinea.textcontent.append("prejudice to applicable State aid rules and to the Union’s international obligations.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 5 Monitoring of implementation"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 126
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "1. The Commission shall monitor the implementation of the Platform and measure the achievement of the Platform objectives set out in Article 2. The monitoring of implementation shall be targeted and proportionate to the activities carried out under the Platform. 2. The monitoring system of the Commission shall ensure that data for monitoring the implementation of the activities carried out under the Platform and the results of those activities are collected efficiently, effectively and in a timely manner. 3. The Commission shall report on the expenditure financed by the Platform. It shall, as appropriate, report on the achievements related to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The Commission shall monitor the implementation of the Platform and measure the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 127
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The Commission shall monitor the implementation of the Platform and measure the achievement of the Platform objectives set out in Article 2. The monitoring of implementation shall be targeted and proportionate to the activities carried out under the Platform. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The Commission shall monitor the implementation of the Platform and measure the")
    thisalinea.textcontent.append("achievement of the Platform objectives set out in Article 2. The monitoring of")
    thisalinea.textcontent.append("implementation shall be targeted and proportionate to the activities carried out under")
    thisalinea.textcontent.append("the Platform.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The monitoring system of the Commission shall ensure that data for monitoring the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 128
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The monitoring system of the Commission shall ensure that data for monitoring the implementation of the activities carried out under the Platform and the results of those activities are collected efficiently, effectively and in a timely manner. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The monitoring system of the Commission shall ensure that data for monitoring the")
    thisalinea.textcontent.append("implementation of the activities carried out under the Platform and the results of")
    thisalinea.textcontent.append("those activities are collected efficiently, effectively and in a timely manner.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The Commission shall report on the expenditure financed by the Platform. It shall, as ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 129
    thisalinea.parentID = 126
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The Commission shall report on the expenditure financed by the Platform. It shall, as appropriate, report on the achievements related to each of the specific Platform objectives. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The Commission shall report on the expenditure financed by the Platform. It shall, as")
    thisalinea.textcontent.append("appropriate, report on the achievements related to each of the specific Platform")
    thisalinea.textcontent.append("objectives.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 6 Sovereignty portal"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 130
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "31 1. The Commission shall establish a dedicated publicly available website (the ‘Sovereignty portal’), providing investors with information about funding opportunities for projects linked to the Platform objectives and grant visibility to those projects, in particular by displaying the following information: (a) ongoing and upcoming calls for proposals and calls for tender linked to the Platform objectives under the respective programmes and funds; (b) projects that have been awarded a Sovereignty Seal quality label in accordance with Article 4; (c) projects that have been identified as strategic projects under the [Net-Zero Industry Act] and the [Critical Raw Materials Act], to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("31")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The Commission shall establish a dedicated publicly available website (the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 131
    thisalinea.parentID = 130
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The Commission shall establish a dedicated publicly available website (the ‘Sovereignty portal’), providing investors with information about funding opportunities for projects linked to the Platform objectives and grant visibility to those projects, in particular by displaying the following information: (a) ongoing and upcoming calls for proposals and calls for tender linked to the Platform objectives under the respective programmes and funds; (b) projects that have been awarded a Sovereignty Seal quality label in accordance with Article 4; (c) projects that have been identified as strategic projects under the [Net-Zero Industry Act] and the [Critical Raw Materials Act], to the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The Commission shall establish a dedicated publicly available website (the")
    thisalinea.textcontent.append("‘Sovereignty portal’), providing investors with information about funding")
    thisalinea.textcontent.append("opportunities for projects linked to the Platform objectives and grant visibility to")
    thisalinea.textcontent.append("those projects, in particular by displaying the following information:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) ongoing and upcoming calls for proposals and calls for tender linked to the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 132
    thisalinea.parentID = 131
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) ongoing and upcoming calls for proposals and calls for tender linked to the Platform objectives under the respective programmes and funds; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) ongoing and upcoming calls for proposals and calls for tender linked to the")
    thisalinea.textcontent.append("Platform objectives under the respective programmes and funds;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) projects that have been awarded a Sovereignty Seal quality label in accordance ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 133
    thisalinea.parentID = 131
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) projects that have been awarded a Sovereignty Seal quality label in accordance with Article 4; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) projects that have been awarded a Sovereignty Seal quality label in accordance")
    thisalinea.textcontent.append("with Article 4;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) projects that have been identified as strategic projects under the [Net-Zero ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 134
    thisalinea.parentID = 131
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) projects that have been identified as strategic projects under the [Net-Zero Industry Act] and the [Critical Raw Materials Act], to the extent that they fall within the scope of Article 2; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) projects that have been identified as strategic projects under the [Net-Zero")
    thisalinea.textcontent.append("Industry Act] and the [Critical Raw Materials Act], to the extent that they fall")
    thisalinea.textcontent.append("within the scope of Article 2;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) contacts to the national competent authorities designated in accordance with ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 135
    thisalinea.parentID = 131
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) contacts to the national competent authorities designated in accordance with paragraph 4; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) contacts to the national competent authorities designated in accordance with")
    thisalinea.textcontent.append("paragraph 4;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The Sovereignty portal shall also display information about the implementation of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 136
    thisalinea.parentID = 130
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The Sovereignty portal shall also display information about the implementation of the Platform and in relation to Union budget expenditure as referred to in Article 5, as well as the performance indicators defined under the respective programmes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The Sovereignty portal shall also display information about the implementation of")
    thisalinea.textcontent.append("the Platform and in relation to Union budget expenditure as referred to in Article 5,")
    thisalinea.textcontent.append("as well as the performance indicators defined under the respective programmes.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The Sovereignty portal shall be launched at the [date of the entry into force ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 137
    thisalinea.parentID = 130
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The Sovereignty portal shall be launched at the [date of the entry into force of this Regulation] and shall be updated by the Commission regularly. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The Sovereignty portal shall be launched at the [date of the entry into force of this")
    thisalinea.textcontent.append("Regulation] and shall be updated by the Commission regularly.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. By [3 months after the entry into force of this Regulation], Member State shall ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 138
    thisalinea.parentID = 130
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. By [3 months after the entry into force of this Regulation], Member State shall designate one national competent authority to act as the main point of contact for the implementation of the Platform at national level. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. By [3 months after the entry into force of this Regulation], Member State shall")
    thisalinea.textcontent.append("designate one national competent authority to act as the main point of contact for the")
    thisalinea.textcontent.append("implementation of the Platform at national level.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 7 Annual report"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 139
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "1. The Commission shall provide an annual report to the European Parliament and the Council on the implementation of the Platform. 2. The annual report shall include consolidated information on the progress made in implementing the Platform objectives under each of the programmes and funds. 3. The annual report shall also include the following information: (a) overall expenditure of the STEP financed under the respective programmes; (b) the performance of the STEP based on the performance indicators defined under the respective programmes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The Commission shall provide an annual report to the European Parliament and the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 140
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The Commission shall provide an annual report to the European Parliament and the Council on the implementation of the Platform. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The Commission shall provide an annual report to the European Parliament and the")
    thisalinea.textcontent.append("Council on the implementation of the Platform.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The annual report shall include consolidated information on the progress made in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 141
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The annual report shall include consolidated information on the progress made in implementing the Platform objectives under each of the programmes and funds. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The annual report shall include consolidated information on the progress made in")
    thisalinea.textcontent.append("implementing the Platform objectives under each of the programmes and funds.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The annual report shall also include the following information: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 142
    thisalinea.parentID = 139
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The annual report shall also include the following information: (a) overall expenditure of the STEP financed under the respective programmes; (b) the performance of the STEP based on the performance indicators defined under the respective programmes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The annual report shall also include the following information:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) overall expenditure of the STEP financed under the respective programmes; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 143
    thisalinea.parentID = 142
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) overall expenditure of the STEP financed under the respective programmes; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) overall expenditure of the STEP financed under the respective programmes;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the performance of the STEP based on the performance indicators defined ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 144
    thisalinea.parentID = 142
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the performance of the STEP based on the performance indicators defined under the respective programmes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the performance of the STEP based on the performance indicators defined")
    thisalinea.textcontent.append("under the respective programmes.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 8 Evaluation of the Platform"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 145
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "1. By 31 December 2025, the Commission shall provide the European Parliament and the Council with an evaluation report on the implementation of the Platform. 2. The evaluation report shall, in particular, assess to which extent the objectives have been achieved, the efficiency of the use of the resources and the European added value. It shall also consider the continued relevance of all objectives and actions, in view of their potential upscaling. 3. Where appropriate, the evaluation shall be accompanied by a proposal for amendments of this Regulation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. By 31 December 2025, the Commission shall provide the European Parliament and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 146
    thisalinea.parentID = 145
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. By 31 December 2025, the Commission shall provide the European Parliament and the Council with an evaluation report on the implementation of the Platform. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. By 31 December 2025, the Commission shall provide the European Parliament and")
    thisalinea.textcontent.append("the Council with an evaluation report on the implementation of the Platform.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The evaluation report shall, in particular, assess to which extent the objectives have ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 147
    thisalinea.parentID = 145
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The evaluation report shall, in particular, assess to which extent the objectives have been achieved, the efficiency of the use of the resources and the European added value. It shall also consider the continued relevance of all objectives and actions, in view of their potential upscaling. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The evaluation report shall, in particular, assess to which extent the objectives have")
    thisalinea.textcontent.append("been achieved, the efficiency of the use of the resources and the European added")
    thisalinea.textcontent.append("value. It shall also consider the continued relevance of all objectives and actions, in")
    thisalinea.textcontent.append("view of their potential upscaling.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Where appropriate, the evaluation shall be accompanied by a proposal for ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 148
    thisalinea.parentID = 145
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Where appropriate, the evaluation shall be accompanied by a proposal for amendments of this Regulation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Where appropriate, the evaluation shall be accompanied by a proposal for")
    thisalinea.textcontent.append("amendments of this Regulation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "CHAPTER 2 AMENDMENTS"
    thisalinea.titlefontsize = "15.960000000000008"
    thisalinea.nativeID = 149
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 9 Amendments to Directive 2003/87/EC [ETS]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 150
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "32 Directive 2003/87/EC is amended as follows: ‘In addition to the allowances referred to in the first to fifth subparagraphs of this paragraph, the Innovation Fund shall also implement a financial envelope for the period from 1 January 2024 to 31 December 2027 of EUR 5 000 000 000 in current prices for supporting investments contributing to the STEP objective referred to in Article 2, point (a)(ii) of Regulation .../...63 [STEP Regulation]. This financial envelope shall be made available to support investments only in Member States whose average GDP per capita is below the EU average of the EU-27 measured "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("32")
    thisalinea.textcontent.append("Directive 2003/87/EC is amended as follows:")
    thisalinea.textcontent.append("‘In addition to the allowances referred to in the first to fifth subparagraphs of this")
    thisalinea.textcontent.append("paragraph, the Innovation Fund shall also implement a financial envelope for the")
    thisalinea.textcontent.append("period from 1 January 2024 to 31 December 2027 of EUR 5 000 000 000 in current")
    thisalinea.textcontent.append("prices for supporting investments contributing to the STEP objective referred to in")
    thisalinea.textcontent.append("Article 2, point (a)(ii) of Regulation .../...63 [STEP Regulation]. This financial")
    thisalinea.textcontent.append("envelope shall be made available to support investments only in Member States")
    thisalinea.textcontent.append("whose average GDP per capita is below the EU average of the EU-27 measured in")
    thisalinea.textcontent.append("purchasing power standards (PPS) and calculated on the basis of Union figures for")
    thisalinea.textcontent.append("the period 2015-2017’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) In Article 10a(8), the following sixth subparagraph is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 151
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) In Article 10a(8), the following sixth subparagraph is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) In Article 10a(8), the following sixth subparagraph is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Amendments to Regulation (EU) 2021/1058 [ERDF and CF]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 152
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 10"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 153
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = "Regulation (EU) 2021/1058 is amended as follows: ‘(vi) supporting investments contributing to the STEP objectives referred to in Article 2 of Regulation .../...64 [STEP Regulation]’ ‘(ix) supporting investments contributing to the STEP objective referred to in Article 2(1), point (a)(ii) of Regulation .../... [STEP Regulation]’ The resources under the specific objective referred to in Article 3(1), first subparagraph, points (a)(vi) and (b)(ix) shall be programmed under dedicated priorities corresponding to the respective policy objective. The Commission shall pay 30 % of the ERDF allocation to that priority as set out in the decision approving the programme amendment as exceptional one-off "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/1058 is amended as follows:")
    thisalinea.textcontent.append("‘(vi) supporting investments contributing to the STEP objectives referred to in")
    thisalinea.textcontent.append("Article 2 of Regulation .../...64 [STEP Regulation]’")
    thisalinea.textcontent.append("‘(ix) supporting investments contributing to the STEP objective referred to in Article")
    thisalinea.textcontent.append("2(1), point (a)(ii) of Regulation .../... [STEP Regulation]’")
    thisalinea.textcontent.append("The resources under the specific objective referred to in Article 3(1), first")
    thisalinea.textcontent.append("subparagraph, points (a)(vi) and (b)(ix) shall be programmed under dedicated")
    thisalinea.textcontent.append("priorities corresponding to the respective policy objective.")
    thisalinea.textcontent.append("The Commission shall pay 30 % of the ERDF allocation to that priority as set out in")
    thisalinea.textcontent.append("the decision approving the programme amendment as exceptional one-off pre-")
    thisalinea.textcontent.append("financing in addition to the yearly pre-financing for the programme provided for in")
    thisalinea.textcontent.append("Article 90(1) and (2) of Regulation (EU) 2021/1060 or in Article 51(2), (3) and (4) of")
    thisalinea.textcontent.append("Regulation (EU) 2021/1059. The exceptional pre-financing shall be paid by 31")
    thisalinea.textcontent.append("December 2024, provided the Commission has adopted the decision approving the")
    thisalinea.textcontent.append("programme amendment by 31 October 2024.")
    thisalinea.textcontent.append("In accordance with Article 90 (5) of Regulation (EU) 2021/1060 and Article 51(5) of")
    thisalinea.textcontent.append("Regulation (EU) 2021/1059, the amount paid as exceptional pre-financing shall be")
    thisalinea.textcontent.append("cleared no later than with the final accounting year.")
    thisalinea.textcontent.append("In accordance with Article 90(6) of Regulation (EU) 2021/1060, any interest")
    thisalinea.textcontent.append("generated by the exceptional pre-financing shall be used for the programme")
    thisalinea.textcontent.append("concerned in the same way as the ERDF and shall be included in the accounts for the")
    thisalinea.textcontent.append("final accounting year.")
    thisalinea.textcontent.append("33")
    thisalinea.textcontent.append("In accordance with Article 97(1) of Regulation (EU) 2021/1060, the exceptional pre-")
    thisalinea.textcontent.append("financing shall not be suspended.")
    thisalinea.textcontent.append("In accordance with Article 105 (1) of Regulation (EU) 2021/1060, the pre-financing")
    thisalinea.textcontent.append("to be taken into account for the purposes of calculating amounts to be de-committed")
    thisalinea.textcontent.append("shall include the exceptional pre-financing paid.")
    thisalinea.textcontent.append("By way of derogation from Article 112 of Regulation (EU) 2021/1060, the maximum")
    thisalinea.textcontent.append("co-financing rates for dedicated priorities established to support the STEP objectives")
    thisalinea.textcontent.append("shall be increased to 100 %.’")
    thisalinea.textcontent.append("‘(e) when they contribute to the specific objective under PO 1 set out in Article 3(1),")
    thisalinea.textcontent.append("first subparagraph, point (a)(vi) or to the specific objective under PO 2 set out in")
    thisalinea.textcontent.append("point (b)(ix) of that subparagraph, in less developed and transition regions, as well as")
    thisalinea.textcontent.append("more developed regions in Member States whose average GDP per capita is below")
    thisalinea.textcontent.append("the EU average of the EU-27 measured in purchasing power standards (PPS) and")
    thisalinea.textcontent.append("calculated on the basis of Union figures for the period 2015-2017.")
    thisalinea.textcontent.append("Point (e) shall apply to Interreg programmes where the geographical coverage of the")
    thisalinea.textcontent.append("programme within the Union consists exclusively of categories of regions set out in")
    thisalinea.textcontent.append("that point.’")
    thisalinea.textcontent.append("‘3a. In order to contribute to the specific objectives under PO 1 set out in Article")
    thisalinea.textcontent.append("3(1), first subparagraph, point (a)(vi) and under PO 2 set out in point (b)(ix) of that")
    thisalinea.textcontent.append("subparagraph, the ERDF shall also support training, life-long learning, reskilling and")
    thisalinea.textcontent.append("education activities’.")
    thisalinea.textcontent.append("34")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) In Article 3(1), point (a), the following point is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 154
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) In Article 3(1), point (a), the following point is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) In Article 3(1), point (a), the following point is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) In Article 3(1), point (b), the following point is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 155
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) In Article 3(1), point (b), the following point is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 3(1), point (b), the following point is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(3) In Article 3, the following paragraph 1a is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 156
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) In Article 3, the following paragraph 1a is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) In Article 3, the following paragraph 1a is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(4) In Article 5(2), the following point (e) is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 157
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) In Article 5(2), the following point (e) is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) In Article 5(2), the following point (e) is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(5) In Article 5, the following new paragraph 3a is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 158
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) In Article 5, the following new paragraph 3a is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) In Article 5, the following new paragraph 3a is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(6) In Annex I, Table I, the following row is added under policy objective 1: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 159
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(6) In Annex I, Table I, the following row is added under policy objective 1: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(6) In Annex I, Table I, the following row is added under policy objective 1:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(7) In Annex I, Table I, the following row is added under policy objective 2: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 160
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(7) In Annex I, Table I, the following row is added under policy objective 2: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(7) In Annex I, Table I, the following row is added under policy objective 2:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(8) In the Table of Annex II, the following row is added under policy objective ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 161
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "(8) In the Table of Annex II, the following row is added under policy objective 1: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(8) In the Table of Annex II, the following row is added under policy objective 1:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(9) In the Table of Annex II, the following row is added under policy objective ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 162
    thisalinea.parentID = 153
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "(9) In the Table of Annex II, the following row is added under policy objective 2: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(9) In the Table of Annex II, the following row is added under policy objective 2:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 11"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 163
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "Regulation (EU) 2021/1056 is amended as follows: (1) Article 2 is replaced by the following: ‘In accordance with the second subparagraph of Article 5(1) of Regulation (EU) 2021/1060, the JTF shall contribute to the specific objective of enabling regions and people to address the social, employment, economic and environmental impacts of the transition towards the Union’s 2030 targets for energy and climate and a climate- neutral economy of the Union by 2050, based on the Paris Agreement. The JTF may also support investments contributing to the STEP objective referred to in Article 2(1), point (a)(ii) of Regulation .../... [STEP Regulation].’ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/1056 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(1) Article 2 is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 164
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) Article 2 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) Article 2 is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Amendments to Regulation (EU) 2021/1056 [JTF]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 165
    thisalinea.parentID = 163
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "‘In accordance with the second subparagraph of Article 5(1) of Regulation (EU) 2021/1060, the JTF shall contribute to the specific objective of enabling regions and people to address the social, employment, economic and environmental impacts of the transition towards the Union’s 2030 targets for energy and climate and a climate- neutral economy of the Union by 2050, based on the Paris Agreement. The JTF may also support investments contributing to the STEP objective referred to in Article 2(1), point (a)(ii) of Regulation .../... [STEP Regulation].’ 35 ‘The JTF may also support productive investments in enterprises other than SMEs contributing to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("‘In accordance with the second subparagraph of Article 5(1) of Regulation (EU)")
    thisalinea.textcontent.append("2021/1060, the JTF shall contribute to the specific objective of enabling regions and")
    thisalinea.textcontent.append("people to address the social, employment, economic and environmental impacts of")
    thisalinea.textcontent.append("the transition towards the Union’s 2030 targets for energy and climate and a climate-")
    thisalinea.textcontent.append("neutral economy of the Union by 2050, based on the Paris Agreement. The JTF may")
    thisalinea.textcontent.append("also support investments contributing to the STEP objective referred to in Article")
    thisalinea.textcontent.append("2(1), point (a)(ii) of Regulation .../... [STEP Regulation].’")
    thisalinea.textcontent.append("35")
    thisalinea.textcontent.append("‘The JTF may also support productive investments in enterprises other than SMEs")
    thisalinea.textcontent.append("contributing to the STEP objectives referred to in Article 2 of Regulation .../...65")
    thisalinea.textcontent.append("[STEPRegulation]. That support may be provided irrespective of whether the gap")
    thisalinea.textcontent.append("analysis was carried out in accordance with Article 11(2)(h) and irrespective of its")
    thisalinea.textcontent.append("outcome. Such investments shall only be eligible where they do not lead to relocation")
    thisalinea.textcontent.append("as defined in point (27) of Article 2 of Regulation (EU) 2021/1060. The provision of")
    thisalinea.textcontent.append("such support shall not require a revision of the territorial just transition plan where")
    thisalinea.textcontent.append("that revision would be exclusively linked to the gap analysis.’")
    thisalinea.textcontent.append("‘The Commission shall pay 30% of the JTF allocation, including amounts transferred")
    thisalinea.textcontent.append("in line with Article 27 of Regulation EU 2021/1060, to a programme as set out in the")
    thisalinea.textcontent.append("decision approving the programme as exceptional one-off pre-financing in addition")
    thisalinea.textcontent.append("to the yearly pre-financing for the programme provided for in Article 90(1) and (2)")
    thisalinea.textcontent.append("of Regulation (EU) 2021/1060. The exceptional pre-financing shall be paid as from")
    thisalinea.textcontent.append("[entry into force of this Regulation].")
    thisalinea.textcontent.append("In accordance with Article 90(5) of Regulation (EU) 2021/1060, the amount paid as")
    thisalinea.textcontent.append("exceptional pre-financing shall be cleared no later than with the final accounting")
    thisalinea.textcontent.append("year.")
    thisalinea.textcontent.append("In accordance with Article 90(6) of Regulation (EU) 2021/1060, any interest")
    thisalinea.textcontent.append("generated by the exceptional pre-financing shall be used for the programme")
    thisalinea.textcontent.append("concerned in the same way as the ERDF and shall be included in the accounts for the")
    thisalinea.textcontent.append("final accounting year.")
    thisalinea.textcontent.append("In accordance with Article 97(1) of Regulation (EU) 2021/1060, the exceptional pre-")
    thisalinea.textcontent.append("financing shall not be suspended.")
    thisalinea.textcontent.append("In accordance with Article 105(1) of Regulation (EU) 2021/1060, the pre-financing")
    thisalinea.textcontent.append("to be taken into account for the purposes of calculating amounts to be de-committed")
    thisalinea.textcontent.append("shall include the exceptional pre-financing paid.")
    thisalinea.textcontent.append("By way of derogation from Article 112 of Regulation (EU) 2021/1060, the maximum")
    thisalinea.textcontent.append("co-financing rates for dedicated priorities established to support the STEP objectives")
    thisalinea.textcontent.append("shall be increased to 100 %.’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(2) In Article 8(2) the following subparagraph is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 166
    thisalinea.parentID = 165
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(2) In Article 8(2) the following subparagraph is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 8(2) the following subparagraph is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(3) In Article 10, the following paragraph 4 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 167
    thisalinea.parentID = 165
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(3) In Article 10, the following paragraph 4 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) In Article 10, the following paragraph 4 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 12 Amendments to Regulation (EU) 2021/1057 [ESF+]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 168
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "Regulation (EU) 2021/1057 is amended as follows: (1) A new article 12a is inserted: In addition to the pre-financing for the programme provided for in Article 90(1) and 36 Regulation .../...66 [STEP Regulation], it shall make an exceptional pre-financing of 30% on the basis of the allocation to those priorities. The exceptional pre-financing shall be paid by 31 December 2024, provided the Commission has adopted the decision approving the programme amendment by 31 October 2024. In accordance with Article 90(5) of Regulation (EU) 2021/1060, the amount paid as exceptional pre-financing shall be cleared no later than with the final accounting "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/1057 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) A new article 12a is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 169
    thisalinea.parentID = 168
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) A new article 12a is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) A new article 12a is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "‘Article 12a"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 170
    thisalinea.parentID = 168
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "In addition to the pre-financing for the programme provided for in Article 90(1) and 36 Regulation .../...66 [STEP Regulation], it shall make an exceptional pre-financing of 30% on the basis of the allocation to those priorities. The exceptional pre-financing shall be paid by 31 December 2024, provided the Commission has adopted the decision approving the programme amendment by 31 October 2024. In accordance with Article 90(5) of Regulation (EU) 2021/1060, the amount paid as exceptional pre-financing shall be cleared no later than with the final accounting year. In accordance with Article 90(6) of Regulation (EU) 2021/1060, any interest generated by "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In addition to the pre-financing for the programme provided for in Article 90(1) and")
    thisalinea.textcontent.append("36")
    thisalinea.textcontent.append("Regulation .../...66 [STEP Regulation], it shall make an exceptional pre-financing of")
    thisalinea.textcontent.append("30% on the basis of the allocation to those priorities. The exceptional pre-financing")
    thisalinea.textcontent.append("shall be paid by 31 December 2024, provided the Commission has adopted the")
    thisalinea.textcontent.append("decision approving the programme amendment by 31 October 2024.")
    thisalinea.textcontent.append("In accordance with Article 90(5) of Regulation (EU) 2021/1060, the amount paid as")
    thisalinea.textcontent.append("exceptional pre-financing shall be cleared no later than with the final accounting")
    thisalinea.textcontent.append("year.")
    thisalinea.textcontent.append("In accordance with Article 90(6) of Regulation (EU) 2021/1060, any interest")
    thisalinea.textcontent.append("generated by the exceptional pre-financing shall be used for the programme")
    thisalinea.textcontent.append("concerned in the same way as the ESF+ and shall be included in the accounts for the")
    thisalinea.textcontent.append("final accounting year.")
    thisalinea.textcontent.append("In accordance with Article 97(1) of Regulation (EU) 2021/1060, the exceptional pre-")
    thisalinea.textcontent.append("financing shall not be suspended.")
    thisalinea.textcontent.append("In accordance with Article 105(1) of Regulation (EU) 2021/1060, the pre-financing")
    thisalinea.textcontent.append("to be taken into account for the purposes of calculating amounts to be de-committed")
    thisalinea.textcontent.append("shall include the exceptional pre-financing paid.")
    thisalinea.textcontent.append("By way of derogation from Article 112 of Regulation (EU) 2021/1060, the maximum")
    thisalinea.textcontent.append("co-financing rates for dedicated priorities established to support the STEP objectives")
    thisalinea.textcontent.append("shall be increased to 100 %.’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(2) of Regulation (EU) 2021/1060, where the Commission approves an amendment ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 171
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(2) of Regulation (EU) 2021/1060, where the Commission approves an amendment of a programme including one or more priorities dedicated to operations supported by the ESF+ contributing to the STEP objectives referred to in Article 2 of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) of Regulation (EU) 2021/1060, where the Commission approves an amendment")
    thisalinea.textcontent.append("of a programme including one or more priorities dedicated to operations supported")
    thisalinea.textcontent.append("by the ESF+ contributing to the STEP objectives referred to in Article 2 of")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 13 Amendments to Regulation (EU) 2021/1060 [CPR]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 172
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = "Regulation (EU) 2021/1060 is amended as follows: ‘(45) ‘Seal of Excellence’ means the quality label attributed by the Commission in respect of a proposal, which shows that the proposal which has been assessed in a call for proposals under a Union instrument is deemed to comply with the minimum quality requirements of that Union instrument, but could not be funded due to lack of budget available for that call for proposals, and might receive support from other Union or national sources of funding; or the ‘Sovereignty Seal’ referred to in Article 4 of Regulation .../...67 [STEP Regulation].’ ‘In accordance with "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/1060 is amended as follows:")
    thisalinea.textcontent.append("‘(45) ‘Seal of Excellence’ means the quality label attributed by the Commission in")
    thisalinea.textcontent.append("respect of a proposal, which shows that the proposal which has been assessed in a")
    thisalinea.textcontent.append("call for proposals under a Union instrument is deemed to comply with the minimum")
    thisalinea.textcontent.append("quality requirements of that Union instrument, but could not be funded due to lack of")
    thisalinea.textcontent.append("budget available for that call for proposals, and might receive support from other")
    thisalinea.textcontent.append("Union or national sources of funding; or the ‘Sovereignty Seal’ referred to in")
    thisalinea.textcontent.append("Article 4 of Regulation .../...67 [STEP Regulation].’")
    thisalinea.textcontent.append("‘In accordance with the second subparagraph of Article 10(4) of the InvestEU")
    thisalinea.textcontent.append("Regulation, where a guarantee agreement has not been concluded within 12 months")
    thisalinea.textcontent.append("from the conclusion of the contribution agreement, the contribution agreement shall")
    thisalinea.textcontent.append("be terminated or prolonged by mutual agreement.’")
    thisalinea.textcontent.append("‘Where support is programmed for the STEP objectives referred to in Article 2 of")
    thisalinea.textcontent.append("Regulation .../... [STEP Regulation], the managing authority shall ensure that all the")
    thisalinea.textcontent.append("information to be published in accordance with paragraph 2 of this Article is also")
    thisalinea.textcontent.append("submitted to the Commission in the format set out in paragraph 4 of this Article for")
    thisalinea.textcontent.append("37")
    thisalinea.textcontent.append("publication on the Sovereignty Portal set out in Article 6 of Regulation .../... [STEP")
    thisalinea.textcontent.append("Regulation], including a timetable of the planned calls for proposals that is updated")
    thisalinea.textcontent.append("at least three times a year, as well as the link to the calls for proposals on the day of")
    thisalinea.textcontent.append("their publication.’")
    thisalinea.textcontent.append("38")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) In Article 2, point (45) is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 173
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) In Article 2, point (45) is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) In Article 2, point (45) is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) In Article 14(5), the first subparagraph is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 174
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) In Article 14(5), the first subparagraph is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 14(5), the first subparagraph is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(3) In Article 49, the following paragraph 2a is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 175
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) In Article 49, the following paragraph 2a is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) In Article 49, the following paragraph 2a is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(4) In the Annex I, Table 1, the following rows are added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 176
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) In the Annex I, Table 1, the following rows are added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) In the Annex I, Table 1, the following rows are added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(5) In Annex I, Table 6, the following row is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 177
    thisalinea.parentID = 172
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) In Annex I, Table 6, the following row is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) In Annex I, Table 6, the following row is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 14 Amendments to Regulation (EU) No 1303/2013 [CPR]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 178
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "Regulation (EU) No 1303/2013 is amended as follows: ‘6. By way of derogation from paragraph 2, the deadline for the submission of the final application for an interim payment for the final accounting year shall be 31 July 2025. The last application for interim payment submitted by 31 July 2025 shall be deemed to be the final application for an interim payment for the final accounting year. Amounts from resources other than REACT-EU reimbursed by the Commission as interim payments in 2025 shall not exceed 1 % of the total financial appropriations to the programme concerned by Fund, REACT-EU resources "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) No 1303/2013 is amended as follows:")
    thisalinea.textcontent.append("‘6. By way of derogation from paragraph 2, the deadline for the submission of the")
    thisalinea.textcontent.append("final application for an interim payment for the final accounting year shall be 31 July")
    thisalinea.textcontent.append("2025. The last application for interim payment submitted by 31 July 2025 shall be")
    thisalinea.textcontent.append("deemed to be the final application for an interim payment for the final accounting")
    thisalinea.textcontent.append("year.")
    thisalinea.textcontent.append("Amounts from resources other than REACT-EU reimbursed by the Commission as")
    thisalinea.textcontent.append("interim payments in 2025 shall not exceed 1 % of the total financial appropriations to")
    thisalinea.textcontent.append("the programme concerned by Fund, REACT-EU resources excluded. Amounts that")
    thisalinea.textcontent.append("would be due to be paid by the Commission in 2025 exceeding this percentage shall")
    thisalinea.textcontent.append("not be paid and shall be used exclusively for the clearing of pre-financing at")
    thisalinea.textcontent.append("closure.’")
    thisalinea.textcontent.append("‘By way of derogation from the deadline set out in the first subparagraph, Member")
    thisalinea.textcontent.append("States may submit the documents referred to under points (a), (b) and (c) for the final")
    thisalinea.textcontent.append("accounting year by 15 February 2026.’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) In Article 135, the following paragraph 6 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 179
    thisalinea.parentID = 178
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) In Article 135, the following paragraph 6 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) In Article 135, the following paragraph 6 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) In Article 138, the following subparagraph is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 180
    thisalinea.parentID = 178
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) In Article 138, the following subparagraph is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 138, the following subparagraph is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 15 Amendment to Regulation (EU) No 223/2014 [FEAD]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 181
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "Regulation (EU) No 223/2014 is amended as follows: ‘5. The Member State shall submit a final report on implementation of the operational programme together with the closure documents as set out in Article 52, by 15 February 2026 at the latest.’ ‘2a. In the case of costs reimbursed pursuant to points (b), (c), (d) and (e) of Article 26(2), the corresponding actions being reimbursed shall be carried out by the submission of the final application for an interim payment for the final accounting year in accordance with Article 45(6).’ ‘6. By way of derogation from paragraph 2, the deadline for "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) No 223/2014 is amended as follows:")
    thisalinea.textcontent.append("‘5. The Member State shall submit a final report on implementation of the")
    thisalinea.textcontent.append("operational programme together with the closure documents as set out in Article 52,")
    thisalinea.textcontent.append("by 15 February 2026 at the latest.’")
    thisalinea.textcontent.append("‘2a. In the case of costs reimbursed pursuant to points (b), (c), (d) and (e) of Article")
    thisalinea.textcontent.append("26(2), the corresponding actions being reimbursed shall be carried out by the")
    thisalinea.textcontent.append("submission of the final application for an interim payment for the final accounting")
    thisalinea.textcontent.append("year in accordance with Article 45(6).’")
    thisalinea.textcontent.append("‘6. By way of derogation from paragraph 2, the deadline for the submission of the")
    thisalinea.textcontent.append("final application for an interim payment for the final accounting year shall be 31 July")
    thisalinea.textcontent.append("2025. The last application for interim payment submitted by 31 July 2025 shall be")
    thisalinea.textcontent.append("deemed to be the final application for an interim payment for the final accounting")
    thisalinea.textcontent.append("year.")
    thisalinea.textcontent.append("Amounts reimbursed by the Commission as interim payments in 2025 shall not")
    thisalinea.textcontent.append("exceed 1 % of the total financial appropriations to the programme concerned.")
    thisalinea.textcontent.append("Amounts that would be due to be paid by the Commission in 2025 exceeding this")
    thisalinea.textcontent.append("percentage shall not be paid and shall be used exclusively for the clearing of pre-")
    thisalinea.textcontent.append("financing at closure.’")
    thisalinea.textcontent.append("39")
    thisalinea.textcontent.append("‘By way of derogation from the deadline set out in the first subparagraph, Member")
    thisalinea.textcontent.append("States may submit the documents referred to under points (a), (b) and (c) for the final")
    thisalinea.textcontent.append("accounting year by 15 February 2026.’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) In Article 13, paragraph 5 is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 182
    thisalinea.parentID = 181
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) In Article 13, paragraph 5 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) In Article 13, paragraph 5 is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) In Article 22, the following paragraph 2a is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 183
    thisalinea.parentID = 181
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) In Article 22, the following paragraph 2a is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 22, the following paragraph 2a is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(3) In Article 45, the following paragraph 6 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 184
    thisalinea.parentID = 181
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) In Article 45, the following paragraph 6 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) In Article 45, the following paragraph 6 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(4) In Article 48, the following subparagraph is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 185
    thisalinea.parentID = 181
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) In Article 48, the following subparagraph is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) In Article 48, the following subparagraph is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 16 Amendments to Regulation (EU) 2021/523 [InvestEU]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 186
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 22
    thisalinea.summary = "Regulation (EU) 2021/523 is amended as follows: ‘(h) supporting investments contributing to the STEP objectives referred to in Article 2 of Regulation .../...68 [STEP Regulation]’ ‘(e) supporting financing and investment operations related to the areas referred to in Article 8(1), point (e).’ ‘The EU guarantee for the purposes of the EU compartment referred to in Article 9(1), point (a), shall be EUR 33 652 310 073 in current prices. It shall be provisioned at the rate of 40 %. The amount referred to in Article 35(3), first subparagraph, point (a), shall be also taken into account for contributing to the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/523 is amended as follows:")
    thisalinea.textcontent.append("‘(h) supporting investments contributing to the STEP objectives referred to in")
    thisalinea.textcontent.append("Article 2 of Regulation .../...68 [STEP Regulation]’")
    thisalinea.textcontent.append("‘(e) supporting financing and investment operations related to the areas")
    thisalinea.textcontent.append("referred to in Article 8(1), point (e).’")
    thisalinea.textcontent.append("‘The EU guarantee for the purposes of the EU compartment referred to in")
    thisalinea.textcontent.append("Article 9(1), point (a), shall be EUR 33 652 310 073 in current prices. It shall")
    thisalinea.textcontent.append("be provisioned at the rate of 40 %. The amount referred to in Article 35(3), first")
    thisalinea.textcontent.append("subparagraph, point (a), shall be also taken into account for contributing to the")
    thisalinea.textcontent.append("provisioning resulting from that provisioning rate.‘;")
    thisalinea.textcontent.append("‘An amount of EUR 18 827 310 073 in current prices of the amount referred to")
    thisalinea.textcontent.append("in the first subparagraph of paragraph 1 of this Article shall be allocated for the")
    thisalinea.textcontent.append("objectives referred to in Article 3(2).’;")
    thisalinea.textcontent.append("‘The indicative distribution of the EU guarantee for the purposes of the EU")
    thisalinea.textcontent.append("compartment is set out in Annex I to this Regulation. Where appropriate, the")
    thisalinea.textcontent.append("Commission may depart from the amounts referred to in Annex I by up to 15")
    thisalinea.textcontent.append("% for each objective referred to in Article 3(2), points (a) to (e). The")
    thisalinea.textcontent.append("Commission shall inform the European Parliament and the Council of any such")
    thisalinea.textcontent.append("departure.’")
    thisalinea.textcontent.append("‘By way of derogation from the first subparagraph, when support from the financial")
    thisalinea.textcontent.append("instruments is combined in a financial product in a subordinated position to the EU")
    thisalinea.textcontent.append("guarantee under this Regulation and/or EU guarantee established by Regulation (EU)")
    thisalinea.textcontent.append("2015/1017, the losses, revenues and repayments from financial products as referred")
    thisalinea.textcontent.append("to in paragraph 1, as well as potential recoveries, may also be attributed on a non pro")
    thisalinea.textcontent.append("40")
    thisalinea.textcontent.append("rata basis between the financial instruments and the EU guarantee under this")
    thisalinea.textcontent.append("Regulation and/or EU guarantee established by Regulation (EU) 2015/1017.’")
    thisalinea.textcontent.append("‘1. The InvestEU Fund shall operate through the following five policy")
    thisalinea.textcontent.append("windows that shall address market failures or suboptimal investment situations")
    thisalinea.textcontent.append("with their specific scope:’;")
    thisalinea.textcontent.append("‘(e) a STEP policy window, which comprises investments contributing to")
    thisalinea.textcontent.append("the STEP objectives referred to in Article 2 of Regulation .../... [STEP")
    thisalinea.textcontent.append("Regulation]’.")
    thisalinea.textcontent.append("‘Where no guarantee agreement has been concluded within 12 months from the")
    thisalinea.textcontent.append("conclusion of the contribution agreement, the contribution agreement shall be")
    thisalinea.textcontent.append("terminated or prolonged by mutual agreement. Where the amount of a contribution")
    thisalinea.textcontent.append("agreement has not been fully committed under one or more guarantee agreements")
    thisalinea.textcontent.append("within twelve months from the conclusion of the contribution agreement, that amount")
    thisalinea.textcontent.append("shall be amended accordingly. The unused amount of provisioning attributable to")
    thisalinea.textcontent.append("amounts allocated by Member States pursuant to the provisions on the use of the")
    thisalinea.textcontent.append("ERDF, the ESF+, the Cohesion Fund and the EMFAF delivered through the")
    thisalinea.textcontent.append("InvestEU Programme laid down in Regulation (EU) 2021/1060 or to the provisions")
    thisalinea.textcontent.append("on the use of the EAFRD delivered through the InvestEU Programme laid down in")
    thisalinea.textcontent.append("the CAP Strategic Plans Regulation shall be re-used in accordance with those")
    thisalinea.textcontent.append("respective Regulations. The unused amount of provisioning attributable to amounts")
    thisalinea.textcontent.append("allocated by a Member State under Article 4(1), third subparagraph, of this")
    thisalinea.textcontent.append("Regulation shall be paid back to the Member State.’")
    thisalinea.textcontent.append("‘4. At least 75 % of the EU guarantee under the EU compartment as referred to in")
    thisalinea.textcontent.append("Article 4(1), first subparagraph, amounting to at least EUR 25 239 232 554, shall be")
    thisalinea.textcontent.append("granted to the EIB Group. The EIB Group shall provide an aggregate financial")
    thisalinea.textcontent.append("contribution amounting to at least EUR 6 309 808 138. That contribution shall be")
    thisalinea.textcontent.append("provided in a manner and form that facilitates the implementation of the InvestEU")
    thisalinea.textcontent.append("Fund and the achievement of the objectives set out in Article 15(2).’;")
    thisalinea.textcontent.append("‘3. In the context of the procedures referred to in paragraphs 1 and 2 of this Article,")
    thisalinea.textcontent.append("the Commission shall take into account any Sovereignty Seal awarded under Article")
    thisalinea.textcontent.append("4 of Regulation .../... [STEP Regulation] to a project’.")
    thisalinea.textcontent.append("‘The Investment Committee shall meet in five different configurations,")
    thisalinea.textcontent.append("corresponding to the five policy windows referred to in Article 8(1).’")
    thisalinea.textcontent.append("‘Four members of the Investment Committee shall be permanent members of")
    thisalinea.textcontent.append("each of the five configurations of the Investment Committee. At least one of")
    thisalinea.textcontent.append("41")
    thisalinea.textcontent.append("the permanent members shall have expertise in sustainable investment. In")
    thisalinea.textcontent.append("addition, each of the five configurations shall have two experts with experience")
    thisalinea.textcontent.append("in investment in sectors covered by the corresponding policy window. The")
    thisalinea.textcontent.append("Steering Board shall assign the Investment Committee members to the")
    thisalinea.textcontent.append("appropriate configuration or configurations. A non-permanent member may")
    thisalinea.textcontent.append("be assigned to maximum two configurations, subject to fulfilling the")
    thisalinea.textcontent.append("requirements for both of them. The Investment Committee shall elect a")
    thisalinea.textcontent.append("chairperson from among its permanent members.’")
    thisalinea.textcontent.append("‘(j) provide advisory support to equity fund managers active in the areas referred")
    thisalinea.textcontent.append("to in point (e) of Article 8(1).’")
    thisalinea.textcontent.append("‘5. In addition to paragraph 4, implementing partners shall also examine projects")
    thisalinea.textcontent.append("having been awarded the Sovereignty Seal under Article 4 of Regulation .../... [STEP")
    thisalinea.textcontent.append("Regulation] whenever those projects fall within their geographic and activity scope’.")
    thisalinea.textcontent.append("‘5. By way of derogation from Article 16, second subparagraph, of this Regulation,")
    thisalinea.textcontent.append("financing and investment operations approved by the implementing partner as of 1")
    thisalinea.textcontent.append("January 2023 until the signature of a guarantee agreement or of an amendment to an")
    thisalinea.textcontent.append("existing one encompassing the STEP Window may be covered by the EU guarantee,")
    thisalinea.textcontent.append("provided that those operations are indicated in the guarantee agreement, pass the")
    thisalinea.textcontent.append("policy check referred to in Article 23(1) or receive a favourable opinion within the")
    thisalinea.textcontent.append("framework of the procedure provided for in Article 19 of the EIB Statute and are in")
    thisalinea.textcontent.append("both cases approved by the Investment Committee in accordance with Article 24.’")
    thisalinea.textcontent.append("‘(e) up to EUR 7 500 000 000 for objectives referred to in Article 3(2), point (e).’")
    thisalinea.textcontent.append("‘(16) scaling up, deployment and large-scale manufacturing of the critical")
    thisalinea.textcontent.append("technologies referred to in Article 2(1), point (a) of Regulation .../... [STEP")
    thisalinea.textcontent.append("Regulation], as well as the respective value chain referred to in Article 2(4) of that")
    thisalinea.textcontent.append("Regulation.’")
    thisalinea.textcontent.append("‘7a. STEP")
    thisalinea.textcontent.append("7a.1 Investment mobilised by technology area: i) deep and digital technologies, ii)")
    thisalinea.textcontent.append("clean technologies and iii) biotechnologies.’")
    thisalinea.textcontent.append("7a.2 Jobs created or supported.")
    thisalinea.textcontent.append("7a.2 Number of enterprises supported by technology area: i) deep and digital")
    thisalinea.textcontent.append("technologies, ii) clean technologies and iii) biotechnologies.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) Article 3 is amended as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 187
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) Article 3 is amended as follows: (a) the following point is added in paragraph 1: (b) the following point is added in paragraph 2: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) Article 3 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the following point is added in paragraph 1: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 188
    thisalinea.parentID = 187
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the following point is added in paragraph 1: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the following point is added in paragraph 1:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the following point is added in paragraph 2: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 189
    thisalinea.parentID = 187
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the following point is added in paragraph 2: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the following point is added in paragraph 2:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) Article 4 is amended as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 190
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) Article 4 is amended as follows: (a) In paragraph 1, the first subparagraph is replaced by the following: (b) paragraph 2, second subparagraph is replaced by the following: (c) the fourth subparagraph of paragraph 2 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) Article 4 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) In paragraph 1, the first subparagraph is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 191
    thisalinea.parentID = 190
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) In paragraph 1, the first subparagraph is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) In paragraph 1, the first subparagraph is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) paragraph 2, second subparagraph is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 192
    thisalinea.parentID = 190
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) paragraph 2, second subparagraph is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) paragraph 2, second subparagraph is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the fourth subparagraph of paragraph 2 is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 193
    thisalinea.parentID = 190
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the fourth subparagraph of paragraph 2 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the fourth subparagraph of paragraph 2 is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(3) In Article 7(3), a second subparagraph is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 194
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) In Article 7(3), a second subparagraph is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) In Article 7(3), a second subparagraph is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(4) Article 8 is amended as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 195
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) Article 8 is amended as follows: (a) In paragraph 1, the introductory wording is replaced by the following: (b) In paragraph 1, the following point (e) is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) Article 8 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) In paragraph 1, the introductory wording is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 196
    thisalinea.parentID = 195
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) In paragraph 1, the introductory wording is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) In paragraph 1, the introductory wording is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) In paragraph 1, the following point (e) is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 197
    thisalinea.parentID = 195
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) In paragraph 1, the following point (e) is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) In paragraph 1, the following point (e) is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(5) In Article 10, the second subparagraph of paragraph 4 is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 198
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) In Article 10, the second subparagraph of paragraph 4 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) In Article 10, the second subparagraph of paragraph 4 is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(6) Article 13(4) is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 199
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(6) Article 13(4) is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(6) Article 13(4) is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(7) In Article 23, the following paragraph 3 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 200
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(7) In Article 23, the following paragraph 3 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(7) In Article 23, the following paragraph 3 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(8) Article 24(2) is amended as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 201
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "(8) Article 24(2) is amended as follows: (a) the first subparagraph is replaced by the following: (b) The fifth subparagraph is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(8) Article 24(2) is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the first subparagraph is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 202
    thisalinea.parentID = 201
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the first subparagraph is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the first subparagraph is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) The fifth subparagraph is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 203
    thisalinea.parentID = 201
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) The fifth subparagraph is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) The fifth subparagraph is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(9) In Article 25, point (j) is added to paragraph 2 as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 204
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "(9) In Article 25, point (j) is added to paragraph 2 as follows: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(9) In Article 25, point (j) is added to paragraph 2 as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(10) In Article 26, the following paragraph 5 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 205
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "(10) In Article 26, the following paragraph 5 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(10) In Article 26, the following paragraph 5 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(11) In Article 35, paragraph 5 is added as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 206
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "(11) In Article 35, paragraph 5 is added as follows: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(11) In Article 35, paragraph 5 is added as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(12) In Annex I, point (e) is added as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 207
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "(12) In Annex I, point (e) is added as follows: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(12) In Annex I, point (e) is added as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(13) In Annex II, point (16) is inserted as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 208
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "(13) In Annex II, point (16) is inserted as follows: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(13) In Annex II, point (16) is inserted as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(14) In Annex III, point (9) is inserted as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 209
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "(14) In Annex III, point (9) is inserted as follows: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(14) In Annex III, point (9) is inserted as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "Amendments to Regulation (EU) 2021/695 [Horizon Europe]"
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 210
    thisalinea.parentID = 186
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Regulation (EU) 2021/695 is amended as follows: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/695 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 17"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 211
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 23
    thisalinea.summary = "42 ‘1. The financial envelope for the implementation of the Programme for the period from 1 January 2021 to 31 December 2027 shall be EUR 86 623 000 000 in current prices for the specific programme referred to in point (a) of Article 1(2) and for the EIT and EUR 9 453 000 000 in current prices for the specific programme referred to in point (c) of Article 1(2). ’ ‘(b) EUR 46 628 000 000 for Pillar II 'Global Challenges and European Industrial Competitiveness' for the period 2021 to 2027, of which: ‘4a. By derogation from Article 209(3) of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("42")
    thisalinea.textcontent.append("‘1. The financial envelope for the implementation of the Programme for the")
    thisalinea.textcontent.append("period from 1 January 2021 to 31 December 2027 shall be EUR 86 623 000")
    thisalinea.textcontent.append("000 in current prices for the specific programme referred to in point (a) of")
    thisalinea.textcontent.append("Article 1(2) and for the EIT and EUR 9 453 000 000 in current prices for the")
    thisalinea.textcontent.append("specific programme referred to in point (c) of Article 1(2). ’")
    thisalinea.textcontent.append("‘(b) EUR 46 628 000 000 for Pillar II 'Global Challenges and European")
    thisalinea.textcontent.append("Industrial Competitiveness' for the period 2021 to 2027, of which:")
    thisalinea.textcontent.append("‘4a. By derogation from Article 209(3) of the Financial Regulation, repayments")
    thisalinea.textcontent.append("including reimbursed advances, revenues and unused amounts net of fees and costs")
    thisalinea.textcontent.append("of EIC blended finance of the EIC pilot under Horizon 2020 shall be considered to be")
    thisalinea.textcontent.append("internal assigned revenues in accordance with Article 21(3), point (f) and Article")
    thisalinea.textcontent.append("21(4) and (5) of the Financial Regulation. The time restriction of two years set out in")
    thisalinea.textcontent.append("the second subparagraph of Article 209(3) of the Financial Regulation shall apply as")
    thisalinea.textcontent.append("from the date of entry into force of Regulation .../...69 [STEP Regulation]’.")
    thisalinea.textcontent.append("‘(d) equity-only support required for scale-up to non-bankable SMEs, including start-")
    thisalinea.textcontent.append("ups, and non-bankable small mid-caps, including entities which have already")
    thisalinea.textcontent.append("received support in line with points (a) to (c), carrying out breakthrough and")
    thisalinea.textcontent.append("disruptive non-bankable innovation in the critical technologies referred to in Article")
    thisalinea.textcontent.append("2(1)(a) of Regulation .../... [STEP Regulation], financed under Article 3(b) of that")
    thisalinea.textcontent.append("Regulation.’")
    thisalinea.textcontent.append("43")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) Article 12 is amended as follows: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 212
    thisalinea.parentID = 211
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) Article 12 is amended as follows: (a) paragraph 1 is replaced by the following: (b) in paragraph 2, points (b) and (c) are replaced by the following: (i) EUR 6 775 000 000 for cluster 'Health'; (ii) EUR 1 350 000 000for cluster 'Culture, Creativity and Inclusive Society'; (iii) EUR 1 276 000 000 for cluster 'Civil Security for Society'; (iv) EUR 13 229 000 000 for cluster 'Digital, Industry and Space'; (v) EUR 13 229 000 000 for cluster 'Climate, Energy and Mobility'; (vi) EUR 8 799 000 000 for cluster 'Food, Bioeconomy, Natural Resources, Agriculture and Environment'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) Article 12 is amended as follows:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) paragraph 1 is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 213
    thisalinea.parentID = 212
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) paragraph 1 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) paragraph 1 is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) in paragraph 2, points (b) and (c) are replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 214
    thisalinea.parentID = 212
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) in paragraph 2, points (b) and (c) are replaced by the following: (i) EUR 6 775 000 000 for cluster 'Health'; (ii) EUR 1 350 000 000for cluster 'Culture, Creativity and Inclusive Society'; (iii) EUR 1 276 000 000 for cluster 'Civil Security for Society'; (iv) EUR 13 229 000 000 for cluster 'Digital, Industry and Space'; (v) EUR 13 229 000 000 for cluster 'Climate, Energy and Mobility'; (vi) EUR 8 799 000 000 for cluster 'Food, Bioeconomy, Natural Resources, Agriculture and Environment'; (vii) EUR 1 970 000 000 for the non-nuclear direct actions of the JRC; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) in paragraph 2, points (b) and (c) are replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(i) EUR 6 775 000 000 for cluster 'Health'; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 215
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) EUR 6 775 000 000 for cluster 'Health'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) EUR 6 775 000 000 for cluster 'Health';")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(ii) EUR 1 350 000 000for cluster 'Culture, Creativity and Inclusive ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 216
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) EUR 1 350 000 000for cluster 'Culture, Creativity and Inclusive Society'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) EUR 1 350 000 000for cluster 'Culture, Creativity and Inclusive")
    thisalinea.textcontent.append("Society';")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(iii) EUR 1 276 000 000 for cluster 'Civil Security for Society'; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 217
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(iii) EUR 1 276 000 000 for cluster 'Civil Security for Society'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iii) EUR 1 276 000 000 for cluster 'Civil Security for Society';")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(iv) EUR 13 229 000 000 for cluster 'Digital, Industry and Space'; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 218
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(iv) EUR 13 229 000 000 for cluster 'Digital, Industry and Space'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iv) EUR 13 229 000 000 for cluster 'Digital, Industry and Space';")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(v) EUR 13 229 000 000 for cluster 'Climate, Energy and Mobility'; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 219
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(v) EUR 13 229 000 000 for cluster 'Climate, Energy and Mobility'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(v) EUR 13 229 000 000 for cluster 'Climate, Energy and Mobility';")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(vi) EUR 8 799 000 000 for cluster 'Food, Bioeconomy, Natural ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 220
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(vi) EUR 8 799 000 000 for cluster 'Food, Bioeconomy, Natural Resources, Agriculture and Environment'; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(vi) EUR 8 799 000 000 for cluster 'Food, Bioeconomy, Natural")
    thisalinea.textcontent.append("Resources, Agriculture and Environment';")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(vii) EUR 1 970 000 000 for the non-nuclear direct actions of the JRC; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 221
    thisalinea.parentID = 214
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(vii) EUR 1 970 000 000 for the non-nuclear direct actions of the JRC; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(vii) EUR 1 970 000 000 for the non-nuclear direct actions of the JRC;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) EUR 13 237 000 000 for Pillar III 'Innovative Europe' for the period 2021 ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 222
    thisalinea.parentID = 212
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) EUR 13 237 000 000 for Pillar III 'Innovative Europe' for the period 2021 to 2027, of which: (i) EUR 10 052 000 000 for the EIC; (ii) EUR 459 000 000 for European innovation ecosystems; (iii) EUR 2 726 000 000 for the EIT;’ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) EUR 13 237 000 000 for Pillar III 'Innovative Europe' for the period 2021")
    thisalinea.textcontent.append("to 2027, of which:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(i) EUR 10 052 000 000 for the EIC; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 223
    thisalinea.parentID = 222
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) EUR 10 052 000 000 for the EIC; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) EUR 10 052 000 000 for the EIC;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(ii) EUR 459 000 000 for European innovation ecosystems; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 224
    thisalinea.parentID = 222
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) EUR 459 000 000 for European innovation ecosystems; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) EUR 459 000 000 for European innovation ecosystems;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(iii) EUR 2 726 000 000 for the EIT;’ "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 225
    thisalinea.parentID = 222
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(iii) EUR 2 726 000 000 for the EIT;’ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iii) EUR 2 726 000 000 for the EIT;’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) In Article 46, the following paragraph 4a is inserted: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 226
    thisalinea.parentID = 211
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) In Article 46, the following paragraph 4a is inserted: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 46, the following paragraph 4a is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(3) In Article 48, the following point (d) is added in the first subparagraph: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 227
    thisalinea.parentID = 211
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) In Article 48, the following point (d) is added in the first subparagraph: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) In Article 48, the following point (d) is added in the first subparagraph:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 18 Amendments to Regulation (EU) 2021/697 [EDF]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 228
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 24
    thisalinea.summary = "Regulation (EU) 2021/697 is amended as follows: ‘1. In accordance with Article 12(1) of Regulation (EU) 2021/695, the financial envelope for the implementation of the Fund for the period from 1 January 2021 to 31 December 2027 shall be EUR 9 453 000 000 in current prices.’ ‘(a) EUR 3 151 000 000 for research actions; ‘An amount of EUR 1 500 000 000 in current prices of the amount referred to in paragraph 2 shall be allocated to calls for proposals or awards of funding supporting investments contributing to the STEP objectives referred to in Article 2(1), point (a)(i) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/697 is amended as follows:")
    thisalinea.textcontent.append("‘1. In accordance with Article 12(1) of Regulation (EU) 2021/695, the")
    thisalinea.textcontent.append("financial envelope for the implementation of the Fund for the period from")
    thisalinea.textcontent.append("1 January 2021 to 31 December 2027 shall be EUR 9 453 000 000 in current")
    thisalinea.textcontent.append("prices.’")
    thisalinea.textcontent.append("‘(a) EUR 3 151 000 000 for research actions;")
    thisalinea.textcontent.append("‘An amount of EUR 1 500 000 000 in current prices of the amount referred to")
    thisalinea.textcontent.append("in paragraph 2 shall be allocated to calls for proposals or awards of funding")
    thisalinea.textcontent.append("supporting investments contributing to the STEP objectives referred to in")
    thisalinea.textcontent.append("Article 2(1), point (a)(i) of Regulation .../...70 [STEP Regulation].’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) Article 4 is amended as follows "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 229
    thisalinea.parentID = 228
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) Article 4 is amended as follows (a) Paragraph 1 is replaced by the following: (b) in paragraph 2, points (a) and (b) are replaced by the following: (b) EUR 6 302 000 000 for development actions.’ (c) Paragraph 5 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) Article 4 is amended as follows")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) Paragraph 1 is replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 230
    thisalinea.parentID = 229
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) Paragraph 1 is replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) Paragraph 1 is replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) in paragraph 2, points (a) and (b) are replaced by the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 231
    thisalinea.parentID = 229
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) in paragraph 2, points (a) and (b) are replaced by the following: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) in paragraph 2, points (a) and (b) are replaced by the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) EUR 6 302 000 000 for development actions.’ "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 232
    thisalinea.parentID = 229
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(b) EUR 6 302 000 000 for development actions.’ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) EUR 6 302 000 000 for development actions.’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) Paragraph 5 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 233
    thisalinea.parentID = 229
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(c) Paragraph 5 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) Paragraph 5 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 19 Amendments to Regulation (EU) 2021/241 [RRF]"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 234
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 25
    thisalinea.summary = "Regulation (EU) 2021/241 is amended as follows: ‘3. Without prejudice to paragraph 2, Member States may also propose to include in their recovery and resilience plan, as estimated costs, the amount of the cash contribution for the purpose of the Member State compartment pursuant to the relevant provisions of the InvestEU Regulation exclusively for measures supporting investment operations contributing to the STEP objectives referred to in Article 2 of Regulation .../...71 [STEP Regulation]. Those costs shall not exceed 6 % of the recovery and resilience plan’s total financial allocation, and the relevant measures, as set out in the recovery and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Regulation (EU) 2021/241 is amended as follows:")
    thisalinea.textcontent.append("‘3. Without prejudice to paragraph 2, Member States may also propose to include in")
    thisalinea.textcontent.append("their recovery and resilience plan, as estimated costs, the amount of the cash")
    thisalinea.textcontent.append("contribution for the purpose of the Member State compartment pursuant to the")
    thisalinea.textcontent.append("relevant provisions of the InvestEU Regulation exclusively for measures supporting")
    thisalinea.textcontent.append("investment operations contributing to the STEP objectives referred to in Article 2 of")
    thisalinea.textcontent.append("Regulation .../...71 [STEP Regulation]. Those costs shall not exceed 6 % of the")
    thisalinea.textcontent.append("recovery and resilience plan’s total financial allocation, and the relevant measures, as")
    thisalinea.textcontent.append("set out in the recovery and resilience plan, shall respect the requirements of this")
    thisalinea.textcontent.append("Regulation.’")
    thisalinea.textcontent.append("‘6. Prior to launching any calls for proposals or tendering procedures related to the")
    thisalinea.textcontent.append("STEP objectives, as defined in Article 2 of Regulation .../... [STEP Regulation],")
    thisalinea.textcontent.append("Member States shall make available the following information on the Sovereignty")
    thisalinea.textcontent.append("portal referred to in Article 6 of that Regulation:")
    thisalinea.textcontent.append("44")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) In Article 7, the following paragraph 3 is added: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 235
    thisalinea.parentID = 234
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) In Article 7, the following paragraph 3 is added: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) In Article 7, the following paragraph 3 is added:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) In Article 29 the following paragraph 6 is inserted: "
    thisalinea.titlefontsize = "12.000000000000028"
    thisalinea.nativeID = 236
    thisalinea.parentID = 234
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) In Article 29 the following paragraph 6 is inserted: (a) geographical area covered by the call for proposal; (b) investment concerned; (c) type of eligible applicants; (d) total amount of support for the call; (e) start and end date of the call; (f) link to the website where the call will be published.’ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) In Article 29 the following paragraph 6 is inserted:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) geographical area covered by the call for proposal; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 237
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) geographical area covered by the call for proposal; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) geographical area covered by the call for proposal;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) investment concerned; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 238
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) investment concerned; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) investment concerned;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) type of eligible applicants; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 239
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) type of eligible applicants; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) type of eligible applicants;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) total amount of support for the call; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 240
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) total amount of support for the call; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) total amount of support for the call;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(e) start and end date of the call; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 241
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(e) start and end date of the call; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(e) start and end date of the call;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(f) link to the website where the call will be published.’ "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 242
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(f) link to the website where the call will be published.’ "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(f) link to the website where the call will be published.’")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "CHAPTER 3 FINAL PROVISIONS"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 243
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 26
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 20 Entry into force and application"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 244
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 27
    thisalinea.summary = "This Regulation shall enter into force on the day following that of its publication in the Official Journal of the European Union. This Regulation shall be binding in its entirety and directly applicable in all Member States. Done at Brussels, 45 LEGISLATIVE FINANCIAL STATEMENT "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Regulation shall enter into force on the day following that of its publication in the")
    thisalinea.textcontent.append("Official Journal of the European Union.")
    thisalinea.textcontent.append("This Regulation shall be binding in its entirety and directly applicable in all Member States.")
    thisalinea.textcontent.append("Done at Brussels,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "For the European Parliament For the Council The President The President"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 245
    thisalinea.parentID = 244
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "45 LEGISLATIVE FINANCIAL STATEMENT "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("45")
    thisalinea.textcontent.append("LEGISLATIVE FINANCIAL STATEMENT")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Contents"
    thisalinea.titlefontsize = "14.039999999999964"
    thisalinea.nativeID = 246
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 28
    thisalinea.summary = "1.1. Title of the proposal/initiative ...................................................................................... 3 1.2. Policy area(s) concerned .............................................................................................. 3 1.3. The proposal/initiative relates to: ................................................................................. 3 1.4. Objective(s) .................................................................................................................. 3 1.4.1. General objective(s) ..................................................................................................... 3 1.4.2. Specific objective(s) ..................................................................................................... 3 1.4.3. Expected result(s) and impact ...................................................................................... 4 1.4.4. Indicators of performance ............................................................................................ 4 1.5. Grounds for the proposal/initiative .............................................................................. 4 1.5.1. Requirement(s) to be met in the short or long term including a detailed timeline for roll-out of the implementation of the initiative ............................................................ 4 1.5.2. Added value of Union involvement (it may result from different factors, e.g. coordination gains, legal certainty, greater effectiveness or complementarities). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1.1. Title of the proposal/initiative ...................................................................................... 3")
    thisalinea.textcontent.append("1.2. Policy area(s) concerned .............................................................................................. 3")
    thisalinea.textcontent.append("1.3. The proposal/initiative relates to: ................................................................................. 3")
    thisalinea.textcontent.append("1.4. Objective(s) .................................................................................................................. 3")
    thisalinea.textcontent.append("1.4.1. General objective(s) ..................................................................................................... 3")
    thisalinea.textcontent.append("1.4.2. Specific objective(s) ..................................................................................................... 3")
    thisalinea.textcontent.append("1.4.3. Expected result(s) and impact ...................................................................................... 4")
    thisalinea.textcontent.append("1.4.4. Indicators of performance ............................................................................................ 4")
    thisalinea.textcontent.append("1.5. Grounds for the proposal/initiative .............................................................................. 4")
    thisalinea.textcontent.append("1.5.1. Requirement(s) to be met in the short or long term including a detailed timeline for")
    thisalinea.textcontent.append("roll-out of the implementation of the initiative ............................................................ 4")
    thisalinea.textcontent.append("1.5.2. Added value of Union involvement (it may result from different factors, e.g.")
    thisalinea.textcontent.append("coordination gains, legal certainty, greater effectiveness or complementarities). For")
    thisalinea.textcontent.append("the purposes of this point 'added value of Union involvement' is the value resulting")
    thisalinea.textcontent.append("from Union intervention which is additional to the value that would have been")
    thisalinea.textcontent.append("otherwise created by Member States alone. ................................................................. 5")
    thisalinea.textcontent.append("1.5.3. Lessons learned from similar experiences in the past .................................................. 5")
    thisalinea.textcontent.append("1.5.4. Compatibility with the Multiannual Financial Framework and possible synergies")
    thisalinea.textcontent.append("with other appropriate instruments............................................................................... 5")
    thisalinea.textcontent.append("1.5.5. Assessment of the different available financing options, including scope for")
    thisalinea.textcontent.append("redeployment ................................................................................................................ 6")
    thisalinea.textcontent.append("1.6. Duration and financial impact of the proposal/initiative ............................................. 7")
    thisalinea.textcontent.append("1.7. Management mode(s) planned ..................................................................................... 7")
    thisalinea.textcontent.append("2.1. Monitoring and reporting rules .................................................................................... 7")
    thisalinea.textcontent.append("2.2. Management and control system(s) ............................................................................. 8")
    thisalinea.textcontent.append("2.2.1. Justification of the management mode(s), the funding implementation mechanism(s),")
    thisalinea.textcontent.append("the payment modalities and the control strategy proposed .......................................... 8")
    thisalinea.textcontent.append("2.2.2. Information concerning the risks identified and the internal control system(s) set up")
    thisalinea.textcontent.append("to mitigate them............................................................................................................ 8")
    thisalinea.textcontent.append('2.2.3. Estimation and justification of the cost-effectiveness of the controls (ratio of "control')
    thisalinea.textcontent.append('costs ÷ value of the related funds managed"), and assessment of the expected levels')
    thisalinea.textcontent.append("of risk of error (at payment & at closure) .................................................................... 8")
    thisalinea.textcontent.append("2.3. Measures to prevent fraud and irregularities ................................................................ 8")
    thisalinea.textcontent.append("1")
    thisalinea.textcontent.append("3.1. Heading(s) of the multiannual financial framework and expenditure budget line(s)")
    thisalinea.textcontent.append("affected ......................................................................................................................... 9")
    thisalinea.textcontent.append("3.2. Estimated financial impact of the proposal on appropriations ................................... 11")
    thisalinea.textcontent.append("3.2.1. Summary of estimated impact on operational appropriations.................................... 11")
    thisalinea.textcontent.append("3.2.2. Estimated output funded with operational appropriations ......................................... 16")
    thisalinea.textcontent.append("3.2.3. Summary of estimated impact on administrative appropriations ............................... 18")
    thisalinea.textcontent.append("3.2.4. Compatibility with the current multiannual financial framework.............................. 20")
    thisalinea.textcontent.append("3.2.5. Third-party contributions ........................................................................................... 20")
    thisalinea.textcontent.append("3.3. Estimated impact on revenue ..................................................................................... 21")
    thisalinea.textcontent.append("2")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. FRAMEWORK OF THE PROPOSAL/INITIATIVE ................................................. 3 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 247
    thisalinea.parentID = 246
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. FRAMEWORK OF THE PROPOSAL/INITIATIVE ................................................. 3 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. FRAMEWORK OF THE PROPOSAL/INITIATIVE ................................................. 3")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. MANAGEMENT MEASURES................................................................................... 7 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 248
    thisalinea.parentID = 246
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. MANAGEMENT MEASURES................................................................................... 7 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. MANAGEMENT MEASURES................................................................................... 7")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. ESTIMATED FINANCIAL IMPACT OF THE PROPOSAL/INITIATIVE .............. 9 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 249
    thisalinea.parentID = 246
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. ESTIMATED FINANCIAL IMPACT OF THE PROPOSAL/INITIATIVE .............. 9 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. ESTIMATED FINANCIAL IMPACT OF THE PROPOSAL/INITIATIVE .............. 9")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. FRAMEWORK OF THE PROPOSAL"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 250
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 29
    thisalinea.summary = "Proposal for a Regulation of the European Parliament and of the Council establishing the Strategic Technologies for Europe Platform (‘STEP’) and amending Directive 2003/87/EC, Regulations (EU) 2021/1058, (EU) 2021/1056, (EU) 2021/1057, (EU) No 1303/2013, (EU) No 223/2014, (EU) 2021/1060, (EU) 2021/523, (EU) 2021/695, (EU) 2021/697 and (EU) 2021/241 Industrial policy European Green Deal Europe fit for the digital age Single Market The EU has put in place over the last years a comprehensive set of instruments to support the decarbonisation and digitalisation of Europe. While the EU has been providing steady financing both to the green and digital transitions, the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1. Title of the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 251
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Proposal for a Regulation of the European Parliament and of the Council establishing the Strategic Technologies for Europe Platform (‘STEP’) and amending Directive 2003/87/EC, Regulations (EU) 2021/1058, (EU) 2021/1056, (EU) 2021/1057, (EU) No 1303/2013, (EU) No 223/2014, (EU) 2021/1060, (EU) 2021/523, (EU) 2021/695, (EU) 2021/697 and (EU) 2021/241 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Proposal for a Regulation of the European Parliament and of the Council establishing")
    thisalinea.textcontent.append("the Strategic Technologies for Europe Platform (‘STEP’) and amending Directive")
    thisalinea.textcontent.append("2003/87/EC, Regulations (EU) 2021/1058, (EU) 2021/1056, (EU) 2021/1057, (EU)")
    thisalinea.textcontent.append("No 1303/2013, (EU) No 223/2014, (EU) 2021/1060, (EU) 2021/523, (EU) 2021/695,")
    thisalinea.textcontent.append("(EU) 2021/697 and (EU) 2021/241")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2. Policy area(s) concerned"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 252
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Industrial policy European Green Deal Europe fit for the digital age Single Market "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Industrial policy")
    thisalinea.textcontent.append("European Green Deal")
    thisalinea.textcontent.append("Europe fit for the digital age")
    thisalinea.textcontent.append("Single Market")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.3. The proposal/initiative relates to:"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 253
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.4. Objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 254
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The EU has put in place over the last years a comprehensive set of instruments to support the decarbonisation and digitalisation of Europe. While the EU has been providing steady financing both to the green and digital transitions, the funds are generally spread across various spending programmes and following different rules. Ensuring coherence among these existing funds towards a common objective has the potential to enhance their effectiveness and accelerate the support to the industrial sectors critical for the twin transition. The STEP aims to strengthen European edge on critical and emerging technologies relevant to the green and digital transitions, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.1. General objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 255
    thisalinea.parentID = 254
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The EU has put in place over the last years a comprehensive set of instruments to support the decarbonisation and digitalisation of Europe. While the EU has been providing steady financing both to the green and digital transitions, the funds are generally spread across various spending programmes and following different rules. Ensuring coherence among these existing funds towards a common objective has the potential to enhance their effectiveness and accelerate the support to the industrial sectors critical for the twin transition. The STEP aims to strengthen European edge on critical and emerging technologies relevant to the green and digital transitions, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU has put in place over the last years a comprehensive set of instruments to")
    thisalinea.textcontent.append("support the decarbonisation and digitalisation of Europe. While the EU has been")
    thisalinea.textcontent.append("providing steady financing both to the green and digital transitions, the funds are")
    thisalinea.textcontent.append("generally spread across various spending programmes and following different rules.")
    thisalinea.textcontent.append("Ensuring coherence among these existing funds towards a common objective has the")
    thisalinea.textcontent.append("potential to enhance their effectiveness and accelerate the support to the industrial")
    thisalinea.textcontent.append("sectors critical for the twin transition.")
    thisalinea.textcontent.append("The STEP aims to strengthen European edge on critical and emerging technologies")
    thisalinea.textcontent.append("relevant to the green and digital transitions, from computing-related technologies,")
    thisalinea.textcontent.append("including microelectronics, quantum computing, and artificial intelligence; to")
    thisalinea.textcontent.append("biotechnology and biomanufacturing, and net-zero technologies.")
    thisalinea.textcontent.append("The STEP aims to achieve its objectives through the following means:")
    thisalinea.textcontent.append("3")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "1. Providing flexibility in existing instruments "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 256
    thisalinea.parentID = 255
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Providing flexibility in existing instruments "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Providing flexibility in existing instruments")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2. Reinforcing the firepower of existing instruments "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 257
    thisalinea.parentID = 255
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Reinforcing the firepower of existing instruments "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Reinforcing the firepower of existing instruments")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3. Creating synergies among instruments towards the common goal "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 258
    thisalinea.parentID = 255
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Creating synergies among instruments towards the common goal "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Creating synergies among instruments towards the common goal")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.2. Specific objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 259
    thisalinea.parentID = 254
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(a) supporting the development or manufacturing throughout the Union, or safeguarding and strengthening the respective value chains, of critical technologies in the following fields, provided those technologies meet certain conditions: (i) deep and digital technologies (ii) clean technologies (iii) biotechnologies (b) addressing shortages of labour and skills critical to all kinds of quality jpbs in support of the objective under point (a). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(a) supporting the development or manufacturing throughout the Union, or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 260
    thisalinea.parentID = 259
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) supporting the development or manufacturing throughout the Union, or safeguarding and strengthening the respective value chains, of critical technologies in the following fields, provided those technologies meet certain conditions: (i) deep and digital technologies (ii) clean technologies (iii) biotechnologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) supporting the development or manufacturing throughout the Union, or")
    thisalinea.textcontent.append("safeguarding and strengthening the respective value chains, of critical technologies in")
    thisalinea.textcontent.append("the following fields, provided those technologies meet certain conditions:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(i) deep and digital technologies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 261
    thisalinea.parentID = 260
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) deep and digital technologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) deep and digital technologies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(ii) clean technologies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 262
    thisalinea.parentID = 260
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) clean technologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) clean technologies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "(iii) biotechnologies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 263
    thisalinea.parentID = 260
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(iii) biotechnologies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iii) biotechnologies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(b) addressing shortages of labour and skills critical to all kinds of quality jpbs in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 264
    thisalinea.parentID = 259
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) addressing shortages of labour and skills critical to all kinds of quality jpbs in support of the objective under point (a). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) addressing shortages of labour and skills critical to all kinds of quality jpbs in")
    thisalinea.textcontent.append("support of the objective under point (a).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.3. Expected result(s) and impact"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 265
    thisalinea.parentID = 254
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The expected impact of the Platform includes a substantial strengthening of the European Union's industrial capabilities and competitiveness in the areas of clean, biotech and deeptech technologies. This impact is projected to reinforce the EU's position as a global leader in these critical areas ultimately enhancing the EU's economic growth, sustainable development and international competitiveness. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The expected impact of the Platform includes a substantial strengthening of the")
    thisalinea.textcontent.append("European Union's industrial capabilities and competitiveness in the areas of clean,")
    thisalinea.textcontent.append("biotech and deeptech technologies. This impact is projected to reinforce the EU's")
    thisalinea.textcontent.append("position as a global leader in these critical areas ultimately enhancing the EU's")
    thisalinea.textcontent.append("economic growth, sustainable development and international competitiveness.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.4. Indicators of performance"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 266
    thisalinea.parentID = 254
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Indicators:"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 267
    thisalinea.parentID = 254
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "1. Enterprises supported 2. Number of participants in trainings 3. Total investment mobilised 4. Number of jobs created or maintained "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "1. Enterprises supported "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 268
    thisalinea.parentID = 267
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Enterprises supported "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Enterprises supported")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "2. Number of participants in trainings "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 269
    thisalinea.parentID = 267
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Number of participants in trainings "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Number of participants in trainings")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3. Total investment mobilised "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 270
    thisalinea.parentID = 267
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Total investment mobilised "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Total investment mobilised")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "4. Number of jobs created or maintained "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 271
    thisalinea.parentID = 267
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Number of jobs created or maintained "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Number of jobs created or maintained")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.5. Grounds for the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 272
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "The Regulation should be fully applicable shortly after its adoption, i.e. the day following its publication in the Official Journal of the European Union. However, some actions will start as of the date of adoption of the proposal by the Commission: The two actions above should be able to produce results as of end 2023. Subject to the adoption of this proposal by the co-legislators, the Commission intends to deploy very quickly the additional resources in the selected programmes so that 4 beneficiaries could start receiving financial support or implementing additional EU guarantee as of 2024. - The Commission will "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.1. Requirement(s) to be met in the short or long term including a detailed timeline for roll-out of the implementation of the initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 273
    thisalinea.parentID = 272
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The Regulation should be fully applicable shortly after its adoption, i.e. the day following its publication in the Official Journal of the European Union. However, some actions will start as of the date of adoption of the proposal by the Commission: The two actions above should be able to produce results as of end 2023. Subject to the adoption of this proposal by the co-legislators, the Commission intends to deploy very quickly the additional resources in the selected programmes so that 4 beneficiaries could start receiving financial support or implementing additional EU guarantee as of 2024. - The Commission will "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The Regulation should be fully applicable shortly after its adoption, i.e. the day")
    thisalinea.textcontent.append("following its publication in the Official Journal of the European Union. However,")
    thisalinea.textcontent.append("some actions will start as of the date of adoption of the proposal by the Commission:")
    thisalinea.textcontent.append("The two actions above should be able to produce results as of end 2023.")
    thisalinea.textcontent.append("Subject to the adoption of this proposal by the co-legislators, the Commission intends")
    thisalinea.textcontent.append("to deploy very quickly the additional resources in the selected programmes so that")
    thisalinea.textcontent.append("4")
    thisalinea.textcontent.append("beneficiaries could start receiving financial support or implementing additional EU")
    thisalinea.textcontent.append("guarantee as of 2024.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- The Commission will start integrating the STEP objectives in the ongoing ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 274
    thisalinea.parentID = 273
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- The Commission will start integrating the STEP objectives in the ongoing implementation of programmes, such as under Horizon Europe or the Innovation Fund. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- The Commission will start integrating the STEP objectives in the ongoing")
    thisalinea.textcontent.append("implementation of programmes, such as under Horizon Europe or the Innovation")
    thisalinea.textcontent.append("Fund.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- The Commission is establishing the One-Stop-Shop as of now to act as the central ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 275
    thisalinea.parentID = 273
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- The Commission is establishing the One-Stop-Shop as of now to act as the central coordinator among EU instruments for the purpose of the Platform. The structure will grow over time to integrate additional resources. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- The Commission is establishing the One-Stop-Shop as of now to act as the central")
    thisalinea.textcontent.append("coordinator among EU instruments for the purpose of the Platform. The structure")
    thisalinea.textcontent.append("will grow over time to integrate additional resources.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.2. Added value of Union involvement (it may result from different factors, e.g. coordination gains, legal certainty, greater effectiveness or complementarities). For the purposes of this point 'added value of Union involvement' is the value resulting from Union intervention, which is additional to the value that would have been otherwise created by Member States alone."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 276
    thisalinea.parentID = 272
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The EU as whole is at the forefront for implementing the actions required to pursue the green and digital transitions. By acting together, Member States are better able to pool resources for achieving these objectives and reinforce the effectiveness of the actions. Sustaining the green and digital transitions with a strong industrial base requires a coordinated action among Member States, also in view of the global competition to attract capital and investments. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU as whole is at the forefront for implementing the actions required to pursue")
    thisalinea.textcontent.append("the green and digital transitions. By acting together, Member States are better able to")
    thisalinea.textcontent.append("pool resources for achieving these objectives and reinforce the effectiveness of the")
    thisalinea.textcontent.append("actions.")
    thisalinea.textcontent.append("Sustaining the green and digital transitions with a strong industrial base requires a")
    thisalinea.textcontent.append("coordinated action among Member States, also in view of the global competition to")
    thisalinea.textcontent.append("attract capital and investments.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.3. Lessons learned from similar experiences in the past"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 277
    thisalinea.parentID = 272
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The EU has adopted in previous years regulatory changes to accelerate the deployment of EU funds, for instance CARE and FAST CARE are examples where the cohesion funds have been subject to targeted changes to face emerging crisis. The EU has also adopted recently the REPowerEU Regulation to reinforce the firepower of an existing instrument, the Recovery and Resilience Facility, and flexibilise at the same time the possibility to use other funds for the REPowerEU purposes. These experiences have been taken into account in the design of this proposal. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The EU has adopted in previous years regulatory changes to accelerate the")
    thisalinea.textcontent.append("deployment of EU funds, for instance CARE and FAST CARE are examples where")
    thisalinea.textcontent.append("the cohesion funds have been subject to targeted changes to face emerging crisis.")
    thisalinea.textcontent.append("The EU has also adopted recently the REPowerEU Regulation to reinforce the")
    thisalinea.textcontent.append("firepower of an existing instrument, the Recovery and Resilience Facility, and")
    thisalinea.textcontent.append("flexibilise at the same time the possibility to use other funds for the REPowerEU")
    thisalinea.textcontent.append("purposes.")
    thisalinea.textcontent.append("These experiences have been taken into account in the design of this proposal.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.4. Compatibility with the Multiannual Financial Framework and possible synergies with other appropriate instruments"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 278
    thisalinea.parentID = 272
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "This Regulation creates the necessary conditions for a more effective, efficient and targeted use of existing EU funds in the name of greater support to STEP projects. The EU has put in place over the last years a comprehensive set of instruments to support the decarbonisation and digitalisation of Europe. The choice of streamlining and making a better use of existing instruments over creating a brand new instrument has two main advantages. First, timing. With the creation of a new instrument potentiallly taking a long time, bringing existing instruments together can be done much more quickly. This would be an "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Regulation creates the necessary conditions for a more effective, efficient and")
    thisalinea.textcontent.append("targeted use of existing EU funds in the name of greater support to STEP projects.")
    thisalinea.textcontent.append("The EU has put in place over the last years a comprehensive set of instruments to")
    thisalinea.textcontent.append("support the decarbonisation and digitalisation of Europe.")
    thisalinea.textcontent.append("The choice of streamlining and making a better use of existing instruments over")
    thisalinea.textcontent.append("creating a brand new instrument has two main advantages. First, timing. With the")
    thisalinea.textcontent.append("creation of a new instrument potentiallly taking a long time, bringing existing")
    thisalinea.textcontent.append("instruments together can be done much more quickly. This would be an indisputable")
    thisalinea.textcontent.append("advantage for the beneficiaries of EU funding as they would have the chance to reap")
    thisalinea.textcontent.append("the benefits of EU funding more swiftly. Second, blending different sources of")
    thisalinea.textcontent.append("financing – under direct, indirect and shared management – could also lead to a more")
    thisalinea.textcontent.append("efficient use of resources.")
    thisalinea.textcontent.append("While the STEP proposal is fully embedded in the exising MFF and the current")
    thisalinea.textcontent.append("instruments, it also requires additional resources to achieve the objectives. As such,")
    thisalinea.textcontent.append("as part of the mid-term review of the MFF, the Commission is proposing targeted")
    thisalinea.textcontent.append("reinforcements for the STEP.")
    thisalinea.textcontent.append("5")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.5. Assessment of the different available financing options, including scope for redeployment"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 279
    thisalinea.parentID = 272
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "N/A 6 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("N/A")
    thisalinea.textcontent.append("6")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.6. Duration and financial impact of the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 280
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = " limited duration  unlimited duration – in effect from [DD/MM]YYYY to 31/12/2030 –  Financial impact from 2023 to 2027 for commitment appropriations and from 2023 to 2030 for payment appropriations. – Implementation with a start-up period from YYYY to YYYY, – followed by full-scale operation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" limited duration")
    thisalinea.textcontent.append(" unlimited duration")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– in effect from [DD/MM]YYYY to 31/12/2030 "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 281
    thisalinea.parentID = 280
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– in effect from [DD/MM]YYYY to 31/12/2030 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– in effect from [DD/MM]YYYY to 31/12/2030")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  Financial impact from 2023 to 2027 for commitment appropriations and from ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 282
    thisalinea.parentID = 280
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  Financial impact from 2023 to 2027 for commitment appropriations and from 2023 to 2030 for payment appropriations. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  Financial impact from 2023 to 2027 for commitment appropriations and from")
    thisalinea.textcontent.append("2023 to 2030 for payment appropriations.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Implementation with a start-up period from YYYY to YYYY, "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 283
    thisalinea.parentID = 280
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– Implementation with a start-up period from YYYY to YYYY, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Implementation with a start-up period from YYYY to YYYY,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– followed by full-scale operation. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 284
    thisalinea.parentID = 280
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– followed by full-scale operation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– followed by full-scale operation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.7. Method(s) of budget implementation planned73"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 285
    thisalinea.parentID = 250
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = " Direct management by the Commission  Shared management with the Member States  Indirect management by entrusting budget implementation tasks to: –  by its departments, including by its staff in the Union delegations; –  by the executive agencies –  third countries or the bodies they have designated; –  international organisations and their agencies (to be specified); – the EIB and the European Investment Fund; –  bodies referred to in Articles 70 and 71 of the Financial Regulation; –  public law bodies; –  bodies governed by private law with a public service mission "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Direct management by the Commission")
    thisalinea.textcontent.append(" Shared management with the Member States")
    thisalinea.textcontent.append(" Indirect management by entrusting budget implementation tasks to:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  by its departments, including by its staff in the Union delegations; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 286
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  by its departments, including by its staff in the Union delegations; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  by its departments, including by its staff in the Union delegations;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  by the executive agencies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 287
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  by the executive agencies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  by the executive agencies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  third countries or the bodies they have designated; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 288
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "–  third countries or the bodies they have designated; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  third countries or the bodies they have designated;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  international organisations and their agencies (to be specified); "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 289
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "–  international organisations and their agencies (to be specified); "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  international organisations and their agencies (to be specified);")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– the EIB and the European Investment Fund; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 290
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "– the EIB and the European Investment Fund; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– the EIB and the European Investment Fund;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  bodies referred to in Articles 70 and 71 of the Financial Regulation; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 291
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "–  bodies referred to in Articles 70 and 71 of the Financial Regulation; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  bodies referred to in Articles 70 and 71 of the Financial Regulation;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  public law bodies; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 292
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "–  public law bodies; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  public law bodies;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  bodies governed by private law with a public service mission to the extent ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 293
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "–  bodies governed by private law with a public service mission to the extent that they are provided with adequate financial guarantees; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  bodies governed by private law with a public service mission to the extent that")
    thisalinea.textcontent.append("they are provided with adequate financial guarantees;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  bodies governed by the private law of a Member State that are entrusted ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 294
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "–  bodies governed by the private law of a Member State that are entrusted with the implementation of a public-private partnership and that are provided with adequate financial guarantees; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  bodies governed by the private law of a Member State that are entrusted with")
    thisalinea.textcontent.append("the implementation of a public-private partnership and that are provided with")
    thisalinea.textcontent.append("adequate financial guarantees;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  bodies or persons entrusted with the implementation of specific actions in the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 295
    thisalinea.parentID = 285
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "–  bodies or persons entrusted with the implementation of specific actions in the CFSP pursuant to Title V of the TEU, and identified in the relevant basic act. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  bodies or persons entrusted with the implementation of specific actions in the")
    thisalinea.textcontent.append("CFSP pursuant to Title V of the TEU, and identified in the relevant basic act.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. MANAGEMENT MEASURES"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 296
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 30
    thisalinea.summary = "In accordance with Article 7 of the STEP Regulation, the Commission shall provide an annual report to the European Parliament and the Council on the implementation of the STEP. The annual report shall provide consolidated information on the progress made in implementing the STEP objectives under each of the programmes referred to in Article 2, including: 7 In addition, in accordance with Article 8 of the STEP Regulation, the Commission will draw up an evaluation report on the implementation of the Fund no later than 31/12/2025 and submit it to the European Parlimament and the Council. The evaluation report shall, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.1. Monitoring and reporting rules"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 297
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "In accordance with Article 7 of the STEP Regulation, the Commission shall provide an annual report to the European Parliament and the Council on the implementation of the STEP. The annual report shall provide consolidated information on the progress made in implementing the STEP objectives under each of the programmes referred to in Article 2, including: 7 In addition, in accordance with Article 8 of the STEP Regulation, the Commission will draw up an evaluation report on the implementation of the Fund no later than 31/12/2025 and submit it to the European Parlimament and the Council. The evaluation report shall, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In accordance with Article 7 of the STEP Regulation, the Commission shall provide")
    thisalinea.textcontent.append("an annual report to the European Parliament and the Council on the implementation")
    thisalinea.textcontent.append("of the STEP. The annual report shall provide consolidated information on the")
    thisalinea.textcontent.append("progress made in implementing the STEP objectives under each of the programmes")
    thisalinea.textcontent.append("referred to in Article 2, including:")
    thisalinea.textcontent.append("7")
    thisalinea.textcontent.append("In addition, in accordance with Article 8 of the STEP Regulation, the Commission")
    thisalinea.textcontent.append("will draw up an evaluation report on the implementation of the Fund no later than")
    thisalinea.textcontent.append("31/12/2025 and submit it to the European Parlimament and the Council. The")
    thisalinea.textcontent.append("evaluation report shall, in particular, assess to which extent the objectives have been")
    thisalinea.textcontent.append("achieved, the efficiency of the use of the resources and the European added value. It")
    thisalinea.textcontent.append("shall also consider the continued relevance of all objectives and actions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) overall STEP expenditure financed under the respective programmes "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 298
    thisalinea.parentID = 297
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) overall STEP expenditure financed under the respective programmes "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) overall STEP expenditure financed under the respective programmes")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the performance of the STEP investments based on the common indicators "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 299
    thisalinea.parentID = 297
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the performance of the STEP investments based on the common indicators "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the performance of the STEP investments based on the common indicators")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.2. Management and control system(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 300
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The STEP shall be implemented in accordance with the management mode, payment modalities and control strategy applicable to the programmes referred to in Article 3 of the Regulation. The STEP will rely on existing EU instruments, including their control set-ups, and as such should not result in additional risks. The budget will be implemented in accordance with the management mode, payment modalities and control strategy applicable to the programmes referred to in Article 3 of the regulation. This approach guarantees an efficient implementation of funds, using proven control systems that are already established. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.1. Justification of the management mode(s), the funding implementation mechanism(s), the payment modalities and the control strategy proposed"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 301
    thisalinea.parentID = 300
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The STEP shall be implemented in accordance with the management mode, payment modalities and control strategy applicable to the programmes referred to in Article 3 of the Regulation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The STEP shall be implemented in accordance with the management mode, payment")
    thisalinea.textcontent.append("modalities and control strategy applicable to the programmes referred to in Article 3")
    thisalinea.textcontent.append("of the Regulation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.2. Information concerning the risks identified and the internal control system(s) set up to mitigate them"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 302
    thisalinea.parentID = 300
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The STEP will rely on existing EU instruments, including their control set-ups, and as such should not result in additional risks. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The STEP will rely on existing EU instruments, including their control set-ups, and")
    thisalinea.textcontent.append("as such should not result in additional risks.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = '2.2.3. Estimation and justification of the cost-effectiveness of the controls (ratio of "control costs ÷ value of the related funds managed"), and assessment of the expected levels of risk of error (at payment & at closure)'
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 303
    thisalinea.parentID = 300
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The budget will be implemented in accordance with the management mode, payment modalities and control strategy applicable to the programmes referred to in Article 3 of the regulation. This approach guarantees an efficient implementation of funds, using proven control systems that are already established. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The budget will be implemented in accordance with the management mode, payment")
    thisalinea.textcontent.append("modalities and control strategy applicable to the programmes referred to in Article 3")
    thisalinea.textcontent.append("of the regulation. This approach guarantees an efficient implementation of funds,")
    thisalinea.textcontent.append("using proven control systems that are already established.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.3. Measures to prevent fraud and irregularities"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 304
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The Platform shall be implemented through the programmes referred to in Article 3 of the Regulation. The prevention and protection measures will be those already in place for those programmes. 8 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The Platform shall be implemented through the programmes referred to in Article 3")
    thisalinea.textcontent.append("of the Regulation. The prevention and protection measures will be those already in")
    thisalinea.textcontent.append("place for those programmes.")
    thisalinea.textcontent.append("8")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. ESTIMATED FINANCIAL IMPACT OF THE PROPOSAL/INITIATIVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 305
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 31
    thisalinea.summary = " Existing budget lines 2a 3 09.03.01 Just Transition Fund (JTF) - Diff No No No Yes 9  New budget lines requested 11 12 13 14 15 This section should be filled in using the 'budget data of an administrative nature' to be firstly introduced in the Annex to the Legislative Financial Statement (Annex 5 to the Commission decision on the internal rules for the implementation of the Commission section of the general budget of the European Union), which is uploaded to DECIDE for interservice consultation purposes. –  The proposal/initiative does not require the use of operational appropriations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.1. Heading(s) of the multiannual financial framework and expenditure budget line(s) affected"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 306
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = " Existing budget lines 2a 3 09.03.01 Just Transition Fund (JTF) - Diff No No No Yes 9  New budget lines requested "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = " Existing budget lines "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 307
    thisalinea.parentID = 306
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = " Existing budget lines "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Existing budget lines")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "In order of multiannual financial framework headings and budget lines."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 308
    thisalinea.parentID = 306
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "2a 3 09.03.01 Just Transition Fund (JTF) - Diff No No No Yes 9  New budget lines requested "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2a")
    thisalinea.textcontent.append("3 09.03.01 Just Transition Fund (JTF) - Diff No No No Yes")
    thisalinea.textcontent.append("9")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = " New budget lines requested "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 309
    thisalinea.parentID = 308
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = " New budget lines requested "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" New budget lines requested")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "In order of multiannual financial framework headings and budget lines."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 310
    thisalinea.parentID = 306
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("10")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.2. Estimated financial impact of the proposal on appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 311
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "11 12 13 14 15 This section should be filled in using the 'budget data of an administrative nature' to be firstly introduced in the Annex to the Legislative Financial Statement (Annex 5 to the Commission decision on the internal rules for the implementation of the Commission section of the general budget of the European Union), which is uploaded to DECIDE for interservice consultation purposes. –  The proposal/initiative does not require the use of operational appropriations – The proposal/initiative requires the use of operational appropriations, as explained below: 16 17 18 –  The proposal/initiative does not require the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.1. Summary of estimated impact on operational appropriations"
    thisalinea.titlefontsize = "11.999999999999943"
    thisalinea.nativeID = 312
    thisalinea.parentID = 311
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "11 12 13 14 15 This section should be filled in using the 'budget data of an administrative nature' to be firstly introduced in the Annex to the Legislative Financial Statement (Annex 5 to the Commission decision on the internal rules for the implementation of the Commission section of the general budget of the European Union), which is uploaded to DECIDE for interservice consultation purposes. –  The proposal/initiative does not require the use of operational appropriations – The proposal/initiative requires the use of operational appropriations, as explained below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("11")
    thisalinea.textcontent.append("12")
    thisalinea.textcontent.append("13")
    thisalinea.textcontent.append("14")
    thisalinea.textcontent.append("15")
    thisalinea.textcontent.append("This section should be filled in using the 'budget data of an administrative nature' to be firstly introduced in the Annex to the Legislative")
    thisalinea.textcontent.append("Financial Statement (Annex 5 to the Commission decision on the internal rules for the implementation of the Commission section of the general")
    thisalinea.textcontent.append("budget of the European Union), which is uploaded to DECIDE for interservice consultation purposes.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "–  The proposal/initiative does not require the use of operational appropriations "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 313
    thisalinea.parentID = 312
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  The proposal/initiative does not require the use of operational appropriations "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative does not require the use of operational appropriations")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "– The proposal/initiative requires the use of operational appropriations, as explained below: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 314
    thisalinea.parentID = 312
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– The proposal/initiative requires the use of operational appropriations, as explained below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The proposal/initiative requires the use of operational appropriations, as explained below:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.2. Estimated output funded with operational appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 315
    thisalinea.parentID = 311
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "16 17 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("16")
    thisalinea.textcontent.append("17")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.3. Summary of estimated impact on administrative appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 316
    thisalinea.parentID = 311
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "18 –  The proposal/initiative does not require the use of appropriations of an administrative nature –  The proposal/initiative requires the use of appropriations of an administrative nature, as explained below: 19 –  The proposal/initiative does not require the use of human resources. –  The proposal/initiative requires the use of human resources, as explained below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("18")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  The proposal/initiative does not require the use of appropriations of an ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 317
    thisalinea.parentID = 316
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  The proposal/initiative does not require the use of appropriations of an administrative nature "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative does not require the use of appropriations of an")
    thisalinea.textcontent.append("administrative nature")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  The proposal/initiative requires the use of appropriations of an administrative ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 318
    thisalinea.parentID = 316
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  The proposal/initiative requires the use of appropriations of an administrative nature, as explained below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative requires the use of appropriations of an administrative")
    thisalinea.textcontent.append("nature, as explained below:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "3.2.3.1. Estimated requirements of human resources"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 319
    thisalinea.parentID = 316
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "19 –  The proposal/initiative does not require the use of human resources. –  The proposal/initiative requires the use of human resources, as explained below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("19")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "–  The proposal/initiative does not require the use of human resources. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 320
    thisalinea.parentID = 319
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  The proposal/initiative does not require the use of human resources. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative does not require the use of human resources.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 5
    thisalinea.texttitle = "–  The proposal/initiative requires the use of human resources, as explained ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 321
    thisalinea.parentID = 319
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  The proposal/initiative requires the use of human resources, as explained below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative requires the use of human resources, as explained")
    thisalinea.textcontent.append("below:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.4. Compatibility with the current multiannual financial framework"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 322
    thisalinea.parentID = 311
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The proposal/initiative: –  can be fully financed through redeployment within the relevant heading of the Multiannual Financial Framework (MFF). –  requires use of the unallocated margin under the relevant heading of the MFF and/or use of the special instruments as defined in the MFF Regulation. –  requires a revision of the MFF. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal/initiative:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  can be fully financed through redeployment within the relevant heading of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 323
    thisalinea.parentID = 322
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  can be fully financed through redeployment within the relevant heading of the Multiannual Financial Framework (MFF). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  can be fully financed through redeployment within the relevant heading of the")
    thisalinea.textcontent.append("Multiannual Financial Framework (MFF).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  requires use of the unallocated margin under the relevant heading of the MFF ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 324
    thisalinea.parentID = 322
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  requires use of the unallocated margin under the relevant heading of the MFF and/or use of the special instruments as defined in the MFF Regulation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  requires use of the unallocated margin under the relevant heading of the MFF")
    thisalinea.textcontent.append("and/or use of the special instruments as defined in the MFF Regulation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  requires a revision of the MFF. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 325
    thisalinea.parentID = 322
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "–  requires a revision of the MFF. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  requires a revision of the MFF.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.5. Third-party contributions"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 326
    thisalinea.parentID = 311
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "The proposal/initiative: 20 –  does not provide for co-financing by third parties –  provides for the co-financing by third parties estimated below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal/initiative:")
    thisalinea.textcontent.append("20")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  does not provide for co-financing by third parties "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 327
    thisalinea.parentID = 326
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  does not provide for co-financing by third parties "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  does not provide for co-financing by third parties")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "–  provides for the co-financing by third parties estimated below: "
    thisalinea.titlefontsize = "11.999999999999943"
    thisalinea.nativeID = 328
    thisalinea.parentID = 326
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  provides for the co-financing by third parties estimated below: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  provides for the co-financing by third parties estimated below:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.3. Estimated impact on revenue"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 329
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "EUR million (to three decimal places) 21 –  The proposal/initiative has no financial impact on revenue. –  The proposal/initiative has the following financial impact: –  on own resources –  on other revenue – please indicate, if the revenue is assigned to expenditure lines  "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("EUR million (to three decimal places)")
    thisalinea.textcontent.append("21")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  The proposal/initiative has no financial impact on revenue. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 330
    thisalinea.parentID = 329
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  The proposal/initiative has no financial impact on revenue. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative has no financial impact on revenue.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  The proposal/initiative has the following financial impact: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 331
    thisalinea.parentID = 329
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  The proposal/initiative has the following financial impact: "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  The proposal/initiative has the following financial impact:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  on own resources "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 332
    thisalinea.parentID = 329
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "–  on own resources "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  on own resources")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  on other revenue "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 333
    thisalinea.parentID = 329
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "–  on other revenue "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  on other revenue")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– please indicate, if the revenue is assigned to expenditure lines  "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 334
    thisalinea.parentID = 329
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "– please indicate, if the revenue is assigned to expenditure lines  "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– please indicate, if the revenue is assigned to expenditure lines ")
    alineas.append(thisalinea)

    return alineas
