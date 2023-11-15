import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Imports from TextPart code:
sys.path.insert(1, '../../')
from TextPart.textsplitter import textsplitter
from TextPart.textalinea import textalinea

# Imports from Tools:
sys.path.insert(2, '../Tools/')
from FileComparison import FileComparison
from AlineasPresent import AlineasPresent

# Imports from Hardcodes:
sys.path.insert(3, '../Hardcodes/')
from cellar_hardcoded_content import hardcodedalineas_cellar
from Copernicus_hardcoded_content import hardcodedalineas_Copernicus
from Plan_Velo_FR_hardcoded_content import hardcodedalineas_Plan_Velo_FR
from Christiaan_PhD_Thesis_hardcoded_content import hardcodedalineas_Christiaan_PhD_Thesis
from Burgerlijk_wetboek_deel_1_hardcoded_content import hardcodedalineas_Burgerlijk_wetboek_deel_1
from EU_soil_proposal_hardcoded_content import hardcodedalineas_EU_soil_proposal
from Kamerbrief_emissie_luchtvaart_hardcoded_content import hardcodedalineas_Kamerbrief_emissie_luchtvaart
from Kamerbrief_circulaire_economie_hardcoded_content import hardcodedalineas_Kamerbrief_circulaire_economie
from Kamerbrief_innovatie_missie_hardcoded_content import hardcodedalineas_Kamerbrief_innovatie_missie
from Kamerbrief_water_en_Bodem_hardcoded_content import hardcodedalineas_Kamerbrief_water_en_Bodem
from AVERE_hardcoded_content import hardcodedalineas_AVERE
from eu_space_hardcoded_content import hardcodedalineas_eu_space
from CADouma_DNN_Publication_hardcoded_content import hardcodedalineas_CADouma_DNN_Publication
from STEP_hardcoded_content import hardcodedalineas_STEP
from BNC_Fiche_hardcoded_content import hardcodedalineas_BNC_Fiche
from AI_Impact_hardcoded_content import hardcodedalineas_AI_Impact

# Definition of paths:
inputpath = "../Regressie/"
outputpath = "../Calc_Outputs/"
truthpath = "../True_Outputs/"

# Definition of Regression tests:
def RegressionTest_a(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (58 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "Copernicus"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("jfhjhfjhs")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Copernicus()
    
    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not ((thetest.footerboundary<55.0)and(thetest.footerboundary>50.0)): Answer = False
    if not (thetest.headerboundary>thetest.max_vert): Answer = False

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary) + ", which should be close to 1000.0")
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary) + ", which should be close to   55.0")
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
        
    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True): 
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Copernicus.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")
    
    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_b(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "cellar"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("jfhjhfjhs")
    thetest.set_LanguageChoice("Dutch")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_cellar()
    
    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not ((thetest.footerboundary<40.0)and(thetest.footerboundary>thetest.min_vert)): Answer = False
    if not (thetest.headerboundary>thetest.max_vert): Answer = False

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary) + ", which should be close to 1000.0")
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary) + ", which should be close to   55.0")
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
        
    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on cellar.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")
    
    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_c(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "Plan_Velo_FR"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("sjhfkjhf")
    thetest.set_LanguageChoice("Dutch")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Plan_Velo_FR()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 21.0):
    if not ((thetest.footerboundary<22.0)and(thetest.footerboundary>thetest.min_vert)): Answer = False
    if not (thetest.headerboundary>thetest.max_vert): Answer = False

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary) + ", which should be close to 1000.0")
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary) + ", which should be close to   21.0")
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
        
    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True): 
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Plan_Velo_FR.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")
    
    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_d(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "eu_space"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("sjfkj")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_eu_space()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on eu_space.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_e(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "CADouma_DNN_Publication"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dskjfkj")
    thetest.set_LanguageChoice("Dutch")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_CADouma_DNN_Publication()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on CADouma_DNN_Publication.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_f(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "STEP"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dfsgdfdf")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_STEP()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on STEP.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_g(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "AVERE"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dfdgdg")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")

    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_AVERE()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on AVERE.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_h(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "EU_soil_proposal"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dsfkjfdjbhf")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_EU_soil_proposal()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas.
    # NOTE: In this case we will not do that, as we deliberately do not test
    # on the last piece of the framework, as that piece contains a lot of tables which we do not have functionality for yet.

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on EU_soil_proposal.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_i(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "Kamerbrief_circulaire_economie"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dfghdfth")
    thetest.set_LanguageChoice("Dutch")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Kamerbrief_circulaire_economie()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if not thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is supposed to be a KAMERBRIEF!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Kamerbrief_circulaire_economie.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_j(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "Kamerbrief_emissie_luchtvaart"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("shjhfj")
    thetest.set_LanguageChoice("Dutch")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Kamerbrief_emissie_luchtvaart()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if not thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is supposed to be a KAMERBRIEF!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Lamerbrief_emissie_luchtvaart.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_k(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "Kamerbrief_innovatie_missie"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dggdfsfg")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Kamerbrief_innovatie_missie()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if not thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is supposed to be a KAMERBRIEF!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Kamerbrief_innovatie_missie.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_l(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "Kamerbrief_water_en_Bodem"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dxdsggdfsg")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Kamerbrief_water_en_Bodem()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if not thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is supposed to be a KAMERBRIEF!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Kamerbrief_water_en_Bodem.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_m(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "BNC_Fiche"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dfsgdsrgg")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_BNC_Fiche()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if not thetest.is_fiche:
        Answer = False
        print(" ==> This document is supposed to be a BNC-FICHE!!!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on BNC_Fiche.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_n(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """

    filename = "AI_Impact"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("fgghfh")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_AI_Impact()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual = 1000.0 & 55.0):
    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary))
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary))
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on CADouma_DNN_Publication.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")

    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_t(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "Christiaan PhD Thesis"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dfrgrdg")
    thetest.set_LanguageChoice("English")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")

    # Import the correct alineas:
    correctalineas = hardcodedalineas_Christiaan_PhD_Thesis()
    
    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manual determined at 625.0 & 40.0):
    if not ((thetest.footerboundary<40.0)and(thetest.footerboundary>thetest.min_vert)): Answer = False
    if not ((thetest.headerboundary>625.0)and(thetest.headerboundary<thetest.max_vert)): Answer = False

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary) + ", which should be close to  625.0")
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary) + ", which should be close to   40.0")
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False
    
    # Check whether we have the correct number of alineas.
    # NOTE: In this case we will not do that, as we deliberately do not test
    # on the list of figures, tables, etc. There is too much complicated
    # stuff in there to try to make sense of it. It will hold future improvements back.
        
    # Next, verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True): 
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a regressiontest on Christiaan PhD Thesis.pdf. It is supposed to fully pass!")
        print("If not, this means that more is going on then just a wrong html-visualization!")
        print("\n")
    
    # Done:
    return Answer

# Definition of Regression tests:
def RegressionTest_w(use_dummy_summary: bool) -> bool:
    """
    # Regression test for documentsplitting using the textsplitter-class (383 calls).
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    
    filename = "Burgerlijk wetboek deel 1"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("jdhdj")
    thetest.set_LanguageChoice("Dutch")
    thetest.set_LanguageModel("gpt-3.5-turbo")
    thetest.process()
    print(" =====> " + str(thetest.callcounter) + " calls counted.")
    
    # Import the correct alineas:
    correctalineas = hardcodedalineas_Burgerlijk_wetboek_deel_1()
    
    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Test whether it is a kamerbrief:
    if thetest.is_kamerbrief:
        Answer = False
        print(" ==> This document is not supposed to be a kamerbrief!")

    # Test whether it is a BNC-Fiche:
    if thetest.is_fiche:
        Answer = False
        print(" ==> This document is not supposed to be a BNC-Fiche!")

    # Check whether we obtain the correct header/footer boundaries (manually determined at 1000.0 & -100.0):
    if not (thetest.footerboundary<thetest.min_vert): Answer = False
    if not (thetest.headerboundary>thetest.max_vert): Answer = False

    if not Answer:
        print("For " + filename + " we obtained headerboundary = " + str(thetest.headerboundary) + ", which should be close to 1000.0")
        print("For " + filename + " we obtained footerboundary = " + str(thetest.footerboundary) + ", which should be close to -100.0")
        print("For " + filename + " the full range of position = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
        Answer = False
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
    
    # Note: This one has thousands of structural elements. Comapring html-files
    # would be too expensive in terms of CPU-power. We skip it.
    
    # Done:
    return Answer
    
# Definition of collection:    
def RegressionTests(use_dummy_summary: bool) -> bool:
    """
    # Collection-function of Regression-tests.
    # Parameters:
    use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Return: bool: the success of the test.
    # Author: christiaan Douma
    """
    # ------------------------------------------------------

    # Declare Answers:
    Copernicus_status = False
    cellar_status = False
    Plan_Velo_FR_Status = False
    eu_space_status = False
    CADouma_DNN_Publication_status = False

    STEP_status = False
    AVERE_status = False
    EU_soil_proposal_status = False
    Kamerbrief_circulaire_economie_status = False
    Kamerbrief_emissie_luchtvaart_status = False

    Kamerbrief_innovatie_missie_status = False
    Kamerbrief_water_en_Bodem_status = False
    BNC_Fiche_status = False
    AI_Impact_status = False
    Christiaan_PhD_Thesis_status = False

    Burgerlijk_wetboek_deel_1_status = False

    # ------------------------------------------------------

    # Perform regression tests:

    #"""
    Copernicus_status = RegressionTest_a(use_dummy_summary)
    print("Coperninus; RegressionTest_a()...")
    cellar_status = RegressionTest_b(use_dummy_summary)
    print("cellar; RegressionTest_b()...")
    Plan_Velo_FR_Status = RegressionTest_c(use_dummy_summary)
    print("Plan_Velo_FR; RegressionTest_c()...")
    eu_space_status = RegressionTest_d(use_dummy_summary)
    print("eu_space; RegressionTest_d()...")
    CADouma_DNN_Publication_status = RegressionTest_e(use_dummy_summary)
    print("CADouma_DNN_Publication; RegressionTest_e()...")

    STEP_status = RegressionTest_f(use_dummy_summary)
    print("STEP; RegressionTest_f()...")
    AVERE_status = RegressionTest_g(use_dummy_summary)
    print("AVERE; RegressionTest_g()...")
    EU_soil_proposal_status = RegressionTest_h(use_dummy_summary)
    print("EU_soil_proposal; RegressionTest_h()...")
    Kamerbrief_circulaire_economie_status = RegressionTest_i(use_dummy_summary)
    print("Kamerbrief_circulaire_economie; RegressionTest_i()...")
    Kamerbrief_emissie_luchtvaart_status = RegressionTest_j(use_dummy_summary)
    print("Kamerbrief_emissie_luchtvaart; RegressionTest_j()...")

    Kamerbrief_innovatie_missie_status = RegressionTest_k(use_dummy_summary)
    print("Kamerbrief_innovatie_missie; RegressionTest_k()...")
    Kamerbrief_water_en_Bodem_status = RegressionTest_l(use_dummy_summary)
    print("Kamerbrief_water_en_Bodem; RegressionTest_l()...")
    BNC_Fiche_status = RegressionTest_m(use_dummy_summary)
    print("BNC_Fiche; RegressionTest_m()...")
    AI_Impact_status = RegressionTest_n(use_dummy_summary)
    print("AI_Impact; RegressionTest_n()...")
    Christiaan_PhD_Thesis_status = RegressionTest_t(use_dummy_summary)
    print("Christiaan PhD Thesis; RegressionTest_t()...")

    Burgerlijk_wetboek_deel_1_status = RegressionTest_w(use_dummy_summary)
    print("Burgerlijk wetboek deel 1; RegressionTest_w()...")
    #"""

    # ------------------------------------------------------

    # Give status rapport:
    print("\n\n ========== REGRESSION TEST RAPPORT ============")
    print("Copernicus (a)                     = " + str(Copernicus_status))
    print("cellar (b)                         = " + str(cellar_status))
    print("Plan_Velo_FR (c)                   = " + str(Plan_Velo_FR_Status))
    print("eu_space (d)                       = " + str(eu_space_status))
    print("CADouma_DNN_Publication (e)        = " + str(CADouma_DNN_Publication_status))

    print("STEP (f)                           = " + str(STEP_status))
    print("AVERE (g)                          = " + str(AVERE_status))
    print("EU_soil_proposal (h)               = " + str(EU_soil_proposal_status))
    print("Kamerbrief_circulaire_economie (i) = " + str(Kamerbrief_circulaire_economie_status))
    print("Kamerbrief_emissie_luchtvaart (j)  = " + str(Kamerbrief_emissie_luchtvaart_status))

    print("Kamerbrief_innovatie_missie (k)    = " + str(Kamerbrief_innovatie_missie_status))
    print("Kamerbrief_water_en_Bodem (l)      = " + str(Kamerbrief_water_en_Bodem_status))
    print("BNC_Fiche (m)                      = " + str(BNC_Fiche_status))
    print ("AI_Impact_status (n)              = " + str(AI_Impact_status))
    print("Christiaan PhD Thesis (t)          = " + str(Christiaan_PhD_Thesis_status))

    print("Burgerlijk wetboek deel 1 (w)      = " + str(Burgerlijk_wetboek_deel_1_status))

    print("")
    # ------------------------------------------------------

    # Compose final answer:
    Answer = True

    if not Copernicus_status: Answer = False
    if not cellar_status: Answer = False
    if not Plan_Velo_FR_Status: Answer = False
    if not eu_space_status: Answer = False
    if not CADouma_DNN_Publication_status: Answer = False

    if not STEP_status: Answer = False
    if not AVERE_status: Answer = False
    if not EU_soil_proposal_status: Answer = False
    if not Kamerbrief_circulaire_economie_status: Answer = False
    if not Kamerbrief_emissie_luchtvaart_status: Answer = False

    if not Kamerbrief_innovatie_missie_status: Answer = False
    if not Kamerbrief_water_en_Bodem_status: Answer = False
    if not BNC_Fiche_status: Answer = False
    if not AI_Impact_status: Answer = False
    if not Christiaan_PhD_Thesis_status: Answer = False

    if not Burgerlijk_wetboek_deel_1_status: Answer = False
    # ------------------------------------------------------

    # Return answer:
    return Answer

if __name__ == '__main__':
    
    # Identify parameters:
    use_dummy_summary = False
    if (len(sys.argv)>1):
        if (sys.argv[1]=="dummy"):
            use_dummy_summary = True

    if RegressionTests(use_dummy_summary):
        print("Regression Test Succeeded!")
    else:
        print("\n==> Regression Test FAILED!!!\n")

        # Provide handle for git pipeline:
        exit(1)
