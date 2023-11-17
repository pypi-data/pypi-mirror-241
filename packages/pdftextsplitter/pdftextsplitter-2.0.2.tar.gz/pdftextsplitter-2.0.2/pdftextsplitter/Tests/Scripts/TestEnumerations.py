import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Imports from TextPart code:
sys.path.insert(1, '../../')
from TextPart.textsplitter import textsplitter
from TextPart.textalinea import textalinea

# Imports from Tools:
sys.path.insert(2, '../Tools/')
from AlineasPresent import AlineasPresent
from FileComparison import FileComparison

# Imports from Hardcodes:
sys.path.insert(3, '../Hardcodes/')
from Opsomming_hardcoded_content import hardcodedalineas_Opsomming
from Opsomming2_hardcoded_content import hardcodedalineas_Opsomming2
from Romans_hardcoded_content import hardcodedalineas_Romans
from RaiseCascades_hardcoded_content import hardcodedalineas_RaiseCascades
from Enums_Chapters_hardcoded_content import hardcodedalineas_Enums_Chapters
from Fiche_1pag_hardcoded_content import hardcodedalineas_Fiche_1pag

# Definition of paths:
inputpath = "../Inputs/"
outputpath = "../Calc_Outputs/"
truthpath = "../True_Outputs/"

def TestEnumerations_a(use_dummy_summary: bool) -> bool:
    """
    # Integration test for testing correct enumerations of the textsplitter-class:
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """
    
    # Run the textsplitter on the specific enumeration we like to test.
    # NOTE: This toy doc is specifically designed to provoke 1. versus 2.
    # chapter/enumeration discrepancies and artikel lid 1. 2. etc. situations.
    filename = "Opsomming"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("fgfghh")
    thetest.process()
    
    # Get the correct alineas:
    correctalineas = hardcodedalineas_Opsomming()
    
    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)
    
    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a integration test on Opsomming.pdf & pdfminer. It is supposed to fully pass!")
        print("\n")
    
    # Return the answer:
    return Answer

def TestEnumerations_b(use_dummy_summary: bool) -> bool:
    """
    # Integration test for testing roman/letter enumerations under h).
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """

    # Run the textsplitter on the specific enumeration we like to test.
    # NOTE: This toy doc is specifically designed to provoke 1. versus 2.
    # chapter/enumeration discrepancies and artikel lid 1. 2. etc. situations.
    filename = "Romans"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("dfgdfhgh")
    thetest.process()

    # Get the correct alineas:
    correctalineas = hardcodedalineas_Romans()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a integration test on Opsomming.pdf & pdfminer. It is supposed to fully pass!")
        print("\n")

    # Return the answer:
    return Answer

def TestEnumerations_c(use_dummy_summary: bool) -> bool:
    """
    # Integration test for testing correct enumerations of the textsplitter-class:
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """

    # Run the textsplitter on the specific enumeration we like to test.
    # NOTE: This toy doc is specifically designed to provoke 1. versus 2.
    # chapter/enumeration discrepancies and artikel lid 1. 2. etc. situations.
    filename = "Opsomming2"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("fgfghh")
    thetest.process()

    # Get the correct alineas:
    correctalineas = hardcodedalineas_Opsomming2()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a integration test on Opsomming.pdf & pdfminer. It is supposed to fully pass!")
        print("\n")

    # Return the answer:
    return Answer

def TestEnumerations_d(use_dummy_summary: bool) -> bool:
    """
    # Integration test for testing correct enumerations of the textsplitter-class:
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """

    # Run the textsplitter on the specific enumeration we like to test.
    # NOTE: This toy doc is specifically designed to provoke 1. versus 2.
    # chapter/enumeration discrepancies and artikel lid 1. 2. etc. situations.
    filename = "RaiseCascades"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("fgfghh")
    thetest.process()

    # Get the correct alineas:
    correctalineas = hardcodedalineas_RaiseCascades()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a integration test on Opsomming.pdf & pdfminer. It is supposed to fully pass!")
        print("\n")

    # Return the answer:
    return Answer

def TestEnumerations_e(use_dummy_summary: bool) -> bool:
    """
    # Integration test for testing correct enumerations of the textsplitter-class:
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """

    # Run the textsplitter on the specific enumeration we like to test.
    # NOTE: This toy doc is specifically designed to provoke 1. versus 2.
    # chapter/enumeration discrepancies and artikel lid 1. 2. etc. situations.
    filename = "Enums_Chapters"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("fgfghh")
    thetest.process()

    # Get the correct alineas:
    correctalineas = hardcodedalineas_Enums_Chapters()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a integration test on Opsomming.pdf & pdfminer. It is supposed to fully pass!")
        print("\n")

    # Return the answer:
    return Answer

def TestEnumerations_f(use_dummy_summary: bool) -> bool:
    """
    # Integration test for testing correct enumerations of the textsplitter-class:
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """

    # Run the textsplitter on the specific enumeration we like to test.
    # NOTE: This toy doc is specifically designed to provoke 1. versus 2.
    # chapter/enumeration discrepancies and artikel lid 1. 2. etc. situations.
    filename = "Fiche_1pag"
    thetest = textsplitter()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_outputpath(outputpath)
    thetest.standard_params()
    thetest.set_UseDummySummary(use_dummy_summary)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("fgfghh")
    thetest.process()

    # Get the correct alineas:
    correctalineas = hardcodedalineas_Fiche_1pag()

    # Compare whether we have the correct alineas:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Verify html-output:
    html_rapport = FileComparison(outputpath + filename + "_html_visualization.html", truthpath + filename + "_html_visualization.html","html")
    if not (html_rapport=="")and(use_dummy_summary==True):
        Answer = False
        print(" ==> HTML Comparison failed. Inspect the alinea-comparison and see if the true html should be adapted.")
        print(" ========== ATTENTION ===========> ")
        print("This is a integration test on Opsomming.pdf & pdfminer. It is supposed to fully pass!")
        print("\n")

    # Return the answer:
    return Answer

# Definition of collection:    
def TestEnumerations(use_dummy_summary: bool) -> bool:
    """
    # Collection-function of integration-tests.
    # Parameters: none; # Returns (bool): succes of the text.
    # use_dummy_summary: bool: decides whether we call ChatGPT to actually make summaries, or use a dummy summarization function.
    # Author: christiaan Douma
    """
    
    Answer = True

    if (TestEnumerations_a(use_dummy_summary)==False):
        Answer=False
        print('\n==> TestEnumerations_a failed!\n')

    if (TestEnumerations_b(use_dummy_summary)==False):
        Answer=False
        print('\n==> TestEnumerations_b failed!\n')

    if (TestEnumerations_c(use_dummy_summary)==False):
        Answer=False
        print('\n==> TestEnumerations_c failed!\n')

    if (TestEnumerations_d(use_dummy_summary)==False):
        Answer=False
        print('\n==> TestEnumerations_d failed!\n')

    if (TestEnumerations_e(use_dummy_summary)==False):
        Answer=False
        print('\n==> TestEnumerations_e failed!\n')

    if (TestEnumerations_f(use_dummy_summary)==False):
        Answer=False
        print('\n==> TestEnumerations_f failed!\n')

    return Answer

if __name__ == '__main__':

    # Identify parameters:
    use_dummy_summary = False

    if (len(sys.argv)>1):
        if (sys.argv[1]=="dummy"):
            use_dummy_summary = True

    if TestEnumerations(use_dummy_summary):
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
