import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Imports from TextPart code:
sys.path.insert(1, '../../')
from TextPart.textsplitter import textsplitter
from TextPart.textalinea import textalinea

# Imports from Tools:
sys.path.insert(2, '../Tools/')
from AlineasPresent import AlineasPresent

# Imports from Hardcodes:
sys.path.insert(3, '../Hardcodes/')
from RaiseCascades_hardcoded_content import hardcodedalineas_RaiseCascades

# Definition of paths:
inputpath = "../Inputs/"
outputpath = "../Calc_Outputs/"
truthpath = "../True_Outputs/"

# Definition of unit tests:
def TestRaising_a() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestRaising"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    
    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_RaiseCascades()

    # Manually shift the cascade levels to obtain a headlines that
    # depends on an enumeration:
    thetest.textalineas[4].textlevel = 3
    thetest.textalineas[4].parentID = 3
    
    # Attempt to correct:
    thetest.raisedependencies()
    
    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_RaiseCascades()
    correctalineas[4].parentID = 3
    # Note that raisedependencies only corrects for cascades, not parents.

    # Make the comparison:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
  
    # Done:
    return Answer
    
# Definition of collection:
def TestRaising() -> bool:
    """
    # Collection-function of unit-tests.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: Christiaan Douma
    """
    
    # Declare the answer:
    Answer = True
    
    # Go over the cases:
    if not TestRaising_a():
        Answer = False
        print('TestRaising_a() failed!')
    
    # Return the answer:
    return Answer

if __name__ == '__main__':
    if TestRaising():
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
