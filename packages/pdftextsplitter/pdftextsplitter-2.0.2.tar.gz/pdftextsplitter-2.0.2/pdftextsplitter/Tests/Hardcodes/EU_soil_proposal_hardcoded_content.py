import sys
sys.path.insert(1, "../../")

from TextPart.textalinea import textalinea
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

def hardcodedalineas_EU_soil_proposal() -> list[textalinea]:
    """
    This code holds the content of the textalineas-array in the textsplitter-class
    for the document EU_soil_proposal
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
    thisalinea.texttitle = "EU_soil_proposal"
    thisalinea.titlefontsize = "1000.0"
    thisalinea.nativeID = 0
    thisalinea.parentID = -1
    thisalinea.alineatype = texttype.TITLE
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Soil is a vital, limited, non-renewable and irreplaceable resource. Healthy soils form the essential basis for our economy, society and environment as they produce food, increase our resilience to climate change, to extreme weather events, drought and floods and support our well-being. Healthy soils store carbon, have more capacity to absorb, store and filter water and provide vital services such as safe and nutritious food and biomass for non-food bioeconomy sectors. Scientific evidence1 indicates that about 60 to 70% of soils in the EU are currently in an unhealthy state. All Member States are facing the problem of soil degradation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
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
    thisalinea.summary = "Soil is a vital, limited, non-renewable and irreplaceable resource. Healthy soils form the essential basis for our economy, society and environment as they produce food, increase our resilience to climate change, to extreme weather events, drought and floods and support our well-being. Healthy soils store carbon, have more capacity to absorb, store and filter water and provide vital services such as safe and nutritious food and biomass for non-food bioeconomy sectors. Scientific evidence1 indicates that about 60 to 70% of soils in the EU are currently in an unhealthy state. All Member States are facing the problem of soil degradation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Reasons for and objectives of the proposal"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 3
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Soil is a vital, limited, non-renewable and irreplaceable resource. Healthy soils form the essential basis for our economy, society and environment as they produce food, increase our resilience to climate change, to extreme weather events, drought and floods and support our well-being. Healthy soils store carbon, have more capacity to absorb, store and filter water and provide vital services such as safe and nutritious food and biomass for non-food bioeconomy sectors. Scientific evidence1 indicates that about 60 to 70% of soils in the EU are currently in an unhealthy state. All Member States are facing the problem of soil degradation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Soil is a vital, limited, non-renewable and irreplaceable resource. Healthy soils form the")
    thisalinea.textcontent.append("essential basis for our economy, society and environment as they produce food, increase our")
    thisalinea.textcontent.append("resilience to climate change, to extreme weather events, drought and floods and support our")
    thisalinea.textcontent.append("well-being. Healthy soils store carbon, have more capacity to absorb, store and filter water")
    thisalinea.textcontent.append("and provide vital services such as safe and nutritious food and biomass for non-food")
    thisalinea.textcontent.append("bioeconomy sectors.")
    thisalinea.textcontent.append("Scientific evidence1 indicates that about 60 to 70% of soils in the EU are currently in an")
    thisalinea.textcontent.append("unhealthy state. All Member States are facing the problem of soil degradation. Degradation")
    thisalinea.textcontent.append("processes are continuing and worsening. The drivers and impacts of the problem go beyond")
    thisalinea.textcontent.append("country borders, reducing the soil’s capacity to provide these vital services throughout the EU")
    thisalinea.textcontent.append("and neighbouring countries. This creates risks for human health, the environment, climate,")
    thisalinea.textcontent.append("economy and society, including risks for food security, water quality, increased impacts from")
    thisalinea.textcontent.append("flooding and droughts, biomass production, carbon emissions and a loss of biodiversity.")
    thisalinea.textcontent.append("The unprovoked and unjustified Russian war of aggression against Ukraine has destabilised")
    thisalinea.textcontent.append("global food systems, intensified food security risks and vulnerabilities across the world, and")
    thisalinea.textcontent.append("amplified the EU’s need to make its food systems sustainable for centuries to come. The")
    thisalinea.textcontent.append("trends and combination of the different drivers impacting food security draw attention to the")
    thisalinea.textcontent.append("fact that availability, access (affordability), utilisation, and stability cannot be taken for")
    thisalinea.textcontent.append("granted in the short or the long term2. In this context, fertile soils are of geo-strategic")
    thisalinea.textcontent.append("importance to secure our access to sufficient, nutritious and affordable food in the long-term.")
    thisalinea.textcontent.append("The food supply chain is highly interconnected and dependant at global level and the EU is an")
    thisalinea.textcontent.append("important global player on international food markets. To produce sufficient food for a global")
    thisalinea.textcontent.append("population that is expected to grow to 9-10 billion people in 2050, fertile soils are a key asset.")
    thisalinea.textcontent.append("Since 95% of our food is directly or indirectly produced on this precious finite natural")
    thisalinea.textcontent.append("resource, soil degradation has a direct impact on food security and the cross-border food")
    thisalinea.textcontent.append("markets.")
    thisalinea.textcontent.append("Pressure on soil and land is increasing globally. In the EU, 4.2% of the territory has been")
    thisalinea.textcontent.append("artificialized by land take; land take and soil sealing continue predominantly at the expense of")
    thisalinea.textcontent.append("agricultural land. In addition, soil degradation affects the potential long-term fertility of")
    thisalinea.textcontent.append("agricultural soils. It is estimated that between 61% and 73% of agricultural soils in the EU is")
    thisalinea.textcontent.append("affected by erosion, loss of organic carbon, nutrient (nitrogen) exceedances, compaction or")
    thisalinea.textcontent.append("secondary salinisation (or a combination of these threats). For instance, soil compaction can")
    thisalinea.textcontent.append("lower crop yields by 2.5-15 %. Without sustainable management and action to regenerate")
    thisalinea.textcontent.append("soils, deteriorating soil health will be a central factor in future food security crises.")
    thisalinea.textcontent.append("Healthy soils are essential for farmers and the agronomic ecosystem overall. Maintaining or")
    thisalinea.textcontent.append("increasing soil fertility over the long-term contributes to stable or even higher yields of crops,")
    thisalinea.textcontent.append("1")
    thisalinea.textcontent.append("feed and biomass required for non-food bioeconomy sectors contributing to the de-")
    thisalinea.textcontent.append("fossilization of our economy3, and gives farmers long-term production security and business")
    thisalinea.textcontent.append("prospects. The availability of healthy and fertile soils and land is crucial in the transition")
    thisalinea.textcontent.append("towards a sustainable bioeconomy and can therefore help increase and preserve the value of")
    thisalinea.textcontent.append("the land. Measures to increase soil fertility can also reduce farms’ operational costs, such as")
    thisalinea.textcontent.append("the cost of inputs or machinery. Farmers can receive financial support for certain practices")
    thisalinea.textcontent.append("e.g. under the Common Agricultural Policy (CAP) or the proposal for an EU carbon removal")
    thisalinea.textcontent.append("certification framework4.")
    thisalinea.textcontent.append("Soil degradation also harms human health. Airborne particulate matter produced by wind")
    thisalinea.textcontent.append("erosion causes or worsens respiratory and cardiovascular diseases. Sealed soils prolong the")
    thisalinea.textcontent.append("duration of high temperatures during heat waves and have less capacity to act as a sink for")
    thisalinea.textcontent.append("pollutants. Contaminated soils also affect food safety. For example, approximately 21% of")
    thisalinea.textcontent.append("agricultural soils in the EU contain cadmium concentrations in the topsoil that exceed the")
    thisalinea.textcontent.append("limit for groundwater. The recreational value of the environment and nature, with links to our")
    thisalinea.textcontent.append("physical and mental health, is also supported by healthy and sustainably managed soils. This")
    thisalinea.textcontent.append("is valuable both in the countryside, and especially in urban areas where the adoption of")
    thisalinea.textcontent.append("sustainable management practices can help create healthy green spaces and reduce heat")
    thisalinea.textcontent.append("islands, improve air quality and housing conditions. Improving soil health is key to increase")
    thisalinea.textcontent.append("the EU’s resilience to adverse events and adaptation to climate change. Europe’s resilience to")
    thisalinea.textcontent.append("climate change depends on the level of soil organic matter and fertility, water retention and")
    thisalinea.textcontent.append("filtering capacity, and resistance to erosion. Carbon farming practices help store CO2 in the")
    thisalinea.textcontent.append("soil and contribute to mitigating climate change. The capacity of soils to retain water helps")
    thisalinea.textcontent.append("both prevent and respond to disaster risks. When soils can absorb more rainfall, it reduces the")
    thisalinea.textcontent.append("intensity of flooding and alleviates the negative effects of drought periods. Some soil bacteria,")
    thisalinea.textcontent.append("part of the biodiversity of healthy soils, can also help crop plants tolerate drought.")
    thisalinea.textcontent.append("As the extreme weather and climate-related hazards intensify, the risk of wildfires is")
    thisalinea.textcontent.append("increasing across Europe. The conditions that heighten the fire risk are set to increase with")
    thisalinea.textcontent.append("climate change, notably heat and humidity of ecosystems, including soils. Healthy soils with")
    thisalinea.textcontent.append("functional water retention capacity also support healthy forest ecosystems that are more")
    thisalinea.textcontent.append("resilient to wildfires. At the same time, wildfires can cause soil degradation, leading to")
    thisalinea.textcontent.append("increased risks of soil erosion, landslides and floods. Strengthening the knowledge base on")
    thisalinea.textcontent.append("soils can contribute to improving disaster risk assessments that recognise the multi-faceted")
    thisalinea.textcontent.append("roles that soils play in mitigating disasters. Measures to strengthen soil health build resilience")
    thisalinea.textcontent.append("to future stress brought on by climate change.")
    thisalinea.textcontent.append("Current EU and national policies have made positive contributions to improving soil health.")
    thisalinea.textcontent.append("But they do not tackle all the drivers of soil degradation and therefore significant gaps remain.")
    thisalinea.textcontent.append("Soils form very slowly (e.g. it takes 500 years or more to create 2,5 cm of new topsoil), but")
    thisalinea.textcontent.append("soil health can be maintained or improved if the right measures are taken and put into")
    thisalinea.textcontent.append("practice.")
    thisalinea.textcontent.append("In this context, the European Green Deal5 sets out an ambitious roadmap to transform the EU")
    thisalinea.textcontent.append("into a fair and prosperous society, with a modern, resource-efficient and competitive")
    thisalinea.textcontent.append("2")
    thisalinea.textcontent.append("economy, aiming to protect, conserve and enhance the EU’s natural capital, and to protect the")
    thisalinea.textcontent.append("health and well-being of citizens from environment-related risks and impacts. As part of the")
    thisalinea.textcontent.append("European Green Deal, the Commission adopted an EU Biodiversity Strategy for 20306, a Zero")
    thisalinea.textcontent.append("Pollution Action Plan7, an EU Climate Adaptation Strategy8 and an EU Soil Strategy for")
    thisalinea.textcontent.append("20309.")
    thisalinea.textcontent.append("The EU Biodiversity Strategy for 2030 stated that it is essential to step up efforts to protect")
    thisalinea.textcontent.append("soil fertility, reduce soil erosion and increase soil organic matter by adopting sustainable soil")
    thisalinea.textcontent.append("management practices. It also stated that significant progress is needed to identify")
    thisalinea.textcontent.append("contaminated sites, restore degraded soils, define the conditions for good ecological status, set")
    thisalinea.textcontent.append("restoration objectives, and improve the monitoring of soil health. The Biodiversity Strategy")
    thisalinea.textcontent.append("also announced the plan to update the 2006 Soil Thematic Strategy to tackle soil degradation")
    thisalinea.textcontent.append("and fulfil EU and international commitments on land-degradation neutrality.")
    thisalinea.textcontent.append("The EU Soil Strategy for 2030 sets out the long-term vision to have all soils in healthy")
    thisalinea.textcontent.append("condition by 2050, to make protection, sustainable use and restoration of soils the norm and")
    thisalinea.textcontent.append("proposes a combination of voluntary and legislative actions to achieve these aims. The")
    thisalinea.textcontent.append("Strategy announced that the Commission would propose a Soil Health Law underpinned by an")
    thisalinea.textcontent.append("impact assessment which should analyse several aspects such as indicators and values for soil")
    thisalinea.textcontent.append("health, provisions for monitoring soils and requirements for a sustainable use of soils.")
    thisalinea.textcontent.append("The 8th Environment Action Programme10 set the priority objective that by 2050 at the latest,")
    thisalinea.textcontent.append("people live well, within planetary boundaries in a well-being economy where nothing is")
    thisalinea.textcontent.append("wasted, growth is regenerative, the EU has achieved climate neutrality and has significantly")
    thisalinea.textcontent.append("reduced inequalities. Some of the enabling conditions needed to meet that objective include")
    thisalinea.textcontent.append("tackling soil degradation and ensuring the protection and sustainable use of soil, including by")
    thisalinea.textcontent.append("a dedicated legislative proposal on soil health.")
    thisalinea.textcontent.append("Institutional stakeholders have called for policy changes. The European Parliament11 called on")
    thisalinea.textcontent.append("the Commission to develop an EU legal framework for soil. It should include definitions and")
    thisalinea.textcontent.append("criteria for good soil status and sustainable use, objectives, harmonised indicators, a")
    thisalinea.textcontent.append("methodology for monitoring and reporting, targets, measures, and financial resources. The")
    thisalinea.textcontent.append("Council of the EU 12 supported the Commission in stepping up efforts to better protect soils")
    thisalinea.textcontent.append("and reaffirmed its commitment to land degradation neutrality. Furthermore, the European")
    thisalinea.textcontent.append("3")
    thisalinea.textcontent.append("Committee of the Regions 13, the European and Economic Social Committee 14 and the")
    thisalinea.textcontent.append("European Court of Auditors 15 all called on the Commission to develop a legal framework for")
    thisalinea.textcontent.append("the sustainable use of soil.")
    thisalinea.textcontent.append("The importance of soil health has also been recognised at global level. The EU has made")
    thisalinea.textcontent.append("commitments in the international context of the three Rio Conventions to address soils")
    thisalinea.textcontent.append("affected by desertification (UN Convention to Combat Desertification), to contribute to")
    thisalinea.textcontent.append("climate change mitigation (UN Framework Convention on Climate Change) and to constitute")
    thisalinea.textcontent.append("an important habitat for biodiversity (Convention on Biological Diversity). Restoring,")
    thisalinea.textcontent.append("maintaining and enhancing soil health is a target in the new Kunming-Montreal Global")
    thisalinea.textcontent.append("Biodiversity Framework.")
    thisalinea.textcontent.append("Soil health also directly contributes to the achievement of several UN Sustainable")
    thisalinea.textcontent.append("Development Goals16 (SDGs), in particular SDG 15.3. This goal aims to combat")
    thisalinea.textcontent.append("desertification, restore degraded land and soil, including land affected by desertification,")
    thisalinea.textcontent.append("drought and floods, and strive to achieve a land degradation-neutral world by 2030.")
    thisalinea.textcontent.append("There is currently a lack of comprehensive and harmonized data on soil health from soil")
    thisalinea.textcontent.append("monitoring. Some Member States have soil monitoring schemes in place, but they are")
    thisalinea.textcontent.append("fragmented, not representative and not harmonised. Member States apply different sampling")
    thisalinea.textcontent.append("methods, frequencies and densities, and use different metrics and analytical methods,")
    thisalinea.textcontent.append("resulting in a lack of consistency and comparability across the EU.")
    thisalinea.textcontent.append("For all these reasons, this proposal puts in place a solid and coherent soil monitoring")
    thisalinea.textcontent.append("framework for all soils across the EU, which will address the current gap of knowledge on")
    thisalinea.textcontent.append("soils. It should be an integrated monitoring system based on EU level, Member State and")
    thisalinea.textcontent.append("private data. This data will be based on a common definition of what constitutes a healthy soil")
    thisalinea.textcontent.append("and will underpin the sustainable management of soils, to maintain or enhance soil health, and")
    thisalinea.textcontent.append("thus to achieve healthy and resilient soils everywhere across the EU by 2050.")
    thisalinea.textcontent.append("The soil monitoring framework is crucial to provide the data and information needed to define")
    thisalinea.textcontent.append("the right measures. This data is also likely to lead to technological development and")
    thisalinea.textcontent.append("innovation and stimulate academic and industrial research, for example artificial intelligence")
    thisalinea.textcontent.append("solutions based on data from sensing systems and field-based measuring systems. Demand for")
    thisalinea.textcontent.append("soil analysis services will also grow, consolidating businesses and the position of specialised")
    thisalinea.textcontent.append("SMEs in the EU. It will also support the development of remote sensing for soil and enable")
    thisalinea.textcontent.append("the Commission to pool resources, based on current mechanisms and technology (LUCAS,")
    thisalinea.textcontent.append("Copernicus) to offer cost-efficient services to interested Member States. This technological")
    thisalinea.textcontent.append("progress is expected to give farmers and foresters easier access to soil data, and also lead to a")
    thisalinea.textcontent.append("wider range, better availability and more affordable technical support for sustainable soil")
    thisalinea.textcontent.append("management, including decision support tools.")
    thisalinea.textcontent.append("4")
    thisalinea.textcontent.append("Member States and EU bodies could use soil health data with sufficient granularity to")
    thisalinea.textcontent.append("improve monitoring and trend analysis of drought and disaster management and resilience17.")
    thisalinea.textcontent.append("Those data would enhance prevention and therefore contribute to a better response to")
    thisalinea.textcontent.append("disasters. Granular soil health data would also be a useful resource for climate change")
    thisalinea.textcontent.append("mitigation and adaptation policy implementation, also in relation to food security, and")
    thisalinea.textcontent.append("pressures on human health and biodiversity.")
    thisalinea.textcontent.append("The application of sustainable management practices will help Member States ensure that")
    thisalinea.textcontent.append("soils will have the capacity to deliver the multiple ecosystems services that are vital both for")
    thisalinea.textcontent.append("human health and the environment. These should improve the safety, health, and")
    thisalinea.textcontent.append("infrastructure of communities and sustains the livelihood in the surrounding areas, e.g. agro-")
    thisalinea.textcontent.append("tourism, markets, infrastructure, culture and well-being.")
    thisalinea.textcontent.append("Current studies on specific practices at farm/land unit level conclude that the costs of")
    thisalinea.textcontent.append("sustainable soil management are in many cases outweighed by the economic benefits, and in")
    thisalinea.textcontent.append("all cases by the environmental benefits18. This proposal creates the requisite framework to")
    thisalinea.textcontent.append("support soil managers until sustainable soil management and healthy soils deliver their")
    thisalinea.textcontent.append("benefits. It can be expected that it will stimulate the earmarking of national and EU funds for")
    thisalinea.textcontent.append("sustainable soil management, and also encourage and support private-sector funding by")
    thisalinea.textcontent.append("financial institutions, investors and related industry, such as food processing businesses. It")
    thisalinea.textcontent.append("would therefore consolidate the competitiveness of the activities related to soil management.")
    thisalinea.textcontent.append("The Horizon Europe research and innovation Mission “A Soil Deal for Europe” also supports")
    thisalinea.textcontent.append("EU ambitions for sustainable land and soil management by providing the knowledge base and")
    thisalinea.textcontent.append("generating solutions for wider action on soil health.")
    thisalinea.textcontent.append("The proposal also tackles soil contamination. Member States must tackle unacceptable risks")
    thisalinea.textcontent.append("for human health and the environment caused by soil contamination to help create a toxic-free")
    thisalinea.textcontent.append("environment by 2050. The proposed risk-based approach will allow for standards to be set at")
    thisalinea.textcontent.append("national level so that the risk reduction measures can be adapted to site-specific conditions.")
    thisalinea.textcontent.append("The proposal will also improve the application of the polluter-pays principle and more")
    thisalinea.textcontent.append("societal fairness by spurring action that will benefit disadvantaged households living closer to")
    thisalinea.textcontent.append("contaminated sites. Requirements to identify, investigate, assess and remediate contaminated")
    thisalinea.textcontent.append("sites will generate jobs and long-term employment (e.g. increase the demand for")
    thisalinea.textcontent.append("environmental consultants, geologists, remediation engineers, etc.).")
    thisalinea.textcontent.append("The legislation proposes taking a gradual and proportionate approach to give Member States")
    thisalinea.textcontent.append("sufficient time to set up their governance system, put in place the soil monitoring system,")
    thisalinea.textcontent.append("assess soil health and start applying measures related to sustainable soil management.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Consistency with existing policy provisions in the policy area"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 4
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Over the past 30 years, the EU has adopted a substantial and wide range of environmental measures with the aim of improving the quality of the environment for European citizens and of creating the conditions for a high quality of life. Current EU law contains several 5 provisions of relevance to soil but there is a clear and indisputable gap in the current EU legal framework that this proposal on soil health is designed to close. The proposal complements existing environmental legislation by providing a coherent EU-level framework for soils. It will also contribute to the objectives set under current "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Over the past 30 years, the EU has adopted a substantial and wide range of environmental")
    thisalinea.textcontent.append("measures with the aim of improving the quality of the environment for European citizens and")
    thisalinea.textcontent.append("of creating the conditions for a high quality of life. Current EU law contains several")
    thisalinea.textcontent.append("5")
    thisalinea.textcontent.append("provisions of relevance to soil but there is a clear and indisputable gap in the current EU legal")
    thisalinea.textcontent.append("framework that this proposal on soil health is designed to close. The proposal complements")
    thisalinea.textcontent.append("existing environmental legislation by providing a coherent EU-level framework for soils. It")
    thisalinea.textcontent.append("will also contribute to the objectives set under current environmental legislation.")
    thisalinea.textcontent.append("Regarding soil contamination, the proposal complements the Industrial Emissions Directive,")
    thisalinea.textcontent.append("the Waste Framework and Landfill Directives, the Environmental Liability Directive and the")
    thisalinea.textcontent.append("Environmental Crime Directive by covering all types of contamination, including historical")
    thisalinea.textcontent.append("soil contamination. It will make a major contribution to the protection of human health which")
    thisalinea.textcontent.append("is one key objective pursued by EU environmental policy.")
    thisalinea.textcontent.append("Healthy soils have an inherent capacity to absorb, store and filter water. The proposal is")
    thisalinea.textcontent.append("therefore expected to contribute to the objectives of the Water Framework Directive, the")
    thisalinea.textcontent.append("Groundwater Directive, the Nitrates Directive, and the Environmental Quality Standards")
    thisalinea.textcontent.append("Directive by tackling soil contamination, soil erosion and by improving soil water retention.")
    thisalinea.textcontent.append("Healthy soils will also contribute to flood prevention, one of the objectives of the Floods")
    thisalinea.textcontent.append("Directive.")
    thisalinea.textcontent.append("The provisions on sustainable soil management complement existing EU legislation relating")
    thisalinea.textcontent.append("to nature (the Habitats and Birds Directives) by improving biodiversity (for example, wild")
    thisalinea.textcontent.append("pollinators that nest in soils), and the air by preventing the erosion of soil particles. Healthy")
    thisalinea.textcontent.append("soils provide the basis for life and biodiversity, including habitats, species and genes, and")
    thisalinea.textcontent.append("contribute to reducing air pollution.")
    thisalinea.textcontent.append("In addition, the knowledge, information and data collected under the monitoring requirements")
    thisalinea.textcontent.append("enshrined in the proposal will help improve the assessment of environmental impacts of")
    thisalinea.textcontent.append("projects, plans and programmes carried out under the Environmental Impact Assessment")
    thisalinea.textcontent.append("Directive and the Strategic Environmental Assessment Directive.")
    thisalinea.textcontent.append("Lastly the proposal is consistent with several other environment policy initiatives such as:")
    thisalinea.textcontent.append("6")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– The EU Biodiversity Strategy for 2030, which sets targets to further protect nature in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 5
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– The EU Biodiversity Strategy for 2030, which sets targets to further protect nature in the EU and in particular the proposal for a regulation on nature restoration19 (Nature Restoration Law (NRL)). The proposed NRL has the goal of 20% of the EU’s land and sea to be covered by restoration measures by 2030 and to cover all ecosystems in need of restoration by restoration measures by 2050. There are many synergies among the proposed NRL and this proposal on soil health. The proposed NRL and this proposal are therefore mutually reinforcing. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The EU Biodiversity Strategy for 2030, which sets targets to further protect nature in")
    thisalinea.textcontent.append("the EU and in particular the proposal for a regulation on nature restoration19 (Nature")
    thisalinea.textcontent.append("Restoration Law (NRL)). The proposed NRL has the goal of 20% of the EU’s land")
    thisalinea.textcontent.append("and sea to be covered by restoration measures by 2030 and to cover all ecosystems in")
    thisalinea.textcontent.append("need of restoration by restoration measures by 2050. There are many synergies")
    thisalinea.textcontent.append("among the proposed NRL and this proposal on soil health. The proposed NRL and")
    thisalinea.textcontent.append("this proposal are therefore mutually reinforcing.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– The Zero Pollution Action Plan sets out the vision that by 2050, air, water ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 6
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– The Zero Pollution Action Plan sets out the vision that by 2050, air, water and soil pollution is reduced to levels no longer considered harmful to health and natural ecosystems. This proposal is consistent with the proposals aiming to revise and strengthen key existing EU legislation in the air and water sectors and the legislation on industrial activities. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Zero Pollution Action Plan sets out the vision that by 2050, air, water and soil")
    thisalinea.textcontent.append("pollution is reduced to levels no longer considered harmful to health and natural")
    thisalinea.textcontent.append("ecosystems. This proposal is consistent with the proposals aiming to revise and")
    thisalinea.textcontent.append("strengthen key existing EU legislation in the air and water sectors and the legislation")
    thisalinea.textcontent.append("on industrial activities.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– The Circular Economy Action Plan, which announces measures to reduce micro- ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 7
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– The Circular Economy Action Plan, which announces measures to reduce micro- plastics and an evaluation of the Sewage Sludge Directive, regulating the quality of sludge used in agriculture. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Circular Economy Action Plan, which announces measures to reduce micro-")
    thisalinea.textcontent.append("plastics and an evaluation of the Sewage Sludge Directive, regulating the quality of")
    thisalinea.textcontent.append("sludge used in agriculture.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– The Chemicals Strategy for Sustainability, which recognises that chemicals are ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 8
    thisalinea.parentID = 4
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– The Chemicals Strategy for Sustainability, which recognises that chemicals are essential for the well-being of modern society but aims to better protect citizens and the environment against their possible hazardous properties. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– The Chemicals Strategy for Sustainability, which recognises that chemicals are")
    thisalinea.textcontent.append("essential for the well-being of modern society but aims to better protect citizens and")
    thisalinea.textcontent.append("the environment against their possible hazardous properties.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Consistency with other Union policies"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 9
    thisalinea.parentID = 2
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The proposal is consistent with EU policies on climate, food and agriculture. The initiative is a crucial centrepiece of the European Green Deal and an instrument to achieve EU policy objectives such as climate neutrality, resilient nature and biodiversity, zero pollution, sustainable food systems, human health and well-being. The objectives of the proposal are complementary and in synergy with the European Climate Law20. They will contribute to the EU climate change adaptation objectives by making the EU more resilient and to its aim to achieve a climate-neutral Europe by 2050. Storing carbon in soil is an essential part of the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal is consistent with EU policies on climate, food and agriculture.")
    thisalinea.textcontent.append("The initiative is a crucial centrepiece of the European Green Deal and an instrument to")
    thisalinea.textcontent.append("achieve EU policy objectives such as climate neutrality, resilient nature and biodiversity, zero")
    thisalinea.textcontent.append("pollution, sustainable food systems, human health and well-being.")
    thisalinea.textcontent.append("The objectives of the proposal are complementary and in synergy with the European Climate")
    thisalinea.textcontent.append("Law20. They will contribute to the EU climate change adaptation objectives by making the EU")
    thisalinea.textcontent.append("more resilient and to its aim to achieve a climate-neutral Europe by 2050. Storing carbon in")
    thisalinea.textcontent.append("soil is an essential part of the action needed to reach climate neutrality. Achieving this")
    thisalinea.textcontent.append("objective requires action in multiple areas, such as carbon removals through sustainable soil")
    thisalinea.textcontent.append("management to balance greenhouse gas emissions that will remain at the end of an ambitious")
    thisalinea.textcontent.append("decarbonisation pathway. This proposal will also contribute to the EU’s climate change")
    thisalinea.textcontent.append("adaptation objectives, make the EU more resilient and reduce its vulnerability to climate")
    thisalinea.textcontent.append("change, for example by enhancing the capacity of soils to retain water.")
    thisalinea.textcontent.append("The proposal is fully complementary and synergetic with the Land Use, Land Use Change and")
    thisalinea.textcontent.append("Forestry (LULUCF) Regulation21, as revised recently to make it fit to the target to reduce net")
    thisalinea.textcontent.append("emissions by 55% by 2030. The revised LULUCF Regulation22 aims to achieve 310 Mt CO2")
    thisalinea.textcontent.append("equivalent net removals in the LULUCF sector by 2030 at EU level. For the period 2026-")
    thisalinea.textcontent.append("2029, each Member State will have a binding national goal to progressively increase of")
    thisalinea.textcontent.append("greenhouse gas removals. These objectives require all Member States to step up the level of")
    thisalinea.textcontent.append("climate ambition for their land use policies. The LULUCF Regulation moreover requires that")
    thisalinea.textcontent.append("Member States set up systems to monitor soil carbon stocks, with the expectation of enhanced")
    thisalinea.textcontent.append("implementation of nature-based climate mitigation in soils. This proposal on soil health and")
    thisalinea.textcontent.append("the revised LULUCF Regulation will be mutually reinforcing, since healthy soils sequester")
    thisalinea.textcontent.append("more carbon and the LULUCF targets promote the sustainable management of soils.")
    thisalinea.textcontent.append("Enhanced and more representative soil monitoring will also improve the monitoring of")
    thisalinea.textcontent.append("successful policy implementation in the LULUCF sector.")
    thisalinea.textcontent.append("The aim of the proposed regulation for a certification framework for carbon removal23 is to")
    thisalinea.textcontent.append("facilitate the deployment of high-quality carbon removals through a voluntary EU")
    thisalinea.textcontent.append("certification framework with high climate and environmental integrity. Carbon removals also")
    thisalinea.textcontent.append("constitute a new business model in the voluntary carbon market. This initiative is instrumental")
    thisalinea.textcontent.append("7")
    thisalinea.textcontent.append("in ensuring the soil’s capacity to absorb and store carbon. Conversely, regenerating soil to")
    thisalinea.textcontent.append("good health is instrumental in increasing its capacity to absorb and store carbon and to")
    thisalinea.textcontent.append("generate carbon removal credits. Moreover, creating soil districts, as envisaged under the")
    thisalinea.textcontent.append("initiative on soil, and generating the related data and knowledge will facilitate implementation")
    thisalinea.textcontent.append("of the carbon removal certification.")
    thisalinea.textcontent.append("Lastly, a commensurate certification of healthy soil is expected to increase the value of the")
    thisalinea.textcontent.append("carbon removal certificate and give greater social and market recognition for sustainable soil")
    thisalinea.textcontent.append("management and related food and non-food products. The benefits of healthy soils and")
    thisalinea.textcontent.append("measures to achieve this will also help boost private financing, as food industry and other")
    thisalinea.textcontent.append("business have already started putting in place programmes to pay for ecosystem services and")
    thisalinea.textcontent.append("support sustainable practices related to soil health. At the same time, soil certified as healthy")
    thisalinea.textcontent.append("is likely to increase the value of the land, e.g. for the purposes of collateral, sale or succession.")
    thisalinea.textcontent.append("This proposal is consistent with the Farm to Fork Strategy24 which aims to reduce nutrient")
    thisalinea.textcontent.append("losses by at least 50% while ensuring that there is no deterioration in soil fertility. In addition,")
    thisalinea.textcontent.append("the proposal on soil health will contribute to making the EU food system more resilient.")
    thisalinea.textcontent.append("The proposal supports the efforts made by the agricultural sector under the CAP25 with its")
    thisalinea.textcontent.append("new rules to increase the environmental performance of the agricultural sector, also")
    thisalinea.textcontent.append("manifested in the CAP strategic plans 2023-202726. This policy includes some mandatory")
    thisalinea.textcontent.append("environmental and climate conditions (good agricultural and environmental conditions) that")
    thisalinea.textcontent.append("farmers must meet in order to receive CAP income support. Some of these conditions are")
    thisalinea.textcontent.append("linked to soil management practices (such as practices to limit soil erosion (e.g. tillage")
    thisalinea.textcontent.append("management), minimum soil cover and crop rotation) and are expected to help maintain or")
    thisalinea.textcontent.append("enhance soil health on agricultural soils. The CAP also provides for financial support to")
    thisalinea.textcontent.append("farmers who commit to undertake specific environmental and climate practices or investments")
    thisalinea.textcontent.append("going beyond these conditions. According to the approved CAP Strategic Plans for the period")
    thisalinea.textcontent.append("2023-2027, by 2027, half of the EU’s used agricultural area will be supported by")
    thisalinea.textcontent.append("commitments beneficial for soil management to improve soil quality and biota (such as")
    thisalinea.textcontent.append("reducing tillage, soil cover in sensitive periods with intermediary crops, crop rotation")
    thisalinea.textcontent.append("including leguminous crops). By strengthening the CAP’s innovation dimension, Member")
    thisalinea.textcontent.append("States have planned to set up more than 6.600 Operational Groups out of which about 1.000")
    thisalinea.textcontent.append("are expected to address soil health issues. Due to these links, this directive should be taken")
    thisalinea.textcontent.append("into account when, in accordance with Article 159 of Regulation (EU) 2021/2115, the")
    thisalinea.textcontent.append("Commission reviews, by 31 December 2025, the list set out in Annex XIII to that Regulation.")
    thisalinea.textcontent.append("This proposal on soil will lay down sustainable management principles applicable to managed")
    thisalinea.textcontent.append("soils in Europe, including agricultural soils. It will give Member States flexibility to apply")
    thisalinea.textcontent.append("these principles as they see best, and to choose how to integrate these in their CAP strategic")
    thisalinea.textcontent.append("plans. This proposal will also provide the tools to improve the monitoring of the impacts of")
    thisalinea.textcontent.append("the support instruments under the CAP.")
    thisalinea.textcontent.append("8")
    thisalinea.textcontent.append("This proposal is consistent with the proposal to transform the current Farm Accountancy Data")
    thisalinea.textcontent.append("Network (FADN) into a Farm Sustainability Data Network (FSDN)27, included in the Farm to")
    thisalinea.textcontent.append("Fork Strategy. The new FSDN will aim to collect farm level data on sustainability and")
    thisalinea.textcontent.append("contribute to the improvement of advisory services to farmers and benchmarking of farm")
    thisalinea.textcontent.append("performance. Once transformed, the new network will allow the European Commission and")
    thisalinea.textcontent.append("Member States to monitor the development of specific agro-environmental practices at farm")
    thisalinea.textcontent.append("level, including soil management practices.")
    thisalinea.textcontent.append("This proposal is consistent with other EU policy objectives aimed at achieving the EU’s open")
    thisalinea.textcontent.append("strategic autonomy, such as the ones under the proposal for a European Critical Raw")
    thisalinea.textcontent.append("Materials Act28 that aim at ensuring secure and sustainable supply of critical raw materials for")
    thisalinea.textcontent.append("Europe’s industry, and should be implemented accordingly.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. LEGAL BASIS, SUBSIDIARITY AND PROPORTIONALITY"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 10
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The provisions of this proposal relate to environmental protection. The legal basis for this proposal is therefore Article 192(1) of the Treaty on the Functioning of the European Union that sets out how Article 191 of the Treaty should be implemented. Article 191 of the Treaty specifies the objectives of EU environmental policy: The proposal does not contain measures affecting land use. Given that this is an area of shared competence between the EU and the Member States, EU action must comply with the subsidiarity principle. – preserving, protecting and improving the quality of the environment; – protecting human health; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Legal basis"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 11
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The provisions of this proposal relate to environmental protection. The legal basis for this proposal is therefore Article 192(1) of the Treaty on the Functioning of the European Union that sets out how Article 191 of the Treaty should be implemented. Article 191 of the Treaty specifies the objectives of EU environmental policy: The proposal does not contain measures affecting land use. Given that this is an area of shared competence between the EU and the Member States, EU action must comply with the subsidiarity principle. – preserving, protecting and improving the quality of the environment; – protecting human health; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The provisions of this proposal relate to environmental protection. The legal basis for this")
    thisalinea.textcontent.append("proposal is therefore Article 192(1) of the Treaty on the Functioning of the European Union")
    thisalinea.textcontent.append("that sets out how Article 191 of the Treaty should be implemented. Article 191 of the Treaty")
    thisalinea.textcontent.append("specifies the objectives of EU environmental policy:")
    thisalinea.textcontent.append("The proposal does not contain measures affecting land use.")
    thisalinea.textcontent.append("Given that this is an area of shared competence between the EU and the Member States, EU")
    thisalinea.textcontent.append("action must comply with the subsidiarity principle.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– preserving, protecting and improving the quality of the environment; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 12
    thisalinea.parentID = 11
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "– preserving, protecting and improving the quality of the environment; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– preserving, protecting and improving the quality of the environment;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– protecting human health; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 13
    thisalinea.parentID = 11
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "– protecting human health; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– protecting human health;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– utilising natural resources prudently and rationally; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 14
    thisalinea.parentID = 11
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– utilising natural resources prudently and rationally; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– utilising natural resources prudently and rationally;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– promoting measures at international level to deal with regional or worldwide ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 15
    thisalinea.parentID = 11
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "– promoting measures at international level to deal with regional or worldwide environmental problems, in particular to combat climate change. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– promoting measures at international level to deal with regional or worldwide")
    thisalinea.textcontent.append("environmental problems, in particular to combat climate change.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Subsidiarity (for non-exclusive competence)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 16
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Action at EU level is justified given the scale and cross-border nature of the problem, the impact of soil degradation across the EU and the risks to the environment, economy and society. Soil degradation is often wrongly considered as a purely local issue and the transboundary impacts are underestimated. The drivers and impacts of the problem go beyond country borders and reduce the provision of ecosystem services in multiple countries as soil is washed away by water or blown by winds. Contaminants can become mobile via the air, surface water and groundwater, they can move across borders and can affect "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Action at EU level is justified given the scale and cross-border nature of the problem, the")
    thisalinea.textcontent.append("impact of soil degradation across the EU and the risks to the environment, economy and")
    thisalinea.textcontent.append("society.")
    thisalinea.textcontent.append("Soil degradation is often wrongly considered as a purely local issue and the transboundary")
    thisalinea.textcontent.append("impacts are underestimated. The drivers and impacts of the problem go beyond country")
    thisalinea.textcontent.append("borders and reduce the provision of ecosystem services in multiple countries as soil is washed")
    thisalinea.textcontent.append("away by water or blown by winds. Contaminants can become mobile via the air, surface water")
    thisalinea.textcontent.append("and groundwater, they can move across borders and can affect food.")
    thisalinea.textcontent.append("9")
    thisalinea.textcontent.append("In ways that are rarely seen or acknowledged, healthy soils are essential to tackle global")
    thisalinea.textcontent.append("societal challenges. Soils play a key role in the nutrient, carbon and water cycles, and these")
    thisalinea.textcontent.append("processes are clearly not constrained by physical and political borders.")
    thisalinea.textcontent.append("Therefore, coordinated measures by all Member States are needed to achieve the vision to")
    thisalinea.textcontent.append("have all soils healthy by 2050, as set out in the Soil Strategy for 2030, and to ensure that soil")
    thisalinea.textcontent.append("has the capacity to provide ecosystem services across the EU in the long-term.")
    thisalinea.textcontent.append("Unless we rapidly halt the current level of soil degradation and regenerate soil to good health,")
    thisalinea.textcontent.append("our food system will become less productive and increasingly vulnerable to climate change")
    thisalinea.textcontent.append("and reliant on resource-intensive inputs. Individual action by the Member States has proven to")
    thisalinea.textcontent.append("be insufficient to remedy the situation, since soil degradation is continuing and even")
    thisalinea.textcontent.append("worsening.")
    thisalinea.textcontent.append("Given that some aspects of soil health are only marginally covered by EU legislation,")
    thisalinea.textcontent.append("additional EU action is needed to complement current requirements and to fill the policy gaps.")
    thisalinea.textcontent.append("The proposal is designed to create the conditions for action to manage soils sustainably and to")
    thisalinea.textcontent.append("tackle the costs of soil degradation. The objectives of the proposed action can be better")
    thisalinea.textcontent.append("achieved at EU level because of the scale and effects it will produce. Coordinated action is")
    thisalinea.textcontent.append("needed at sufficiently large scale to monitor and to sustainably manage soils in order to")
    thisalinea.textcontent.append("benefit from synergies, effectiveness and efficiency gains. Coordinated action is also needed")
    thisalinea.textcontent.append("to meet the commitments on soil health made at both EU and global level. There is a risk that")
    thisalinea.textcontent.append("if soil is not properly protected, the EU and its Member States will fail to meet international")
    thisalinea.textcontent.append("and European Green Deal commitments on the environment, sustainable development and")
    thisalinea.textcontent.append("climate. Lastly, action at EU level is essential to address potential distortions on the internal")
    thisalinea.textcontent.append("market and unfair competition among businesses since there are lower environmental")
    thisalinea.textcontent.append("requirements in some Member States.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Proportionality"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 17
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The proposal complies with the proportionality principle because it does not go beyond what is necessary to have all soils in the EU healthy by 2050. The proposed instrument is a directive that leaves much flexibility to the Member States to identify the best measures for them and to adapt the approach to local conditions. This is crucial to take account of the regional and local specificities as regards soil variability, land use, climatological conditions and socio-economic aspects. The proposal ensures that its objectives are reached with requirements that are both realistic and do not go beyond what is necessary. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal complies with the proportionality principle because it does not go beyond what")
    thisalinea.textcontent.append("is necessary to have all soils in the EU healthy by 2050. The proposed instrument is a")
    thisalinea.textcontent.append("directive that leaves much flexibility to the Member States to identify the best measures for")
    thisalinea.textcontent.append("them and to adapt the approach to local conditions. This is crucial to take account of the")
    thisalinea.textcontent.append("regional and local specificities as regards soil variability, land use, climatological conditions")
    thisalinea.textcontent.append("and socio-economic aspects.")
    thisalinea.textcontent.append("The proposal ensures that its objectives are reached with requirements that are both realistic")
    thisalinea.textcontent.append("and do not go beyond what is necessary. For this reason, Member States are given sufficient")
    thisalinea.textcontent.append("time to gradually put in place the governance, the mechanisms to monitor and assess soil")
    thisalinea.textcontent.append("health and the measures needed to implement the sustainable soil management principles.")
    thisalinea.textcontent.append("To ensure the EU reaches its objectives, the proposal lays down obligations to monitor and")
    thisalinea.textcontent.append("assess soil health and to review the effectiveness of the measures taken. The impact")
    thisalinea.textcontent.append("assessment evaluated the impacts of all policy options and showed that the proposals are")
    thisalinea.textcontent.append("proportionate.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Choice of the instrument"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 18
    thisalinea.parentID = 10
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "A legislative rather than a non-legislative approach is needed to meet the long-term objective of healthy soil in the EU by 2050. The proposal provides a coherent framework for soil monitoring and sustainable management in this respect. The proposal leaves much flexibility 10 to the Member States to identify the best measures for them and to adapt the approach to local conditions. These objectives can be best pursued in the form of a directive. The wide range of soil conditions and uses across the EU, and the need for flexibility and subsidiarity, mean that a directive is the best legal "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("A legislative rather than a non-legislative approach is needed to meet the long-term objective")
    thisalinea.textcontent.append("of healthy soil in the EU by 2050. The proposal provides a coherent framework for soil")
    thisalinea.textcontent.append("monitoring and sustainable management in this respect. The proposal leaves much flexibility")
    thisalinea.textcontent.append("10")
    thisalinea.textcontent.append("to the Member States to identify the best measures for them and to adapt the approach to local")
    thisalinea.textcontent.append("conditions. These objectives can be best pursued in the form of a directive. The wide range of")
    thisalinea.textcontent.append("soil conditions and uses across the EU, and the need for flexibility and subsidiarity, mean that")
    thisalinea.textcontent.append("a directive is the best legal instrument to meet this purpose.")
    thisalinea.textcontent.append("A directive requires Member States to achieve its objectives and implement the measures into")
    thisalinea.textcontent.append("their national substantive and procedural law systems. But directives give Member States")
    thisalinea.textcontent.append("more freedom when implementing an EU measure than regulations, in that Member States")
    thisalinea.textcontent.append("can choose how to implement the measures set out in the directive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. RESULTS OF EX-POST EVALUATIONS, STAKEHOLDER CONSULTATIONS AND IMPACT ASSESSMENTS"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 19
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Not applicable since there is currently no EU-wide legislation specifically on soil. The evaluation of the EU Biodiversity Strategy to 2020 (SWD(2022)284) confirmed that soil degradation and loss and desertification pose a threat to habitats and species. It also stated that nature-based solutions are essential to help reduce emissions and adapt to a changing climate. The Commission organised a call for evidence on soil health between 16 February 2022 and 16 March 2022 that received 189 replies. Between 1 August 2022 and 24 October 2022, the Commission organised an online public consultation on the potential Soil Health Law on protecting, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Ex-post evaluations/fitness checks of existing legislation"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 20
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Not applicable since there is currently no EU-wide legislation specifically on soil. The evaluation of the EU Biodiversity Strategy to 2020 (SWD(2022)284) confirmed that soil degradation and loss and desertification pose a threat to habitats and species. It also stated that nature-based solutions are essential to help reduce emissions and adapt to a changing climate. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Not applicable since there is currently no EU-wide legislation specifically on soil.")
    thisalinea.textcontent.append("The evaluation of the EU Biodiversity Strategy to 2020 (SWD(2022)284) confirmed that soil")
    thisalinea.textcontent.append("degradation and loss and desertification pose a threat to habitats and species. It also stated that")
    thisalinea.textcontent.append("nature-based solutions are essential to help reduce emissions and adapt to a changing climate.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Stakeholder consultations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 21
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The Commission organised a call for evidence on soil health between 16 February 2022 and 16 March 2022 that received 189 replies. Between 1 August 2022 and 24 October 2022, the Commission organised an online public consultation on the potential Soil Health Law on protecting, sustainably managing and restoring soils. It received 5 782 responses. Since 2015, the Commission has maintained an open dialogue with Member States via the EU expert group on soil protection. The group typically met twice a year but convened eight times in 2022 to discuss several aspects of the Soil Health Law based on thematic "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The Commission organised a call for evidence on soil health between 16 February 2022 and")
    thisalinea.textcontent.append("16 March 2022 that received 189 replies.")
    thisalinea.textcontent.append("Between 1 August 2022 and 24 October 2022, the Commission organised an online public")
    thisalinea.textcontent.append("consultation on the potential Soil Health Law on protecting, sustainably managing and")
    thisalinea.textcontent.append("restoring soils. It received 5 782 responses.")
    thisalinea.textcontent.append("Since 2015, the Commission has maintained an open dialogue with Member States via the EU")
    thisalinea.textcontent.append("expert group on soil protection. The group typically met twice a year but convened eight")
    thisalinea.textcontent.append("times in 2022 to discuss several aspects of the Soil Health Law based on thematic working")
    thisalinea.textcontent.append("papers prepared by the Commission. In October 2022, the expert group was extended to")
    thisalinea.textcontent.append("include stakeholder groups other than Member States. The expert group met twice in the new")
    thisalinea.textcontent.append("composition on 4 October 2022 and 7 February 2023 and discussed the Soil Law in these")
    thisalinea.textcontent.append("meetings.")
    thisalinea.textcontent.append("The Commission also organised interviews and sent targeted questionnaires to elicit the views")
    thisalinea.textcontent.append("of experts on the costs, feasibility and impacts of certain measures. It collected responses")
    thisalinea.textcontent.append("between 14 and 28 November 2022.")
    thisalinea.textcontent.append("A synopsis report of all consultation activities is annexed to the impact assessment (Annex 2).")
    thisalinea.textcontent.append("It describes the strategy, method and overview of the feedback received. The Commission")
    thisalinea.textcontent.append("took full account of the views of the stakeholders when comparing the various policy options")
    thisalinea.textcontent.append("(see Annex 10 to the impact assessment).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Collection and use of expertise"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 22
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The Commission drew substantially from the expertise of the EU expert group on soil protection which discussed several thematic papers prepared by the Commission and on the internal research expertise developed by the Joint Research Centre. 11 The Commission also drew on the publicly available data and knowledge from competent organisations such as the FAO, EEA, IPBES and European Academies Science Advisory Council. It collected further expertise through service contracts and EU-funded projects notably under Horizon programmes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The Commission drew substantially from the expertise of the EU expert group on soil")
    thisalinea.textcontent.append("protection which discussed several thematic papers prepared by the Commission and on the")
    thisalinea.textcontent.append("internal research expertise developed by the Joint Research Centre.")
    thisalinea.textcontent.append("11")
    thisalinea.textcontent.append("The Commission also drew on the publicly available data and knowledge from competent")
    thisalinea.textcontent.append("organisations such as the FAO, EEA, IPBES and European Academies Science Advisory")
    thisalinea.textcontent.append("Council. It collected further expertise through service contracts and EU-funded projects")
    thisalinea.textcontent.append("notably under Horizon programmes.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Impact assessment"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 23
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The proposal is based on an impact assessment. After having resolved the issues raised in the Regulatory Scrutiny Board’s negative opinion issued on 17 February 2023, the draft impact assessment received a positive opinion with reservations on 28 April 2023. The Regulatory Scrutiny Board required in particular to clarify the content and feasibility of the options, to reflect the risks of not reaching the objective of healthy soils across EU by 2050, to nuance the analysis of the impacts on competitiveness and to be more explicit on the views of Member States. In the impact assessment, the policy options have "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal is based on an impact assessment. After having resolved the issues raised in the")
    thisalinea.textcontent.append("Regulatory Scrutiny Board’s negative opinion issued on 17 February 2023, the draft impact")
    thisalinea.textcontent.append("assessment received a positive opinion with reservations on 28 April 2023. The Regulatory")
    thisalinea.textcontent.append("Scrutiny Board required in particular to clarify the content and feasibility of the options, to")
    thisalinea.textcontent.append("reflect the risks of not reaching the objective of healthy soils across EU by 2050, to nuance")
    thisalinea.textcontent.append("the analysis of the impacts on competitiveness and to be more explicit on the views of")
    thisalinea.textcontent.append("Member States.")
    thisalinea.textcontent.append("In the impact assessment, the policy options have been described by using five key building")
    thisalinea.textcontent.append("blocks:")
    thisalinea.textcontent.append("Options have been designed for each of the five building blocks, by modulating flexibility and")
    thisalinea.textcontent.append("harmonisation to different degrees corresponding to meaningful potential solutions. One")
    thisalinea.textcontent.append("option was designed to give the highest degree of flexibility for Member States, another with")
    thisalinea.textcontent.append("the highest degree of harmonisation and a third gives an intermediate degree of harmonisation")
    thisalinea.textcontent.append("and flexibility. Option 1 is a monitoring-only scenario without measures on sustainable soil")
    thisalinea.textcontent.append("management, regeneration and remediation, but it was discarded at an early stage because it")
    thisalinea.textcontent.append("was deemed insufficient to achieve the objectives and meet stakeholders’ expectations.")
    thisalinea.textcontent.append("The preferred option combined the most effective, efficient and policy coherent options")
    thisalinea.textcontent.append("selected from each building block. For all building blocks, except for the remediation of")
    thisalinea.textcontent.append("contaminated sites, Option 3 providing an intermediate level of flexibility and harmonisation")
    thisalinea.textcontent.append("was chosen (and very flexible Option 2 for remediation). The preferred option resulting from")
    thisalinea.textcontent.append("the impact assessment was based on a staged approach that would give Member States time to")
    thisalinea.textcontent.append("put in place the mechanisms to first assess the condition of soils and then decide on the")
    thisalinea.textcontent.append("regeneration measures needed once the conclusions are available.")
    thisalinea.textcontent.append("The preferred option was designed to tackle the costs of soil degradation, in particular the")
    thisalinea.textcontent.append("resulting loss of ecosystem services. It would ensure that the EU will achieve its policy")
    thisalinea.textcontent.append("objectives, such as healthy soils and the zero-pollution ambition by 2050, in a cost-efficient")
    thisalinea.textcontent.append("manner. Most benefits come from avoiding costs by tackling soil degradation. The highest")
    thisalinea.textcontent.append("costs relate to the implementation of measures for sustainable soil management and")
    thisalinea.textcontent.append("regeneration. The benefits of the initiative were estimated at around EUR 74 billion per year.")
    thisalinea.textcontent.append("Total costs would be of the order of EUR 28-38 billion per year. For contaminated sites, the")
    thisalinea.textcontent.append("annual cost is highly uncertain. It is estimated at EUR 1.9 billion for the identify and")
    thisalinea.textcontent.append("investigate contaminated sites and EUR 1 billion a year to remediate contaminated sites.")
    thisalinea.textcontent.append("12")
    thisalinea.textcontent.append("Although it was not possible to quantify and monetise all impacts, the benefit-cost ratio of the")
    thisalinea.textcontent.append("preferred option was estimated at a conservative and prudent 1.7. It also requires Member")
    thisalinea.textcontent.append("States to ensure public participation, in particular from soil managers, farmers and foresters.")
    thisalinea.textcontent.append("The transition to sustainable soil management requires investments to reap the long-term")
    thisalinea.textcontent.append("benefits of healthy soils for the environment, economy and society. Successful")
    thisalinea.textcontent.append("implementation of the preferred option requires tapping various sources of funding at")
    thisalinea.textcontent.append("European, national, regional and local level. Therefore, this proposal is published alongside a")
    thisalinea.textcontent.append("Staff Working Document (SWD) providing an overview of funding opportunities available")
    thisalinea.textcontent.append("under the EU’s 2021-2027 multiannual budget for the protection, sustainable management,")
    thisalinea.textcontent.append("and regeneration of soils. Member States also continue sharing knowledge, experience and")
    thisalinea.textcontent.append("expertise in several interconnected EU platforms on soil health.")
    thisalinea.textcontent.append("The proposal corresponds to the preferred option for all building blocks except for the")
    thisalinea.textcontent.append("building block on soil restoration. The proposal is less demanding in terms of soil")
    thisalinea.textcontent.append("regeneration than the preferred option contained in the impact assessment in order to limit the")
    thisalinea.textcontent.append("burden on Member States, landowners and land managers. In particular, the proposal does not")
    thisalinea.textcontent.append("require Member States to create any new programmes of measures or soil health plans.")
    thisalinea.textcontent.append("However, since this approach may entail an increased risk not to reach the objective of")
    thisalinea.textcontent.append("healthy soils by 2050, it is proposed that the Commission will carry out an analysis on the")
    thisalinea.textcontent.append("need to set more specific requirements to restore/regenerate unhealthy soils by 2050 in the")
    thisalinea.textcontent.append("context of an early evaluation of the directive scheduled 6 years after its entry into force. This")
    thisalinea.textcontent.append("analysis will be based on exchanges with the Member States and interested parties, and will")
    thisalinea.textcontent.append("take into account the conclusions of the assessment of soil health, the progress on sustainable")
    thisalinea.textcontent.append("soil management and the advancement of knowledge on the criteria for the descriptors of soil")
    thisalinea.textcontent.append("health.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(1) definition of soil health and establishment of soil districts, "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 24
    thisalinea.parentID = 23
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) definition of soil health and establishment of soil districts, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) definition of soil health and establishment of soil districts,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(2) monitoring of soil health, "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 25
    thisalinea.parentID = 23
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) monitoring of soil health, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) monitoring of soil health,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(3) sustainable soil management, "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 26
    thisalinea.parentID = 23
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) sustainable soil management, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) sustainable soil management,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(4) identification, registration, investigation and assessment of contaminated sites, "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 27
    thisalinea.parentID = 23
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) identification, registration, investigation and assessment of contaminated sites, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) identification, registration, investigation and assessment of contaminated sites,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(5) restoration (regeneration) of soil health and remediation of contaminated sites. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 28
    thisalinea.parentID = 23
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) restoration (regeneration) of soil health and remediation of contaminated sites. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) restoration (regeneration) of soil health and remediation of contaminated sites.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Regulatory fitness and simplification"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 29
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "The business sectors expected to be affected by the initiative include agriculture, forestry and related extension services, business activities that have contaminated the soil, business activities related to remediation of contaminated sites, research and laboratories. Soil degradation affects their productivity and competitiveness. Action taken to address degradation is not rewarded, and affects the level playing field. Implementing the proposal will create several opportunities for growth and innovation, including for EU SMEs, both in designing and applying sustainable soil management practices, and in investigating and remediating contaminated soils. In addition, setting up a soil monitoring system is expected to create opportunities "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The business sectors expected to be affected by the initiative include agriculture, forestry and")
    thisalinea.textcontent.append("related extension services, business activities that have contaminated the soil, business")
    thisalinea.textcontent.append("activities related to remediation of contaminated sites, research and laboratories. Soil")
    thisalinea.textcontent.append("degradation affects their productivity and competitiveness. Action taken to address")
    thisalinea.textcontent.append("degradation is not rewarded, and affects the level playing field.")
    thisalinea.textcontent.append("Implementing the proposal will create several opportunities for growth and innovation,")
    thisalinea.textcontent.append("including for EU SMEs, both in designing and applying sustainable soil management")
    thisalinea.textcontent.append("practices, and in investigating and remediating contaminated soils. In addition, setting up a")
    thisalinea.textcontent.append("soil monitoring system is expected to create opportunities for research and development and")
    thisalinea.textcontent.append("business to develop new technologies and innovations for monitoring and assessing soil")
    thisalinea.textcontent.append("health.")
    thisalinea.textcontent.append("To further reduce the administrative burden, the proposal does not require Member States to")
    thisalinea.textcontent.append("create any new programmes of measures for sustainable soil management or regeneration. In")
    thisalinea.textcontent.append("addition, it draws as much as possible on digital and remote sensing solutions. The Member")
    thisalinea.textcontent.append("States will report to the Commission only every 5 years and reporting is limited to the")
    thisalinea.textcontent.append("information that the Commission needs to fulfil its role in overseeing implementation of the")
    thisalinea.textcontent.append("directive, evaluate it and report to the other EU institutions.")
    thisalinea.textcontent.append("13")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Fundamental rights"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 30
    thisalinea.parentID = 19
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "The proposed directive respects fundamental rights and the principles enshrined in the EU Charter of Fundamental Rights. The proposal lays down measures to achieve healthy soils by 2050 and to ensure that soil contamination is reduced to levels no longer considered harmful to human health and the environment. This will provide protection to socially and economically disadvantaged communities living on or close to contaminated sites. The proposal seeks to integrate into EU policies a high level of environmental protection and to improve the quality of the environment, in line with the principle of sustainable development laid down in Article 37 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposed directive respects fundamental rights and the principles enshrined in the EU")
    thisalinea.textcontent.append("Charter of Fundamental Rights. The proposal lays down measures to achieve healthy soils by")
    thisalinea.textcontent.append("2050 and to ensure that soil contamination is reduced to levels no longer considered harmful")
    thisalinea.textcontent.append("to human health and the environment. This will provide protection to socially and")
    thisalinea.textcontent.append("economically disadvantaged communities living on or close to contaminated sites. The")
    thisalinea.textcontent.append("proposal seeks to integrate into EU policies a high level of environmental protection and to")
    thisalinea.textcontent.append("improve the quality of the environment, in line with the principle of sustainable development")
    thisalinea.textcontent.append("laid down in Article 37 of the EU Charter of Fundamental Rights. It also puts into concrete")
    thisalinea.textcontent.append("terms the obligation to protect the right to life as laid down in Article 2 of the Charter.")
    thisalinea.textcontent.append("The proposal contributes to the right to an effective remedy before a tribunal, as laid down in")
    thisalinea.textcontent.append("Article 47 of the Charter, with detailed provisions on access to justice and penalties.")
    thisalinea.textcontent.append("The proposal does not regulate the use of property and respects the right of property laid")
    thisalinea.textcontent.append("down in Article 17 of the Charter. However, to fulfil the obligations related to monitoring soil")
    thisalinea.textcontent.append("health (to take soil samples), the competent authorities in the Member States may need to")
    thisalinea.textcontent.append("require landowners to give them the right to access their property in line with the applicable")
    thisalinea.textcontent.append("national rules and procedures. Member States may also require that landowners implement")
    thisalinea.textcontent.append("measures to manage the soil in a sustainable manner.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "4. BUDGETARY IMPLICATIONS"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 31
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The proposal will have budgetary implications for the Commission in terms of the human and administrative resources required. The Commission’s implementation and enforcement workload will increase because of this new initiative, which sets a new framework for soil monitoring and assessment, sustainable management and regeneration. The Commission will need to manage a new committee and verify the completeness and compliance of transposition measures. It will also need to monitor and analyse data reported by Member States, adopt implementing acts and provide guidance where needed. The Commission will step up action on soil monitoring implementation and integration. It will seek support "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposal will have budgetary implications for the Commission in terms of the human and")
    thisalinea.textcontent.append("administrative resources required.")
    thisalinea.textcontent.append("The Commission’s implementation and enforcement workload will increase because of this")
    thisalinea.textcontent.append("new initiative, which sets a new framework for soil monitoring and assessment, sustainable")
    thisalinea.textcontent.append("management and regeneration. The Commission will need to manage a new committee and")
    thisalinea.textcontent.append("verify the completeness and compliance of transposition measures. It will also need to")
    thisalinea.textcontent.append("monitor and analyse data reported by Member States, adopt implementing acts and provide")
    thisalinea.textcontent.append("guidance where needed.")
    thisalinea.textcontent.append("The Commission will step up action on soil monitoring implementation and integration. It")
    thisalinea.textcontent.append("will seek support from the scientific community with support from the Joint Research Centre")
    thisalinea.textcontent.append("and by launching EU-funded projects.")
    thisalinea.textcontent.append("The European Environment Agency will create a new infrastructure for reporting analyses,")
    thisalinea.textcontent.append("support for policies on soil protection and the work needed to integrate soil data with other")
    thisalinea.textcontent.append("policy areas. Synergies will be sought with other tasks. A potential need for minor")
    thisalinea.textcontent.append("reinforcement will be grouped together in a Legislative Financial Statement of a forthcoming")
    thisalinea.textcontent.append("legal proposal.")
    thisalinea.textcontent.append("The annexed financial statement shows the budgetary implications and the human and")
    thisalinea.textcontent.append("administrative resources required.")
    thisalinea.textcontent.append("14")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "5. OTHER ELEMENTS"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 32
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "After the proposed directive enters into force, Member States will have a maximum of 2 years to adopt measures needed to transpose the directive and to notify these measures to the Commission. The Commission will verify the completeness of the transposition measures notified by the Member States and the compliance of these measures based on explanatory documents explaining the relationship between the components of the directive and the corresponding parts of national transposition instruments. The proposal has several provisions governing the monitoring arrangements. It puts in place a coherent soil monitoring framework to provide data on soil health in all "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Implementation plans and monitoring, evaluation and reporting arrangements"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 33
    thisalinea.parentID = 32
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "After the proposed directive enters into force, Member States will have a maximum of 2 years to adopt measures needed to transpose the directive and to notify these measures to the Commission. The Commission will verify the completeness of the transposition measures notified by the Member States and the compliance of these measures based on explanatory documents explaining the relationship between the components of the directive and the corresponding parts of national transposition instruments. The proposal has several provisions governing the monitoring arrangements. It puts in place a coherent soil monitoring framework to provide data on soil health in all "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("After the proposed directive enters into force, Member States will have a maximum of 2 years")
    thisalinea.textcontent.append("to adopt measures needed to transpose the directive and to notify these measures to the")
    thisalinea.textcontent.append("Commission.")
    thisalinea.textcontent.append("The Commission will verify the completeness of the transposition measures notified by the")
    thisalinea.textcontent.append("Member States and the compliance of these measures based on explanatory documents")
    thisalinea.textcontent.append("explaining the relationship between the components of the directive and the corresponding")
    thisalinea.textcontent.append("parts of national transposition instruments.")
    thisalinea.textcontent.append("The proposal has several provisions governing the monitoring arrangements. It puts in place a")
    thisalinea.textcontent.append("coherent soil monitoring framework to provide data on soil health in all Member States and")
    thisalinea.textcontent.append("for all soils. These data will be made public in accordance with the applicable legislation.")
    thisalinea.textcontent.append("The register of contaminated and potentially contaminated sites will enable the Commission")
    thisalinea.textcontent.append("and citizens, NGOs and other interested parties to monitor the obligations regarding soil")
    thisalinea.textcontent.append("contamination.")
    thisalinea.textcontent.append("The proposal also sets out reporting provisions. Member States are required to report to the")
    thisalinea.textcontent.append("Commission on a limited number of issues every 5 years.")
    thisalinea.textcontent.append("The proposal provides for an evaluation of the directive which will be based on the")
    thisalinea.textcontent.append("information reported by Member States and any other available information. This evaluation")
    thisalinea.textcontent.append("will serve as a basis for revising the directive. The main findings of the evaluation will be")
    thisalinea.textcontent.append("transmitted to the European Parliament, the Council, the European Economic and Social")
    thisalinea.textcontent.append("Committee, and the Committee of the Regions.")
    thisalinea.textcontent.append("The proposal also contains provisions to adapt the rules in line with scientific and technical")
    thisalinea.textcontent.append("progress.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Explanatory documents (for directives)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 34
    thisalinea.parentID = 32
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "The proposed directive touches on environmental law and aims to regulate soil health at EU level while giving Member States a wide degree of flexibility on how to achieve the objectives. There is currently no dedicated EU legislation on soil and the proposed directive contains new concepts and obligations regarding soils which will mainly affect public authorities and stakeholders in agriculture, forestry and industrial sectors. Member States might use different legal instruments to transpose the directive and might need to amend existing national provisions. It is likely that implementing the directive will affect not only the central/national level of legislation "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposed directive touches on environmental law and aims to regulate soil health at EU")
    thisalinea.textcontent.append("level while giving Member States a wide degree of flexibility on how to achieve the")
    thisalinea.textcontent.append("objectives. There is currently no dedicated EU legislation on soil and the proposed directive")
    thisalinea.textcontent.append("contains new concepts and obligations regarding soils which will mainly affect public")
    thisalinea.textcontent.append("authorities and stakeholders in agriculture, forestry and industrial sectors.")
    thisalinea.textcontent.append("Member States might use different legal instruments to transpose the directive and might need")
    thisalinea.textcontent.append("to amend existing national provisions. It is likely that implementing the directive will affect")
    thisalinea.textcontent.append("not only the central/national level of legislation in the Member States but also different levels")
    thisalinea.textcontent.append("of regional and local legislation. Explanatory documents will therefore aid the process to")
    thisalinea.textcontent.append("verify transposition and help reducing the administrative burden on the Commission of")
    thisalinea.textcontent.append("compliance monitoring. Without these, considerable resources and numerous contacts with")
    thisalinea.textcontent.append("national authorities would be required to track the methods of transposition in all Member")
    thisalinea.textcontent.append("States.")
    thisalinea.textcontent.append("Against this background it is proportionate to ask Member States to shoulder the burden of")
    thisalinea.textcontent.append("providing explanatory documents in order to equip the Commission for overseeing")
    thisalinea.textcontent.append("transposition of the proposed directive, which is central to the European Green Deal. Member")
    thisalinea.textcontent.append("15")
    thisalinea.textcontent.append("States should therefore notify transposition measures along with one or more documents")
    thisalinea.textcontent.append("explaining how the components of the directive are linked with the corresponding parts of")
    thisalinea.textcontent.append("national transposition instruments. This is in accordance with the Joint Political Declaration of")
    thisalinea.textcontent.append("28 September 2011 of Member States and the Commission on explanatory documents.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "• Detailed explanation of the specific provisions of the proposal"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 35
    thisalinea.parentID = 32
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "16 contaminated site poses unacceptable risks to human health or the environment and to take the appropriate risk reduction measures. Articles 18 contains reporting requirements. It states that Member States must regularly report data and information to the Commission in electronic format. Articles 20 sets out the conditions for the Commission to adopt delegated acts. 17 2023/0232 (COD) Proposal for a Article 1 sets out the overarching objective of the directive which is to put in place a coherent soil monitoring framework that will provide data on soil health in all Member States and to ensure that EU soils are "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("16")
    thisalinea.textcontent.append("contaminated site poses unacceptable risks to human health or the environment and to take the")
    thisalinea.textcontent.append("appropriate risk reduction measures.")
    thisalinea.textcontent.append("Articles 18 contains reporting requirements. It states that Member States must regularly report")
    thisalinea.textcontent.append("data and information to the Commission in electronic format.")
    thisalinea.textcontent.append("Articles 20 sets out the conditions for the Commission to adopt delegated acts.")
    thisalinea.textcontent.append("17")
    thisalinea.textcontent.append("2023/0232 (COD)")
    thisalinea.textcontent.append("Proposal for a")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 1 sets out the overarching objective of the directive which is to put in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 36
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Article 1 sets out the overarching objective of the directive which is to put in place a coherent soil monitoring framework that will provide data on soil health in all Member States and to ensure that EU soils are in healthy condition by 2050 at the latest, so that they can supply multiple services at a scale sufficient to meet environmental, societal and economic needs and to reduce soil pollution to levels no longer considered harmful to human health. The directive contributes to preventing and mitigating the impacts of climate change, increasing resilience against natural disasters and ensuring food security. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 1 sets out the overarching objective of the directive which is to put in place a coherent")
    thisalinea.textcontent.append("soil monitoring framework that will provide data on soil health in all Member States and to")
    thisalinea.textcontent.append("ensure that EU soils are in healthy condition by 2050 at the latest, so that they can supply")
    thisalinea.textcontent.append("multiple services at a scale sufficient to meet environmental, societal and economic needs and")
    thisalinea.textcontent.append("to reduce soil pollution to levels no longer considered harmful to human health. The directive")
    thisalinea.textcontent.append("contributes to preventing and mitigating the impacts of climate change, increasing resilience")
    thisalinea.textcontent.append("against natural disasters and ensuring food security.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 2 sets out the territorial scope of the directive which applies to all soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 37
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Article 2 sets out the territorial scope of the directive which applies to all soil in the EU. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 2 sets out the territorial scope of the directive which applies to all soil in the EU.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 3 provides definitions. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 38
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "Article 3 provides definitions. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 3 provides definitions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Articles 4 and 5 set out the governance requirements. Article 4 states that Member States ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 39
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "Articles 4 and 5 set out the governance requirements. Article 4 states that Member States must establish soil districts throughout their territory to manage the soils and the requirements of the directive. Article 4 also lays down criteria for Member States to use when establishing such soil districts. Article 5 requires Member States to appoint the authorities tasked with carrying out the obligations set out in the directive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Articles 4 and 5 set out the governance requirements. Article 4 states that Member States must")
    thisalinea.textcontent.append("establish soil districts throughout their territory to manage the soils and the requirements of")
    thisalinea.textcontent.append("the directive. Article 4 also lays down criteria for Member States to use when establishing")
    thisalinea.textcontent.append("such soil districts. Article 5 requires Member States to appoint the authorities tasked with")
    thisalinea.textcontent.append("carrying out the obligations set out in the directive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 6 describes the overall monitoring framework based on the soil districts, to ensure that ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 40
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "Article 6 describes the overall monitoring framework based on the soil districts, to ensure that soil health is monitored regularly. It also describes how the Commission can support the action taken by the Member States on soil health monitoring. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 6 describes the overall monitoring framework based on the soil districts, to ensure that")
    thisalinea.textcontent.append("soil health is monitored regularly. It also describes how the Commission can support the")
    thisalinea.textcontent.append("action taken by the Member States on soil health monitoring.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 7 lays down the soil descriptors and criteria for monitoring and assessing soil health. ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 41
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "Article 7 lays down the soil descriptors and criteria for monitoring and assessing soil health. It specifies that some criteria will be established by the Member States. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 7 lays down the soil descriptors and criteria for monitoring and assessing soil health. It")
    thisalinea.textcontent.append("specifies that some criteria will be established by the Member States.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 8 states that Member States must carry out regular soil measurements. It further lays ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 42
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "Article 8 states that Member States must carry out regular soil measurements. It further lays down methodologies for identifying the sampling points and for measuring the soil descriptors. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 8 states that Member States must carry out regular soil measurements. It further lays")
    thisalinea.textcontent.append("down methodologies for identifying the sampling points and for measuring the soil")
    thisalinea.textcontent.append("descriptors.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 9 requires Member States to assess soil health based on regular soil measurements in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 43
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "Article 9 requires Member States to assess soil health based on regular soil measurements in order to ascertain whether the soils are healthy. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 9 requires Member States to assess soil health based on regular soil measurements in")
    thisalinea.textcontent.append("order to ascertain whether the soils are healthy.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 10 lays down sustainable soil management principles that aim to maintain or enhance ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 44
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "Article 10 lays down sustainable soil management principles that aim to maintain or enhance soil health. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 10 lays down sustainable soil management principles that aim to maintain or enhance")
    thisalinea.textcontent.append("soil health.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 11 provides for mitigation principles that the Member States must follow in the event ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 45
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "Article 11 provides for mitigation principles that the Member States must follow in the event of land take. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 11 provides for mitigation principles that the Member States must follow in the event")
    thisalinea.textcontent.append("of land take.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 12 sets an overarching obligation to take a risk-based approach to identifying and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 46
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "Article 12 sets an overarching obligation to take a risk-based approach to identifying and investigating potentially contaminated sites and for managing contaminated sites. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 12 sets an overarching obligation to take a risk-based approach to identifying and")
    thisalinea.textcontent.append("investigating potentially contaminated sites and for managing contaminated sites.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 13 requires that all potentially contaminated sites are identified and Article 14 requires ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 47
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "Article 13 requires that all potentially contaminated sites are identified and Article 14 requires that these sites are investigated to ascertain the presence of contamination. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 13 requires that all potentially contaminated sites are identified and Article 14 requires")
    thisalinea.textcontent.append("that these sites are investigated to ascertain the presence of contamination.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 15 contains obligations regarding the management of contaminated sites. It sets out ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 48
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "Article 15 contains obligations regarding the management of contaminated sites. It sets out that Member States must carry out a site-specific risk assessment to ascertain whether the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 15 contains obligations regarding the management of contaminated sites. It sets out")
    thisalinea.textcontent.append("that Member States must carry out a site-specific risk assessment to ascertain whether the")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 16 requires Member States to draw up a register of contaminated sites and potentially ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 49
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "Article 16 requires Member States to draw up a register of contaminated sites and potentially contaminated sites. It states that the register must contain the information set out in Annex VII and that it must be publicly accessible and kept up to date. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 16 requires Member States to draw up a register of contaminated sites and potentially")
    thisalinea.textcontent.append("contaminated sites. It states that the register must contain the information set out in Annex VII")
    thisalinea.textcontent.append("and that it must be publicly accessible and kept up to date.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 17 contains provisions regarding EU financing. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 50
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "Article 17 contains provisions regarding EU financing. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 17 contains provisions regarding EU financing.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 19 provides for access to information to increase transparency. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 51
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "Article 19 provides for access to information to increase transparency. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 19 provides for access to information to increase transparency.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 21 sets out the conditions for the Commission to adopt implementing acts (Committee ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 52
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = "Article 21 sets out the conditions for the Commission to adopt implementing acts (Committee procedure). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 21 sets out the conditions for the Commission to adopt implementing acts (Committee")
    thisalinea.textcontent.append("procedure).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 22 contains requirements governing access to justice. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 53
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "Article 22 contains requirements governing access to justice. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 22 contains requirements governing access to justice.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 23 requires Member States to lay down the rules on penalties applicable to breaches ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 54
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "Article 23 requires Member States to lay down the rules on penalties applicable to breaches of the national provisions adopted under the directive. The penalties must be effective, proportionate and dissuasive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 23 requires Member States to lay down the rules on penalties applicable to breaches of")
    thisalinea.textcontent.append("the national provisions adopted under the directive. The penalties must be effective,")
    thisalinea.textcontent.append("proportionate and dissuasive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 24 provides for an evaluation of the directive. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 55
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = "Article 24 provides for an evaluation of the directive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 24 provides for an evaluation of the directive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 25 contains requirements to transpose the directive into national law. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 56
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "Article 25 contains requirements to transpose the directive into national law. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 25 contains requirements to transpose the directive into national law.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 26 provides for the entry into force of the directive. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 57
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "Article 26 provides for the entry into force of the directive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 26 provides for the entry into force of the directive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "Article 27 specifies that the directive is addressed to the Member States. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 58
    thisalinea.parentID = 35
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 22
    thisalinea.summary = "Article 27 specifies that the directive is addressed to the Member States. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Article 27 specifies that the directive is addressed to the Member States.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "DIRECTIVE OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on Soil Monitoring and Resilience (Soil Monitoring Law)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 59
    thisalinea.parentID = 32
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION, Having regard to the Treaty on the Functioning of the European Union, and in particular Article 192(1) thereof, Having regard to the proposal from the European Commission, After transmission of the draft legislative act to the national parliaments, Having regard to the opinion of the European Economic and Social Committee29, Having regard to the opinion of the Committee of the Regions30, Acting in accordance with the ordinary legislative procedure, Whereas: 18 Strategy33, the Zero Pollution Action Plan34, the EU Climate Adaptation Strategy35 and the EU Soil Strategy for 203036. 19 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION,")
    thisalinea.textcontent.append("Having regard to the Treaty on the Functioning of the European Union, and in particular")
    thisalinea.textcontent.append("Article 192(1) thereof,")
    thisalinea.textcontent.append("Having regard to the proposal from the European Commission,")
    thisalinea.textcontent.append("After transmission of the draft legislative act to the national parliaments,")
    thisalinea.textcontent.append("Having regard to the opinion of the European Economic and Social Committee29,")
    thisalinea.textcontent.append("Having regard to the opinion of the Committee of the Regions30,")
    thisalinea.textcontent.append("Acting in accordance with the ordinary legislative procedure,")
    thisalinea.textcontent.append("Whereas:")
    thisalinea.textcontent.append("18")
    thisalinea.textcontent.append("Strategy33, the Zero Pollution Action Plan34, the EU Climate Adaptation Strategy35 and")
    thisalinea.textcontent.append("the EU Soil Strategy for 203036.")
    thisalinea.textcontent.append("19")
    thisalinea.textcontent.append("sustainable soil management practices. It also states that significant progress is needed")
    thisalinea.textcontent.append("on identifying contaminated soil sites, restoring degraded soils, defining the conditions")
    thisalinea.textcontent.append("for good ecological status of soils, introducing restoration objectives, and improving")
    thisalinea.textcontent.append("the monitoring of soil health.")
    thisalinea.textcontent.append("20")
    thisalinea.textcontent.append("biodiversity. The Commission’s Communication on Sustainable Carbon Cycles45")
    thisalinea.textcontent.append("underlined the need for clear and transparent identification of the activities that")
    thisalinea.textcontent.append("unambiguously remove carbon from the atmosphere such as the development of a EU")
    thisalinea.textcontent.append("framework for the certification of carbon removals from natural ecosystems including")
    thisalinea.textcontent.append("soils. Moreover, the revised Regulation on Land Use, Land Use Change and Forestry")
    thisalinea.textcontent.append("not only places soil carbon central to the achievement of targets on the pathway to a")
    thisalinea.textcontent.append("climate neutral Europe, but also calls for Member States to prepare a system for the")
    thisalinea.textcontent.append("monitoring of soil carbon stocks, using, inter alia, the land use/cover area frame")
    thisalinea.textcontent.append("statistical survey (LUCAS) dataset.")
    thisalinea.textcontent.append("21")
    thisalinea.textcontent.append("and natural disasters. Practices that enhance water retention and nutrient availability in")
    thisalinea.textcontent.append("soils, soil structure, soil biodiversity and carbon sequestration, increase the resilience")
    thisalinea.textcontent.append("of ecosystems, plants and crops to withstand and recover from drought, natural")
    thisalinea.textcontent.append("disasters, heatwaves and extreme weather events which will become more frequent in")
    thisalinea.textcontent.append("the future due to climate change. In turn, without proper soil management, drought and")
    thisalinea.textcontent.append("natural disasters cause soil degradation and make soils unhealthy. Improvement of soil")
    thisalinea.textcontent.append("health helps to mitigate the economic losses and fatalities associated with climate-")
    thisalinea.textcontent.append("related extremes, which amounted to approximately 560 billion EUR and more than")
    thisalinea.textcontent.append("182.000 casualties in the Union between 1980 and 2021.")
    thisalinea.textcontent.append("22")
    thisalinea.textcontent.append("and of the Council+. There should be a minimum number of soil districts in each")
    thisalinea.textcontent.append("Member State taking into account the size of the Member State. This minimum")
    thisalinea.textcontent.append("number of soil districts for each Member State shall correspond to the number of")
    thisalinea.textcontent.append("NUTS 1 territorial units established in Regulation (EC) No 1059/2003 of the European")
    thisalinea.textcontent.append("Parliament and of the Council48.")
    thisalinea.textcontent.append("23")
    thisalinea.textcontent.append("24")
    thisalinea.textcontent.append("data coming from various sources. That portal should primarily include all the data")
    thisalinea.textcontent.append("collected by the Member States and the Commission as required by this Directive. It")
    thisalinea.textcontent.append("should also be possible to integrate in the portal, on a voluntary basis, other relevant")
    thisalinea.textcontent.append("soil data collected by Member States or any other party (and in particular data")
    thisalinea.textcontent.append("resulting from projects under Horizon Europe and the Mission ‘A Soil Deal for")
    thisalinea.textcontent.append("Europe’), provided that those data meet certain requirements as regards format and")
    thisalinea.textcontent.append("specifications. Those requirements should be specified by the Commission by way of")
    thisalinea.textcontent.append("implementing acts.")
    thisalinea.textcontent.append("25")
    thisalinea.textcontent.append("26")
    thisalinea.textcontent.append("European Parliament and of the Council59, the integrated national energy and climate")
    thisalinea.textcontent.append("plans established in accordance with Regulation (EU) 2018/1999 of the European")
    thisalinea.textcontent.append("Parliament and of the Council60, the national air pollution control programmes")
    thisalinea.textcontent.append("prepared under Directive (EU) 2016/2284 of the European Parliament and of the")
    thisalinea.textcontent.append("Council61, risk assessments and disaster risk management planning established in")
    thisalinea.textcontent.append("accordance with Decision No 1313/2013/EU of the European Parliament and of the")
    thisalinea.textcontent.append("Council62, and national action plans established in accordance with Regulation (UE)")
    thisalinea.textcontent.append("…/… of the European Parliament and of the Council63+. Sustainable soil management")
    thisalinea.textcontent.append("and regeneration practices should be, as far as possible, integrated within these")
    thisalinea.textcontent.append("programmes, plans and measures to the extent that they contribute to the achievement")
    thisalinea.textcontent.append("of their objectives. Consequently, relevant indicators and data, such as soil-related")
    thisalinea.textcontent.append("result indicators under the CAP Regulation and statistical data on agricultural input")
    thisalinea.textcontent.append("and output reported under Regulation (EU) 2022/2379 of the European Parliament and")
    thisalinea.textcontent.append("of the Council64, should be accessible to the competent authorities responsible for")
    thisalinea.textcontent.append("sustainable soil management and regeneration practices and soil health assessment in")
    thisalinea.textcontent.append("order to cross-link these data and indicators and thus enable the most accurate possible")
    thisalinea.textcontent.append("assessment of the effectiveness of the measures chosen.")
    thisalinea.textcontent.append("27")
    thisalinea.textcontent.append("lay down specific events that also trigger such investigation. Such triggering events")
    thisalinea.textcontent.append("may include the request or review of an environmental or building permit or an")
    thisalinea.textcontent.append("authorisation required pursuant to Union legislation or national legislation, soil")
    thisalinea.textcontent.append("excavation activities, land use changes or land or real estate transactions. Soil")
    thisalinea.textcontent.append("investigations may follow different stages, such as a desk study, site visit, preliminary")
    thisalinea.textcontent.append("or exploratory investigation, more detailed or descriptive investigation, and field or")
    thisalinea.textcontent.append("laboratory testing. Baseline reports and monitoring measures implemented in")
    thisalinea.textcontent.append("accordance with Directive 2010/75/EU of the European Parliament and of the")
    thisalinea.textcontent.append("Council65 could also qualify as soil investigation where appropriate.")
    thisalinea.textcontent.append("28")
    thisalinea.textcontent.append("be informed on the existence and on the management of potentially contaminated sites")
    thisalinea.textcontent.append("and contaminated sites. Because the presence of soil contamination is not yet")
    thisalinea.textcontent.append("confirmed but only suspected on potentially contaminated sites, the difference between")
    thisalinea.textcontent.append("contaminated sites and potentially contaminated sites has to be communicated and")
    thisalinea.textcontent.append("explained well to the public to avoid raising unnecessary concern.")
    thisalinea.textcontent.append("29")
    thisalinea.textcontent.append("appropriate consultations during its preparatory work, including at expert level, and")
    thisalinea.textcontent.append("that those consultations be conducted in accordance with the principles laid down in")
    thisalinea.textcontent.append("the Interinstitutional Agreement on Better Law-Making of 13 April 201671. In")
    thisalinea.textcontent.append("particular, to ensure equal participation in the preparation of delegated acts, the")
    thisalinea.textcontent.append("European Parliament and the Council receive all documents at the same time as")
    thisalinea.textcontent.append("Member States’ experts, and their experts systematically have access to meetings of")
    thisalinea.textcontent.append("Commission expert groups dealing with the preparation of delegated acts.")
    thisalinea.textcontent.append("30")
    thisalinea.textcontent.append("HAVE ADOPTED THIS DIRECTIVE:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(1) Soil is a vital, limited, non-renewable and irreplaceable resource that is crucial for the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 60
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) Soil is a vital, limited, non-renewable and irreplaceable resource that is crucial for the economy, the environment and the society. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) Soil is a vital, limited, non-renewable and irreplaceable resource that is crucial for the")
    thisalinea.textcontent.append("economy, the environment and the society.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(2) Healthy soils are in good chemical, biological and physical condition so that they can ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 61
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) Healthy soils are in good chemical, biological and physical condition so that they can provide ecosystem services that are vital to humans and the environment, such as safe, nutritious and sufficient food, biomass, clean water, nutrients cycling, carbon storage and a habitat for biodiversity. However, 60 to 70 % of the soils in the Union are deteriorated and continue to deteriorate. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) Healthy soils are in good chemical, biological and physical condition so that they can")
    thisalinea.textcontent.append("provide ecosystem services that are vital to humans and the environment, such as safe,")
    thisalinea.textcontent.append("nutritious and sufficient food, biomass, clean water, nutrients cycling, carbon storage")
    thisalinea.textcontent.append("and a habitat for biodiversity. However, 60 to 70 % of the soils in the Union are")
    thisalinea.textcontent.append("deteriorated and continue to deteriorate.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(3) Soil degradation is costing the Union several tens of billion euro every year. Soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 62
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) Soil degradation is costing the Union several tens of billion euro every year. Soil health is impacting the provision of ecosystem services that have an important economic return. Sustainable management and regeneration of soils therefore makes sound economic sense and can significantly increase the price and value of the land in the Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) Soil degradation is costing the Union several tens of billion euro every year. Soil")
    thisalinea.textcontent.append("health is impacting the provision of ecosystem services that have an important")
    thisalinea.textcontent.append("economic return. Sustainable management and regeneration of soils therefore makes")
    thisalinea.textcontent.append("sound economic sense and can significantly increase the price and value of the land in")
    thisalinea.textcontent.append("the Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(4) The European Green Deal31 has set out an ambitious roadmap to transform the Union ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 63
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) The European Green Deal31 has set out an ambitious roadmap to transform the Union into a fair and prosperous society, with a modern, resource-efficient and competitive economy, aiming to protect, conserve and enhance the Union’s natural capital, and to protect the health and well-being of citizens. As part of the European Green Deal, the Commission has adopted the EU Biodiversity Strategy for 203032, the Farm to Fork "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) The European Green Deal31 has set out an ambitious roadmap to transform the Union")
    thisalinea.textcontent.append("into a fair and prosperous society, with a modern, resource-efficient and competitive")
    thisalinea.textcontent.append("economy, aiming to protect, conserve and enhance the Union’s natural capital, and to")
    thisalinea.textcontent.append("protect the health and well-being of citizens. As part of the European Green Deal, the")
    thisalinea.textcontent.append("Commission has adopted the EU Biodiversity Strategy for 203032, the Farm to Fork")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(5) The Union is committed to the 2030 Agenda for Sustainable Development and its ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 64
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) The Union is committed to the 2030 Agenda for Sustainable Development and its Sustainable Development Goals (SDGs)37. Healthy soils contribute directly to the achievement of several SDGs, in particular SDG 2 (zero hunger), SDG 3 (good health and well-being), SDG 6 (clean water and sanitation), SDG 11 (sustainable cities and communities), SDG 12 (responsible consumption and production), SDG 13 (climate action) and SDG 15 (life on land). SDG 15.3 aims to combat desertification, restore degraded land and soil, including land affected by desertification, drought and floods, and strive to achieve a land degradation-neutral world by 2030. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) The Union is committed to the 2030 Agenda for Sustainable Development and its")
    thisalinea.textcontent.append("Sustainable Development Goals (SDGs)37. Healthy soils contribute directly to the")
    thisalinea.textcontent.append("achievement of several SDGs, in particular SDG 2 (zero hunger), SDG 3 (good health")
    thisalinea.textcontent.append("and well-being), SDG 6 (clean water and sanitation), SDG 11 (sustainable cities and")
    thisalinea.textcontent.append("communities), SDG 12 (responsible consumption and production), SDG 13 (climate")
    thisalinea.textcontent.append("action) and SDG 15 (life on land). SDG 15.3 aims to combat desertification, restore")
    thisalinea.textcontent.append("degraded land and soil, including land affected by desertification, drought and floods,")
    thisalinea.textcontent.append("and strive to achieve a land degradation-neutral world by 2030.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(6) The Union and its Member States, as parties to the Convention on Biological ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 65
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(6) The Union and its Member States, as parties to the Convention on Biological Diversity, approved by Council Decision 93/626/EEC38, agreed at the 15th Conference of the Parties on the “Kunming-Montreal Global Biodiversity Framework” (GBF)39 which comprises several action-oriented global targets for 2030 of relevance for soil health. Nature’s contributions to people, including soil health, should be restored, maintained and enhanced. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(6) The Union and its Member States, as parties to the Convention on Biological")
    thisalinea.textcontent.append("Diversity, approved by Council Decision 93/626/EEC38, agreed at the 15th Conference")
    thisalinea.textcontent.append("of the Parties on the “Kunming-Montreal Global Biodiversity Framework” (GBF)39")
    thisalinea.textcontent.append("which comprises several action-oriented global targets for 2030 of relevance for soil")
    thisalinea.textcontent.append("health. Nature’s contributions to people, including soil health, should be restored,")
    thisalinea.textcontent.append("maintained and enhanced.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(7) The Union and its Member States, as Parties to the UN Convention to Combat ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 66
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(7) The Union and its Member States, as Parties to the UN Convention to Combat Desertification (UNCCD), approved by Council Decision 98/216/EC40, have committed to combat desertification and mitigate the effects of drought in affected countries. Thirteen Member States41 have declared themselves as parties affected by desertification under the UNCDD. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(7) The Union and its Member States, as Parties to the UN Convention to Combat")
    thisalinea.textcontent.append("Desertification (UNCCD), approved by Council Decision 98/216/EC40, have")
    thisalinea.textcontent.append("committed to combat desertification and mitigate the effects of drought in affected")
    thisalinea.textcontent.append("countries. Thirteen Member States41 have declared themselves as parties affected by")
    thisalinea.textcontent.append("desertification under the UNCDD.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(8) In the context of United Nations Framework Convention on Climate Change ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 67
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "(8) In the context of United Nations Framework Convention on Climate Change (UNFCCC) land and soil is considered simultaneously as a source and a sink of carbon. The Union and Member States as parties have committed to promote sustainable management, conservation and enhancement of carbon sinks and reservoirs. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(8) In the context of United Nations Framework Convention on Climate Change")
    thisalinea.textcontent.append("(UNFCCC) land and soil is considered simultaneously as a source and a sink of")
    thisalinea.textcontent.append("carbon. The Union and Member States as parties have committed to promote")
    thisalinea.textcontent.append("sustainable management, conservation and enhancement of carbon sinks and")
    thisalinea.textcontent.append("reservoirs.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(9) The EU Biodiversity Strategy for 2030 states that it is essential to step up ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 68
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "(9) The EU Biodiversity Strategy for 2030 states that it is essential to step up efforts to protect soil fertility, reduce soil erosion and increase soil organic matter by adopting "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(9) The EU Biodiversity Strategy for 2030 states that it is essential to step up efforts to")
    thisalinea.textcontent.append("protect soil fertility, reduce soil erosion and increase soil organic matter by adopting")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(10) The EU Soil Strategy for 2030 sets the long-term vision that by 2050, all ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 69
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "(10) The EU Soil Strategy for 2030 sets the long-term vision that by 2050, all EU soil ecosystems are in healthy condition and are thus more resilient. As a key solution, healthy soils contribute to address the EU’s goals of achieving climate neutrality and becoming resilient to climate change, developing a clean and circular (bio)economy, reversing biodiversity loss, safeguarding human health, halting desertification and reversing land degradation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(10) The EU Soil Strategy for 2030 sets the long-term vision that by 2050, all EU soil")
    thisalinea.textcontent.append("ecosystems are in healthy condition and are thus more resilient. As a key solution,")
    thisalinea.textcontent.append("healthy soils contribute to address the EU’s goals of achieving climate neutrality and")
    thisalinea.textcontent.append("becoming resilient to climate change, developing a clean and circular (bio)economy,")
    thisalinea.textcontent.append("reversing biodiversity loss, safeguarding human health, halting desertification and")
    thisalinea.textcontent.append("reversing land degradation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(11) Funding is vital to enable a transition to healthy soils. The Multiannual Financial ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 70
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "(11) Funding is vital to enable a transition to healthy soils. The Multiannual Financial Framework presents several funding opportunities available for the protection, sustainable management and regeneration of soils. A ‘Soil Deal for Europe’ is one of the five EU missions of the Horizon Europe programme and is specifically dedicated to promoting soil health. The Soil Mission is a key instrument for the implementation of this Directive. It aims to lead the transition to healthy soils through funding an ambitious research and innovation programme, establishing a network of 100 living labs and lighthouses in rural and urban areas, advancing the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(11) Funding is vital to enable a transition to healthy soils. The Multiannual Financial")
    thisalinea.textcontent.append("Framework presents several funding opportunities available for the protection,")
    thisalinea.textcontent.append("sustainable management and regeneration of soils. A ‘Soil Deal for Europe’ is one of")
    thisalinea.textcontent.append("the five EU missions of the Horizon Europe programme and is specifically dedicated")
    thisalinea.textcontent.append("to promoting soil health. The Soil Mission is a key instrument for the implementation")
    thisalinea.textcontent.append("of this Directive. It aims to lead the transition to healthy soils through funding an")
    thisalinea.textcontent.append("ambitious research and innovation programme, establishing a network of 100 living")
    thisalinea.textcontent.append("labs and lighthouses in rural and urban areas, advancing the development of a")
    thisalinea.textcontent.append("harmonized soil monitoring framework and increasing the awareness of the")
    thisalinea.textcontent.append("importance of soil. Other Union programmes that present objectives contributing to")
    thisalinea.textcontent.append("healthy soils are the Common Agricultural Policy, the Cohesion Policy funds, the")
    thisalinea.textcontent.append("Programme for Environment and Climate Action, the Horizon Europe work")
    thisalinea.textcontent.append("programme, the Technical Support Instrument, the Recovery and Resilience Facility")
    thisalinea.textcontent.append("and InvestEU.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(12) The Soil Strategy for 2030 announced that the Commission would table a legislative ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 71
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "(12) The Soil Strategy for 2030 announced that the Commission would table a legislative proposal on soil health to enable the objectives of the Soil Strategy and to achieve good soil health across the EU by 2050. In its resolution of 28 April 2021 on soil protection42, the European Parliament emphasised the importance of protecting soil and promoting healthy soils in the Union, bearing in mind that the degradation continues, despite the limited and uneven action being taken in some Member States. The European Parliament called on the Commission to design a Union wide common legal framework, with full respect "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(12) The Soil Strategy for 2030 announced that the Commission would table a legislative")
    thisalinea.textcontent.append("proposal on soil health to enable the objectives of the Soil Strategy and to achieve")
    thisalinea.textcontent.append("good soil health across the EU by 2050. In its resolution of 28 April 2021 on soil")
    thisalinea.textcontent.append("protection42, the European Parliament emphasised the importance of protecting soil")
    thisalinea.textcontent.append("and promoting healthy soils in the Union, bearing in mind that the degradation")
    thisalinea.textcontent.append("continues, despite the limited and uneven action being taken in some Member States.")
    thisalinea.textcontent.append("The European Parliament called on the Commission to design a Union wide common")
    thisalinea.textcontent.append("legal framework, with full respect for the subsidiarity principle, for the protection and")
    thisalinea.textcontent.append("sustainable use of soil, addressing all major soil threats.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(13) In its conclusions of 23 October 202043, the Council supported the Commission in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 72
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "(13) In its conclusions of 23 October 202043, the Council supported the Commission in stepping up efforts to better protect soils and soil biodiversity, as a non-renewable resource of vital importance. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(13) In its conclusions of 23 October 202043, the Council supported the Commission in")
    thisalinea.textcontent.append("stepping up efforts to better protect soils and soil biodiversity, as a non-renewable")
    thisalinea.textcontent.append("resource of vital importance.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(14) Regulation (EU) 2021/1119 of the European Parliament and of the Council44 sets out a ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 73
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "(14) Regulation (EU) 2021/1119 of the European Parliament and of the Council44 sets out a binding objective of climate neutrality in the Union by 2050 and negative emissions thereafter, and of prioritising swift and predictable emission reductions and, at the same time, enhancing removals by natural sinks. Sustainable soil management results in increased carbon sequestration and in most cases in co-benefits for ecosystems and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(14) Regulation (EU) 2021/1119 of the European Parliament and of the Council44 sets out a")
    thisalinea.textcontent.append("binding objective of climate neutrality in the Union by 2050 and negative emissions")
    thisalinea.textcontent.append("thereafter, and of prioritising swift and predictable emission reductions and, at the")
    thisalinea.textcontent.append("same time, enhancing removals by natural sinks. Sustainable soil management results")
    thisalinea.textcontent.append("in increased carbon sequestration and in most cases in co-benefits for ecosystems and")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(15) The Commission’s Communication on adaptation to climate change46 underlined that ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 74
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "(15) The Commission’s Communication on adaptation to climate change46 underlined that using nature-based solutions inland, including the restoration of the sponge-like function of soils, will boost the supply of clean and fresh water, reduce the impacts of flooding and alleviate the impacts of droughts. It is important to maximise the capacity of soils to retain and purify water and reduce pollution. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(15) The Commission’s Communication on adaptation to climate change46 underlined that")
    thisalinea.textcontent.append("using nature-based solutions inland, including the restoration of the sponge-like")
    thisalinea.textcontent.append("function of soils, will boost the supply of clean and fresh water, reduce the impacts of")
    thisalinea.textcontent.append("flooding and alleviate the impacts of droughts. It is important to maximise the capacity")
    thisalinea.textcontent.append("of soils to retain and purify water and reduce pollution.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(16) The Zero Pollution Action Plan adopted by the Commission sets out the vision for ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 75
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "(16) The Zero Pollution Action Plan adopted by the Commission sets out the vision for 2050 that air, water and soil pollution is reduced to levels no longer considered harmful to health and natural ecosystems and that respect the boundaries our planet can cope with, thus creating a toxic-free environment. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(16) The Zero Pollution Action Plan adopted by the Commission sets out the vision for")
    thisalinea.textcontent.append("2050 that air, water and soil pollution is reduced to levels no longer considered")
    thisalinea.textcontent.append("harmful to health and natural ecosystems and that respect the boundaries our planet")
    thisalinea.textcontent.append("can cope with, thus creating a toxic-free environment.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(17) The Commission’s Communication on safeguarding food security and reinforcing the ..."
    thisalinea.titlefontsize = "11.999999999999943"
    thisalinea.nativeID = 76
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = "(17) The Commission’s Communication on safeguarding food security and reinforcing the resilience of food systems47 stressed that food sustainability is fundamental for food security. Healthy soils make the Union food system more resilient by providing the basis for nutritious and sufficient food. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(17) The Commission’s Communication on safeguarding food security and reinforcing the")
    thisalinea.textcontent.append("resilience of food systems47 stressed that food sustainability is fundamental for food")
    thisalinea.textcontent.append("security. Healthy soils make the Union food system more resilient by providing the")
    thisalinea.textcontent.append("basis for nutritious and sufficient food.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(18) It is necessary to set measures for monitoring and assessing soil health, managing soils ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 77
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "(18) It is necessary to set measures for monitoring and assessing soil health, managing soils sustainably and tackling contaminated sites to achieve healthy soils by 2050, to maintain them in healthy condition and meet the Union’s objectives on climate and biodiversity, to prevent and respond to droughts and natural disasters, to protect human health and to ensure food security and safety. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(18) It is necessary to set measures for monitoring and assessing soil health, managing soils")
    thisalinea.textcontent.append("sustainably and tackling contaminated sites to achieve healthy soils by 2050, to")
    thisalinea.textcontent.append("maintain them in healthy condition and meet the Union’s objectives on climate and")
    thisalinea.textcontent.append("biodiversity, to prevent and respond to droughts and natural disasters, to protect")
    thisalinea.textcontent.append("human health and to ensure food security and safety.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(19) Soils host more than 25% of all biodiversity and are the second largest carbon ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 78
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "(19) Soils host more than 25% of all biodiversity and are the second largest carbon pool of the planet. Due to their ability to capture and store carbon, healthy soils contribute to the achievement of the Union’s objectives on climate change. Healthy soils also provide a favourable habitat for organisms to thrive and are crucial for enhancing biodiversity and the stability of ecosystems. Biodiversity below and above ground are intimately connected and interact through mutualistic relationships (e.g. mycorrhizal fungi that connect plant roots). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(19) Soils host more than 25% of all biodiversity and are the second largest carbon pool of")
    thisalinea.textcontent.append("the planet. Due to their ability to capture and store carbon, healthy soils contribute to")
    thisalinea.textcontent.append("the achievement of the Union’s objectives on climate change. Healthy soils also")
    thisalinea.textcontent.append("provide a favourable habitat for organisms to thrive and are crucial for enhancing")
    thisalinea.textcontent.append("biodiversity and the stability of ecosystems. Biodiversity below and above ground are")
    thisalinea.textcontent.append("intimately connected and interact through mutualistic relationships (e.g. mycorrhizal")
    thisalinea.textcontent.append("fungi that connect plant roots).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(20) Floods, wildfires and extreme weather events are natural disaster risks of the highest ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 79
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = "(20) Floods, wildfires and extreme weather events are natural disaster risks of the highest concern across Europe. The concern for droughts and water scarcity is rapidly increasing across the Union. In 2020, 24 Member States considered droughts and water scarcity to be key emerging or climate related disaster risks, compared to only 11 Member States in 2015. Healthy soils are instrumental for the resilience to droughts "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(20) Floods, wildfires and extreme weather events are natural disaster risks of the highest")
    thisalinea.textcontent.append("concern across Europe. The concern for droughts and water scarcity is rapidly")
    thisalinea.textcontent.append("increasing across the Union. In 2020, 24 Member States considered droughts and")
    thisalinea.textcontent.append("water scarcity to be key emerging or climate related disaster risks, compared to only")
    thisalinea.textcontent.append("11 Member States in 2015. Healthy soils are instrumental for the resilience to droughts")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(21) Soil health contributes directly to human health and well-being. Healthy soils provide ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 80
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "(21) Soil health contributes directly to human health and well-being. Healthy soils provide safe and nutritious food, and have the ability to filter contaminants, hence preserving drinking water quality. Soil contamination can harm human health through ingestion, inhalation or dermal contact. Human exposure to the healthy soil microbial community is beneficial to develop the immune system and resistance against certain diseases and allergies. Healthy soils support the growth of trees, flowers, and grasses, and create green infrastructure that offers aesthetic value, well-being, and quality of life. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(21) Soil health contributes directly to human health and well-being. Healthy soils provide")
    thisalinea.textcontent.append("safe and nutritious food, and have the ability to filter contaminants, hence preserving")
    thisalinea.textcontent.append("drinking water quality. Soil contamination can harm human health through ingestion,")
    thisalinea.textcontent.append("inhalation or dermal contact. Human exposure to the healthy soil microbial community")
    thisalinea.textcontent.append("is beneficial to develop the immune system and resistance against certain diseases and")
    thisalinea.textcontent.append("allergies. Healthy soils support the growth of trees, flowers, and grasses, and create")
    thisalinea.textcontent.append("green infrastructure that offers aesthetic value, well-being, and quality of life.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(22) Soil degradation impacts fertility, yields, pest resistance and nutritional food quality. ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 81
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "(22) Soil degradation impacts fertility, yields, pest resistance and nutritional food quality. Since 95 % of our food is directly or indirectly produced on soils and the global population continues to increase, it is key that this finite natural resource remains healthy to ensure food security in the long-term and secure the productivity and profitability of Union agriculture. Sustainable soil management practices maintain or enhance soil health and contribute to the sustainability and resilience of the food system. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(22) Soil degradation impacts fertility, yields, pest resistance and nutritional food quality.")
    thisalinea.textcontent.append("Since 95 % of our food is directly or indirectly produced on soils and the global")
    thisalinea.textcontent.append("population continues to increase, it is key that this finite natural resource remains")
    thisalinea.textcontent.append("healthy to ensure food security in the long-term and secure the productivity and")
    thisalinea.textcontent.append("profitability of Union agriculture. Sustainable soil management practices maintain or")
    thisalinea.textcontent.append("enhance soil health and contribute to the sustainability and resilience of the food")
    thisalinea.textcontent.append("system.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(23) The long-term objective of the Directive is to achieve healthy soils by 2050. As ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 82
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 22
    thisalinea.summary = "(23) The long-term objective of the Directive is to achieve healthy soils by 2050. As an intermediate step, in light of the limited knowledge about the condition of soils and about the effectiveness and costs of the measures to regenerate their health, the directive takes a staged approach. In the first stage the focus will be on setting up the soil monitoring framework and assessing the situation of soils throughout the EU. It also includes requirements to lay down measures to manage soils sustainably and regenerate unhealthy soils once their condition is established, but without imposing an obligation to achieve "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(23) The long-term objective of the Directive is to achieve healthy soils by 2050. As an")
    thisalinea.textcontent.append("intermediate step, in light of the limited knowledge about the condition of soils and")
    thisalinea.textcontent.append("about the effectiveness and costs of the measures to regenerate their health, the")
    thisalinea.textcontent.append("directive takes a staged approach. In the first stage the focus will be on setting up the")
    thisalinea.textcontent.append("soil monitoring framework and assessing the situation of soils throughout the EU. It")
    thisalinea.textcontent.append("also includes requirements to lay down measures to manage soils sustainably and")
    thisalinea.textcontent.append("regenerate unhealthy soils once their condition is established, but without imposing an")
    thisalinea.textcontent.append("obligation to achieve healthy soils by 2050 neither intermediate targets. This")
    thisalinea.textcontent.append("proportionate approach will allow sustainable soil management and regeneration of")
    thisalinea.textcontent.append("unhealthy soils to be well prepared, incentivised and set in motion. In a second stage,")
    thisalinea.textcontent.append("as soon as the results of the first assessment of soils and trends analysis are available,")
    thisalinea.textcontent.append("the Commission will take stock of the progress towards the 2050 objective and the")
    thisalinea.textcontent.append("experience thereof, and will propose a review of the directive if necessary to accelerate")
    thisalinea.textcontent.append("progress towards 2050.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(24) Addressing the pressures on soils and identifying the appropriate measures to maintain ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 83
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 23
    thisalinea.summary = "(24) Addressing the pressures on soils and identifying the appropriate measures to maintain or regenerate soil health requires that the variety of soil types, the specific local and climatic conditions and the land use or the land cover is taken into account. It is therefore appropriate that Member States establish soil districts. Soil districts should constitute the basic governance units to manage soils and to take measures to comply with the requirements laid down in this Directive, in particular with regard to the monitoring and assessment of soil health. The number, geographic extent and boundaries of soil districts for each "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(24) Addressing the pressures on soils and identifying the appropriate measures to maintain")
    thisalinea.textcontent.append("or regenerate soil health requires that the variety of soil types, the specific local and")
    thisalinea.textcontent.append("climatic conditions and the land use or the land cover is taken into account. It is")
    thisalinea.textcontent.append("therefore appropriate that Member States establish soil districts. Soil districts should")
    thisalinea.textcontent.append("constitute the basic governance units to manage soils and to take measures to comply")
    thisalinea.textcontent.append("with the requirements laid down in this Directive, in particular with regard to the")
    thisalinea.textcontent.append("monitoring and assessment of soil health. The number, geographic extent and")
    thisalinea.textcontent.append("boundaries of soil districts for each Member State should be determined in order to")
    thisalinea.textcontent.append("facilitate the implementation of Regulation (UE) …/…. of the European Parliament")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(25) In order to ensure an appropriate governance on soils, Member States should be ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 84
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 24
    thisalinea.summary = "(25) In order to ensure an appropriate governance on soils, Member States should be required to appoint a competent authority for each soil district. Member States should be allowed to appoint any additional competent authority at appropriate level including at national or regional level. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(25) In order to ensure an appropriate governance on soils, Member States should be")
    thisalinea.textcontent.append("required to appoint a competent authority for each soil district. Member States should")
    thisalinea.textcontent.append("be allowed to appoint any additional competent authority at appropriate level")
    thisalinea.textcontent.append("including at national or regional level.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(26) In order to have a common definition of healthy soil condition, there is a ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 85
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 25
    thisalinea.summary = "(26) In order to have a common definition of healthy soil condition, there is a need to define a minimum common set of measurable criteria, which, if not respected leads to a critical loss in the soil’s capacity to function as a vital living system and to provide ecosystem services. Such criteria should reflect and be based on the existing level of soil science. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(26) In order to have a common definition of healthy soil condition, there is a need to")
    thisalinea.textcontent.append("define a minimum common set of measurable criteria, which, if not respected leads to")
    thisalinea.textcontent.append("a critical loss in the soil’s capacity to function as a vital living system and to provide")
    thisalinea.textcontent.append("ecosystem services. Such criteria should reflect and be based on the existing level of")
    thisalinea.textcontent.append("soil science.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(27) In order to describe soil degradation it is necessary to establish soil descriptors that ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 86
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 26
    thisalinea.summary = "(27) In order to describe soil degradation it is necessary to establish soil descriptors that can be measured or estimated. Even if there is significant variability between soil types, climatic conditions and land uses, the current scientific knowledge allows to set criteria at Union level for some of those soil descriptors. However, Member States should be able to adapt the criteria for some of these soil descriptors based on specific national or local conditions and define the criteria for other soil descriptors for which common criteria at EU level cannot be established at this stage. For those descriptors for which "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(27) In order to describe soil degradation it is necessary to establish soil descriptors that can")
    thisalinea.textcontent.append("be measured or estimated. Even if there is significant variability between soil types,")
    thisalinea.textcontent.append("climatic conditions and land uses, the current scientific knowledge allows to set")
    thisalinea.textcontent.append("criteria at Union level for some of those soil descriptors. However, Member States")
    thisalinea.textcontent.append("should be able to adapt the criteria for some of these soil descriptors based on specific")
    thisalinea.textcontent.append("national or local conditions and define the criteria for other soil descriptors for which")
    thisalinea.textcontent.append("common criteria at EU level cannot be established at this stage. For those descriptors")
    thisalinea.textcontent.append("for which clear criteria that would distinguish between healthy and unhealthy")
    thisalinea.textcontent.append("condition cannot be identified now, only monitoring and assessment are required. This")
    thisalinea.textcontent.append("will facilitate the development of such criteria in future.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(28) In order to create incentives, Member States should set up mechanisms to recognize ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 87
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 27
    thisalinea.summary = "(28) In order to create incentives, Member States should set up mechanisms to recognize the efforts of landowners and land managers to maintain the soil in healthy condition, including in the form of soil health certification complementary to the Union regulatory framework for carbon removals, and supporting the implementation of the renewable energy sustainability criteria set out in article 29 of Directive (EU) 2018/2001 of the European Parliament and of the Council49. The Commission should facilitate soil health certification by inter alia exchanging information and promoting best practices, raising awareness and assessing feasibility of developing recognition of certification schemes at "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(28) In order to create incentives, Member States should set up mechanisms to recognize")
    thisalinea.textcontent.append("the efforts of landowners and land managers to maintain the soil in healthy condition,")
    thisalinea.textcontent.append("including in the form of soil health certification complementary to the Union")
    thisalinea.textcontent.append("regulatory framework for carbon removals, and supporting the implementation of the")
    thisalinea.textcontent.append("renewable energy sustainability criteria set out in article 29 of Directive (EU)")
    thisalinea.textcontent.append("2018/2001 of the European Parliament and of the Council49. The Commission should")
    thisalinea.textcontent.append("facilitate soil health certification by inter alia exchanging information and promoting")
    thisalinea.textcontent.append("best practices, raising awareness and assessing feasibility of developing recognition of")
    thisalinea.textcontent.append("certification schemes at Union level. Synergies between different certification schemes")
    thisalinea.textcontent.append("should be exploited as much as possible to reduce administrative burden for those")
    thisalinea.textcontent.append("applying for relevant certifications.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(29) Some soils have special characteristics either because they are atypical by nature and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 88
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 28
    thisalinea.summary = "(29) Some soils have special characteristics either because they are atypical by nature and constitute rare habitats for biodiversity or unique landscapes or because they have been heavily modified by humans. Those characteristics should be taken into account in the context of the definition of healthy soils and the requirements to achieve healthy soil condition. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(29) Some soils have special characteristics either because they are atypical by nature and")
    thisalinea.textcontent.append("constitute rare habitats for biodiversity or unique landscapes or because they have")
    thisalinea.textcontent.append("been heavily modified by humans. Those characteristics should be taken into account")
    thisalinea.textcontent.append("in the context of the definition of healthy soils and the requirements to achieve healthy")
    thisalinea.textcontent.append("soil condition.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(30) Soil is a limited resource subject to an ever-growing competition for different uses. ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 89
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 29
    thisalinea.summary = "(30) Soil is a limited resource subject to an ever-growing competition for different uses. Land take is a process often driven by economic development needs, that transforms natural and semi-natural areas (including agricultural and forestry land, gardens and parks) into artificial land development, using soil as a platform for constructions and infrastructure, as a direct source of raw material or as archive for historic patrimony. This transformation may cause the loss, often irreversibly, of the capacity of soils to provide other ecosystem services (provision of food and biomass, water and nutrients cycling, basis for biodiversity and carbon storage). In particular, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(30) Soil is a limited resource subject to an ever-growing competition for different uses.")
    thisalinea.textcontent.append("Land take is a process often driven by economic development needs, that transforms")
    thisalinea.textcontent.append("natural and semi-natural areas (including agricultural and forestry land, gardens and")
    thisalinea.textcontent.append("parks) into artificial land development, using soil as a platform for constructions and")
    thisalinea.textcontent.append("infrastructure, as a direct source of raw material or as archive for historic patrimony.")
    thisalinea.textcontent.append("This transformation may cause the loss, often irreversibly, of the capacity of soils to")
    thisalinea.textcontent.append("provide other ecosystem services (provision of food and biomass, water and nutrients")
    thisalinea.textcontent.append("cycling, basis for biodiversity and carbon storage). In particular, land take often affects")
    thisalinea.textcontent.append("the most fertile agricultural soils, putting food security in jeopardy. Sealed soil also")
    thisalinea.textcontent.append("exposes human settlements to higher flood peaks and more intense heat island effects.")
    thisalinea.textcontent.append("Therefore, it is necessary to monitor land take and soil sealing and their effects on")
    thisalinea.textcontent.append("soil’s capacity to provide ecosystem services. It is also appropriate to lay down certain")
    thisalinea.textcontent.append("principles to mitigate the impacts of land take as part of sustainable soil management.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(31) The assessment of soil health based on the monitoring network should be accurate ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 90
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 30
    thisalinea.summary = "(31) The assessment of soil health based on the monitoring network should be accurate while at the same time keeping the costs of such monitoring at reasonable level. It is therefore appropriate to lay down criteria for sampling points that are representative of the soil condition under different soil types, climatic conditions and land use. The grid of sampling points should be determined by using geostatistical methods and be sufficiently dense to provide an estimation of the area of healthy soils, at national level, within an uncertainty of not more than 5%. This value is commonly considered to provide a "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(31) The assessment of soil health based on the monitoring network should be accurate")
    thisalinea.textcontent.append("while at the same time keeping the costs of such monitoring at reasonable level. It is")
    thisalinea.textcontent.append("therefore appropriate to lay down criteria for sampling points that are representative of")
    thisalinea.textcontent.append("the soil condition under different soil types, climatic conditions and land use. The grid")
    thisalinea.textcontent.append("of sampling points should be determined by using geostatistical methods and be")
    thisalinea.textcontent.append("sufficiently dense to provide an estimation of the area of healthy soils, at national")
    thisalinea.textcontent.append("level, within an uncertainty of not more than 5%. This value is commonly considered")
    thisalinea.textcontent.append("to provide a statistically sound estimation and reasonable assurance that the objective")
    thisalinea.textcontent.append("has been achieved.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(32) The Commission should assist and support Member States’ monitoring of soil health ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 91
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 31
    thisalinea.summary = "(32) The Commission should assist and support Member States’ monitoring of soil health by continuing to carry out and enhancing regular in-situ soil sampling and related soil measurements (LUCAS soil) as part of the Land Use/Cover Area frame statistical Survey (LUCAS) Programme. For that purpose, the LUCAS Programme shall be enhanced and upgraded to fully align it with the specific quality requirements to be met for the purpose of this Directive. In order to alleviate the burden, Member States should be allowed to take into account the soil health data surveyed under the enhanced LUCAS soil. The Member States thus "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(32) The Commission should assist and support Member States’ monitoring of soil health")
    thisalinea.textcontent.append("by continuing to carry out and enhancing regular in-situ soil sampling and related soil")
    thisalinea.textcontent.append("measurements (LUCAS soil) as part of the Land Use/Cover Area frame statistical")
    thisalinea.textcontent.append("Survey (LUCAS) Programme. For that purpose, the LUCAS Programme shall be")
    thisalinea.textcontent.append("enhanced and upgraded to fully align it with the specific quality requirements to be")
    thisalinea.textcontent.append("met for the purpose of this Directive. In order to alleviate the burden, Member States")
    thisalinea.textcontent.append("should be allowed to take into account the soil health data surveyed under the")
    thisalinea.textcontent.append("enhanced LUCAS soil. The Member States thus supported should take the necessary")
    thisalinea.textcontent.append("legal arrangements to ensure that the Commission can carry out such in-situ soil")
    thisalinea.textcontent.append("sampling, including on privately owned fields, and in compliance with applicable")
    thisalinea.textcontent.append("national or Union legislation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(33) The Commission is developing remote sensing services in the context of Copernicus ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 92
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 32
    thisalinea.summary = "(33) The Commission is developing remote sensing services in the context of Copernicus as a user-driven programme, hereby also supporting Member States. In order to increase the timeliness and effectiveness of soil health monitoring, and where relevant, Member States should use remote sensing data including outputs from the Copernicus services for monitoring relevant soil descriptors and for assessing soil health. The Commission and the European Environment Agency should support exploring and developing soil remote sensing products, to assist the Member States in monitoring the relevant soil descriptors. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(33) The Commission is developing remote sensing services in the context of Copernicus")
    thisalinea.textcontent.append("as a user-driven programme, hereby also supporting Member States. In order to")
    thisalinea.textcontent.append("increase the timeliness and effectiveness of soil health monitoring, and where relevant,")
    thisalinea.textcontent.append("Member States should use remote sensing data including outputs from the Copernicus")
    thisalinea.textcontent.append("services for monitoring relevant soil descriptors and for assessing soil health. The")
    thisalinea.textcontent.append("Commission and the European Environment Agency should support exploring and")
    thisalinea.textcontent.append("developing soil remote sensing products, to assist the Member States in monitoring the")
    thisalinea.textcontent.append("relevant soil descriptors.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(34) Building on and upgrading the existing EU soil observatory, the Commission should ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 93
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 33
    thisalinea.summary = "(34) Building on and upgrading the existing EU soil observatory, the Commission should establish a digital soil health data portal that should be compatible with the EU Data Strategy50 and the EU data spaces and which should be a hub providing access to soil "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(34) Building on and upgrading the existing EU soil observatory, the Commission should")
    thisalinea.textcontent.append("establish a digital soil health data portal that should be compatible with the EU Data")
    thisalinea.textcontent.append("Strategy50 and the EU data spaces and which should be a hub providing access to soil")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(35) It is also necessary to improve the harmonization of soil monitoring systems used in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 94
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 34
    thisalinea.summary = "(35) It is also necessary to improve the harmonization of soil monitoring systems used in the Member States and exploit the synergies between Union and national monitoring systems in order to have more comparable data across the Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(35) It is also necessary to improve the harmonization of soil monitoring systems used in")
    thisalinea.textcontent.append("the Member States and exploit the synergies between Union and national monitoring")
    thisalinea.textcontent.append("systems in order to have more comparable data across the Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(36) In order to make the widest possible use of soil health data generated by ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 95
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 35
    thisalinea.summary = "(36) In order to make the widest possible use of soil health data generated by the monitoring carried out under this Directive, Member States should be required to facilitate the access to such data for relevant stakeholders such as farmers, foresters, land owners and local authorities. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(36) In order to make the widest possible use of soil health data generated by the")
    thisalinea.textcontent.append("monitoring carried out under this Directive, Member States should be required to")
    thisalinea.textcontent.append("facilitate the access to such data for relevant stakeholders such as farmers, foresters,")
    thisalinea.textcontent.append("land owners and local authorities.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(37) To maintain or enhance soil health, soils need to be managed sustainably. Sustainable ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 96
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 36
    thisalinea.summary = "(37) To maintain or enhance soil health, soils need to be managed sustainably. Sustainable soil management will enable the long-term provision of soil services, including improved air and water quality and food security. It is therefore appropriate to lay down sustainable soil management principles to guide soil management practices. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(37) To maintain or enhance soil health, soils need to be managed sustainably. Sustainable")
    thisalinea.textcontent.append("soil management will enable the long-term provision of soil services, including")
    thisalinea.textcontent.append("improved air and water quality and food security. It is therefore appropriate to lay")
    thisalinea.textcontent.append("down sustainable soil management principles to guide soil management practices.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(38) Economic instruments, including those under the Common Agricultural Policy (CAP) ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 97
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 37
    thisalinea.summary = "(38) Economic instruments, including those under the Common Agricultural Policy (CAP) that provide support to farmers, have a crucial role in the transition to the sustainable management of agricultural soils and, to a lesser extent, forest soils. The CAP aims to support soil health through the implementation of conditionality, eco-schemes and rural development measures. Financial support for farmers and foresters who apply sustainable soil management practices can also be generated by the private sector. Voluntary sustainability labels in the food, wood, bio-based, and energy industry, for example, established by private stakeholders, can take into account the sustainable soil management principles "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(38) Economic instruments, including those under the Common Agricultural Policy (CAP)")
    thisalinea.textcontent.append("that provide support to farmers, have a crucial role in the transition to the sustainable")
    thisalinea.textcontent.append("management of agricultural soils and, to a lesser extent, forest soils. The CAP aims to")
    thisalinea.textcontent.append("support soil health through the implementation of conditionality, eco-schemes and")
    thisalinea.textcontent.append("rural development measures. Financial support for farmers and foresters who apply")
    thisalinea.textcontent.append("sustainable soil management practices can also be generated by the private sector.")
    thisalinea.textcontent.append("Voluntary sustainability labels in the food, wood, bio-based, and energy industry, for")
    thisalinea.textcontent.append("example, established by private stakeholders, can take into account the sustainable soil")
    thisalinea.textcontent.append("management principles set out in this Directive. This can enable food, wood, and other")
    thisalinea.textcontent.append("biomass producers that follow those principles in their production to reflect these in")
    thisalinea.textcontent.append("the value of their products. Additional funding for a network of real-life sites for")
    thisalinea.textcontent.append("testing, demonstrating and upscaling of solutions, including on carbon farming, will be")
    thisalinea.textcontent.append("provided through the Soil Mission’s living labs and lighthouses. Without prejudice to")
    thisalinea.textcontent.append("the polluter pays principle, support and advice should be provided by Member States")
    thisalinea.textcontent.append("to help landowners and land users affected by action taken under this Directive taking")
    thisalinea.textcontent.append("into account, in particular, the needs and limited capacities of small and medium sized")
    thisalinea.textcontent.append("enterprises.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(39) Pursuant to Regulation (EU) 2021/2115 of the European Parliament and of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 98
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 38
    thisalinea.summary = "(39) Pursuant to Regulation (EU) 2021/2115 of the European Parliament and of the Council51, Member States have to describe in their CAP Strategic Plans how the environmental and climate architecture of those Plans is meant to contribute to the achievement of, and be consistent with, the long-term national targets set out in, or deriving from, the legislative acts listed in Annex XIII to that Regulation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(39) Pursuant to Regulation (EU) 2021/2115 of the European Parliament and of the")
    thisalinea.textcontent.append("Council51, Member States have to describe in their CAP Strategic Plans how the")
    thisalinea.textcontent.append("environmental and climate architecture of those Plans is meant to contribute to the")
    thisalinea.textcontent.append("achievement of, and be consistent with, the long-term national targets set out in, or")
    thisalinea.textcontent.append("deriving from, the legislative acts listed in Annex XIII to that Regulation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(40) In order to ensure that the best sustainable soil management practices are ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 99
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 39
    thisalinea.summary = "(40) In order to ensure that the best sustainable soil management practices are implemented, Member States should be required to closely monitor the impact of soil management practices and adjust practices and recommendations as necessary, taking into account new knowledge from research and innovation. Valuable contributions are expected in this respect from the Horizon Europe Mission ‘A Soil Deal for Europe’ and in particular its living labs and activities to support soil monitoring, soil education and citizen engagement. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(40) In order to ensure that the best sustainable soil management practices are")
    thisalinea.textcontent.append("implemented, Member States should be required to closely monitor the impact of soil")
    thisalinea.textcontent.append("management practices and adjust practices and recommendations as necessary, taking")
    thisalinea.textcontent.append("into account new knowledge from research and innovation. Valuable contributions are")
    thisalinea.textcontent.append("expected in this respect from the Horizon Europe Mission ‘A Soil Deal for Europe’")
    thisalinea.textcontent.append("and in particular its living labs and activities to support soil monitoring, soil education")
    thisalinea.textcontent.append("and citizen engagement.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(41) Regeneration brings degraded soils back to healthy condition. When defining soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 100
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 40
    thisalinea.summary = "(41) Regeneration brings degraded soils back to healthy condition. When defining soil regeneration measures, Member States should be required to take into account the outcome of the soil health assessment and to adapt those regeneration measures to the specific characteristics of the situation, the type, the use and the condition of the soil and the local, climatic and environmental conditions. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(41) Regeneration brings degraded soils back to healthy condition. When defining soil")
    thisalinea.textcontent.append("regeneration measures, Member States should be required to take into account the")
    thisalinea.textcontent.append("outcome of the soil health assessment and to adapt those regeneration measures to the")
    thisalinea.textcontent.append("specific characteristics of the situation, the type, the use and the condition of the soil")
    thisalinea.textcontent.append("and the local, climatic and environmental conditions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(42) To ensure synergies between the different measures adopted under other Union ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 101
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 41
    thisalinea.summary = "(42) To ensure synergies between the different measures adopted under other Union legislation that may have an impact on soil health, and the measures that are to be put in place to sustainably manage and regenerate soils in the Union, Member States should ensure that the sustainable soil management and regeneration practices are coherent with the national restoration plans adopted in accordance with Regulation (UE) …/… of the European Parliament and of the Council52+; the strategic plans to be drawn up by Member States under the Common Agricultural Policy in accordance with Regulation (EU) 2021/2115, the codes of good agricultural "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(42) To ensure synergies between the different measures adopted under other Union")
    thisalinea.textcontent.append("legislation that may have an impact on soil health, and the measures that are to be put")
    thisalinea.textcontent.append("in place to sustainably manage and regenerate soils in the Union, Member States")
    thisalinea.textcontent.append("should ensure that the sustainable soil management and regeneration practices are")
    thisalinea.textcontent.append("coherent with the national restoration plans adopted in accordance with Regulation")
    thisalinea.textcontent.append("(UE) …/… of the European Parliament and of the Council52+; the strategic plans to be")
    thisalinea.textcontent.append("drawn up by Member States under the Common Agricultural Policy in accordance")
    thisalinea.textcontent.append("with Regulation (EU) 2021/2115, the codes of good agricultural practices and the")
    thisalinea.textcontent.append("action programmes for designated vulnerable zones adopted in accordance with")
    thisalinea.textcontent.append("Council Directive 91/676/EEC53, the conservation measures and prioritized action")
    thisalinea.textcontent.append("framework established for Natura 2000 sites in accordance with Council Directive")
    thisalinea.textcontent.append("92/43/EEC54, the measures for achieving good ecological and chemical status of water")
    thisalinea.textcontent.append("bodies included in river basin management plans prepared in accordance with")
    thisalinea.textcontent.append("Directive 2000/60/EC of the European Parliament and of the Council55, the flood risk")
    thisalinea.textcontent.append("management measures established in accordance with Directive 2007/60/EC of the")
    thisalinea.textcontent.append("European Parliament and of the Council56, the drought management plans promoted in")
    thisalinea.textcontent.append("the Union Strategy on Adaptation to Climate Change57, the national action")
    thisalinea.textcontent.append("programmes established in accordance with Article 10 of the United Nations")
    thisalinea.textcontent.append("Convention to Combat Desertification, targets set out under Regulation (EU) 2018/841")
    thisalinea.textcontent.append("of the European Parliament and of the Council58 and Regulation (EU) 2018/842 of the")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(43) Contaminated sites are the legacy of decades of industrial activity in the EU and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 102
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 42
    thisalinea.summary = "(43) Contaminated sites are the legacy of decades of industrial activity in the EU and may lead to risks for human health and the environment now and in the future. It is therefore necessary first to identify and investigate potentially contaminated sites and then, in case of confirmed contamination, to assess the risks and take measures to address unacceptable risks. Soil investigation may prove that a potentially contaminated site is in fact not contaminated. In that case, the site should no longer be labelled by the Member State as potentially contaminated, unless contamination is suspected based on new evidence. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(43) Contaminated sites are the legacy of decades of industrial activity in the EU and may")
    thisalinea.textcontent.append("lead to risks for human health and the environment now and in the future. It is")
    thisalinea.textcontent.append("therefore necessary first to identify and investigate potentially contaminated sites and")
    thisalinea.textcontent.append("then, in case of confirmed contamination, to assess the risks and take measures to")
    thisalinea.textcontent.append("address unacceptable risks. Soil investigation may prove that a potentially")
    thisalinea.textcontent.append("contaminated site is in fact not contaminated. In that case, the site should no longer be")
    thisalinea.textcontent.append("labelled by the Member State as potentially contaminated, unless contamination is")
    thisalinea.textcontent.append("suspected based on new evidence.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(44) To identify potentially contaminated sites, Member States should collect evidence ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 103
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 43
    thisalinea.summary = "(44) To identify potentially contaminated sites, Member States should collect evidence among others through historical research, past industrial incidents and accidents, environmental permits and notifications by the public or authorities. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(44) To identify potentially contaminated sites, Member States should collect evidence")
    thisalinea.textcontent.append("among others through historical research, past industrial incidents and accidents,")
    thisalinea.textcontent.append("environmental permits and notifications by the public or authorities.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(45) In order to ensure that soil investigations on potentially contaminated sites are carried ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 104
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 44
    thisalinea.summary = "(45) In order to ensure that soil investigations on potentially contaminated sites are carried out timely and effectively, Member States should, in addition to the obligation to lay down the deadline by which those investigations should be carried out, be required to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(45) In order to ensure that soil investigations on potentially contaminated sites are carried")
    thisalinea.textcontent.append("out timely and effectively, Member States should, in addition to the obligation to lay")
    thisalinea.textcontent.append("down the deadline by which those investigations should be carried out, be required to")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(46) Flexibility for the management of potentially contaminated sites and contaminated ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 105
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 45
    thisalinea.summary = "(46) Flexibility for the management of potentially contaminated sites and contaminated sites is needed to take account of costs, benefits and local specificities. Member States should therefore at least adopt a risk-based approach for managing potentially contaminated sites and contaminated sites, taking into account the difference between these two categories, and which allows to allocate resources taking account of the specific environmental, economic and social context. Decisions should be taken based on the nature and extent of potential risks for human health and the environment resulting from exposure to soil contaminants (e.g. exposure of vulnerable populations such as pregnant women, "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(46) Flexibility for the management of potentially contaminated sites and contaminated")
    thisalinea.textcontent.append("sites is needed to take account of costs, benefits and local specificities. Member States")
    thisalinea.textcontent.append("should therefore at least adopt a risk-based approach for managing potentially")
    thisalinea.textcontent.append("contaminated sites and contaminated sites, taking into account the difference between")
    thisalinea.textcontent.append("these two categories, and which allows to allocate resources taking account of the")
    thisalinea.textcontent.append("specific environmental, economic and social context. Decisions should be taken based")
    thisalinea.textcontent.append("on the nature and extent of potential risks for human health and the environment")
    thisalinea.textcontent.append("resulting from exposure to soil contaminants (e.g. exposure of vulnerable populations")
    thisalinea.textcontent.append("such as pregnant women, persons with disabilities, elderly people and children). The")
    thisalinea.textcontent.append("cost-benefit analysis of undertaking remediation should be positive. The optimum")
    thisalinea.textcontent.append("remediation solution should be sustainable and selected through a balanced decision-")
    thisalinea.textcontent.append("making process that takes account of the environmental, economic and social impacts.")
    thisalinea.textcontent.append("The management of potentially contaminated sites and contaminated sites should")
    thisalinea.textcontent.append("respect the polluter-pays, precautionary and proportionality principles. Member States")
    thisalinea.textcontent.append("should lay down the specific methodology for determining the site-specific risks of")
    thisalinea.textcontent.append("contaminated sites. Member States should also define what constitutes an")
    thisalinea.textcontent.append("unacceptable risk from a contaminated site based on scientific knowledge, the")
    thisalinea.textcontent.append("precautionary principle, local specificities, and current and future land use. In order to")
    thisalinea.textcontent.append("reduce the risks of contaminated sites to an acceptable level for human health and the")
    thisalinea.textcontent.append("environment, Member States should take adequate risk reduction measures including")
    thisalinea.textcontent.append("remediation. It should be possible to qualify measures taken under other Union")
    thisalinea.textcontent.append("legislation as risk reduction measures under this Directive when those measures")
    thisalinea.textcontent.append("effectively reduce risks posed by contaminated sites.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(47) Measures taken pursuant to this Directive should also take account of other EU policy ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 106
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 46
    thisalinea.summary = "(47) Measures taken pursuant to this Directive should also take account of other EU policy objectives, such as the objectives pursued by [Regulation (EU) xxxx/xxxx66+] that aim at ensuring secure and sustainable supply of critical raw materials for Europe’s industry. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(47) Measures taken pursuant to this Directive should also take account of other EU policy")
    thisalinea.textcontent.append("objectives, such as the objectives pursued by [Regulation (EU) xxxx/xxxx66+] that aim")
    thisalinea.textcontent.append("at ensuring secure and sustainable supply of critical raw materials for Europe’s")
    thisalinea.textcontent.append("industry.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(48) Transparency is an essential component of soil policy and ensures public ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 107
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 47
    thisalinea.summary = "(48) Transparency is an essential component of soil policy and ensures public accountability and awareness, fair market conditions and the monitoring of progress. Therefore, Member States should set up and maintain a national register of contaminated sites and potentially contaminated sites which contains site-specific information that should be made publicly accessible in an online georeferenced spatial database. The register should contain the information that is necessary for the public to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(48) Transparency is an essential component of soil policy and ensures public")
    thisalinea.textcontent.append("accountability and awareness, fair market conditions and the monitoring of progress.")
    thisalinea.textcontent.append("Therefore, Member States should set up and maintain a national register of")
    thisalinea.textcontent.append("contaminated sites and potentially contaminated sites which contains site-specific")
    thisalinea.textcontent.append("information that should be made publicly accessible in an online georeferenced spatial")
    thisalinea.textcontent.append("database. The register should contain the information that is necessary for the public to")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(49) Article 19(1) of the Treaty on European Union (TEU) requires Member States to ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 108
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 48
    thisalinea.summary = "(49) Article 19(1) of the Treaty on European Union (TEU) requires Member States to provide remedies sufficient to ensure effective judicial protection in the fields covered by Union law. In addition, in accordance with the Convention on access to information, public participation in decision‐making and access to justice in environmental matters67 (Aarhus Convention), members of the public concerned should have access to justice in order to contribute to the protection of the right to live in an environment which is adequate for personal health and well-being. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(49) Article 19(1) of the Treaty on European Union (TEU) requires Member States to")
    thisalinea.textcontent.append("provide remedies sufficient to ensure effective judicial protection in the fields covered")
    thisalinea.textcontent.append("by Union law. In addition, in accordance with the Convention on access to")
    thisalinea.textcontent.append("information, public participation in decision‐making and access to justice in")
    thisalinea.textcontent.append("environmental matters67 (Aarhus Convention), members of the public concerned")
    thisalinea.textcontent.append("should have access to justice in order to contribute to the protection of the right to live")
    thisalinea.textcontent.append("in an environment which is adequate for personal health and well-being.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(50) Directive (EU) 2019/1024 of the European Parliament and of the Council68 mandates ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 109
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 49
    thisalinea.summary = "(50) Directive (EU) 2019/1024 of the European Parliament and of the Council68 mandates the release of public sector data in free and open formats. The overall objective is to continue the strengthening of the EU’s data economy by increasing the amount of public sector data available for re-use, ensuring fair competition and easy access to public sector information, and enhancing cross-border innovation based on data. The main principle is that government data should be open by default and design. Directive 2003/4/EC of the European Parliament and of the Council69 is aimed at guaranteeing the right of access to environmental information "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(50) Directive (EU) 2019/1024 of the European Parliament and of the Council68 mandates")
    thisalinea.textcontent.append("the release of public sector data in free and open formats. The overall objective is to")
    thisalinea.textcontent.append("continue the strengthening of the EU’s data economy by increasing the amount of")
    thisalinea.textcontent.append("public sector data available for re-use, ensuring fair competition and easy access to")
    thisalinea.textcontent.append("public sector information, and enhancing cross-border innovation based on data. The")
    thisalinea.textcontent.append("main principle is that government data should be open by default and design. Directive")
    thisalinea.textcontent.append("2003/4/EC of the European Parliament and of the Council69 is aimed at guaranteeing")
    thisalinea.textcontent.append("the right of access to environmental information in the Member States in line with the")
    thisalinea.textcontent.append("Aarhus Convention. The Aarhus Convention and Directive 2003/4/EC encompass")
    thisalinea.textcontent.append("broad obligations related both to making environmental information available upon")
    thisalinea.textcontent.append("request and actively disseminating such information. Directive 2007/2/EC of the")
    thisalinea.textcontent.append("European Parliament and of the Council70 is also of broad scope, covering the sharing")
    thisalinea.textcontent.append("of spatial information, including data sets on different environmental topics. It is")
    thisalinea.textcontent.append("important that provisions of this Directive related to access to information and data-")
    thisalinea.textcontent.append("sharing arrangements complement those Directives and do not create a separate legal")
    thisalinea.textcontent.append("regime. Therefore, the provisions of this Directive regarding information to the public")
    thisalinea.textcontent.append("and information on monitoring of implementation should be without prejudice to")
    thisalinea.textcontent.append("Directives (EU) 2019/1024, 2003/4/EC and 2007/2/EC.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(51) In order to ensure the necessary adaptation of the rules on soil health monitoring, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 110
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 50
    thisalinea.summary = "(51) In order to ensure the necessary adaptation of the rules on soil health monitoring, sustainable soil management and management of contaminated sites, the power to adopt acts in accordance with Article 290 of the Treaty on the Functioning of the European Union should be delegated to the Commission in respect of amending this Directive to adapt to technical and scientific progress the methodologies for monitoring soil health, the list of sustainable soil management principles, the indicative list of risk reduction measures, the phases and requirements for the site- specific risk assessment and the content of the register of contaminated "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(51) In order to ensure the necessary adaptation of the rules on soil health monitoring,")
    thisalinea.textcontent.append("sustainable soil management and management of contaminated sites, the power to")
    thisalinea.textcontent.append("adopt acts in accordance with Article 290 of the Treaty on the Functioning of the")
    thisalinea.textcontent.append("European Union should be delegated to the Commission in respect of amending this")
    thisalinea.textcontent.append("Directive to adapt to technical and scientific progress the methodologies for")
    thisalinea.textcontent.append("monitoring soil health, the list of sustainable soil management principles, the")
    thisalinea.textcontent.append("indicative list of risk reduction measures, the phases and requirements for the site-")
    thisalinea.textcontent.append("specific risk assessment and the content of the register of contaminated and potentially")
    thisalinea.textcontent.append("contaminated sites. It is of particular importance that the Commission carries out")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(52) In order to ensure uniform conditions for the implementation of this Directive, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 111
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 51
    thisalinea.summary = "(52) In order to ensure uniform conditions for the implementation of this Directive, implementing powers should be conferred on the Commission in order to set out the format, structure and detailed arrangements for reporting data and information electronically to the Commission. Those powers should be exercised in accordance with Regulation (EU) No 182/2011 of the European Parliament and the Council72. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(52) In order to ensure uniform conditions for the implementation of this Directive,")
    thisalinea.textcontent.append("implementing powers should be conferred on the Commission in order to set out the")
    thisalinea.textcontent.append("format, structure and detailed arrangements for reporting data and information")
    thisalinea.textcontent.append("electronically to the Commission. Those powers should be exercised in accordance")
    thisalinea.textcontent.append("with Regulation (EU) No 182/2011 of the European Parliament and the Council72.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(53) The Commission should carry out an evidence-based evaluation and, where relevant, a ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 112
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 52
    thisalinea.summary = "(53) The Commission should carry out an evidence-based evaluation and, where relevant, a revision of this Directive, 6 years after its entry into force on the basis of the results of the soil health assessment. The evaluation should assess in particular the need to set more specific requirements to make sure unhealthy soils are regenerated and the objective to achieve healthy soils by 2050 is achieved. The evaluation should also assess the need to adapt the definition of healthy soils to scientific and technical progress by adding provisions on certain descriptors or criteria based on new scientific evidence relating to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(53) The Commission should carry out an evidence-based evaluation and, where relevant, a")
    thisalinea.textcontent.append("revision of this Directive, 6 years after its entry into force on the basis of the results of")
    thisalinea.textcontent.append("the soil health assessment. The evaluation should assess in particular the need to set")
    thisalinea.textcontent.append("more specific requirements to make sure unhealthy soils are regenerated and the")
    thisalinea.textcontent.append("objective to achieve healthy soils by 2050 is achieved. The evaluation should also")
    thisalinea.textcontent.append("assess the need to adapt the definition of healthy soils to scientific and technical")
    thisalinea.textcontent.append("progress by adding provisions on certain descriptors or criteria based on new scientific")
    thisalinea.textcontent.append("evidence relating to the protection of soils or on the grounds of a problem specific to a")
    thisalinea.textcontent.append("Member State arising from new environmental or climatic circumstances. Pursuant to")
    thisalinea.textcontent.append("paragraph 22 of the Interinstitutional Agreement on Better Law-Making, that")
    thisalinea.textcontent.append("evaluation should be based on the criteria of efficiency, effectiveness, relevance,")
    thisalinea.textcontent.append("coherence and EU value added and should provide the basis for impact assessments of")
    thisalinea.textcontent.append("possible further measures.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(54) Coordinated measures by all Member States are necessary to achieve the vision to ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 113
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 53
    thisalinea.summary = "(54) Coordinated measures by all Member States are necessary to achieve the vision to have all soils healthy by 2050 and to secure the provision of ecosystem services by soils across the Union in the long-term. Individual actions of Member States have proven to be insufficient since the soil degradation is continuing and even deteriorating. Since the objectives of this Directive cannot be sufficiently achieved by the Member States but can rather, by reason of the scale and effects of the action, be better achieved at Union level, the Union may adopt measures, in accordance with the principle of subsidiarity "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(54) Coordinated measures by all Member States are necessary to achieve the vision to")
    thisalinea.textcontent.append("have all soils healthy by 2050 and to secure the provision of ecosystem services by")
    thisalinea.textcontent.append("soils across the Union in the long-term. Individual actions of Member States have")
    thisalinea.textcontent.append("proven to be insufficient since the soil degradation is continuing and even")
    thisalinea.textcontent.append("deteriorating. Since the objectives of this Directive cannot be sufficiently achieved by")
    thisalinea.textcontent.append("the Member States but can rather, by reason of the scale and effects of the action, be")
    thisalinea.textcontent.append("better achieved at Union level, the Union may adopt measures, in accordance with the")
    thisalinea.textcontent.append("principle of subsidiarity as set out in Article 5 TEU. In accordance with the principle")
    thisalinea.textcontent.append("of proportionality as set out in that Article, this Directive does not go beyond what is")
    thisalinea.textcontent.append("necessary in order to achieve those objectives.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(55) In accordance with the Joint Political Declaration of 28 September 2011 of Member ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 114
    thisalinea.parentID = 59
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 54
    thisalinea.summary = "(55) In accordance with the Joint Political Declaration of 28 September 2011 of Member States and the Commission on explanatory documents73, Member States have undertaken to accompany, in justified cases, the notification of their transposition measures with one or more documents explaining the relationship between the components of a directive and the corresponding parts of national transposition instruments. With regard to this Directive, the legislator considers the transmission of such documents to be justified. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(55) In accordance with the Joint Political Declaration of 28 September 2011 of Member")
    thisalinea.textcontent.append("States and the Commission on explanatory documents73, Member States have")
    thisalinea.textcontent.append("undertaken to accompany, in justified cases, the notification of their transposition")
    thisalinea.textcontent.append("measures with one or more documents explaining the relationship between the")
    thisalinea.textcontent.append("components of a directive and the corresponding parts of national transposition")
    thisalinea.textcontent.append("instruments. With regard to this Directive, the legislator considers the transmission of")
    thisalinea.textcontent.append("such documents to be justified.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter I General provisions"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 115
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
    thisalinea.texttitle = "Article 1 Objective and Subject matter"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 116
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "This Directive applies to all soils in the territory of Member States. 1. The objective of the Directive is to put in place a solid and coherent soil monitoring framework for all soils across the EU and to continuously improve soil health in the Union with the view to achieve healthy soils by 2050 and maintain soils in healthy condition, so that they can supply multiple ecosystem services at a scale sufficient to meet environmental, societal and economic needs, prevent and mitigate the impacts of climate change and biodiversity loss, increase the resilience against natural disasters and for food security "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Directive applies to all soils in the territory of Member States.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The objective of the Directive is to put in place a solid and coherent ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 117
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The objective of the Directive is to put in place a solid and coherent soil monitoring framework for all soils across the EU and to continuously improve soil health in the Union with the view to achieve healthy soils by 2050 and maintain soils in healthy condition, so that they can supply multiple ecosystem services at a scale sufficient to meet environmental, societal and economic needs, prevent and mitigate the impacts of climate change and biodiversity loss, increase the resilience against natural disasters and for food security and that soil contamination is reduced to levels no longer considered harmful "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The objective of the Directive is to put in place a solid and coherent soil monitoring")
    thisalinea.textcontent.append("framework for all soils across the EU and to continuously improve soil health in the")
    thisalinea.textcontent.append("Union with the view to achieve healthy soils by 2050 and maintain soils in healthy")
    thisalinea.textcontent.append("condition, so that they can supply multiple ecosystem services at a scale sufficient to")
    thisalinea.textcontent.append("meet environmental, societal and economic needs, prevent and mitigate the impacts")
    thisalinea.textcontent.append("of climate change and biodiversity loss, increase the resilience against natural")
    thisalinea.textcontent.append("disasters and for food security and that soil contamination is reduced to levels no")
    thisalinea.textcontent.append("longer considered harmful to human health and the environment.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. This Directive lays down measures on: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 118
    thisalinea.parentID = 116
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. This Directive lays down measures on: (a) monitoring and assessment of soil health; (b) sustainable soil management; (c) contaminated sites. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. This Directive lays down measures on:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) monitoring and assessment of soil health; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 119
    thisalinea.parentID = 118
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) monitoring and assessment of soil health; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) monitoring and assessment of soil health;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) sustainable soil management; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 120
    thisalinea.parentID = 118
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) sustainable soil management; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) sustainable soil management;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) contaminated sites. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 121
    thisalinea.parentID = 118
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) contaminated sites. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) contaminated sites.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 2 Scope"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 122
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 3 Definitions"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 123
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "For the purposes of this Directive, the following definitions shall apply: 31 32 (1) ‘soil’ means the top layer of the Earth’s crust situated between the bedrock and the land surface, which is composed of mineral particles, organic matter, water, air and living organisms; (2) ‘ecosystem’ means a dynamic complex of plant, animal, and micro-organism communities and their non-living environment interacting as a functional unit; (3) ‘ecosystem services’ means indirect contributions of ecosystems to the economic, social, cultural and other benefits that people derive from those ecosystems; (4) ‘soil health’ means the physical, chemical and biological condition of the soil "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("For the purposes of this Directive, the following definitions shall apply:")
    thisalinea.textcontent.append("31")
    thisalinea.textcontent.append("32")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(1) ‘soil’ means the top layer of the Earth’s crust situated between the bedrock and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 124
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(1) ‘soil’ means the top layer of the Earth’s crust situated between the bedrock and the land surface, which is composed of mineral particles, organic matter, water, air and living organisms; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(1) ‘soil’ means the top layer of the Earth’s crust situated between the bedrock and the")
    thisalinea.textcontent.append("land surface, which is composed of mineral particles, organic matter, water, air and")
    thisalinea.textcontent.append("living organisms;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(2) ‘ecosystem’ means a dynamic complex of plant, animal, and micro-organism ..."
    thisalinea.titlefontsize = "12.000000000000028"
    thisalinea.nativeID = 125
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(2) ‘ecosystem’ means a dynamic complex of plant, animal, and micro-organism communities and their non-living environment interacting as a functional unit; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(2) ‘ecosystem’ means a dynamic complex of plant, animal, and micro-organism")
    thisalinea.textcontent.append("communities and their non-living environment interacting as a functional unit;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(3) ‘ecosystem services’ means indirect contributions of ecosystems to the economic, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 126
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(3) ‘ecosystem services’ means indirect contributions of ecosystems to the economic, social, cultural and other benefits that people derive from those ecosystems; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(3) ‘ecosystem services’ means indirect contributions of ecosystems to the economic,")
    thisalinea.textcontent.append("social, cultural and other benefits that people derive from those ecosystems;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(4) ‘soil health’ means the physical, chemical and biological condition of the soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 127
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(4) ‘soil health’ means the physical, chemical and biological condition of the soil determining its capacity to function as a vital living system and to provide ecosystem services; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(4) ‘soil health’ means the physical, chemical and biological condition of the soil")
    thisalinea.textcontent.append("determining its capacity to function as a vital living system and to provide ecosystem")
    thisalinea.textcontent.append("services;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(5) ‘sustainable soil management’ means soil management practices that maintain or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 128
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(5) ‘sustainable soil management’ means soil management practices that maintain or enhance the ecosystem services provided by the soil without impairing the functions enabling those services, or being detrimental to other properties of the environment; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(5) ‘sustainable soil management’ means soil management practices that maintain or")
    thisalinea.textcontent.append("enhance the ecosystem services provided by the soil without impairing the functions")
    thisalinea.textcontent.append("enabling those services, or being detrimental to other properties of the environment;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(6) ‘soil management practices’ mean practices that impact the physical, chemical or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 129
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(6) ‘soil management practices’ mean practices that impact the physical, chemical or biological qualities of a soil; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(6) ‘soil management practices’ mean practices that impact the physical, chemical or")
    thisalinea.textcontent.append("biological qualities of a soil;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(7) ‘managed soils’ means soils where soil management practices are carried out; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 130
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(7) ‘managed soils’ means soils where soil management practices are carried out; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(7) ‘managed soils’ means soils where soil management practices are carried out;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(8) ‘soil district’ means the part of the territory of a Member State, as delimited ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 131
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "(8) ‘soil district’ means the part of the territory of a Member State, as delimited by that Member State in accordance with this Directive; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(8) ‘soil district’ means the part of the territory of a Member State, as delimited by that")
    thisalinea.textcontent.append("Member State in accordance with this Directive;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(9) ‘soil health assessment’ means the evaluation of the health of the soil based on ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 132
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 8
    thisalinea.summary = "(9) ‘soil health assessment’ means the evaluation of the health of the soil based on the measurement or estimation of soil descriptors; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(9) ‘soil health assessment’ means the evaluation of the health of the soil based on the")
    thisalinea.textcontent.append("measurement or estimation of soil descriptors;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(10) ‘contaminated site’ means a delineated area of one or several plots with confirmed ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 133
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "(10) ‘contaminated site’ means a delineated area of one or several plots with confirmed presence of soil contamination caused by point-source anthropogenic activities; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(10) ‘contaminated site’ means a delineated area of one or several plots with confirmed")
    thisalinea.textcontent.append("presence of soil contamination caused by point-source anthropogenic activities;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(11) ‘soil descriptor’ means a parameter describing a physical, chemical, or biological ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 134
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "(11) ‘soil descriptor’ means a parameter describing a physical, chemical, or biological characteristic of soil health; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(11) ‘soil descriptor’ means a parameter describing a physical, chemical, or biological")
    thisalinea.textcontent.append("characteristic of soil health;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(12) ‘land’ means the surface of the Earth that is not covered by water; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 135
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = "(12) ‘land’ means the surface of the Earth that is not covered by water; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(12) ‘land’ means the surface of the Earth that is not covered by water;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(13) ‘land cover’ means the physical and biological cover of the earth’s surface; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 136
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "(13) ‘land cover’ means the physical and biological cover of the earth’s surface; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(13) ‘land cover’ means the physical and biological cover of the earth’s surface;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(14) ‘natural land’ means an area where human activity has not substantially modified an ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 137
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "(14) ‘natural land’ means an area where human activity has not substantially modified an area’s primary ecological functions and species composition; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(14) ‘natural land’ means an area where human activity has not substantially modified an")
    thisalinea.textcontent.append("area’s primary ecological functions and species composition;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(15) ‘semi-natural land‘ means an area where ecological assemblages have been ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 138
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "(15) ‘semi-natural land‘ means an area where ecological assemblages have been substantially modified in their composition, balance or function by human activities, but maintain potentially high value in terms of biodiversity and the ecosystem services it provides; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(15) ‘semi-natural land‘ means an area where ecological assemblages have been")
    thisalinea.textcontent.append("substantially modified in their composition, balance or function by human activities,")
    thisalinea.textcontent.append("but maintain potentially high value in terms of biodiversity and the ecosystem")
    thisalinea.textcontent.append("services it provides;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(16) ‘artificial land’ means land used as a platform for constructions and infrastructure or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 139
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "(16) ‘artificial land’ means land used as a platform for constructions and infrastructure or as a direct source of raw material or as archive for historic patrimony at the expense of the capacity of soils to provide other ecosystem services; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(16) ‘artificial land’ means land used as a platform for constructions and infrastructure or")
    thisalinea.textcontent.append("as a direct source of raw material or as archive for historic patrimony at the expense")
    thisalinea.textcontent.append("of the capacity of soils to provide other ecosystem services;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(17) ‘land take’ means the conversion of natural and semi-natural land into artificial land; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 140
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = "(17) ‘land take’ means the conversion of natural and semi-natural land into artificial land; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(17) ‘land take’ means the conversion of natural and semi-natural land into artificial land;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(18) ‘transfer function’ means a mathematical rule that allows to convert the value of a ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 141
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "(18) ‘transfer function’ means a mathematical rule that allows to convert the value of a measurement, performed using a methodology different from a reference methodology, into the value that would be obtained by performing the soil measurement using the reference methodology; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(18) ‘transfer function’ means a mathematical rule that allows to convert the value of a")
    thisalinea.textcontent.append("measurement, performed using a methodology different from a reference")
    thisalinea.textcontent.append("methodology, into the value that would be obtained by performing the soil")
    thisalinea.textcontent.append("measurement using the reference methodology;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(19) ‘public concerned’ means the public affected or likely to be affected by soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 142
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "(19) ‘public concerned’ means the public affected or likely to be affected by soil degradation, or having an interest in the decision-making procedures related to the implementation of the obligations under this Directive, including land owners and land users, as well as non-governmental organisations promoting the protection of human health or the environment and meeting any requirements under national law. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(19) ‘public concerned’ means the public affected or likely to be affected by soil")
    thisalinea.textcontent.append("degradation, or having an interest in the decision-making procedures related to the")
    thisalinea.textcontent.append("implementation of the obligations under this Directive, including land owners and")
    thisalinea.textcontent.append("land users, as well as non-governmental organisations promoting the protection of")
    thisalinea.textcontent.append("human health or the environment and meeting any requirements under national law.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(20) ‘soil contamination’ means the presence of a chemical or substance in the soil in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 143
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = "(20) ‘soil contamination’ means the presence of a chemical or substance in the soil in a concentration that may be harmful to human health or the environment; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(20) ‘soil contamination’ means the presence of a chemical or substance in the soil in a")
    thisalinea.textcontent.append("concentration that may be harmful to human health or the environment;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(21) ‘contaminant’ means a substance liable to cause soil contamination; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 144
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "(21) ‘contaminant’ means a substance liable to cause soil contamination; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(21) ‘contaminant’ means a substance liable to cause soil contamination;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(22) ‘regeneration’ means an intentional activity aimed at reversing soil from degraded to ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 145
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "(22) ‘regeneration’ means an intentional activity aimed at reversing soil from degraded to healthy condition; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(22) ‘regeneration’ means an intentional activity aimed at reversing soil from degraded to")
    thisalinea.textcontent.append("healthy condition;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(23) ‘risk’ means the possibility of harmful effects to human health or the environment ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 146
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 22
    thisalinea.summary = "(23) ‘risk’ means the possibility of harmful effects to human health or the environment resulting from exposure to soil contamination; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(23) ‘risk’ means the possibility of harmful effects to human health or the environment")
    thisalinea.textcontent.append("resulting from exposure to soil contamination;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(24) ‘soil investigation’ means a process to assess the presence and concentration of ..."
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 147
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 23
    thisalinea.summary = "(24) ‘soil investigation’ means a process to assess the presence and concentration of contaminants in the soil which is usually performed in different stages; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(24) ‘soil investigation’ means a process to assess the presence and concentration of")
    thisalinea.textcontent.append("contaminants in the soil which is usually performed in different stages;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(25) ‘geographically explicit’ means information referenced and stored in a manner that ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 148
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 24
    thisalinea.summary = "(25) ‘geographically explicit’ means information referenced and stored in a manner that permits it to be mapped and localised with specific precision and accuracy. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(25) ‘geographically explicit’ means information referenced and stored in a manner that")
    thisalinea.textcontent.append("permits it to be mapped and localised with specific precision and accuracy.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(26) ‘soil remediation’ means a regeneration action that reduces, isolates or immobilizes ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 149
    thisalinea.parentID = 123
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 25
    thisalinea.summary = "(26) ‘soil remediation’ means a regeneration action that reduces, isolates or immobilizes contaminant concentrations in the soil. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(26) ‘soil remediation’ means a regeneration action that reduces, isolates or immobilizes")
    thisalinea.textcontent.append("contaminant concentrations in the soil.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 4 Soil districts"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 150
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 9
    thisalinea.summary = "The number of soil districts for each Member State shall as a minimum correspond to the number of NUTS 1 territorial units established under Regulation (EC) No 1059/2003. 1. Member States shall establish soil districts throughout their territory. 2. When establishing the geographic extent of soil districts, Member States may take into account existing administrative units and shall seek homogeneity within each soil district regarding the following parameters: (a) soil type as defined in the World Reference Base for Soil Resources74; (b) climatic conditions; (c) environmental zone as described in Alterra Report 228175; (d) land use or land cover as "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The number of soil districts for each Member State shall as a minimum correspond to")
    thisalinea.textcontent.append("the number of NUTS 1 territorial units established under Regulation (EC) No")
    thisalinea.textcontent.append("1059/2003.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall establish soil districts throughout their territory. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 151
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall establish soil districts throughout their territory. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall establish soil districts throughout their territory.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. When establishing the geographic extent of soil districts, Member States may take ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 152
    thisalinea.parentID = 150
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. When establishing the geographic extent of soil districts, Member States may take into account existing administrative units and shall seek homogeneity within each soil district regarding the following parameters: (a) soil type as defined in the World Reference Base for Soil Resources74; (b) climatic conditions; (c) environmental zone as described in Alterra Report 228175; (d) land use or land cover as used in the Land Use/Cover Area frame statistical Survey (LUCAS) programme. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. When establishing the geographic extent of soil districts, Member States may take")
    thisalinea.textcontent.append("into account existing administrative units and shall seek homogeneity within each")
    thisalinea.textcontent.append("soil district regarding the following parameters:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) soil type as defined in the World Reference Base for Soil Resources74; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 153
    thisalinea.parentID = 152
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) soil type as defined in the World Reference Base for Soil Resources74; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) soil type as defined in the World Reference Base for Soil Resources74;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) climatic conditions; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 154
    thisalinea.parentID = 152
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) climatic conditions; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) climatic conditions;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) environmental zone as described in Alterra Report 228175; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 155
    thisalinea.parentID = 152
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) environmental zone as described in Alterra Report 228175; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) environmental zone as described in Alterra Report 228175;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) land use or land cover as used in the Land Use/Cover Area frame statistical ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 156
    thisalinea.parentID = 152
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) land use or land cover as used in the Land Use/Cover Area frame statistical Survey (LUCAS) programme. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) land use or land cover as used in the Land Use/Cover Area frame statistical")
    thisalinea.textcontent.append("Survey (LUCAS) programme.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 5 Competent authorities"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 157
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 10
    thisalinea.summary = "Member States shall designate the competent authorities responsible at an appropriate level for carrying out the duties laid down in this Directive. Member States shall designate one competent authority for each soil district established in accordance with Article 4. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Member States shall designate the competent authorities responsible at an appropriate level")
    thisalinea.textcontent.append("for carrying out the duties laid down in this Directive.")
    thisalinea.textcontent.append("Member States shall designate one competent authority for each soil district established in")
    thisalinea.textcontent.append("accordance with Article 4.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter II Monitoring and assessment of soil health"
    thisalinea.titlefontsize = "15.95999999999998"
    thisalinea.nativeID = 158
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 11
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 6 Soil health and land take monitoring framework"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 159
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 12
    thisalinea.summary = "33 1. Member States shall establish a monitoring framework based on the soil districts established in accordance with Article 4(1), to ensure that regular and accurate monitoring of soil health is carried out in accordance with this Article and Annexes I and II. 2. Member States shall monitor soil health and land take in each soil district. 3. The monitoring framework shall be based on the following: (a) the soil descriptors and soil health criteria referred to in Article 7; (b) the soil sampling points to be determined in accordance with Article 8(2); (c) the soil measurement carried out by "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("33")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall establish a monitoring framework based on the soil districts ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 160
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall establish a monitoring framework based on the soil districts established in accordance with Article 4(1), to ensure that regular and accurate monitoring of soil health is carried out in accordance with this Article and Annexes I and II. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall establish a monitoring framework based on the soil districts")
    thisalinea.textcontent.append("established in accordance with Article 4(1), to ensure that regular and accurate")
    thisalinea.textcontent.append("monitoring of soil health is carried out in accordance with this Article and Annexes I")
    thisalinea.textcontent.append("and II.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall monitor soil health and land take in each soil district. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 161
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States shall monitor soil health and land take in each soil district. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall monitor soil health and land take in each soil district.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The monitoring framework shall be based on the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 162
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The monitoring framework shall be based on the following: (a) the soil descriptors and soil health criteria referred to in Article 7; (b) the soil sampling points to be determined in accordance with Article 8(2); (c) the soil measurement carried out by the Commission in accordance with paragraph 4 of this Article, if any; (d) the remote sensing data and products referred to in paragraph 5 of this Article, if any; (e) the land take and soil sealing indicators referred to in Article 7(1). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The monitoring framework shall be based on the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the soil descriptors and soil health criteria referred to in Article 7; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 163
    thisalinea.parentID = 162
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the soil descriptors and soil health criteria referred to in Article 7; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the soil descriptors and soil health criteria referred to in Article 7;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the soil sampling points to be determined in accordance with Article 8(2); "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 164
    thisalinea.parentID = 162
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the soil sampling points to be determined in accordance with Article 8(2); "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the soil sampling points to be determined in accordance with Article 8(2);")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the soil measurement carried out by the Commission in accordance with ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 165
    thisalinea.parentID = 162
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the soil measurement carried out by the Commission in accordance with paragraph 4 of this Article, if any; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the soil measurement carried out by the Commission in accordance with")
    thisalinea.textcontent.append("paragraph 4 of this Article, if any;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) the remote sensing data and products referred to in paragraph 5 of this Article, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 166
    thisalinea.parentID = 162
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) the remote sensing data and products referred to in paragraph 5 of this Article, if any; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) the remote sensing data and products referred to in paragraph 5 of this Article,")
    thisalinea.textcontent.append("if any;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(e) the land take and soil sealing indicators referred to in Article 7(1). "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 167
    thisalinea.parentID = 162
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(e) the land take and soil sealing indicators referred to in Article 7(1). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(e) the land take and soil sealing indicators referred to in Article 7(1).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. The Commission shall, subject to agreement from Member States concerned, carry ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 168
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. The Commission shall, subject to agreement from Member States concerned, carry out regular soil measurements on soil samples taken in-situ, based on the relevant descriptors and methodologies referred to in Articles 7 and 8, to support Member States’ monitoring of soil health. Where a Member State provides agreement in accordance with this paragraph, it shall ensure that the Commission can carry out such in-situ soil sampling. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. The Commission shall, subject to agreement from Member States concerned, carry")
    thisalinea.textcontent.append("out regular soil measurements on soil samples taken in-situ, based on the relevant")
    thisalinea.textcontent.append("descriptors and methodologies referred to in Articles 7 and 8, to support Member")
    thisalinea.textcontent.append("States’ monitoring of soil health. Where a Member State provides agreement in")
    thisalinea.textcontent.append("accordance with this paragraph, it shall ensure that the Commission can carry out")
    thisalinea.textcontent.append("such in-situ soil sampling.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. The Commission and the European Environment Agency (EEA) shall leverage ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 169
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. The Commission and the European Environment Agency (EEA) shall leverage existing space-based data and products delivered under the Copernicus component of the EU Space Programme established by Regulation (EU) 2021/696 to explore and develop soil remote sensing products, to support the Member States in monitoring the relevant soil descriptors. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. The Commission and the European Environment Agency (EEA) shall leverage")
    thisalinea.textcontent.append("existing space-based data and products delivered under the Copernicus component of")
    thisalinea.textcontent.append("the EU Space Programme established by Regulation (EU) 2021/696 to explore and")
    thisalinea.textcontent.append("develop soil remote sensing products, to support the Member States in monitoring")
    thisalinea.textcontent.append("the relevant soil descriptors.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. The Commission and the EEA shall, on the basis of existing data and within ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 170
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. The Commission and the EEA shall, on the basis of existing data and within two years of the entry into force of this Directive, establish a digital soil health data portal that shall provide access in georeferenced spatial format to at least the available soil health data resulting from: (a) the soil measurements referred to in Article 8(2); (b) the soil measurements referred to in paragraph 4 of this Article; (c) the relevant soil remote sensing data and products referred to in paragraph 5 of this Article. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. The Commission and the EEA shall, on the basis of existing data and within two")
    thisalinea.textcontent.append("years of the entry into force of this Directive, establish a digital soil health data portal")
    thisalinea.textcontent.append("that shall provide access in georeferenced spatial format to at least the available soil")
    thisalinea.textcontent.append("health data resulting from:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the soil measurements referred to in Article 8(2); "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 171
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the soil measurements referred to in Article 8(2); "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the soil measurements referred to in Article 8(2);")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the soil measurements referred to in paragraph 4 of this Article; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 172
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the soil measurements referred to in paragraph 4 of this Article; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the soil measurements referred to in paragraph 4 of this Article;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the relevant soil remote sensing data and products referred to in paragraph 5 of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 173
    thisalinea.parentID = 170
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the relevant soil remote sensing data and products referred to in paragraph 5 of this Article. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the relevant soil remote sensing data and products referred to in paragraph 5 of")
    thisalinea.textcontent.append("this Article.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "7. The digital soil health data portal referred to in paragraph 6 may also provide ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 174
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "7. The digital soil health data portal referred to in paragraph 6 may also provide access to other soil health related data than the data referred to in that paragraph if those data were shared or collected in accordance with the formats or methods established by the Commission pursuant to paragraph 8. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("7. The digital soil health data portal referred to in paragraph 6 may also provide access")
    thisalinea.textcontent.append("to other soil health related data than the data referred to in that paragraph if those")
    thisalinea.textcontent.append("data were shared or collected in accordance with the formats or methods established")
    thisalinea.textcontent.append("by the Commission pursuant to paragraph 8.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "8. The Commission shall adopt implementing acts to establish formats or methods for ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 175
    thisalinea.parentID = 159
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 7
    thisalinea.summary = "8. The Commission shall adopt implementing acts to establish formats or methods for sharing or collecting the data referred to in paragraph 7 or for integrating those data in the digital soil health data portal. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 21. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("8. The Commission shall adopt implementing acts to establish formats or methods for")
    thisalinea.textcontent.append("sharing or collecting the data referred to in paragraph 7 or for integrating those data")
    thisalinea.textcontent.append("in the digital soil health data portal. Those implementing acts shall be adopted in")
    thisalinea.textcontent.append("accordance with the examination procedure referred to in Article 21.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 7 Soil descriptors, criteria for healthy soil condition, and land take and soil sealing indicators"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 176
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 13
    thisalinea.summary = "34 When monitoring land take, Member States shall apply the land take and soil sealing indicators referred to in Annex I. 1. When monitoring and assessing soil health, Member States shall apply the soil descriptors and soil health criteria listed in Annex I. 2. Member States may adapt the soil descriptors and the soil health criteria referred to in part A of Annex I, in accordance with the specifications referred to in the second and third columns in part A of Annex I. 3. Member States shall determine the organic contaminants for the soil descriptor related to soil contamination referred "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("34")
    thisalinea.textcontent.append("When monitoring land take, Member States shall apply the land take and soil sealing")
    thisalinea.textcontent.append("indicators referred to in Annex I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. When monitoring and assessing soil health, Member States shall apply the soil ..."
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 177
    thisalinea.parentID = 176
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. When monitoring and assessing soil health, Member States shall apply the soil descriptors and soil health criteria listed in Annex I. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. When monitoring and assessing soil health, Member States shall apply the soil")
    thisalinea.textcontent.append("descriptors and soil health criteria listed in Annex I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States may adapt the soil descriptors and the soil health criteria referred to ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 178
    thisalinea.parentID = 176
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States may adapt the soil descriptors and the soil health criteria referred to in part A of Annex I, in accordance with the specifications referred to in the second and third columns in part A of Annex I. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States may adapt the soil descriptors and the soil health criteria referred to")
    thisalinea.textcontent.append("in part A of Annex I, in accordance with the specifications referred to in the second")
    thisalinea.textcontent.append("and third columns in part A of Annex I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall determine the organic contaminants for the soil descriptor ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 179
    thisalinea.parentID = 176
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall determine the organic contaminants for the soil descriptor related to soil contamination referred to in part B of Annex I. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall determine the organic contaminants for the soil descriptor")
    thisalinea.textcontent.append("related to soil contamination referred to in part B of Annex I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Member States shall set soil health criteria for the soil descriptors listed in part ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 180
    thisalinea.parentID = 176
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Member States shall set soil health criteria for the soil descriptors listed in part B of Annex I in accordance with the provisions set out in the third column in part B of Annex I. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Member States shall set soil health criteria for the soil descriptors listed in part B of")
    thisalinea.textcontent.append("Annex I in accordance with the provisions set out in the third column in part B of")
    thisalinea.textcontent.append("Annex I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. Member States may set additional soil descriptors and land take indicators, including ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 181
    thisalinea.parentID = 176
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. Member States may set additional soil descriptors and land take indicators, including but not limited to the optional descriptors and indicators listed in part C and D of Annex I, for monitoring purposes (‘additional soil descriptors’ and ‘additional land take indicators’). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. Member States may set additional soil descriptors and land take indicators, including")
    thisalinea.textcontent.append("but not limited to the optional descriptors and indicators listed in part C and D of")
    thisalinea.textcontent.append("Annex I, for monitoring purposes (‘additional soil descriptors’ and ‘additional land")
    thisalinea.textcontent.append("take indicators’).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. Member States shall inform the Commission when soil descriptors, land take ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 182
    thisalinea.parentID = 176
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. Member States shall inform the Commission when soil descriptors, land take indicators and soil health criteria are set or adapted in accordance with paragraphs 2 to 5 of this Article. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. Member States shall inform the Commission when soil descriptors, land take")
    thisalinea.textcontent.append("indicators and soil health criteria are set or adapted in accordance with paragraphs 2")
    thisalinea.textcontent.append("to 5 of this Article.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 8 Measurements and methodologies"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 183
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 14
    thisalinea.summary = "Member States may apply other methodologies than the ones listed in the first subparagraph, points (a) and (b), provided that validated transfer functions are available, as required in Annex II, part B, fourth column. 35 Member States shall ensure that the value of the land take and soil sealing indicators are updated at least every year. 1. Member States shall determine sampling points by applying the methodology set out in part A of Annex II. 2. Member States shall carry out soil measurements by taking soil samples at the sampling points referred to in paragraph 1 and collect, process and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Member States may apply other methodologies than the ones listed in the first")
    thisalinea.textcontent.append("subparagraph, points (a) and (b), provided that validated transfer functions are")
    thisalinea.textcontent.append("available, as required in Annex II, part B, fourth column.")
    thisalinea.textcontent.append("35")
    thisalinea.textcontent.append("Member States shall ensure that the value of the land take and soil sealing indicators")
    thisalinea.textcontent.append("are updated at least every year.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall determine sampling points by applying the methodology set out ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 184
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall determine sampling points by applying the methodology set out in part A of Annex II. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall determine sampling points by applying the methodology set out")
    thisalinea.textcontent.append("in part A of Annex II.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall carry out soil measurements by taking soil samples at the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 185
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States shall carry out soil measurements by taking soil samples at the sampling points referred to in paragraph 1 and collect, process and analyse data in order to determine the following: (a) the values of the soil descriptors as set in Annex I; (b) where relevant, the values of the additional soil descriptors; (c) the values of the land take and soil sealing indicators listed in part D of Annex "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall carry out soil measurements by taking soil samples at the")
    thisalinea.textcontent.append("sampling points referred to in paragraph 1 and collect, process and analyse data in")
    thisalinea.textcontent.append("order to determine the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the values of the soil descriptors as set in Annex I; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 186
    thisalinea.parentID = 185
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the values of the soil descriptors as set in Annex I; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the values of the soil descriptors as set in Annex I;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) where relevant, the values of the additional soil descriptors; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 187
    thisalinea.parentID = 185
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) where relevant, the values of the additional soil descriptors; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) where relevant, the values of the additional soil descriptors;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the values of the land take and soil sealing indicators listed in part D ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 188
    thisalinea.parentID = 185
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the values of the land take and soil sealing indicators listed in part D of Annex "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the values of the land take and soil sealing indicators listed in part D of Annex")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "I. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 189
    thisalinea.parentID = 188
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.BIGROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall apply the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 190
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall apply the following: (a) the methodologies for determining or estimating the values of the soil descriptors set out in part B of Annex II; (b) the minimum methodological criteria for determining the values of the land take and soil sealing indicators set out in part C of Annex II; (c) any requirements laid down by the Commission in accordance with paragraph 6. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall apply the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the methodologies for determining or estimating the values of the soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 191
    thisalinea.parentID = 190
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the methodologies for determining or estimating the values of the soil descriptors set out in part B of Annex II; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the methodologies for determining or estimating the values of the soil")
    thisalinea.textcontent.append("descriptors set out in part B of Annex II;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the minimum methodological criteria for determining the values of the land ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 192
    thisalinea.parentID = 190
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the minimum methodological criteria for determining the values of the land take and soil sealing indicators set out in part C of Annex II; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the minimum methodological criteria for determining the values of the land")
    thisalinea.textcontent.append("take and soil sealing indicators set out in part C of Annex II;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) any requirements laid down by the Commission in accordance with paragraph ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 193
    thisalinea.parentID = 190
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) any requirements laid down by the Commission in accordance with paragraph 6. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) any requirements laid down by the Commission in accordance with paragraph")
    thisalinea.textcontent.append("6.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Member States shall ensure that the first soil measurements are performed at the ..."
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 194
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Member States shall ensure that the first soil measurements are performed at the latest by… (OP: please insert the date = 4 years after date of entry into force of the Directive). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Member States shall ensure that the first soil measurements are performed at the")
    thisalinea.textcontent.append("latest by… (OP: please insert the date = 4 years after date of entry into force of the")
    thisalinea.textcontent.append("Directive).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. Member States shall ensure that new soil measurements are performed at least every ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 195
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. Member States shall ensure that new soil measurements are performed at least every 5 years. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. Member States shall ensure that new soil measurements are performed at least every")
    thisalinea.textcontent.append("5 years.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. The Commission is empowered to adopt delegated acts in accordance with Article 20 ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 196
    thisalinea.parentID = 183
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. The Commission is empowered to adopt delegated acts in accordance with Article 20 to amend Annex II in order to adapt the reference methodologies mentioned in it to scientific and technical progress, in particular where values of soil descriptors can be determined by remote sensing referred to in Article 6(5). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. The Commission is empowered to adopt delegated acts in accordance with Article 20")
    thisalinea.textcontent.append("to amend Annex II in order to adapt the reference methodologies mentioned in it to")
    thisalinea.textcontent.append("scientific and technical progress, in particular where values of soil descriptors can be")
    thisalinea.textcontent.append("determined by remote sensing referred to in Article 6(5).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 9 Assessment of the soil health"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 197
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 15
    thisalinea.summary = "Member States shall also take into account the data collected in the context of soil investigations referred to in Article 14. Member States shall ensure that soil health assessments are performed at least every 5 years and that the first soil health assessment is performed by … (OP: please insert the date = 5 years after date of entry into force of the Directive). By way of derogation from the first subparagraph the assessment of soils within a land area listed in the fourth column of Annex I, shall not take into account the values set out in the third "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Member States shall also take into account the data collected in the context of soil")
    thisalinea.textcontent.append("investigations referred to in Article 14.")
    thisalinea.textcontent.append("Member States shall ensure that soil health assessments are performed at least every")
    thisalinea.textcontent.append("5 years and that the first soil health assessment is performed by … (OP: please insert")
    thisalinea.textcontent.append("the date = 5 years after date of entry into force of the Directive).")
    thisalinea.textcontent.append("By way of derogation from the first subparagraph the assessment of soils within a")
    thisalinea.textcontent.append("land area listed in the fourth column of Annex I, shall not take into account the")
    thisalinea.textcontent.append("values set out in the third column for that land area.")
    thisalinea.textcontent.append("Soil is unhealthy where at least one of the criteria referred to in subparagraph 1 is not")
    thisalinea.textcontent.append("met (‘unhealthy soil’).")
    thisalinea.textcontent.append("Member States shall analyse the values of land take and soil sealing indicators listed")
    thisalinea.textcontent.append("in part D of Annex I and assess their impact on the loss of ecosystem services and on")
    thisalinea.textcontent.append("the objectives and targets established under Regulation (EU) 2018/841.")
    thisalinea.textcontent.append("36")
    thisalinea.textcontent.append("The Commission may adopt implementing acts to harmonise the format of soil health")
    thisalinea.textcontent.append("certification. Those implementing acts shall be adopted in accordance with the")
    thisalinea.textcontent.append("examination procedure referred to in Article 21.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall assess the soil health in all their soil districts based on ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 198
    thisalinea.parentID = 197
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall assess the soil health in all their soil districts based on the data collected in the context of the monitoring referred to in Articles 6, 7 and 8 for each of the soil descriptors referred to in Parts A and B of Annex I. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall assess the soil health in all their soil districts based on the data")
    thisalinea.textcontent.append("collected in the context of the monitoring referred to in Articles 6, 7 and 8 for each of")
    thisalinea.textcontent.append("the soil descriptors referred to in Parts A and B of Annex I.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. A soil is considered healthy in accordance with this Directive where the following ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 199
    thisalinea.parentID = 197
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. A soil is considered healthy in accordance with this Directive where the following cumulative conditions are fulfilled: (a) the values for all soil descriptors listed in part A of Annex I meet the criteria laid down therein and, where applicable, adapted in accordance with Article 7; (b) the values for all soil descriptors listed in part B of Annex I meet the criteria set in accordance with Article 7 (‘healthy soil’). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. A soil is considered healthy in accordance with this Directive where the following")
    thisalinea.textcontent.append("cumulative conditions are fulfilled:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the values for all soil descriptors listed in part A of Annex I meet ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 200
    thisalinea.parentID = 199
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the values for all soil descriptors listed in part A of Annex I meet the criteria laid down therein and, where applicable, adapted in accordance with Article 7; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the values for all soil descriptors listed in part A of Annex I meet the criteria")
    thisalinea.textcontent.append("laid down therein and, where applicable, adapted in accordance with Article 7;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the values for all soil descriptors listed in part B of Annex I meet ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 201
    thisalinea.parentID = 199
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the values for all soil descriptors listed in part B of Annex I meet the criteria set in accordance with Article 7 (‘healthy soil’). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the values for all soil descriptors listed in part B of Annex I meet the criteria set")
    thisalinea.textcontent.append("in accordance with Article 7 (‘healthy soil’).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall analyse the values for the soil descriptors listed in part C ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 202
    thisalinea.parentID = 197
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall analyse the values for the soil descriptors listed in part C of Annex I and assess whether there is a critical loss of ecosystem services, taking into account the relevant data and available scientific knowledge. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall analyse the values for the soil descriptors listed in part C of")
    thisalinea.textcontent.append("Annex I and assess whether there is a critical loss of ecosystem services, taking into")
    thisalinea.textcontent.append("account the relevant data and available scientific knowledge.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Based on the assessment of soil health carried out in accordance with this Article, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 203
    thisalinea.parentID = 197
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Based on the assessment of soil health carried out in accordance with this Article, the competent authority shall, where relevant in coordination with local, regional, national authorities, identify, in each soil district, the areas which present unhealthy soils and inform the public in accordance with Article 19. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Based on the assessment of soil health carried out in accordance with this Article, the")
    thisalinea.textcontent.append("competent authority shall, where relevant in coordination with local, regional,")
    thisalinea.textcontent.append("national authorities, identify, in each soil district, the areas which present unhealthy")
    thisalinea.textcontent.append("soils and inform the public in accordance with Article 19.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. Member States shall set up a mechanism for a voluntary soil health certification for ..."
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 204
    thisalinea.parentID = 197
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. Member States shall set up a mechanism for a voluntary soil health certification for land owners and managers pursuant to the conditions in paragraph 2 of this Article. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. Member States shall set up a mechanism for a voluntary soil health certification for")
    thisalinea.textcontent.append("land owners and managers pursuant to the conditions in paragraph 2 of this Article.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. Member States shall communicate soil health data and assessment referred to in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 205
    thisalinea.parentID = 197
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. Member States shall communicate soil health data and assessment referred to in Articles 6 to 9 to the relevant land owners and land managers upon their request, in particular to support the development of the advice referred to in Article 10(3). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. Member States shall communicate soil health data and assessment referred to in")
    thisalinea.textcontent.append("Articles 6 to 9 to the relevant land owners and land managers upon their request, in")
    thisalinea.textcontent.append("particular to support the development of the advice referred to in Article 10(3).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter III Sustainable soil management"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 206
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 16
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 10 Sustainable soil management"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 207
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 17
    thisalinea.summary = "Directive), Member States shall take at least the following measures, taking into account the type, use and condition of soil: When defining the practices and measures referred to in this paragraph, Member States shall take into account the programmes, plans, targets and measures listed in Annex IV as well as the latest existing scientific knowledge including results coming out of the Horizon Europe Mission a Soil Deal for Europe. Member States shall identify synergies with the programmes, plans and measures set out in Annex IV. The soil health monitoring data, the results of the soil health assessments, the analysis referred "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Directive), Member States shall take at least the following measures, taking into")
    thisalinea.textcontent.append("account the type, use and condition of soil:")
    thisalinea.textcontent.append("When defining the practices and measures referred to in this paragraph, Member")
    thisalinea.textcontent.append("States shall take into account the programmes, plans, targets and measures listed in")
    thisalinea.textcontent.append("Annex IV as well as the latest existing scientific knowledge including results coming")
    thisalinea.textcontent.append("out of the Horizon Europe Mission a Soil Deal for Europe.")
    thisalinea.textcontent.append("Member States shall identify synergies with the programmes, plans and measures set")
    thisalinea.textcontent.append("out in Annex IV. The soil health monitoring data, the results of the soil health")
    thisalinea.textcontent.append("assessments, the analysis referred to in Article 9 and the sustainable soil management")
    thisalinea.textcontent.append("measures shall inform the development of the programmes, plans and measures set")
    thisalinea.textcontent.append("out in Annex IV.")
    thisalinea.textcontent.append("Member States shall ensure that the process of elaboration of the practices referred to")
    thisalinea.textcontent.append("in the first subparagraph is open, inclusive and effective and that the public")
    thisalinea.textcontent.append("concerned, in particular landowners and managers, are involved and are given early")
    thisalinea.textcontent.append("and effective opportunities to participate in their elaboration.")
    thisalinea.textcontent.append("Member States shall also take the following measures:")
    thisalinea.textcontent.append("37")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) defining sustainable soil management practices respecting the sustainable soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 208
    thisalinea.parentID = 207
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) defining sustainable soil management practices respecting the sustainable soil management principles listed in Annex III to be gradually implemented on all managed soils and, on the basis of the outcome of the soil assessments carried out in accordance with Article 9, regeneration practices to be gradually implemented on the unhealthy soils in the Member States; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) defining sustainable soil management practices respecting the sustainable soil")
    thisalinea.textcontent.append("management principles listed in Annex III to be gradually implemented on all")
    thisalinea.textcontent.append("managed soils and, on the basis of the outcome of the soil assessments carried")
    thisalinea.textcontent.append("out in accordance with Article 9, regeneration practices to be gradually")
    thisalinea.textcontent.append("implemented on the unhealthy soils in the Member States;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) defining soil management practices and other practices affecting negatively the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 209
    thisalinea.parentID = 207
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) defining soil management practices and other practices affecting negatively the soil health to be avoided by soil managers. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) defining soil management practices and other practices affecting negatively the")
    thisalinea.textcontent.append("soil health to be avoided by soil managers.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall ensure easy access to impartial and independent advice on ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 210
    thisalinea.parentID = 207
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "2. Member States shall ensure easy access to impartial and independent advice on sustainable soil management, training activities and capacity building for soil managers, landowners and relevant authorities. (a) promoting awareness on the medium- and long-term multiple benefits of sustainable soil management and the need to manage soils in a sustainable manner; (b) promoting research and implementation of holistic soil management concepts; (c) making available a regularly updated mapping of available funding instruments and activities to support the implementation of sustainable soil management. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall ensure easy access to impartial and independent advice on")
    thisalinea.textcontent.append("sustainable soil management, training activities and capacity building for soil")
    thisalinea.textcontent.append("managers, landowners and relevant authorities.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) promoting awareness on the medium- and long-term multiple benefits of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 211
    thisalinea.parentID = 210
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) promoting awareness on the medium- and long-term multiple benefits of sustainable soil management and the need to manage soils in a sustainable manner; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) promoting awareness on the medium- and long-term multiple benefits of")
    thisalinea.textcontent.append("sustainable soil management and the need to manage soils in a sustainable")
    thisalinea.textcontent.append("manner;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) promoting research and implementation of holistic soil management concepts; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 212
    thisalinea.parentID = 210
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) promoting research and implementation of holistic soil management concepts; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) promoting research and implementation of holistic soil management concepts;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) making available a regularly updated mapping of available funding instruments ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 213
    thisalinea.parentID = 210
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) making available a regularly updated mapping of available funding instruments and activities to support the implementation of sustainable soil management. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) making available a regularly updated mapping of available funding instruments")
    thisalinea.textcontent.append("and activities to support the implementation of sustainable soil management.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall regularly assess the effectiveness of the measures taken in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 214
    thisalinea.parentID = 207
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "3. Member States shall regularly assess the effectiveness of the measures taken in accordance with this Article and, where relevant, review and revise those measures, taking into account the soil health monitoring and assessment referred to in Articles 6 to 9. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall regularly assess the effectiveness of the measures taken in")
    thisalinea.textcontent.append("accordance with this Article and, where relevant, review and revise those measures,")
    thisalinea.textcontent.append("taking into account the soil health monitoring and assessment referred to in Articles 6")
    thisalinea.textcontent.append("to 9.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. The Commission is empowered to adopt delegated acts in accordance with Article 20 ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 215
    thisalinea.parentID = 207
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "4. The Commission is empowered to adopt delegated acts in accordance with Article 20 to amend Annex III in order to adapt the sustainable soil management principles to take into account scientific and technical progress. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. The Commission is empowered to adopt delegated acts in accordance with Article 20")
    thisalinea.textcontent.append("to amend Annex III in order to adapt the sustainable soil management principles to")
    thisalinea.textcontent.append("take into account scientific and technical progress.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 11 Land take mitigation principles"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 216
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 18
    thisalinea.summary = "Member States shall ensure that the following principles are respected in case of land take: (a) avoid or reduce as much as technically and economically possible the loss of the capacity of the soil to provide multiple ecosystem services, including food production, by: (i) reducing the area affected by the land take to the extent possible and (ii) selecting areas where the loss of ecosystem services would be minimized and (iii) performing the land take in a way that minimizes the negative impact on soil; (b) compensate as much as possible the loss of soil capacity to provide multiple ecosystem "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Member States shall ensure that the following principles are respected in case of land take:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(a) avoid or reduce as much as technically and economically possible the loss of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 217
    thisalinea.parentID = 216
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) avoid or reduce as much as technically and economically possible the loss of the capacity of the soil to provide multiple ecosystem services, including food production, by: (i) reducing the area affected by the land take to the extent possible and (ii) selecting areas where the loss of ecosystem services would be minimized and (iii) performing the land take in a way that minimizes the negative impact on soil; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) avoid or reduce as much as technically and economically possible the loss of the")
    thisalinea.textcontent.append("capacity of the soil to provide multiple ecosystem services, including food")
    thisalinea.textcontent.append("production, by:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(i) reducing the area affected by the land take to the extent possible and "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 218
    thisalinea.parentID = 217
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) reducing the area affected by the land take to the extent possible and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) reducing the area affected by the land take to the extent possible and")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(ii) selecting areas where the loss of ecosystem services would be minimized ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 219
    thisalinea.parentID = 217
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) selecting areas where the loss of ecosystem services would be minimized and "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) selecting areas where the loss of ecosystem services would be minimized")
    thisalinea.textcontent.append("and")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(iii) performing the land take in a way that minimizes the negative impact on ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 220
    thisalinea.parentID = 217
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(iii) performing the land take in a way that minimizes the negative impact on soil; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iii) performing the land take in a way that minimizes the negative impact on")
    thisalinea.textcontent.append("soil;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "(b) compensate as much as possible the loss of soil capacity to provide multiple ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 221
    thisalinea.parentID = 216
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) compensate as much as possible the loss of soil capacity to provide multiple ecosystem services. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) compensate as much as possible the loss of soil capacity to provide multiple")
    thisalinea.textcontent.append("ecosystem services.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter IV Contaminated sites"
    thisalinea.titlefontsize = "15.95999999999998"
    thisalinea.nativeID = 222
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 19
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 12 Risk-based approach"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 223
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 20
    thisalinea.summary = "38 1. Member States shall manage the risks for human health and the environment of potentially contaminated sites and contaminated sites, and keep them to acceptable levels, taking account of the environmental, social and economic impacts of the soil contamination and of the risk reduction measures taken pursuant to Article 15 paragraph 4. 2. By … (OP: please insert the date =4 years after the date of entry into force of the Directive) Member States shall establish a risk-based approach for the following: (a) the identification of potentially contaminated sites in accordance with Article 13; (b) the investigation of potentially "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("38")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall manage the risks for human health and the environment of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 224
    thisalinea.parentID = 223
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall manage the risks for human health and the environment of potentially contaminated sites and contaminated sites, and keep them to acceptable levels, taking account of the environmental, social and economic impacts of the soil contamination and of the risk reduction measures taken pursuant to Article 15 paragraph 4. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall manage the risks for human health and the environment of")
    thisalinea.textcontent.append("potentially contaminated sites and contaminated sites, and keep them to acceptable")
    thisalinea.textcontent.append("levels, taking account of the environmental, social and economic impacts of the soil")
    thisalinea.textcontent.append("contamination and of the risk reduction measures taken pursuant to Article 15")
    thisalinea.textcontent.append("paragraph 4.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. By … (OP: please insert the date =4 years after the date of entry ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 225
    thisalinea.parentID = 223
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. By … (OP: please insert the date =4 years after the date of entry into force of the Directive) Member States shall establish a risk-based approach for the following: (a) the identification of potentially contaminated sites in accordance with Article 13; (b) the investigation of potentially contaminated sites in accordance with Article 14; (c) the management of contaminated sites in accordance with Article 15. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. By … (OP: please insert the date =4 years after the date of entry into force of the")
    thisalinea.textcontent.append("Directive) Member States shall establish a risk-based approach for the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the identification of potentially contaminated sites in accordance with Article ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 226
    thisalinea.parentID = 225
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the identification of potentially contaminated sites in accordance with Article 13; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the identification of potentially contaminated sites in accordance with Article")
    thisalinea.textcontent.append("13;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the investigation of potentially contaminated sites in accordance with Article ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 227
    thisalinea.parentID = 225
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the investigation of potentially contaminated sites in accordance with Article 14; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the investigation of potentially contaminated sites in accordance with Article")
    thisalinea.textcontent.append("14;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the management of contaminated sites in accordance with Article 15. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 228
    thisalinea.parentID = 225
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the management of contaminated sites in accordance with Article 15. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the management of contaminated sites in accordance with Article 15.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The requirement laid down in paragraph 2 is without prejudice to more stringent ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 229
    thisalinea.parentID = 223
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The requirement laid down in paragraph 2 is without prejudice to more stringent requirements arising from Union or national legislation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The requirement laid down in paragraph 2 is without prejudice to more stringent")
    thisalinea.textcontent.append("requirements arising from Union or national legislation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. The public concerned shall be given early and effective opportunities: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 230
    thisalinea.parentID = 223
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. The public concerned shall be given early and effective opportunities: (a) to participate in the establishment and concrete application of the risk-based approach as defined in this Article; (b) to provide information relevant for the identification of potentially contaminated sites in accordance with Article 13, the investigation of potentially contaminated sites in accordance with Article 14 and the management of contaminated sites in accordance with Article 15; (c) to request correction of information contained in the register for contaminated sites and potentially contaminated sites in accordance with Article 16. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. The public concerned shall be given early and effective opportunities:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) to participate in the establishment and concrete application of the risk-based ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 231
    thisalinea.parentID = 230
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) to participate in the establishment and concrete application of the risk-based approach as defined in this Article; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) to participate in the establishment and concrete application of the risk-based")
    thisalinea.textcontent.append("approach as defined in this Article;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) to provide information relevant for the identification of potentially ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 232
    thisalinea.parentID = 230
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) to provide information relevant for the identification of potentially contaminated sites in accordance with Article 13, the investigation of potentially contaminated sites in accordance with Article 14 and the management of contaminated sites in accordance with Article 15; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) to provide information relevant for the identification of potentially")
    thisalinea.textcontent.append("contaminated sites in accordance with Article 13, the investigation of")
    thisalinea.textcontent.append("potentially contaminated sites in accordance with Article 14 and the")
    thisalinea.textcontent.append("management of contaminated sites in accordance with Article 15;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) to request correction of information contained in the register for contaminated ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 233
    thisalinea.parentID = 230
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) to request correction of information contained in the register for contaminated sites and potentially contaminated sites in accordance with Article 16. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) to request correction of information contained in the register for contaminated")
    thisalinea.textcontent.append("sites and potentially contaminated sites in accordance with Article 16.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 13 Identification of potentially contaminated sites"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 234
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 21
    thisalinea.summary = "For the purpose of the first subparagraph point (a), Member States shall lay down a list of potentially contaminating risk activities. Those activities may be further classified according to their risk to cause soil contamination based on scientific evidence. 39 1. Member States shall systematically and actively identify all sites where a soil contamination is suspected based on evidence collected through all available means (‘potentially contaminated sites’). 2. When identifying the potentially contaminated sites Member States shall take into account the following criteria: (a) operation of an active or inactive potentially contaminating risk activity; (b) operation of an activity referred "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("For the purpose of the first subparagraph point (a), Member States shall lay down a")
    thisalinea.textcontent.append("list of potentially contaminating risk activities. Those activities may be further")
    thisalinea.textcontent.append("classified according to their risk to cause soil contamination based on scientific")
    thisalinea.textcontent.append("evidence.")
    thisalinea.textcontent.append("39")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall systematically and actively identify all sites where a soil ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 235
    thisalinea.parentID = 234
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall systematically and actively identify all sites where a soil contamination is suspected based on evidence collected through all available means (‘potentially contaminated sites’). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall systematically and actively identify all sites where a soil")
    thisalinea.textcontent.append("contamination is suspected based on evidence collected through all available means")
    thisalinea.textcontent.append("(‘potentially contaminated sites’).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. When identifying the potentially contaminated sites Member States shall take into ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 236
    thisalinea.parentID = 234
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. When identifying the potentially contaminated sites Member States shall take into account the following criteria: (a) operation of an active or inactive potentially contaminating risk activity; (b) operation of an activity referred to in Annex I to Directive 2010/75/EU; (c) operation of an establishment referred to in Directive 2012/18/EU of the European Parliament and of the Council76; (d) operation of an activity referred to in Annex III to Directive 2004/35/CE of the European Parliament and of the Council77; (e) occurrence of a potentially contaminating accident, calamity, disaster, incident or spill; (f) any other event liable to cause soil contamination; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. When identifying the potentially contaminated sites Member States shall take into")
    thisalinea.textcontent.append("account the following criteria:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) operation of an active or inactive potentially contaminating risk activity; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 237
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) operation of an active or inactive potentially contaminating risk activity; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) operation of an active or inactive potentially contaminating risk activity;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) operation of an activity referred to in Annex I to Directive 2010/75/EU; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 238
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) operation of an activity referred to in Annex I to Directive 2010/75/EU; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) operation of an activity referred to in Annex I to Directive 2010/75/EU;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) operation of an establishment referred to in Directive 2012/18/EU of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 239
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) operation of an establishment referred to in Directive 2012/18/EU of the European Parliament and of the Council76; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) operation of an establishment referred to in Directive 2012/18/EU of the")
    thisalinea.textcontent.append("European Parliament and of the Council76;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) operation of an activity referred to in Annex III to Directive 2004/35/CE of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 240
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) operation of an activity referred to in Annex III to Directive 2004/35/CE of the European Parliament and of the Council77; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) operation of an activity referred to in Annex III to Directive 2004/35/CE of the")
    thisalinea.textcontent.append("European Parliament and of the Council77;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(e) occurrence of a potentially contaminating accident, calamity, disaster, incident ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 241
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(e) occurrence of a potentially contaminating accident, calamity, disaster, incident or spill; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(e) occurrence of a potentially contaminating accident, calamity, disaster, incident")
    thisalinea.textcontent.append("or spill;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(f) any other event liable to cause soil contamination; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 242
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "(f) any other event liable to cause soil contamination; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(f) any other event liable to cause soil contamination;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(g) any information resulting from the soil health monitoring carried out in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 243
    thisalinea.parentID = 236
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "(g) any information resulting from the soil health monitoring carried out in accordance with Articles 6, 7 and 8. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(g) any information resulting from the soil health monitoring carried out in")
    thisalinea.textcontent.append("accordance with Articles 6, 7 and 8.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall ensure that all potentially contaminated sites are identified by ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 244
    thisalinea.parentID = 234
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall ensure that all potentially contaminated sites are identified by (OP: please insert date = 7 years after date of entry into force of the Directive) and are duly recorded in the register referred to in Article 16 by that date. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall ensure that all potentially contaminated sites are identified by")
    thisalinea.textcontent.append("(OP: please insert date = 7 years after date of entry into force of the Directive) and")
    thisalinea.textcontent.append("are duly recorded in the register referred to in Article 16 by that date.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 14 Investigation of potentially contaminated sites"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 245
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 22
    thisalinea.summary = "Member States may consider baseline reports and monitoring measures implemented in accordance with the Directive 2010/75/EU as soil investigation where appropriate. 1. Member States shall ensure that all potentially contaminated sites identified in accordance with Article 13 are subject to soil investigation. 2. Member States shall lay down the rules concerning the deadline, content, form and the prioritisation of the soil investigations. Those rules shall be established in accordance with the risk-based approach referred to in Article 12 and the list of potentially contaminating risk activities referred to in Article 13(2), second subparagraph. 3. Member States shall also establish specific "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Member States may consider baseline reports and monitoring measures implemented")
    thisalinea.textcontent.append("in accordance with the Directive 2010/75/EU as soil investigation where appropriate.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall ensure that all potentially contaminated sites identified in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 246
    thisalinea.parentID = 245
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall ensure that all potentially contaminated sites identified in accordance with Article 13 are subject to soil investigation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall ensure that all potentially contaminated sites identified in")
    thisalinea.textcontent.append("accordance with Article 13 are subject to soil investigation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall lay down the rules concerning the deadline, content, form and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 247
    thisalinea.parentID = 245
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States shall lay down the rules concerning the deadline, content, form and the prioritisation of the soil investigations. Those rules shall be established in accordance with the risk-based approach referred to in Article 12 and the list of potentially contaminating risk activities referred to in Article 13(2), second subparagraph. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall lay down the rules concerning the deadline, content, form and")
    thisalinea.textcontent.append("the prioritisation of the soil investigations. Those rules shall be established in")
    thisalinea.textcontent.append("accordance with the risk-based approach referred to in Article 12 and the list of")
    thisalinea.textcontent.append("potentially contaminating risk activities referred to in Article 13(2), second")
    thisalinea.textcontent.append("subparagraph.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall also establish specific events that trigger an investigation before ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 248
    thisalinea.parentID = 245
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall also establish specific events that trigger an investigation before the deadline set in accordance with paragraph 2. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall also establish specific events that trigger an investigation before")
    thisalinea.textcontent.append("the deadline set in accordance with paragraph 2.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 15 Risk assessment and management of contaminated sites"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 249
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 23
    thisalinea.summary = "40 1. Member States shall lay down the specific methodology for determining the site- specific risks of contaminated sites. Such methodology shall be based on the phases and requirements for site-specific risk assessment listed in Annex VI. 2. Member States shall define what constitutes an unacceptable risk for human health and the environment resulting from contaminated sites by taking into account existing scientific knowledge, the precautionary principle, local specificities, and current and future land use. 3. For each contaminated site identified pursuant to Article 14 or by any other means, the responsible competent authority shall carry out a site-specific assessment "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("40")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall lay down the specific methodology for determining the site- ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 250
    thisalinea.parentID = 249
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall lay down the specific methodology for determining the site- specific risks of contaminated sites. Such methodology shall be based on the phases and requirements for site-specific risk assessment listed in Annex VI. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall lay down the specific methodology for determining the site-")
    thisalinea.textcontent.append("specific risks of contaminated sites. Such methodology shall be based on the phases")
    thisalinea.textcontent.append("and requirements for site-specific risk assessment listed in Annex VI.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall define what constitutes an unacceptable risk for human health ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 251
    thisalinea.parentID = 249
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States shall define what constitutes an unacceptable risk for human health and the environment resulting from contaminated sites by taking into account existing scientific knowledge, the precautionary principle, local specificities, and current and future land use. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall define what constitutes an unacceptable risk for human health")
    thisalinea.textcontent.append("and the environment resulting from contaminated sites by taking into account")
    thisalinea.textcontent.append("existing scientific knowledge, the precautionary principle, local specificities, and")
    thisalinea.textcontent.append("current and future land use.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. For each contaminated site identified pursuant to Article 14 or by any other means, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 252
    thisalinea.parentID = 249
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. For each contaminated site identified pursuant to Article 14 or by any other means, the responsible competent authority shall carry out a site-specific assessment for the current and planned land uses to determine whether the contaminated site poses unacceptable risks for human health or the environment. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. For each contaminated site identified pursuant to Article 14 or by any other means,")
    thisalinea.textcontent.append("the responsible competent authority shall carry out a site-specific assessment for the")
    thisalinea.textcontent.append("current and planned land uses to determine whether the contaminated site poses")
    thisalinea.textcontent.append("unacceptable risks for human health or the environment.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. On the basis of the outcome of the assessment referred to in paragraph 3, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 253
    thisalinea.parentID = 249
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. On the basis of the outcome of the assessment referred to in paragraph 3, the responsible competent authority shall take the appropriate measures to bring the risks to an acceptable level for human health and the environment (‘risk reduction measures’). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. On the basis of the outcome of the assessment referred to in paragraph 3, the")
    thisalinea.textcontent.append("responsible competent authority shall take the appropriate measures to bring the risks")
    thisalinea.textcontent.append("to an acceptable level for human health and the environment (‘risk reduction")
    thisalinea.textcontent.append("measures’).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. The risk reduction measures may consist of the measures referred to in Annex V. ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 254
    thisalinea.parentID = 249
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. The risk reduction measures may consist of the measures referred to in Annex V. When deciding on the appropriate risk reduction measures, the competent authority shall take into consideration the costs, benefits, effectiveness, durability, and technical feasibility of available risk reduction measures. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. The risk reduction measures may consist of the measures referred to in Annex V.")
    thisalinea.textcontent.append("When deciding on the appropriate risk reduction measures, the competent authority")
    thisalinea.textcontent.append("shall take into consideration the costs, benefits, effectiveness, durability, and")
    thisalinea.textcontent.append("technical feasibility of available risk reduction measures.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. The Commission is empowered to adopt delegated acts in accordance with Article 20 ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 255
    thisalinea.parentID = 249
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. The Commission is empowered to adopt delegated acts in accordance with Article 20 to amend Annexes V and VI to adapt the list of risk reduction measures and the requirements for site-specific risk assessment to scientific and technical progress. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. The Commission is empowered to adopt delegated acts in accordance with Article 20")
    thisalinea.textcontent.append("to amend Annexes V and VI to adapt the list of risk reduction measures and the")
    thisalinea.textcontent.append("requirements for site-specific risk assessment to scientific and technical progress.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 16 Register"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 256
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 24
    thisalinea.summary = "The register shall be made available in an online georeferenced spatial database. 1. By … (OP : please insert date = 4 years after entry into force of the Directive), Member States shall, in accordance with paragraph 2, draw up a register of contaminated sites and potentially contaminated sites. 2. The register shall contain the information set out in Annex VII. 3. The register shall be managed by the responsible competent authority and shall be regularly kept under review and up to date. 4. Member States shall make public the register and information referred to in paragraphs 1 and 2. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The register shall be made available in an online georeferenced spatial database.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. By … (OP : please insert date = 4 years after entry into force ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 257
    thisalinea.parentID = 256
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. By … (OP : please insert date = 4 years after entry into force of the Directive), Member States shall, in accordance with paragraph 2, draw up a register of contaminated sites and potentially contaminated sites. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. By … (OP : please insert date = 4 years after entry into force of the Directive),")
    thisalinea.textcontent.append("Member States shall, in accordance with paragraph 2, draw up a register of")
    thisalinea.textcontent.append("contaminated sites and potentially contaminated sites.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The register shall contain the information set out in Annex VII. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 258
    thisalinea.parentID = 256
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The register shall contain the information set out in Annex VII. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The register shall contain the information set out in Annex VII.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The register shall be managed by the responsible competent authority and shall be ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 259
    thisalinea.parentID = 256
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The register shall be managed by the responsible competent authority and shall be regularly kept under review and up to date. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The register shall be managed by the responsible competent authority and shall be")
    thisalinea.textcontent.append("regularly kept under review and up to date.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Member States shall make public the register and information referred to in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 260
    thisalinea.parentID = 256
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Member States shall make public the register and information referred to in paragraphs 1 and 2. Disclosure of any information may be refused or restricted by the competent authority where the conditions laid down in Article 4 of Directive 2003/4/EC of the European Parliament and of the Council78 are fulfilled. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Member States shall make public the register and information referred to in")
    thisalinea.textcontent.append("paragraphs 1 and 2. Disclosure of any information may be refused or restricted by the")
    thisalinea.textcontent.append("competent authority where the conditions laid down in Article 4 of Directive")
    thisalinea.textcontent.append("2003/4/EC of the European Parliament and of the Council78 are fulfilled.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. The Commission shall adopt implementing acts establishing the format of the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 261
    thisalinea.parentID = 256
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. The Commission shall adopt implementing acts establishing the format of the register. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 21. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. The Commission shall adopt implementing acts establishing the format of the")
    thisalinea.textcontent.append("register. Those implementing acts shall be adopted in accordance with the")
    thisalinea.textcontent.append("examination procedure referred to in Article 21.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter V Financing, information to the public and reporting by Member States"
    thisalinea.titlefontsize = "15.95999999999998"
    thisalinea.nativeID = 262
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 25
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 17 Union financing"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 263
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 26
    thisalinea.summary = "Given the priority inherently attached to the establishment of soil monitoring and sustainable management and regeneration of soils, the implementation of this Directive shall be supported by existing Union financial programmes in accordance with their applicable rules and conditions. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Given the priority inherently attached to the establishment of soil monitoring and sustainable")
    thisalinea.textcontent.append("management and regeneration of soils, the implementation of this Directive shall be supported")
    thisalinea.textcontent.append("by existing Union financial programmes in accordance with their applicable rules and")
    thisalinea.textcontent.append("conditions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 18 Reporting by Member States"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 264
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 27
    thisalinea.summary = "41 The first reports shall be submitted by … (OP: please insert date = 5 years and 6 months after entry into force of the Directive). 1. Member States shall electronically report the following data and information to the Commission and to the EEA every 5 years: (a) the data and results of the soil health monitoring and assessment carried out in accordance with Articles 6 to 9; (b) a trend analysis of the soil health for the descriptors listed in parts A, B, and C of Annex I and for the land take and soil sealing indicators listed in "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("41")
    thisalinea.textcontent.append("The first reports shall be submitted by … (OP: please insert date = 5 years and 6")
    thisalinea.textcontent.append("months after entry into force of the Directive).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall electronically report the following data and information to the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 265
    thisalinea.parentID = 264
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall electronically report the following data and information to the Commission and to the EEA every 5 years: (a) the data and results of the soil health monitoring and assessment carried out in accordance with Articles 6 to 9; (b) a trend analysis of the soil health for the descriptors listed in parts A, B, and C of Annex I and for the land take and soil sealing indicators listed in part D of Annex I in accordance with Article 9; (c) a summary of the progress on: (i) implementing sustainable soil management principles in accordance with "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall electronically report the following data and information to the")
    thisalinea.textcontent.append("Commission and to the EEA every 5 years:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the data and results of the soil health monitoring and assessment carried out in ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 266
    thisalinea.parentID = 265
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the data and results of the soil health monitoring and assessment carried out in accordance with Articles 6 to 9; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the data and results of the soil health monitoring and assessment carried out in")
    thisalinea.textcontent.append("accordance with Articles 6 to 9;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) a trend analysis of the soil health for the descriptors listed in parts A, ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 267
    thisalinea.parentID = 265
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) a trend analysis of the soil health for the descriptors listed in parts A, B, and C of Annex I and for the land take and soil sealing indicators listed in part D of Annex I in accordance with Article 9; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) a trend analysis of the soil health for the descriptors listed in parts A, B, and C")
    thisalinea.textcontent.append("of Annex I and for the land take and soil sealing indicators listed in part D of")
    thisalinea.textcontent.append("Annex I in accordance with Article 9;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) a summary of the progress on: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 268
    thisalinea.parentID = 265
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) a summary of the progress on: (i) implementing sustainable soil management principles in accordance with Article 10; (ii) the registration, identification, investigation, and management of contaminated sites in accordance with Articles 12 to 16; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) a summary of the progress on:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(i) implementing sustainable soil management principles in accordance with ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 269
    thisalinea.parentID = 268
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) implementing sustainable soil management principles in accordance with Article 10; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) implementing sustainable soil management principles in accordance with")
    thisalinea.textcontent.append("Article 10;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(ii) the registration, identification, investigation, and management of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 270
    thisalinea.parentID = 268
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) the registration, identification, investigation, and management of contaminated sites in accordance with Articles 12 to 16; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) the registration, identification, investigation, and management of")
    thisalinea.textcontent.append("contaminated sites in accordance with Articles 12 to 16;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) the data and information contained in the register referred to in Article 16. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 271
    thisalinea.parentID = 265
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) the data and information contained in the register referred to in Article 16. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) the data and information contained in the register referred to in Article 16.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall ensure that the Commission and the EEA have permanent ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 272
    thisalinea.parentID = 264
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States shall ensure that the Commission and the EEA have permanent access to the information and data referred to in paragraph 1. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall ensure that the Commission and the EEA have permanent")
    thisalinea.textcontent.append("access to the information and data referred to in paragraph 1.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall provide the Commission with online access to the following: "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 273
    thisalinea.parentID = 264
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall provide the Commission with online access to the following: (a) an up-to-date list and spatial data of their soil districts referred to in Article 4 by … (OP: please insert the date = 2 years and 3 months after date of entry into force of the Directive); (b) an up-to-date list of the competent authorities referred to in Article 5 by … (OP: please insert the date = 2 years and 3 months after date of entry into force of the Directive); (c) the measures and sustainable soil management practices referred to in Article 10 by… "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall provide the Commission with online access to the following:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) an up-to-date list and spatial data of their soil districts referred to in Article ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 274
    thisalinea.parentID = 273
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) an up-to-date list and spatial data of their soil districts referred to in Article 4 by … (OP: please insert the date = 2 years and 3 months after date of entry into force of the Directive); "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) an up-to-date list and spatial data of their soil districts referred to in Article 4")
    thisalinea.textcontent.append("by … (OP: please insert the date = 2 years and 3 months after date of entry into")
    thisalinea.textcontent.append("force of the Directive);")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) an up-to-date list of the competent authorities referred to in Article 5 by … ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 275
    thisalinea.parentID = 273
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) an up-to-date list of the competent authorities referred to in Article 5 by … (OP: please insert the date = 2 years and 3 months after date of entry into force of the Directive); "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) an up-to-date list of the competent authorities referred to in Article 5 by …")
    thisalinea.textcontent.append("(OP: please insert the date = 2 years and 3 months after date of entry into force")
    thisalinea.textcontent.append("of the Directive);")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the measures and sustainable soil management practices referred to in Article ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 276
    thisalinea.parentID = 273
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the measures and sustainable soil management practices referred to in Article 10 by… (OP: please insert the date = 4 years and 3 months after date of entry into force of the Directive). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the measures and sustainable soil management practices referred to in Article")
    thisalinea.textcontent.append("10 by… (OP: please insert the date = 4 years and 3 months after date of entry")
    thisalinea.textcontent.append("into force of the Directive).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. The Commission is empowered to adopt implementing acts establishing the format ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 277
    thisalinea.parentID = 264
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. The Commission is empowered to adopt implementing acts establishing the format and the modalities for submitting the information referred to paragraph 1 of this Article. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 21. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. The Commission is empowered to adopt implementing acts establishing the format")
    thisalinea.textcontent.append("and the modalities for submitting the information referred to paragraph 1 of this")
    thisalinea.textcontent.append("Article. Those implementing acts shall be adopted in accordance with the")
    thisalinea.textcontent.append("examination procedure referred to in Article 21.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 19 Information to the public"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 278
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 28
    thisalinea.summary = "42 Council80 and Regulation (EC) No 1367/2006 of the European Parliament and of the Council81. 1. Member States shall make public the data generated by the monitoring carried out under Article 8 and the assessment carried out under Article 9 of this Directive accessible to the public, in accordance with the provisions under Article 11 of Directive 2007/2/EC of the European Parliament and of the Council79 for geographically explicit data and Article 5 of Directive (EU) 2019/1024 for other data. 2. The Commission shall ensure that soil health data made accessible through the digital soil health data portal referred to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("42")
    thisalinea.textcontent.append("Council80 and Regulation (EC) No 1367/2006 of the European Parliament and of the")
    thisalinea.textcontent.append("Council81.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall make public the data generated by the monitoring carried out ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 279
    thisalinea.parentID = 278
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall make public the data generated by the monitoring carried out under Article 8 and the assessment carried out under Article 9 of this Directive accessible to the public, in accordance with the provisions under Article 11 of Directive 2007/2/EC of the European Parliament and of the Council79 for geographically explicit data and Article 5 of Directive (EU) 2019/1024 for other data. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall make public the data generated by the monitoring carried out")
    thisalinea.textcontent.append("under Article 8 and the assessment carried out under Article 9 of this Directive")
    thisalinea.textcontent.append("accessible to the public, in accordance with the provisions under Article 11 of")
    thisalinea.textcontent.append("Directive 2007/2/EC of the European Parliament and of the Council79 for")
    thisalinea.textcontent.append("geographically explicit data and Article 5 of Directive (EU) 2019/1024 for other")
    thisalinea.textcontent.append("data.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The Commission shall ensure that soil health data made accessible through the ..."
    thisalinea.titlefontsize = "12.000000000000028"
    thisalinea.nativeID = 280
    thisalinea.parentID = 278
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The Commission shall ensure that soil health data made accessible through the digital soil health data portal referred to in Article 6 is available to the public in accordance with Regulation (EU) 2018/1725 of the European Parliament and of the "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The Commission shall ensure that soil health data made accessible through the")
    thisalinea.textcontent.append("digital soil health data portal referred to in Article 6 is available to the public in")
    thisalinea.textcontent.append("accordance with Regulation (EU) 2018/1725 of the European Parliament and of the")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall ensure that the information referred to in Article 18 of this ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 281
    thisalinea.parentID = 278
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall ensure that the information referred to in Article 18 of this Directive is available and accessible to the public in accordance with Directive 2003/4/EC, Directive 2007/2/EC and Directive (EU) 2019/1024 of the Parliament and of the Council82. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall ensure that the information referred to in Article 18 of this")
    thisalinea.textcontent.append("Directive is available and accessible to the public in accordance with Directive")
    thisalinea.textcontent.append("2003/4/EC, Directive 2007/2/EC and Directive (EU) 2019/1024 of the Parliament")
    thisalinea.textcontent.append("and of the Council82.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Disclosure of any information required under this Directive may be refused or ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 282
    thisalinea.parentID = 278
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Disclosure of any information required under this Directive may be refused or restricted where the conditions laid down in Article 4 of Directive 2003/4/EC are fulfilled. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Disclosure of any information required under this Directive may be refused or")
    thisalinea.textcontent.append("restricted where the conditions laid down in Article 4 of Directive 2003/4/EC are")
    thisalinea.textcontent.append("fulfilled.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter VI Delegation and Committee procedure"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 283
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 29
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 20 Exercise of the delegation"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 284
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 30
    thisalinea.summary = "43 Parliament and the Council have both informed the Commission that they will not object. That period shall be extended by two months at the initiative of the European Parliament or of the Council. 1. The power to adopt delegated acts is conferred on the Commission subject to the conditions laid down in this Article. 2. The power to adopt delegated acts referred to in Articles 8, 10, 15 and 16 shall be conferred on the Commission for an indeterminate period of time from the date of entry into force of this Directive. 3. The delegation of power referred to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("43")
    thisalinea.textcontent.append("Parliament and the Council have both informed the Commission that they will not")
    thisalinea.textcontent.append("object. That period shall be extended by two months at the initiative of the European")
    thisalinea.textcontent.append("Parliament or of the Council.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The power to adopt delegated acts is conferred on the Commission subject to the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 285
    thisalinea.parentID = 284
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The power to adopt delegated acts is conferred on the Commission subject to the conditions laid down in this Article. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The power to adopt delegated acts is conferred on the Commission subject to the")
    thisalinea.textcontent.append("conditions laid down in this Article.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The power to adopt delegated acts referred to in Articles 8, 10, 15 and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 286
    thisalinea.parentID = 284
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The power to adopt delegated acts referred to in Articles 8, 10, 15 and 16 shall be conferred on the Commission for an indeterminate period of time from the date of entry into force of this Directive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The power to adopt delegated acts referred to in Articles 8, 10, 15 and 16 shall be")
    thisalinea.textcontent.append("conferred on the Commission for an indeterminate period of time from the date of")
    thisalinea.textcontent.append("entry into force of this Directive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. The delegation of power referred to in Articles 8, 10, 15 and 16 may ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 287
    thisalinea.parentID = 284
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. The delegation of power referred to in Articles 8, 10, 15 and 16 may be revoked at any time by the European Parliament or by the Council. A decision to revoke shall put an end to the delegation of the power specified in that decision. It shall take effect the day following the publication of the decision in the Official Journal of the European Union or at a later date specified therein. It shall not affect the validity of any delegated acts already in force. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. The delegation of power referred to in Articles 8, 10, 15 and 16 may be revoked at")
    thisalinea.textcontent.append("any time by the European Parliament or by the Council. A decision to revoke shall")
    thisalinea.textcontent.append("put an end to the delegation of the power specified in that decision. It shall take")
    thisalinea.textcontent.append("effect the day following the publication of the decision in the Official Journal of the")
    thisalinea.textcontent.append("European Union or at a later date specified therein. It shall not affect the validity of")
    thisalinea.textcontent.append("any delegated acts already in force.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Before adopting a delegated act, the Commission shall consult experts designated by ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 288
    thisalinea.parentID = 284
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Before adopting a delegated act, the Commission shall consult experts designated by each Member State in accordance with the principles laid down in the Interinstitutional Agreement of 13 April 2016 on Better Law-Making. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Before adopting a delegated act, the Commission shall consult experts designated by")
    thisalinea.textcontent.append("each Member State in accordance with the principles laid down in the")
    thisalinea.textcontent.append("Interinstitutional Agreement of 13 April 2016 on Better Law-Making.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "5. As soon as it adopts a delegated act, the Commission shall notify it simultaneously ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 289
    thisalinea.parentID = 284
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "5. As soon as it adopts a delegated act, the Commission shall notify it simultaneously to the European Parliament and to the Council. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("5. As soon as it adopts a delegated act, the Commission shall notify it simultaneously to")
    thisalinea.textcontent.append("the European Parliament and to the Council.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "6. A delegated act adopted pursuant to Articles 8, 10, 15 and 16 shall enter ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 290
    thisalinea.parentID = 284
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "6. A delegated act adopted pursuant to Articles 8, 10, 15 and 16 shall enter into force only if no objection has been expressed either by the European Parliament or the Council within a period of two months of notification of that act to the European Parliament and the Council or if, before the expiry of that period, the European "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("6. A delegated act adopted pursuant to Articles 8, 10, 15 and 16 shall enter into force")
    thisalinea.textcontent.append("only if no objection has been expressed either by the European Parliament or the")
    thisalinea.textcontent.append("Council within a period of two months of notification of that act to the European")
    thisalinea.textcontent.append("Parliament and the Council or if, before the expiry of that period, the European")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 21 Committee"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 291
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 31
    thisalinea.summary = "1. The Commission shall be assisted by a committee. That committee shall be a committee within the meaning of Regulation (EU) No 182/2011. 2. Where reference is made to this paragraph, Article 5 of Regulation (EU) No 182/2011 shall apply. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. The Commission shall be assisted by a committee. That committee shall be a ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 292
    thisalinea.parentID = 291
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. The Commission shall be assisted by a committee. That committee shall be a committee within the meaning of Regulation (EU) No 182/2011. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. The Commission shall be assisted by a committee. That committee shall be a")
    thisalinea.textcontent.append("committee within the meaning of Regulation (EU) No 182/2011.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Where reference is made to this paragraph, Article 5 of Regulation (EU) No ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 293
    thisalinea.parentID = 291
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Where reference is made to this paragraph, Article 5 of Regulation (EU) No 182/2011 shall apply. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Where reference is made to this paragraph, Article 5 of Regulation (EU) No")
    thisalinea.textcontent.append("182/2011 shall apply.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Chapter VII Final provisions"
    thisalinea.titlefontsize = "15.960000000000036"
    thisalinea.nativeID = 294
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 32
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 22 Access to justice"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 295
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 33
    thisalinea.summary = "Member States shall ensure that members of the public, in accordance with national law, that have a sufficient interest or that maintain the impairment of a right, have access to a review procedure before a court of law, or an independent and impartial body established by law, to challenge the substantive or procedural legality of the assessment of soil health, the measures taken pursuant to this Directive and any failures to act of the competent authorities. Member States shall determine what constitutes a sufficient interest and impairment of a right, consistently with the objective of providing the public with wide "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Member States shall ensure that members of the public, in accordance with national law, that")
    thisalinea.textcontent.append("have a sufficient interest or that maintain the impairment of a right, have access to a review")
    thisalinea.textcontent.append("procedure before a court of law, or an independent and impartial body established by law, to")
    thisalinea.textcontent.append("challenge the substantive or procedural legality of the assessment of soil health, the measures")
    thisalinea.textcontent.append("taken pursuant to this Directive and any failures to act of the competent authorities.")
    thisalinea.textcontent.append("Member States shall determine what constitutes a sufficient interest and impairment of a right,")
    thisalinea.textcontent.append("consistently with the objective of providing the public with wide access to justice. For the")
    thisalinea.textcontent.append("purposes of paragraph 1, any non-governmental organisation promoting environmental")
    thisalinea.textcontent.append("protection and meeting any requirements under national law shall be deemed to have rights")
    thisalinea.textcontent.append("capable of being impaired and their interest shall be deemed sufficient.")
    thisalinea.textcontent.append("Review procedures referred to in paragraph 1 shall be fair, equitable, timely and free of")
    thisalinea.textcontent.append("charge or not prohibitively expensive, and shall provide adequate and effective remedies,")
    thisalinea.textcontent.append("including injunctive relief where necessary.")
    thisalinea.textcontent.append("Member States shall ensure that practical information is made available to the public on")
    thisalinea.textcontent.append("access to the administrative and judicial review procedures referred to in this Article.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 23 Penalties"
    thisalinea.titlefontsize = "12.000000000000028"
    thisalinea.nativeID = 296
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 34
    thisalinea.summary = "44 that they effectively deprive the person responsible for the violation of the economic benefits derived from that violation. In the case of a violation committed by a legal person, such fines shall be proportionate to the legal person’s annual turnover in the Member State concerned, taking account, inter alia, the specificities of small and medium-sized enterprises (SMEs). 1. Without prejudice to the obligations of Member States under Directive 2008/99/EC of the European Parliament and of the Council, Member States shall lay down the rules on penalties applicable to violations by natural and legal persons, of the national provisions adopted "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("44")
    thisalinea.textcontent.append("that they effectively deprive the person responsible for the violation of the economic")
    thisalinea.textcontent.append("benefits derived from that violation. In the case of a violation committed by a legal")
    thisalinea.textcontent.append("person, such fines shall be proportionate to the legal person’s annual turnover in the")
    thisalinea.textcontent.append("Member State concerned, taking account, inter alia, the specificities of small and")
    thisalinea.textcontent.append("medium-sized enterprises (SMEs).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Without prejudice to the obligations of Member States under Directive 2008/99/EC ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 297
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Without prejudice to the obligations of Member States under Directive 2008/99/EC of the European Parliament and of the Council, Member States shall lay down the rules on penalties applicable to violations by natural and legal persons, of the national provisions adopted pursuant to this Directive and shall ensure that those rules are implemented. The penalties provided for shall be effective, proportionate and dissuasive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Without prejudice to the obligations of Member States under Directive 2008/99/EC")
    thisalinea.textcontent.append("of the European Parliament and of the Council, Member States shall lay down the")
    thisalinea.textcontent.append("rules on penalties applicable to violations by natural and legal persons, of the")
    thisalinea.textcontent.append("national provisions adopted pursuant to this Directive and shall ensure that those")
    thisalinea.textcontent.append("rules are implemented. The penalties provided for shall be effective, proportionate")
    thisalinea.textcontent.append("and dissuasive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The penalties referred to in paragraph 1 shall include fines proportionate to the ..."
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 298
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The penalties referred to in paragraph 1 shall include fines proportionate to the turnover of the legal person or to the income of the natural person having committed the violation. The level of the fines shall be calculated in such a way as to make sure "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The penalties referred to in paragraph 1 shall include fines proportionate to the")
    thisalinea.textcontent.append("turnover of the legal person or to the income of the natural person having committed")
    thisalinea.textcontent.append("the violation. The level of the fines shall be calculated in such a way as to make sure")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3. Member States shall ensure that the penalties established pursuant to this Article give ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 299
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "3. Member States shall ensure that the penalties established pursuant to this Article give due regard to the following, as applicable: (a) the nature, gravity, and extent of the violation; (b) the intentional or negligent character of the violation; (c) the population or the environment affected by the violation, bearing in mind the impact of the infringement on the objective of achieving a high level of protection of human health and the environment. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("3. Member States shall ensure that the penalties established pursuant to this Article give")
    thisalinea.textcontent.append("due regard to the following, as applicable:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the nature, gravity, and extent of the violation; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 300
    thisalinea.parentID = 299
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the nature, gravity, and extent of the violation; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the nature, gravity, and extent of the violation;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the intentional or negligent character of the violation; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 301
    thisalinea.parentID = 299
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the intentional or negligent character of the violation; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the intentional or negligent character of the violation;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) the population or the environment affected by the violation, bearing in mind ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 302
    thisalinea.parentID = 299
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) the population or the environment affected by the violation, bearing in mind the impact of the infringement on the objective of achieving a high level of protection of human health and the environment. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) the population or the environment affected by the violation, bearing in mind")
    thisalinea.textcontent.append("the impact of the infringement on the objective of achieving a high level of")
    thisalinea.textcontent.append("protection of human health and the environment.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "4. Member States shall without undue delay notify the Commission of the rules and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 303
    thisalinea.parentID = 296
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "4. Member States shall without undue delay notify the Commission of the rules and measures referred to in paragraph 1 and of any subsequent amendments affecting them. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("4. Member States shall without undue delay notify the Commission of the rules and")
    thisalinea.textcontent.append("measures referred to in paragraph 1 and of any subsequent amendments affecting")
    thisalinea.textcontent.append("them.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 24 Evaluation and review"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 304
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 35
    thisalinea.summary = "1. By (OP :please insert the date = 6 years after the date of entry into force of the Directive), the Commission shall carry out an evaluation of this Directive to assess the progress towards its objectives and the need to amend its provisions in order to set more specific requirements to ensure that unhealthy soils are regenerated and that all soils will be healthy by 2050. This evaluation shall take into account, inter alia, the following elements: (a) the experience gained through the implementation of this Directive; (b) the data and information referred to in Article 18; (c) relevant "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. By (OP :please insert the date = 6 years after the date of entry ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 305
    thisalinea.parentID = 304
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. By (OP :please insert the date = 6 years after the date of entry into force of the Directive), the Commission shall carry out an evaluation of this Directive to assess the progress towards its objectives and the need to amend its provisions in order to set more specific requirements to ensure that unhealthy soils are regenerated and that all soils will be healthy by 2050. This evaluation shall take into account, inter alia, the following elements: (a) the experience gained through the implementation of this Directive; (b) the data and information referred to in Article 18; (c) relevant "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. By (OP :please insert the date = 6 years after the date of entry into force of the")
    thisalinea.textcontent.append("Directive), the Commission shall carry out an evaluation of this Directive to assess")
    thisalinea.textcontent.append("the progress towards its objectives and the need to amend its provisions in order to")
    thisalinea.textcontent.append("set more specific requirements to ensure that unhealthy soils are regenerated and that")
    thisalinea.textcontent.append("all soils will be healthy by 2050. This evaluation shall take into account, inter alia,")
    thisalinea.textcontent.append("the following elements:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(a) the experience gained through the implementation of this Directive; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 306
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(a) the experience gained through the implementation of this Directive; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(a) the experience gained through the implementation of this Directive;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(b) the data and information referred to in Article 18; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 307
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(b) the data and information referred to in Article 18; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(b) the data and information referred to in Article 18;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(c) relevant scientific and analytical data, including results from research projects ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 308
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(c) relevant scientific and analytical data, including results from research projects funded by the Union; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(c) relevant scientific and analytical data, including results from research projects")
    thisalinea.textcontent.append("funded by the Union;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(d) an analysis of the gap towards achieving healthy soils by 2050; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 309
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "(d) an analysis of the gap towards achieving healthy soils by 2050; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(d) an analysis of the gap towards achieving healthy soils by 2050;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "(e) an analysis of the possible need to adapt to scientific and technical progress the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 310
    thisalinea.parentID = 305
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLLETTER
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "(e) an analysis of the possible need to adapt to scientific and technical progress the provisions of this Directive in particular regarding the following items: (i) the definition of healthy soils; (ii) the establishment of criteria for soil descriptors listed in part C of annex I; (iii) the addition of new soil descriptors for monitoring purposes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(e) an analysis of the possible need to adapt to scientific and technical progress the")
    thisalinea.textcontent.append("provisions of this Directive in particular regarding the following items:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(i) the definition of healthy soils; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 311
    thisalinea.parentID = 310
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "(i) the definition of healthy soils; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(i) the definition of healthy soils;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(ii) the establishment of criteria for soil descriptors listed in part C of annex ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 312
    thisalinea.parentID = 310
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "(ii) the establishment of criteria for soil descriptors listed in part C of annex I; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(ii) the establishment of criteria for soil descriptors listed in part C of annex")
    thisalinea.textcontent.append("I;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "(iii) the addition of new soil descriptors for monitoring purposes. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 313
    thisalinea.parentID = 310
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SMALLROMAN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "(iii) the addition of new soil descriptors for monitoring purposes. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("(iii) the addition of new soil descriptors for monitoring purposes.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. The Commission shall present a report on the main findings of the evaluation ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 314
    thisalinea.parentID = 304
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. The Commission shall present a report on the main findings of the evaluation referred to in paragraph 1 to the European Parliament, the Council, the European Economic and Social Committee, and the Committee of the Regions. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. The Commission shall present a report on the main findings of the evaluation")
    thisalinea.textcontent.append("referred to in paragraph 1 to the European Parliament, the Council, the European")
    thisalinea.textcontent.append("Economic and Social Committee, and the Committee of the Regions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 25 Transposition"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 315
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 36
    thisalinea.summary = "45 When Member States adopt those provisions, they shall contain a reference to this Directive or be accompanied by such a reference on the occasion of their official publication. Member States shall determine how such reference is to be made. 1. Member States shall bring into force the laws, regulations and administrative provisions necessary to comply with this Directive by … [OP please insert date = 2 years after date of entry into force of the Directive]. They shall forthwith communicate to the Commission the text of those provisions. 2. Member States shall communicate to the Commission the text of "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("45")
    thisalinea.textcontent.append("When Member States adopt those provisions, they shall contain a reference to this")
    thisalinea.textcontent.append("Directive or be accompanied by such a reference on the occasion of their official")
    thisalinea.textcontent.append("publication. Member States shall determine how such reference is to be made.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1. Member States shall bring into force the laws, regulations and administrative ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 316
    thisalinea.parentID = 315
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "1. Member States shall bring into force the laws, regulations and administrative provisions necessary to comply with this Directive by … [OP please insert date = 2 years after date of entry into force of the Directive]. They shall forthwith communicate to the Commission the text of those provisions. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1. Member States shall bring into force the laws, regulations and administrative")
    thisalinea.textcontent.append("provisions necessary to comply with this Directive by … [OP please insert date = 2")
    thisalinea.textcontent.append("years after date of entry into force of the Directive]. They shall forthwith")
    thisalinea.textcontent.append("communicate to the Commission the text of those provisions.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2. Member States shall communicate to the Commission the text of the main provisions ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 317
    thisalinea.parentID = 315
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.DIGIT
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "2. Member States shall communicate to the Commission the text of the main provisions of national law which they adopt in the field covered by this Directive. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2. Member States shall communicate to the Commission the text of the main provisions")
    thisalinea.textcontent.append("of national law which they adopt in the field covered by this Directive.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 26 Entry into force"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 318
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 37
    thisalinea.summary = "This Directive shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Directive shall enter into force on the twentieth day following that of its publication in")
    thisalinea.textcontent.append("the Official Journal of the European Union.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "Article 27 Addressees"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 319
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 38
    thisalinea.summary = "This Directive is addressed to the Member States. Done at Brussels, 46 LEGISLATIVE FINANCIAL STATEMENT "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("This Directive is addressed to the Member States.")
    thisalinea.textcontent.append("Done at Brussels,")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "For the European Parliament For the Council The President The President"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 320
    thisalinea.parentID = 319
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "46 LEGISLATIVE FINANCIAL STATEMENT "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("46")
    thisalinea.textcontent.append("LEGISLATIVE FINANCIAL STATEMENT")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. FRAMEWORK OF THE PROPOSAL/INITIATIVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 321
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 39
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1. Title of the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 322
    thisalinea.parentID = 321
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2. Policy area(s) concerned"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 323
    thisalinea.parentID = 321
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.3. The proposal/initiative relates to:"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 324
    thisalinea.parentID = 321
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
    thisalinea.nativeID = 325
    thisalinea.parentID = 321
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.1. General objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 326
    thisalinea.parentID = 325
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.2. Specific objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 327
    thisalinea.parentID = 325
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.3. Expected result(s) and impact"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 328
    thisalinea.parentID = 325
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.4. Indicators of performance"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 329
    thisalinea.parentID = 325
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.5. Grounds for the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 330
    thisalinea.parentID = 321
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.1. Requirement(s) to be met in the short or long term including a detailed timeline for roll-out of the implementation of the initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 331
    thisalinea.parentID = 330
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.2. Added value of Union involvement (it may result from different factors, e.g. coordination gains, legal certainty, greater effectiveness or complementarities). For the purposes of this point 'added value of Union involvement' is the value resulting from Union intervention, which is additional to the value that would have been otherwise created by Member States alone."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 332
    thisalinea.parentID = 330
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.3. Lessons learned from similar experiences in the past"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 333
    thisalinea.parentID = 330
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.4. Compatibility with the Multiannual Financial Framework and possible synergies with other appropriate instruments"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 334
    thisalinea.parentID = 330
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.5. Assessment of the different available financing options, including scope for redeployment"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 335
    thisalinea.parentID = 330
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.6. Duration and financial impact of the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 336
    thisalinea.parentID = 321
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.7. Method(s) of budget implementation planned"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 337
    thisalinea.parentID = 321
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "2. MANAGEMENT MEASURES"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 338
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 40
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.1. Monitoring and reporting rules"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 339
    thisalinea.parentID = 338
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.2. Management and control system(s)"
    thisalinea.titlefontsize = "12.000000000000028"
    thisalinea.nativeID = 340
    thisalinea.parentID = 338
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.1. Justification of the management mode(s), the funding implementation mechanism(s), the payment modalities and the control strategy proposed"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 341
    thisalinea.parentID = 340
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.2. Information concerning the risks identified and the internal control system(s) set up to mitigate them"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 342
    thisalinea.parentID = 340
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = '2.2.3. Estimation and justification of the cost-effectiveness of the controls (ratio of "control costs ÷ value of the related funds managed"), and assessment of the expected levels of risk of error (at payment & at closure)'
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 343
    thisalinea.parentID = 340
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.3. Measures to prevent fraud and irregularities"
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 344
    thisalinea.parentID = 338
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "3. ESTIMATED FINANCIAL IMPACT OF THE PROPOSAL/INITIATIVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 345
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 41
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("1")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.1. Heading(s) of the multiannual financial framework and expenditure budget line(s) affected"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 346
    thisalinea.parentID = 345
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.2. Estimated financial impact of the proposal on appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 347
    thisalinea.parentID = 345
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.1. Summary of estimated impact on operational appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 348
    thisalinea.parentID = 347
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.2. Estimated output funded with operational appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 349
    thisalinea.parentID = 347
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.3. Summary of estimated impact on administrative appropriations"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 350
    thisalinea.parentID = 347
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.3.1. Estimated requirements of human resources"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 351
    thisalinea.parentID = 347
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.4. Compatibility with the current multiannual financial framework"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 352
    thisalinea.parentID = 347
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "3.2.5. Third-party contributions"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 353
    thisalinea.parentID = 347
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "3.3. Estimated impact on revenue"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 354
    thisalinea.parentID = 345
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = ""
    thisalinea.sum_CanbeEmpty = True
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("2")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 1
    thisalinea.texttitle = "1. FRAMEWORK OF THE PROPOSAL/INITIATIVE"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 355
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 42
    thisalinea.summary = "Proposal for a Directive of the European Parliament and of the Council on Soil Monitoring and Resilience (Soil Monitoring Law). 09 -Environment and Climate Action Activities: 09 02 - Programme for Environment and Climate Action (LIFE)  a new action The objective of the proposed Directive is to contribute to address the big societal challenges of: - Achieving climate neutrality and becoming resilient to climate change - Reversing biodiversity loss and fulfilling international commitments on biodiversity - Reducing pollution to levels no longer considered harmful to human health and the environment - Fulfilling international commitments on land degradation neutrality Following "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.1. Title of the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 356
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "Proposal for a Directive of the European Parliament and of the Council on Soil Monitoring and Resilience (Soil Monitoring Law). "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Proposal for a Directive of the European Parliament and of the Council on Soil")
    thisalinea.textcontent.append("Monitoring and Resilience (Soil Monitoring Law).")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.2. Policy area(s) concerned"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 357
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "09 -Environment and Climate Action Activities: 09 02 - Programme for Environment and Climate Action (LIFE) "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("09 -Environment and Climate Action")
    thisalinea.textcontent.append("Activities:")
    thisalinea.textcontent.append("09 02 - Programme for Environment and Climate Action (LIFE)")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.3. The proposal/initiative relates to:"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 358
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = " a new action "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" a new action")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.4. Objective(s)"
    thisalinea.titlefontsize = "11.999999999999943"
    thisalinea.nativeID = 359
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The objective of the proposed Directive is to contribute to address the big societal challenges of: - Achieving climate neutrality and becoming resilient to climate change - Reversing biodiversity loss and fulfilling international commitments on biodiversity - Reducing pollution to levels no longer considered harmful to human health and the environment - Fulfilling international commitments on land degradation neutrality Following from the general objective, the specific objective of this proposed Directive is: Following from the specific objective, the operational objectives are: 3 - To stop soil degradation and achieve healthy soils across the EU by 2050, so ensuring that EU "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.1. General objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 360
    thisalinea.parentID = 359
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The objective of the proposed Directive is to contribute to address the big societal challenges of: - Achieving climate neutrality and becoming resilient to climate change - Reversing biodiversity loss and fulfilling international commitments on biodiversity - Reducing pollution to levels no longer considered harmful to human health and the environment - Fulfilling international commitments on land degradation neutrality "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The objective of the proposed Directive is to contribute to address the big societal")
    thisalinea.textcontent.append("challenges of:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- Achieving climate neutrality and becoming resilient to climate change "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 361
    thisalinea.parentID = 360
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- Achieving climate neutrality and becoming resilient to climate change "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Achieving climate neutrality and becoming resilient to climate change")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- Reversing biodiversity loss and fulfilling international commitments on biodiversity "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 362
    thisalinea.parentID = 360
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- Reversing biodiversity loss and fulfilling international commitments on biodiversity "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Reversing biodiversity loss and fulfilling international commitments on biodiversity")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- Reducing pollution to levels no longer considered harmful to human health and the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 363
    thisalinea.parentID = 360
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "- Reducing pollution to levels no longer considered harmful to human health and the environment "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Reducing pollution to levels no longer considered harmful to human health and the")
    thisalinea.textcontent.append("environment")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- Fulfilling international commitments on land degradation neutrality "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 364
    thisalinea.parentID = 360
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "- Fulfilling international commitments on land degradation neutrality "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- Fulfilling international commitments on land degradation neutrality")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.2. Specific objective(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 365
    thisalinea.parentID = 359
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Following from the general objective, the specific objective of this proposed Directive is: Following from the specific objective, the operational objectives are: 3 - To stop soil degradation and achieve healthy soils across the EU by 2050, so ensuring that EU soils can supply multiple ecosystem services at a scale sufficient to meet environmental, societal and economic needs, and reducing soil pollution to levels no longer considered harmful to human health and the environment. - To establish measures to stop degrading soils and regenerate soil health. - To establish an effective framework to ensure implementation in particular by the obligation "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Following from the general objective, the specific objective of this proposed")
    thisalinea.textcontent.append("Directive is:")
    thisalinea.textcontent.append("Following from the specific objective, the operational objectives are:")
    thisalinea.textcontent.append("3")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- To stop soil degradation and achieve healthy soils across the EU by 2050, so ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 366
    thisalinea.parentID = 365
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- To stop soil degradation and achieve healthy soils across the EU by 2050, so ensuring that EU soils can supply multiple ecosystem services at a scale sufficient to meet environmental, societal and economic needs, and reducing soil pollution to levels no longer considered harmful to human health and the environment. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- To stop soil degradation and achieve healthy soils across the EU by 2050, so")
    thisalinea.textcontent.append("ensuring that EU soils can supply multiple ecosystem services at a scale sufficient to")
    thisalinea.textcontent.append("meet environmental, societal and economic needs, and reducing soil pollution to")
    thisalinea.textcontent.append("levels no longer considered harmful to human health and the environment.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- To establish measures to stop degrading soils and regenerate soil health. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 367
    thisalinea.parentID = 365
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- To establish measures to stop degrading soils and regenerate soil health. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- To establish measures to stop degrading soils and regenerate soil health.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- To establish an effective framework to ensure implementation in particular by the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 368
    thisalinea.parentID = 365
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "- To establish an effective framework to ensure implementation in particular by the obligation for the Member States to assess soil health as well as for reporting and review. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- To establish an effective framework to ensure implementation in particular by the")
    thisalinea.textcontent.append("obligation for the Member States to assess soil health as well as for reporting and")
    thisalinea.textcontent.append("review.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.3. Expected result(s) and impact"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 369
    thisalinea.parentID = 359
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "The proposed intiative will deliver significant environmental benefits and improve soil health with knock-on effects on the quality of both water and air, biodiversity, climate benefits and food benefits. It addresses the risks to human health and the environment coming from contaminated sites. The welfare and well-being of current and future generations depends on soil health. The implementation of the proposal is expected to create plenty of opportunities for SMEs both for growth (e.g. investigation and remediation of contaminated sites, advisory services for soil health, soil testing labs) and for innovation in the devise and application of sustainable soil management "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposed intiative will deliver significant environmental benefits and improve")
    thisalinea.textcontent.append("soil health with knock-on effects on the quality of both water and air, biodiversity,")
    thisalinea.textcontent.append("climate benefits and food benefits. It addresses the risks to human health and the")
    thisalinea.textcontent.append("environment coming from contaminated sites.")
    thisalinea.textcontent.append("The welfare and well-being of current and future generations depends on soil health.")
    thisalinea.textcontent.append("The implementation of the proposal is expected to create plenty of opportunities for")
    thisalinea.textcontent.append("SMEs both for growth (e.g. investigation and remediation of contaminated sites,")
    thisalinea.textcontent.append("advisory services for soil health, soil testing labs) and for innovation in the devise")
    thisalinea.textcontent.append("and application of sustainable soil management and restoration measures, as well as")
    thisalinea.textcontent.append("in relation to the investigation and remediation of contaminated soils.")
    thisalinea.textcontent.append("The implementation of soil monitoring is also expected to create opportunities for")
    thisalinea.textcontent.append("research and development and business to develop parameters and soil observation.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.4.4. Indicators of performance"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 370
    thisalinea.parentID = 359
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The implementation of the proposal should ensure that soils across the EU are healthy by 2050 and that they are managed sustainable so that they do not further deteriorate. These are the main indicators foreseen to monitor the implementation: - number of soil health monitoring points - proportion of the EU territory where soils are in healthy status - sustainable soil management measures adopted - regeneration measures put in place - number of potentially contaminated sites registered in the dedicated national registers - number of investigated potentially contaminated sites - number of remediated or properly managed contaminated sites "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The implementation of the proposal should ensure that soils across the EU are")
    thisalinea.textcontent.append("healthy by 2050 and that they are managed sustainable so that they do not further")
    thisalinea.textcontent.append("deteriorate.")
    thisalinea.textcontent.append("These are the main indicators foreseen to monitor the implementation:")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- number of soil health monitoring points "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 371
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- number of soil health monitoring points "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- number of soil health monitoring points")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- proportion of the EU territory where soils are in healthy status "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 372
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- proportion of the EU territory where soils are in healthy status "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- proportion of the EU territory where soils are in healthy status")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- sustainable soil management measures adopted "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 373
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "- sustainable soil management measures adopted "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- sustainable soil management measures adopted")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- regeneration measures put in place "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 374
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "- regeneration measures put in place "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- regeneration measures put in place")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- number of potentially contaminated sites registered in the dedicated national ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 375
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "- number of potentially contaminated sites registered in the dedicated national registers "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- number of potentially contaminated sites registered in the dedicated national")
    thisalinea.textcontent.append("registers")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- number of investigated potentially contaminated sites "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 376
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "- number of investigated potentially contaminated sites "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- number of investigated potentially contaminated sites")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- number of remediated or properly managed contaminated sites "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 377
    thisalinea.parentID = 370
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "- number of remediated or properly managed contaminated sites "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- number of remediated or properly managed contaminated sites")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.5. Grounds for the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 378
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "The proposed Directive will entry into force after its adoption but there will be a transposition period of 2 years for the Member States to adopt and notify the laws, regulations and administrative provisions necessary to comply with this Directive. During this transposition period the Commission will assist Member States via: 4 After adoption of the Directive, the Commission: After expiration of the transposition deadline, the Commission will, in accordance with its policy on the verification of the implementation of EU legislation: After expiration of the transposition deadline, Member States will need: to put in place the appropriate governance to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.1. Requirement(s) to be met in the short or long term including a detailed timeline for roll-out of the implementation of the initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 379
    thisalinea.parentID = 378
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The proposed Directive will entry into force after its adoption but there will be a transposition period of 2 years for the Member States to adopt and notify the laws, regulations and administrative provisions necessary to comply with this Directive. During this transposition period the Commission will assist Member States via: 4 After adoption of the Directive, the Commission: After expiration of the transposition deadline, the Commission will, in accordance with its policy on the verification of the implementation of EU legislation: After expiration of the transposition deadline, Member States will need: to put in place the appropriate governance to "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The proposed Directive will entry into force after its adoption but there will be a")
    thisalinea.textcontent.append("transposition period of 2 years for the Member States to adopt and notify the laws,")
    thisalinea.textcontent.append("regulations and administrative provisions necessary to comply with this Directive.")
    thisalinea.textcontent.append("During this transposition period the Commission will assist Member States via:")
    thisalinea.textcontent.append("4")
    thisalinea.textcontent.append("After adoption of the Directive, the Commission:")
    thisalinea.textcontent.append("After expiration of the transposition deadline, the Commission will, in accordance")
    thisalinea.textcontent.append("with its policy on the verification of the implementation of EU legislation:")
    thisalinea.textcontent.append("After expiration of the transposition deadline, Member States will need:")
    thisalinea.textcontent.append("to put in place the appropriate governance")
    thisalinea.textcontent.append("to establish soil districts")
    thisalinea.textcontent.append("to put in place the soil monitoring framework including the determination of")
    thisalinea.textcontent.append("sampling points and adopting methodologies")
    thisalinea.textcontent.append("to set up a register of potentially contaminated sites.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- guidance document for the transposition of the Directive; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 380
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "- guidance document for the transposition of the Directive; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- guidance document for the transposition of the Directive;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- development of various guidance and information material if need be regarding the ..."
    thisalinea.titlefontsize = "11.999999999999986"
    thisalinea.nativeID = 381
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "- development of various guidance and information material if need be regarding the implementation of the Directive "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- development of various guidance and information material if need be regarding the")
    thisalinea.textcontent.append("implementation of the Directive")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- helpdesk function "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 382
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "- helpdesk function "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- helpdesk function")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- will regularly convene the specific new committee which will assist the ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 383
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "- will regularly convene the specific new committee which will assist the Commission as well as expert group meetings "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- will regularly convene the specific new committee which will assist the")
    thisalinea.textcontent.append("Commission as well as expert group meetings")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- take the necessary steps and arrangements to update and put in place the LUCAS ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 384
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "- take the necessary steps and arrangements to update and put in place the LUCAS soil programme which will complement the monitoring framework of the Member States; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- take the necessary steps and arrangements to update and put in place the LUCAS")
    thisalinea.textcontent.append("soil programme which will complement the monitoring framework of the Member")
    thisalinea.textcontent.append("States;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- verify the completeness of the transposition measures notified by the Member ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 385
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "- verify the completeness of the transposition measures notified by the Member States and if need be may initiate infringement procedures; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- verify the completeness of the transposition measures notified by the Member")
    thisalinea.textcontent.append("States and if need be may initiate infringement procedures;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 4
    thisalinea.texttitle = "- verify the conformity of the transposition measures Member States and if need be ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 386
    thisalinea.parentID = 379
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = "- verify the conformity of the transposition measures Member States and if need be may initiate infringement procedures. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("- verify the conformity of the transposition measures Member States and if need be")
    thisalinea.textcontent.append("may initiate infringement procedures.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.2. Added value of Union involvement (it may result from different factors, e.g. coordination gains, legal certainty, greater effectiveness or complementarities). For the purposes of this point 'added value of Union involvement' is the value resulting from Union intervention, which is additional to the value that would have been otherwise created by Member States alone."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 387
    thisalinea.parentID = 378
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "Reasons for action at European level (ex-ante) Drivers and impacts of soil degradation exceed country borders and reduce the provision of ecosystem services throughout the EU and its neighbours. National action has proven to be insufficient to address soil degradation across the EU and has led to divergent levels of protection of the environment and human health. Expected generated EU added value (ex-post) Coordinated action at EU level is expected to generate synergies, effectiveness and efficiency gains for monitoring and restoring soil health and ensuring that soils are managed in a sustainable way. Coordinated action is also expected to deliver "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("Reasons for action at European level (ex-ante)")
    thisalinea.textcontent.append("Drivers and impacts of soil degradation exceed country borders and reduce the")
    thisalinea.textcontent.append("provision of ecosystem services throughout the EU and its neighbours. National")
    thisalinea.textcontent.append("action has proven to be insufficient to address soil degradation across the EU and has")
    thisalinea.textcontent.append("led to divergent levels of protection of the environment and human health.")
    thisalinea.textcontent.append("Expected generated EU added value (ex-post)")
    thisalinea.textcontent.append("Coordinated action at EU level is expected to generate synergies, effectiveness and")
    thisalinea.textcontent.append("efficiency gains for monitoring and restoring soil health and ensuring that soils are")
    thisalinea.textcontent.append("managed in a sustainable way. Coordinated action is also expected to deliver on the")
    thisalinea.textcontent.append("commitments that rely as well on soil health made in the EU and in the global")
    thisalinea.textcontent.append("context, namely on addressing climate change, reverse biodiversity loss, aim at zero")
    thisalinea.textcontent.append("pollution and achieve land degradation neutrality. Lastly, action at EU level is")
    thisalinea.textcontent.append("expected to address potential distortions in the internal market and unfair competition")
    thisalinea.textcontent.append("among businesses, since there are lower environmental requirements in some")
    thisalinea.textcontent.append("Member States.")
    thisalinea.textcontent.append("5")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.3. Lessons learned from similar experiences in the past"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 388
    thisalinea.parentID = 378
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "In April 2002, the Commission announced for the first time its intention to develop a Strategy for Soil Protection and to prepare the ground for a proposal for EU soil legislation. A first proposal was subsequently adopted by the Commission in 2006 but difficult political discussions took place in the Council of the EU under successive EU presidencies. No agreement was found due to a blocking minority of five Member States. As a consequence, the Commission withdrew its proposal in 2014. The debates showed that regulating soil at EU level can trigger resistance from different stakeholder groups and Member States. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("In April 2002, the Commission announced for the first time its intention to develop a")
    thisalinea.textcontent.append("Strategy for Soil Protection and to prepare the ground for a proposal for EU soil")
    thisalinea.textcontent.append("legislation. A first proposal was subsequently adopted by the Commission in 2006")
    thisalinea.textcontent.append("but difficult political discussions took place in the Council of the EU under")
    thisalinea.textcontent.append("successive EU presidencies. No agreement was found due to a blocking minority of")
    thisalinea.textcontent.append("five Member States. As a consequence, the Commission withdrew its proposal in")
    thisalinea.textcontent.append("2014.")
    thisalinea.textcontent.append("The debates showed that regulating soil at EU level can trigger resistance from")
    thisalinea.textcontent.append("different stakeholder groups and Member States. Therefore, before preparing this")
    thisalinea.textcontent.append("new initiative the Commission has invested extensively in meeting and consulting")
    thisalinea.textcontent.append("stakeholders and Member States and some through the establishment of the EU")
    thisalinea.textcontent.append("expert group on soil protection.")
    thisalinea.textcontent.append("Particular attention was paid to the principles of subsidiarity and proportionality")
    thisalinea.textcontent.append("through sufficient flexibility. The proposal also takes largely into account of the")
    thisalinea.textcontent.append("variability of soils, climatic conditions and land use.")
    thisalinea.textcontent.append("A more result-oriented approach with clear targets and less focus on the process or")
    thisalinea.textcontent.append("measures to be implemented provides more flexibility at national level, while still")
    thisalinea.textcontent.append("satisfying the need for protecting soil coherently across the EU.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.4. Compatibility with the Multiannual Financial Framework and possible synergies with other appropriate instruments"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 389
    thisalinea.parentID = 378
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 3
    thisalinea.summary = "The initiative falls under Heading 3 (Natural Resources and Environment), Title 9 (Environment and Climate Action) of the Multiannual Financial Framework (MFF) 2021-2027 The initiative falls under the umbrella of the European Green Deal. It also follows from and contributes to achieving the ambitions set out in the EU Soil Strategy for 2030. The EU Soil Strategy is a key deliverable of the EU biodiversity strategy for 2030 and sets out a framework and concrete measures to protect and restore soils, and ensure that they are used sustainably. It sets as well a vision and objectives to achieve healthy soils "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The initiative falls under Heading 3 (Natural Resources and Environment), Title 9")
    thisalinea.textcontent.append("(Environment and Climate Action) of the Multiannual Financial Framework (MFF)")
    thisalinea.textcontent.append("2021-2027")
    thisalinea.textcontent.append("The initiative falls under the umbrella of the European Green Deal. It also follows")
    thisalinea.textcontent.append("from and contributes to achieving the ambitions set out in the EU Soil Strategy for")
    thisalinea.textcontent.append("2030. The EU Soil Strategy is a key deliverable of the EU biodiversity strategy for")
    thisalinea.textcontent.append("2030 and sets out a framework and concrete measures to protect and restore soils,")
    thisalinea.textcontent.append("and ensure that they are used sustainably. It sets as well a vision and objectives to")
    thisalinea.textcontent.append("achieve healthy soils by 2050, with concrete actions by 2030.")
    thisalinea.textcontent.append("The proposal is complementary to other measures outlined in the Biodiversity")
    thisalinea.textcontent.append("Strategy 2030 (such as the nature restoration law) and in the EU Soil Strategy (such")
    thisalinea.textcontent.append("as the guidance on risk assessment, soil sealing and funding).")
    thisalinea.textcontent.append("Implementation of the initiative by Member States and businesses will be supported")
    thisalinea.textcontent.append("by a range of EU programmes such the European Agricultural Guarantee Fund, the")
    thisalinea.textcontent.append("European Agricultural Fund for Rural Development, the European Regional and")
    thisalinea.textcontent.append("Development Fund, the Cohesion Fund, the Programme for the Environment and")
    thisalinea.textcontent.append("Climate Action (LIFE), the Framework Programme for Research and Innovation")
    thisalinea.textcontent.append("(Horizon Europe, HE) notably through the HE Mission “A Soil Deal for Europe”, the")
    thisalinea.textcontent.append("Recovery and Resilience Facility (RRF), InvestEU, and national financing by EU")
    thisalinea.textcontent.append("Member States and private funding.")
    thisalinea.textcontent.append("6")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "1.5.5. Assessment of the different available financing options, including scope for redeployment"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 390
    thisalinea.parentID = 378
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "The implementation of the new Directive will entail new tasks and activities for the Commission. This will require human resources, EEA support, procurement resources for external contractors and one or more administrative arrangement with JRC. There is currently no dedicated existing EU binding instrument on soil and the implementation and monitoring of the Directive are therefore new responsabilities for the Commission and the Member States. This requires additional resources with high capacity of political judgement, policy knowledge, analytical skills, independence and resilience throughout the long-term implementation of the legislation. Additional expert support will be equally needed, also through outsourcing, where "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The implementation of the new Directive will entail new tasks and activities for the")
    thisalinea.textcontent.append("Commission. This will require human resources, EEA support, procurement")
    thisalinea.textcontent.append("resources for external contractors and one or more administrative arrangement with")
    thisalinea.textcontent.append("JRC.")
    thisalinea.textcontent.append("There is currently no dedicated existing EU binding instrument on soil and the")
    thisalinea.textcontent.append("implementation and monitoring of the Directive are therefore new responsabilities")
    thisalinea.textcontent.append("for the Commission and the Member States.")
    thisalinea.textcontent.append("This requires additional resources with high capacity of political judgement, policy")
    thisalinea.textcontent.append("knowledge, analytical skills, independence and resilience throughout the long-term")
    thisalinea.textcontent.append("implementation of the legislation. Additional expert support will be equally needed,")
    thisalinea.textcontent.append("also through outsourcing, where possible, but core tasks that involve a high degree of")
    thisalinea.textcontent.append("political sensitivity need to be carried out by the Commission.")
    thisalinea.textcontent.append("7")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "1.6. Duration and financial impact of the proposal/initiative"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 391
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = " limited duration  unlimited duration –  in effect from [DD/MM]YYYY to [DD/MM]YYYY –  Financial impact from YYYY to YYYY for commitment appropriations and from YYYY to YYYY for payment appropriations. – Implementation with a start-up period corresponding to the transposition period of 2 years – followed by full-scale operation. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" limited duration")
    thisalinea.textcontent.append(" unlimited duration")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  in effect from [DD/MM]YYYY to [DD/MM]YYYY "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 392
    thisalinea.parentID = 391
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  in effect from [DD/MM]YYYY to [DD/MM]YYYY "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  in effect from [DD/MM]YYYY to [DD/MM]YYYY")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  Financial impact from YYYY to YYYY for commitment appropriations and ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 393
    thisalinea.parentID = 391
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  Financial impact from YYYY to YYYY for commitment appropriations and from YYYY to YYYY for payment appropriations. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  Financial impact from YYYY to YYYY for commitment appropriations and")
    thisalinea.textcontent.append("from YYYY to YYYY for payment appropriations.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– Implementation with a start-up period corresponding to the transposition period of ..."
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 394
    thisalinea.parentID = 391
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "– Implementation with a start-up period corresponding to the transposition period of 2 years "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– Implementation with a start-up period corresponding to the transposition period of")
    thisalinea.textcontent.append("2 years")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– followed by full-scale operation. "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 395
    thisalinea.parentID = 391
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
    thisalinea.texttitle = "1.7. Method(s) of budget implementation planned"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 396
    thisalinea.parentID = 355
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 6
    thisalinea.summary = " Direct management by the Commission  Shared management with the Member States  Indirect management by entrusting budget implementation tasks to: Comments N/A 8 –  by its departments, including by its staff in the Union delegations; –  by the executive agencies –  third countries or the bodies they have designated; –  international organisations and their agencies (to be specified); –  the EIB and the European Investment Fund; – bodies referred to in Articles 70 and 71 of the Financial Regulation; –  public law bodies; –  bodies governed by private law with a "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append(" Direct management by the Commission")
    thisalinea.textcontent.append(" Shared management with the Member States")
    thisalinea.textcontent.append(" Indirect management by entrusting budget implementation tasks to:")
    thisalinea.textcontent.append("Comments")
    thisalinea.textcontent.append("N/A")
    thisalinea.textcontent.append("8")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  by its departments, including by its staff in the Union delegations; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 397
    thisalinea.parentID = 396
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "–  by its departments, including by its staff in the Union delegations; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  by its departments, including by its staff in the Union delegations;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  by the executive agencies "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 398
    thisalinea.parentID = 396
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "–  by the executive agencies "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  by the executive agencies")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  third countries or the bodies they have designated; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 399
    thisalinea.parentID = 396
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
    thisalinea.nativeID = 400
    thisalinea.parentID = 396
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
    thisalinea.texttitle = "–  the EIB and the European Investment Fund; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 401
    thisalinea.parentID = 396
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 4
    thisalinea.summary = "–  the EIB and the European Investment Fund; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("–  the EIB and the European Investment Fund;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "– bodies referred to in Articles 70 and 71 of the Financial Regulation; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 402
    thisalinea.parentID = 396
    thisalinea.alineatype = texttype.ENUMERATION
    thisalinea.enumtype = enum_type.SIGNMARK
    thisalinea.horizontal_ordering = 5
    thisalinea.summary = "– bodies referred to in Articles 70 and 71 of the Financial Regulation; "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("– bodies referred to in Articles 70 and 71 of the Financial Regulation;")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "–  public law bodies; "
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 403
    thisalinea.parentID = 396
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
    thisalinea.nativeID = 404
    thisalinea.parentID = 396
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
    thisalinea.nativeID = 405
    thisalinea.parentID = 396
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
    thisalinea.nativeID = 406
    thisalinea.parentID = 396
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
    thisalinea.nativeID = 407
    thisalinea.parentID = 0
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 43
    thisalinea.summary = "The initiative involves procurement, administrative arrangements with the JRC, and impact on the COM HR. Standard rules for this type of expenditure apply. N/A –cf. above. N/A –cf. above. N/A –cf. above. N/A –cf. above. 9 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.1. Monitoring and reporting rules"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 408
    thisalinea.parentID = 407
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "The initiative involves procurement, administrative arrangements with the JRC, and impact on the COM HR. Standard rules for this type of expenditure apply. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("The initiative involves procurement, administrative arrangements with the JRC, and")
    thisalinea.textcontent.append("impact on the COM HR. Standard rules for this type of expenditure apply.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.2. Management and control system(s)"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 409
    thisalinea.parentID = 407
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "N/A –cf. above. N/A –cf. above. N/A –cf. above. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.1. Justification of the management mode(s), the funding implementation mechanism(s), the payment modalities and the control strategy proposed"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 410
    thisalinea.parentID = 409
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 0
    thisalinea.summary = "N/A –cf. above. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("N/A –cf. above.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = "2.2.2. Information concerning the risks identified and the internal control system(s) set up to mitigate them"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 411
    thisalinea.parentID = 409
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 1
    thisalinea.summary = "N/A –cf. above. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("N/A –cf. above.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 3
    thisalinea.texttitle = '2.2.3. Estimation and justification of the cost-effectiveness of the controls (ratio of "control costs ÷ value of the related funds managed"), and assessment of the expected levels of risk of error (at payment & at closure)'
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 412
    thisalinea.parentID = 409
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "N/A –cf. above. "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("N/A –cf. above.")
    alineas.append(thisalinea)

    thisalinea = textalinea()
    thisalinea.textlevel = 2
    thisalinea.texttitle = "2.3. Measures to prevent fraud and irregularities"
    thisalinea.titlefontsize = "12.0"
    thisalinea.nativeID = 413
    thisalinea.parentID = 407
    thisalinea.alineatype = texttype.HEADLINES
    thisalinea.enumtype = enum_type.UNKNOWN
    thisalinea.horizontal_ordering = 2
    thisalinea.summary = "N/A –cf. above. 9 "
    thisalinea.sum_CanbeEmpty = False
    thisalinea.textcontent.clear()
    thisalinea.textcontent.append("N/A –cf. above.")
    thisalinea.textcontent.append("9")
    alineas.append(thisalinea)

    return alineas
