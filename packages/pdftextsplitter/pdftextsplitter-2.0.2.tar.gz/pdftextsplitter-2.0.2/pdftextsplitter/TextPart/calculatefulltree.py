# Textpart imports:
from .textalinea import textalinea
from .masterrule import texttype

def calculatefulltree_textsplitter(self):
    """
    This function will repeat calculatetree and raisedependenies
    over and over until raisedependenies will no longer make any
    changes to the data. This is the only way to know for sure that
    we are done with raising dependencies.
    
    # Parameters: None; taken from the textsplitter-class.
    # Return: None; stored inside the textalineas.
    """
    
    # ---------------------------------------------------------------------
    
    # Begin by declaring the condition:
    Recalculate_tree = True
    while_index = 0

    # initiate the while-loop:
    while (Recalculate_tree)and(while_index<10):

        # Begin by collecting all textlevels:
        initial_textlevels = []
        for alinea in self.textalineas:
            initial_textlevels.append(alinea.textlevel)

        # Then, calculate the tree:
        self.calculatetree()

        # Next, raise the dependencies:
        self.raisedependencies()

        # recollect the textlevels:
        final_textlevels = []
        for alinea in self.textalineas:
            final_textlevels.append(alinea.textlevel)

        # Now, find out if the two arrays are the same:
        Arrays_are_equal = True
        if not (len(initial_textlevels)==len(final_textlevels)): Arrays_are_equal = False
        else:
            for k in range(0,len(initial_textlevels)):
                if not (initial_textlevels[k]==final_textlevels[k]):
                    Arrays_are_equal = False

        # So now adapt the condition for the while-loop:
        if Arrays_are_equal:
            Recalculate_tree = False

        # Increase index; it should not be necessary, but we take a safety precaution:
        while_index = while_index + 1
