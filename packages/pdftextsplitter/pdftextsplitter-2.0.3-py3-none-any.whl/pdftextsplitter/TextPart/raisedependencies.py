# Textpart imports:
from .textalinea import textalinea
from .masterrule import texttype

def raisedependencies_textsplitter(self):
    """
    Once the calculation of the tree structure is done, it is sometimes
    necessary to raise the cascade level of certain headlines, because
    they would otherwise end up as depencies of enumerations. This is
    what we do here. Of course, this does mean that afterwards,
    calculatetree has to be called a second time.
    
    # Parameters: None; taken from the textsplitter-class.
    # Return: None; stored inside the textalineas.
    """
    
    # ---------------------------------------------------------------------
    
    # If we have a chapter-title as a subitem of an enumeration, we must raise
    # the chapter-level:
    self.textalineas = sorted(self.textalineas, key=lambda x: x.nativeID, reverse=False)
    alineaindex = -1

    # Begin by looping over the array of textalineas:
    for alinea in self.textalineas:

        # Increase index:
        alineaindex = alineaindex + 1

        # Identify the current alinea:
        if (alinea.alineatype==texttype.HEADLINES):

            # Then, we search for its parent:
            if (alinea.parentID>=0)and(alinea.parentID<len(self.textalineas)):
                parentalinea = self.textalineas[alinea.parentID]

                # Then, ifentify if the parent is an enumeration:
                if (parentalinea.alineatype==texttype.ENUMERATION):

                    # If this is the case, continue finding parents until
                    # we end up with a headlines
                    thisindex = parentalinea.nativeID

                    while (thisindex>=0)and(thisindex<len(self.textalineas))and(parentalinea.textlevel>0)and(not(parentalinea.alineatype==texttype.HEADLINES)):
                        thisindex = parentalinea.parentID
                        parentalinea = self.textalineas[thisindex]

                    # So the while-loop ends when:
                    # 1) we can no longer find a valid parentID
                    # 2) we ended with the master-document-alinea
                    # 3) parent of parent of ... etc. is a headlines again.
                    # conditions 1 & 2 make sure the while-loop always ends and condition 3
                    # makes sure then when we exit, parentalinea will be the first headlines above alinea.

                    # So now we can adapt:
                    if (parentalinea.textlevel>0):

                        # Shift & calculate the level difference:
                        alinea_textlevel_old = alinea.textlevel
                        alinea.textlevel = parentalinea.textlevel+1
                        Level_difference = abs(alinea.textlevel - alinea_textlevel_old)

                        # And that is it. Other parts of the calculations are being taken
                        # care of once the calculatetree is re-executed.
