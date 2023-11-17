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
from hardcodedalineas import hardcodedalineas_SplitDoc
from hardcodedalineas import hardcodedalineas_TestTex

# Definition of unit tests:
def TestTreeStructure_a() -> bool:
    """
    # Unit test for the calculatetree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestTreeStructure"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/either/")
    
    # Next, gather the alineas we want to calculate the tree structure for:
    thetest.textalineas = hardcodedalineas_SplitDoc("pdfminer")
    truealineas = hardcodedalineas_SplitDoc("pdfminer")
    # We call the same function twice, because we do not want python to create 2 
    # pointers to the same object, we really want 2 different objects.
    
    # Then, blind the parentID & horizontal ordering:
    for alinea in thetest.textalineas:
        alinea.parentID = -1
        alinea.horizontal_ordering = -1
        
    # Then, calculate the tree structure:
    thetest.calculatetree()
    
    # Next, see if we found the correct structure:
    index = 0
    Answer = True
    for alinea in thetest.textalineas:
        if not alinea.compare_samearray(truealineas[index]): # Because in these unit-tests we know we get exactly the correct parentID.
            Answer = False
            print(" ==> We calculated the wrong parentID ["+str(alinea.parentID)+"] or horizontal ordering ["+str(alinea.horizontal_ordering)+"] for the following alinea:")
            truealineas[index].printalinea()
        index = index + 1
  
    # Done:
    return Answer

def TestTreeStructure_b() -> bool:
    """
    # Unit test for the calculatetree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestTreeStructure"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/either/")
    
    # Next, gather the alineas we want to calculate the tree structure for:
    thetest.textalineas = hardcodedalineas_SplitDoc("pymupdf")
    truealineas = hardcodedalineas_SplitDoc("pymupdf")
    # We call the same function twice, because we do not want python to create 2 
    # pointers to the same object, we really want 2 different objects.
    
    # Then, blind the parentID & horizontal ordering:
    for alinea in thetest.textalineas:
        alinea.parentID = -1
        alinea.horizontal_ordering = -1
    
    # Then, calculate the tree structure:
    thetest.calculatetree()
    
    # Next, see if we found the correct structure:
    index = 0
    Answer = True
    for alinea in thetest.textalineas:
        if not alinea.compare_samearray(truealineas[index]):
            Answer = False
            print(" ==> We calculated the wrong parentID ["+str(alinea.parentID)+"] or horizontal ordering ["+str(alinea.horizontal_ordering)+"] for the following alinea:")
            truealineas[index].printalinea()
        index = index + 1
  
    # Done:
    return Answer

def TestTreeStructure_c() -> bool:
    """
    # Unit test for the calculatetree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestTreeStructure"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/either/")
    
    # Next, gather the alineas we want to calculate the tree structure for:
    thetest.textalineas = hardcodedalineas_TestTex("pdfminer")
    truealineas = hardcodedalineas_TestTex("pdfminer")
    # We call the same function twice, because we do not want python to create 2 
    # pointers to the same object, we really want 2 different objects.
    
    # Then, blind the parentID & horizontal ordering:
    for alinea in thetest.textalineas:
        alinea.parentID = -1
        alinea.horizontal_ordering = -1

    # Then, calculate the tree structure:
    thetest.calculatetree()
    
    # Next, see if we found the correct structure:
    index = 0
    Answer = True
    for alinea in thetest.textalineas:
        if not alinea.compare_samearray(truealineas[index]):
            Answer = False
            print(" ==> We calculated the wrong parentID ["+str(alinea.parentID)+"] or horizontal ordering ["+str(alinea.horizontal_ordering)+"] for the following alinea:")
            truealineas[index].printalinea()
        index = index + 1
  
    # Done:
    return Answer

def TestTreeStructure_d() -> bool:
    """
    # Unit test for the calculatetree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestTreeStructure"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/either/")
    
    # Next, gather the alineas we want to calculate the tree structure for:
    thetest.textalineas = hardcodedalineas_TestTex("pymupdf")
    truealineas = hardcodedalineas_TestTex("pymupdf")
    # We call the same function twice, because we do not want python to create 2 
    # pointers to the same object, we really want 2 different objects.
    
    # Then, blind the parentID & horizontal ordering:
    for alinea in thetest.textalineas:
        alinea.parentID = -1
        alinea.horizontal_ordering = -1
    
    # Then, calculate the tree structure:
    thetest.calculatetree()
    
    # Next, see if we found the correct structure:
    index = 0
    Answer = True
    for alinea in thetest.textalineas:
        if not alinea.compare_samearray(truealineas[index]):
            Answer = False
            print(" ==> We calculated the wrong parentID ["+str(alinea.parentID)+"] or horizontal ordering ["+str(alinea.horizontal_ordering)+"] for the following alinea:")
            truealineas[index].printalinea()
        index = index + 1
  
    # Done:
    return Answer

def TestTreeStructure_e() -> bool:
    """
    # Unit test for the calculatetree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Begin by creating a textsplitter:
    filename = "TestTreeStructure"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/either/")
    
    # Next, gather the alineas we want to calculate the tree structure for. This time, we do it without
    # the top-level alinea, so we know for sure that this works too.
    thetest.textalineas = hardcodedalineas_SplitDoc("pdfminer")
    thetest.textalineas.pop(0)
    truealineas = hardcodedalineas_SplitDoc("pdfminer")
    truealineas.pop(0)
    # We call the same function twice, because we do not want python to create 2 
    # pointers to the same object, we really want 2 different objects.
    
    # Then, blind the parentID & horizontal ordering:
    for alinea in thetest.textalineas:
        alinea.parentID = -1
        alinea.horizontal_ordering = -1
    
    # Then, calculate the tree structure:
    thetest.calculatetree()
    
    # Next, change parentID's in true alineas to the situation of the missing top-alinea:
    for alinea in truealineas:
        if (alinea.parentID==0):
            alinea.parentID = -1
        else:
            alinea.parentID = alinea.parentID - 1
    
    # Next, see if we found the correct structure:
    index = 0
    Answer = True
    for alinea in thetest.textalineas:
        if not alinea.compare_samearray(truealineas[index]): # Because in these unit-tests we know we get exactly the correct parentID.
            Answer = False
            print(" ==> We calculated the wrong parentID ["+str(alinea.parentID)+"] or horizontal ordering ["+str(alinea.horizontal_ordering)+"] for the following alinea:")
            truealineas[index].printalinea()
        index = index + 1
  
    # Done:
    return Answer

# Definition of unit tests:
def TestTreeStructure_f() -> bool:
    """
    # Unit test for the calculatefulltree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """

    # Begin by creating a textsplitter:
    filename = "TestTreeStructure"
    thetest = textsplitter()
    thetest.set_documentpath("/not/important/here/")
    thetest.set_documentname(filename)
    thetest.set_labelname(filename)
    thetest.set_outputpath("/not/important/either/")

    # Next, gather the alineas we want to calculate the tree structure for:
    thetest.textalineas = hardcodedalineas_SplitDoc("pdfminer")
    truealineas = hardcodedalineas_SplitDoc("pdfminer")
    # We call the same function twice, because we do not want python to create 2
    # pointers to the same object, we really want 2 different objects.

    # Then, blind the parentID & horizontal ordering:
    for alinea in thetest.textalineas:
        alinea.parentID = -1
        alinea.horizontal_ordering = -1

    # Then, calculate the tree structure:
    thetest.calculatefulltree()

    # Next, see if we found the correct structure:
    index = 0
    Answer = True
    for alinea in thetest.textalineas:
        if not alinea.compare_samearray(truealineas[index]): # Because in these unit-tests we know we get exactly the correct parentID.
            Answer = False
            print(" ==> We calculated the wrong parentID ["+str(alinea.parentID)+"] or horizontal ordering ["+str(alinea.horizontal_ordering)+"] for the following alinea:")
            truealineas[index].printalinea()
        index = index + 1

    # Done:
    return Answer

def TestTreeStructure() -> bool:
    """
    # Collection of unit test for the calculatetree-function of the textsplitter-class.
    # Parameters: none; # Returns (bool): succes of the text.
    # Author: christiaan Douma
    """
    
    # Declare the answer:
    Answer = True
    
    if not TestTreeStructure_a():
        Answer = False
        print("==> TestTreeStructure_a() failed!")
    
    if not TestTreeStructure_b():
        Answer = False
        print("==> TestTreeStructure_b() failed!")
    
    if not TestTreeStructure_c():
        Answer = False
        print("==> TestTreeStructure_c() failed!")
    
    if not TestTreeStructure_d():
        Answer = False
        print("==> TestTreeStructure_d() failed!")
    
    if not TestTreeStructure_e():
        Answer = False
        print("==> TestTreeStructure_e() failed!")

    if not TestTreeStructure_f():
        Answer = False
        print("==> TestTreeStructure_f() failed!")
    
    # Done:
    return Answer
    
if __name__ == '__main__':
    if TestTreeStructure():
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
