import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Imports from TextPart code:
sys.path.insert(1, '../../')
from TextPart.textsplitter import textsplitter
from TextPart.textalinea import textalinea
from TextPart.fontregion import fontregion
from TextPart.masterrule import texttype
from TextPart.enum_type import enum_type

# Imports from Tools:
sys.path.insert(2, '../Tools/')
from AlineasPresent import AlineasPresent

# Imports from Hardcodes:
sys.path.insert(3, '../Hardcodes/')
from hardconedalineas_shifting import hardcodedalineas_Signings_Correct
from hardconedalineas_shifting import hardcodedalineas_Signings_Wrong
from Opsomming_wrongcascades_hardcoded_content import hardcodedalineas_Opsomming_wrongcascades
from Opsomming_wrongcascades2_hardcoded_content import hardcodedalineas_Opsomming_wrongcascades2
from Opsomming_wrongarticles_hardcoded_content import hardcodedalineas_Opsomming_wrongarticles
from Opsomming_wrongarticles_hardcoded_content import hardcodedalineas_Opsomming_wrongarticles_corrected
from Enums_Chapters_hardcoded_content import hardcodedalineas_Enums_Chapters
from hardcodedalineas import hardcodedalineas_SplitDoc

# Definition of paths:
inputpath = "../Inputs/"
outputpath = "../Calc_Outputs/"
truthpath = "../True_Outputs/"

# Definition of unit tests:
def TestShifting_a() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestShifting"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    thetest.set_labelname("TestShifting")
    
    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_Signings_Wrong()
    
    # Execute the shift:
    thetest.shiftcontents()
    
    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_Signings_Correct()
    Answer = AlineasPresent(correctalineas,thetest.textalineas)
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
  
    # Done:
    return Answer

# Definition of unit tests:
def TestShifting_b() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestShifting"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    thetest.set_labelname("TestShifting")
    
    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_SplitDoc("pdfminer")

    # Now, manually put back the two subtitles in the TOC:
    thetest.textalineas[4].textlevel = 1
    thetest.textalineas[5].textlevel = 1
    
    # Execute the shift (which, for these alineas, should counteract those effects):
    thetest.shiftcontents()
    
    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_SplitDoc("pdfminer")
    Answer = AlineasPresent(correctalineas,thetest.textalineas)
    
    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")
  
    # Done:
    return Answer

# Definition of unit tests:
def TestShifting_c() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textsplitter:
    filename = "TestShifting"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    thetest.set_labelname("TestShifting")

    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_Opsomming_wrongcascades()

    # Blind out parentID's; we are not supposed to know these:
    for alinea in thetest.textalineas:
        alinea.parentID = -1

    # Next, execute the shift, which should but all at cascade level 2:
    thetest.shiftcontents()

    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_Opsomming_wrongcascades()

    # Blind out parentID's and give correct cascades:
    for alinea in correctalineas:
        alinea.parentID = -1
        if (alinea.textlevel>2):
            alinea.textlevel = 2

    # then, compare:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Done:
    return Answer

# Definition of unit tests:
def TestShifting_d() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textsplitter:
    filename = "TestShifting"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    thetest.set_labelname("TestShifting")

    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_Opsomming_wrongcascades2()

    # Blind out parentID's; we are not supposed to know these:
    for alinea in thetest.textalineas:
        alinea.parentID = -1

    # Next, execute the shift, which should but all at cascade level 2:
    thetest.shiftcontents()

    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_Opsomming_wrongcascades2()

    # Blind out parentID's and give correct cascades:
    for alinea in correctalineas:
        alinea.parentID = -1
        if (alinea.textlevel>2):
            alinea.textlevel = 2

    # then, compare:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Done:
    return Answer

# Definition of unit tests:
def TestShifting_e() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textsplitter:
    filename = "TestShifting"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    thetest.set_labelname("TestShifting")

    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_Opsomming_wrongarticles()

    # Blind out parentID's; we are not supposed to know these:
    for alinea in thetest.textalineas:
        alinea.parentID = -1

    # Next, execute the shift, which should put everything in cascade level 1.
    thetest.shiftcontents()

    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_Opsomming_wrongarticles_corrected()

    # Blind out parentID's there as well:
    for alinea in correctalineas:
        alinea.parentID = -1

    # then, compare:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Done:
    return Answer

# Definition of unit tests:
def TestShifting_f() -> bool:
    """
    # Unit test for the shiftcontent-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textsplitter:
    filename = "TestShifting"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/here/")
    thetest.set_labelname("TestShifting")

    # Next, put in the alineas hardcoded:
    thetest.textalineas = hardcodedalineas_Enums_Chapters()

    # Change the first title to an enumeration:
    thetest.textalineas[1].texttitle = "1. Dit wordt dus eerst als opsomming herkent, maar moet een hoofdstuk worden."
    thetest.textalineas[1].textcontent.append("1. Dit wordt dus eerst als opsomming herkent, maar moet een hoofdstuk worden.")
    thetest.textalineas[1].alineatype = texttype.ENUMERATION
    thetest.textalineas[1].enumtype = enum_type.DIGIT

    # We also require a fontregion in this case:
    thetest.fontregions.append(fontregion())
    thetest.fontregions[0].left = 8.0
    thetest.fontregions[0].right = 12.0
    thetest.fontregions[0].value = 10.0
    thetest.fontregions[0].frequency = 0.9
    thetest.fontregions[0].cascadelevel = 5
    thetest.fontregions[0].isregular = True

    # Next, execute the shift, which should put everything above back:
    thetest.shiftcontents()

    # Then, compare to what it should be:
    correctalineas = hardcodedalineas_Enums_Chapters()

    # then, compare:
    Answer = AlineasPresent(correctalineas,thetest.textalineas)

    # Check whether we have the correct number of alineas:
    if not (len(correctalineas)==len(thetest.textalineas)):
        Answer = False
        print("The code found some additional structure-elements that were not supposed to be found!")

    # Done:
    return Answer
    
# Definition of collection:
def TestShifting() -> bool:
    """
    # Collection-function of unit-tests.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: Christiaan Douma
    """
    
    # Declare the answer:
    Answer = True
    
    # Go over the cases:
    if not TestShifting_a():
        Answer = False
        print('TestShifting_a() failed!')

    if not TestShifting_b():
        Answer = False
        print('TestShifting_b() failed!')

    if not TestShifting_c():
        Answer = False
        print('TestShifting_c() failed!')

    if not TestShifting_d():
        Answer = False
        print('TestShifting_d() failed!')

    if not TestShifting_e():
        Answer = False
        print('TestShifting_e() failed!')

    if not TestShifting_f():
        Answer = False
        print('TestShifting_f() failed!')

    # Return the answer:
    return Answer

if __name__ == '__main__':
    if TestShifting():
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
