import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Imports from TextPart code:
sys.path.insert(1, '../../')
from TextPart.textpart import textpart

# Imports from Hardcodes:
sys.path.insert(3, '../Hardcodes/')
from hardcodedtextlines import hardcodedtextlines

# Definition of paths:
inputpath = "../Inputs/"
outputpath = "../Calc_Outputs/"
truthpath = "../True_Outputs/"

# Definition of unit tests:
def TestCalculateBoundaries_a() -> bool:
    """
    # Unit test for the calculate_footerboundaries-function of the textpart-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textpart:
    filename = "TestCalculateBoundaries"
    thetest = textpart()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath(outputpath)
    
    # Next, put everything in there hard-coded:
    thelines = hardcodedtextlines()
    thetest.textcontent.clear()
    thetest.positioncontent.clear()
    thetest.fontsize_perline.clear()
    thetest.whitelinesize.clear()
    
    # Loop over the hardcoded textlines:
    for oneline in thelines:
        thetest.textcontent.append(oneline.textline)
        thetest.positioncontent.append(oneline.vertical_position)
        thetest.pagenumbers.append(oneline.current_pagenumber)
        thetest.fontsize_perline.append(oneline.fontsize)
        thetest.is_bold.append(oneline.is_bold)
        thetest.is_italic.append(oneline.is_italic)
        thetest.is_highlighted.append(oneline.is_highlighted)
    
    # Then, execute the calculation-function:
    thetest.calculate_footerboundaries(0)

    # Then, see if we calculated the proper answers:
    Answer = True
    if (abs(thetest.headerboundary-626.5052555999999)>1e-3): Answer = False
    if (abs(thetest.footerboundary-38.14725560000004)>1e-3): Answer = False

    if not Answer:
        print(" Headerboundary = " + str(thetest.headerboundary) + " which should have been: 626.5052555999999")
        print(" Footerboundary = " + str(thetest.footerboundary) + " which should have been: 38.14725560000004")
        print(" Range = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")
    
    # Done:
    return Answer

# Definition of unit tests:
def TestCalculateBoundaries_b() -> bool:
    """
    # Unit test for the calculate_footerboundaries-function of the textpart-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textpart:
    filename = "Kamerbrief_1pag"
    thetest = textpart()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath(outputpath)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("sjkhfjh")

    # Read the document and calculate the boundaries:
    thetest.textgeneration("pdfminer")
    thetest.calculate_footerboundaries(1)

    # Then, see if we calculated the proper answers:
    Answer = True
    if (abs(thetest.headerboundary-700.0592876960001)>1e-3): Answer = False
    if (abs(thetest.footerboundary-28.45747069600004)>1e-3): Answer = False

    if not Answer:
        print(" Headerboundary = " + str(thetest.headerboundary) + " which should have been: 626.5052555999999")
        print(" Footerboundary = " + str(thetest.footerboundary) + " which should have been: 38.14725560000004")
        print(" Range = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")

    # Done:
    return Answer

# Definition of unit tests:
def TestCalculateBoundaries_c() -> bool:
    """
    # Unit test for the calculate_footerboundaries-function of the textpart-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textpart:
    filename = "Fiche_1pag"
    thetest = textpart()
    thetest.set_documentpath(inputpath)
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath(outputpath)
    thetest.set_ruleverbosity(1)
    thetest.set_verbosetextline("sjkhfjh")

    # Read the document and calculate the boundaries:
    thetest.textgeneration("pdfminer")
    thetest.calculate_footerboundaries(0)

    # Then, see if we calculated the proper answers:
    Answer = True
    if (abs(thetest.headerboundary-761.198572239)>1e-3): Answer = False
    if (abs(thetest.footerboundary-36.45264123900007)>1e-3): Answer = False

    if not Answer:
        print(" Headerboundary = " + str(thetest.headerboundary) + " which should have been: 626.5052555999999")
        print(" Footerboundary = " + str(thetest.footerboundary) + " which should have been: 38.14725560000004")
        print(" Range = [" + str(thetest.min_vert) + "," + str(thetest.max_vert) + "]")

    # Done:
    return Answer
    
# Definition of collection:
def TestCalculateBoundaries() -> bool:
    """
    # Collection-function of unit-tests.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: Christiaan Douma
    """

    # Declare the answer:
    Answer = True

    # Go over the cases:
    if not TestCalculateBoundaries_a():
        Answer = False
        print('TestCalculateBoundaries_a() failed!')

    if not TestCalculateBoundaries_b():
        Answer = False
        print('TestCalculateBoundaries_b() failed!')

    if not TestCalculateBoundaries_c():
        Answer = False
        print('TestCalculateBoundaries_c() failed!')

    # Return the answer:
    return Answer

if __name__ == '__main__':
    if TestCalculateBoundaries():
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
