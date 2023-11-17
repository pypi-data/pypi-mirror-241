# Third-party imports:
from thefuzz import fuzz

# Textpart imports:
from .regex_expressions import contains_letter_signing
from .regex_expressions import contains_tablecontentsregex
from .regex_expressions import contains_sectionregex
from .regex_expressions import contains_chapterregex
from .regex_expressions import equals_artikelregex
from .regex_expressions import contains_pointh_enumeration
from .regex_expressions import contains_pointi_enumeration
from .regex_expressions import contains_pointii_enumeration
from .regex_expressions import contains_pointj_enumeration
from .regex_expressions import contains_pointI_enumeration
from .regex_expressions import contains_pointH_enumeration
from .regex_expressions import contains_pointII_enumeration
from .regex_expressions import contains_pointJ_enumeration
from .textalinea import textalinea
from .masterrule import texttype
from .enum_type import enum_type

def shiftcontents_textsplitter(self):
    """
    This function is meant to be called immendiately after breakdown
    and before calculating the tree structure (all member functions
    of textsplitter, just like this one). Some documents can contain
    structures that can only be corrected for, afterwards.

    An example is letters from politicians, which are then signed by
    their names. Without this function, the name of the politician would
    become a headlines-title with the content
    FOLLOWING their name. This is not correct for signed letters. As such,
    this function will take those situations and shift title/content
    to make sure that the right letters go to the right names.

    Another example is, if the code identifies headlines INSIDE the
    table of contents (TOC). As the titles inside the TOC match the ones
    in the document, the TOC will trigger regex, so only a small amount of
    style attributes are enough to also trigger them inside the TOC, which
    is not correct. In this section we correct for it.

    Also, the title of an enumeration may not have '...' in the end, while
    it should have those dots. This happens if the line has less words then
    the threshold, while it is followed by another line.
    
    # Parameters: None (taken from the class).
    # Return: none (stored in the class).
    
    """
    
    # --------------------------------------------------------------------------
    
    # Begin by sorting the array to nativeID (which is the same as their index):
    self.textalineas = sorted(self.textalineas, key=lambda x: x.nativeID, reverse=False)
    
    # Extract the length:
    alinealength = len(self.textalineas)

    # --------------------------------------------------------------------------

    # Correct for letters from politicians in the document:

    # Search the alineas for letter signings:
    Letter_Signings = []
    for alinea in self.textalineas:
        if contains_letter_signing(alinea.texttitle):
            Letter_Signings.append(alinea)
    
    # Next, we require that the LAST element of the letter signing has empty content.
    # If the document indeed contains letter signings, then the last signing
    # should always be followed by a new headline or other structural element,
    # leaving the last signing an empty alinea. This is not only a good check to
    # see when it is wise to fiddle with content/title combinations, but it will also
    # ensure that we have space to put the new content in.
    
    # Collect parameters:
    nr_signings = len(Letter_Signings)
    
    # Collect textual content:
    Textual_content = ""
    if (nr_signings>0):
        for textline in Letter_Signings[nr_signings-1].textcontent:
            Textual_content = Textual_content + textline
        
        # Prepare textual content:
        Textual_content = Textual_content.replace("\n","")
        Textual_content = Textual_content.replace(" ","")
        
    else:
        Textual_content = "We found no signings"
        # this will make sure the test does not pass; as should be the case here.
    
    # Make the test. If we do not pass; we will simply not do anything to the content:
    if (Textual_content==""):
        
        # Next, we will loop over the letter-signings in REVERSE order and put in the content
        # that belongs to the nativeID-1 element (provided it exist). We will then delete
        # the content of that element (making room for the next signing; due to reverse-looping).
        for index in range(nr_signings-1,-1,-1):
       
            # Check that we actually can access nativeID-1:
            ThisNativeID = Letter_Signings[index].nativeID
            if (ThisNativeID>0):
                
                # Loop over the textual content:
                textindex = 0
                for textline in self.textalineas[ThisNativeID-1].textcontent:
                    
                    # Insert the textual content of the previous item ABOVE the one of the current signing (so no text is lost):
                    Letter_Signings[index].textcontent.insert(textindex,textline)
                    if (textindex<len(self.textalineas[ThisNativeID-1].pagenumbers)):
                        Letter_Signings[index].pagenumbers.insert(textindex,self.textalineas[ThisNativeID-1].pagenumbers[textindex])
                    
                    # Update the textindex:
                    textindex = textindex + 1
                
                # Next, clear out the content of the previous alinea:
                self.textalineas[ThisNativeID-1].textcontent.clear()
                self.textalineas[ThisNativeID-1].pagenumbers.clear()
                
                # And, due to the reverse-looping: that should do it.

    # --------------------------------------------------------------------------

    # Sometimes, an enumeration (like TOC in AVERE) actually has to be a chapter:
    alinealength = len(self.textalineas)
    for k in range(0,alinealength-1):

        # Collect alineas:
        thisalinea = self.textalineas[k]
        nextalinea = self.textalineas[k+1]

        # Test that this is a digit-enumeration of a single line:
        if (thisalinea.alineatype==texttype.ENUMERATION):
            if (thisalinea.enumtype==enum_type.DIGIT):
                if (len(thisalinea.textcontent)==1):

                    # Test that the next one is a section:
                    if (nextalinea.alineatype==texttype.HEADLINES):
                        if (contains_sectionregex(nextalinea.texttitle)):

                            # This only happens in TOC, where we encounter the problem:
                            if (self.fontsize_equalstoregular(float(nextalinea.titlefontsize))==True):

                                # Calculate ratio of where we are in the document for structure elements:
                                structure_position_ratio = thisalinea.nativeID/alinealength

                                # Then, we only do this early in the document:
                                if (structure_position_ratio<0.3):

                                    # Then, thisalinea has to be changed to a chapter:
                                    thisalinea.texttitle = thisalinea.textcontent[0]
                                    thisalinea.textcontent.clear()
                                    thisalinea.alineatype = texttype.HEADLINES
                                    thisalinea.enumtype = enum_type.UNKNOWN
                                    thisalinea.textlevel = nextalinea.textlevel-1

    # --------------------------------------------------------------------------

    # Correct for misidentified chapter-titles in the TOC:
    TOC_Found = False
    alineaindex = -1

    # Begin by looping over the array of textalineas:
    for alinea in self.textalineas:

        # Increase index:
        alineaindex = alineaindex + 1

        # Begin by identifyting the TOC:
        if (contains_tablecontentsregex(alinea.texttitle))and(alinea.textlevel==1):
            TOC_Found = True

        # We only have to be concerned with the alineas AFTER identifying the TOC:
        if TOC_Found:

            # Then, loop over the remainder of the objects to see if
            # the alinea has a matching title somewhere further down
            # in the document:
            MatchFound = False
            MatchIndex = -1

            if (alineaindex<(alinealength-1)):
                for k in range(alineaindex+1,alinealength):

                    # Obtain fuzzy match between the titles:
                    firsttitles = []
                    firsttitles.append(alinea.texttitle)
                    firsttitles.append(firsttitles[0].replace(".",""))
                    firsttitles.append(firsttitles[1].replace("Chapter",""))

                    secondtitles = []
                    secondtitles.append(self.textalineas[k].texttitle)
                    secondtitles.append(secondtitles[0].replace(".",""))
                    secondtitles.append(secondtitles[1].replace("Chapter",""))

                    # Calculate all scenario's:
                    maxfuzzymatch = 0.0
                    for k1 in range(0,len(firsttitles)):
                        for k2 in range(0,len(secondtitles)):
                            thisfuzzymatch = fuzz.ratio(firsttitles[k1],secondtitles[k2])
                            if (thisfuzzymatch>maxfuzzymatch):
                                maxfuzzymatch = thisfuzzymatch

                    # Check if we found a match. NOTE: 88.0 is a very specific value (eu_space vs. thesis).
                    if (maxfuzzymatch>88.0)and(alinea.textlevel==self.textalineas[k].textlevel):
                        MatchFound = True
                        MatchIndex = k

            # If we found a match, then clearly we detected the same chapter twice.
            # However, we do not know in advance whether the first or the second one
            # is in the TOC.
            # So we will then increase the textlevel +1 for the TOC one; the one with
            # the smallerst textcontent, so it becomes a child of the TOC-element.
            if MatchFound:

                # Perform the shift:
                alinea.textlevel = alinea.textlevel+1
                alinea.typelevel = alinea.typelevel+1
                alinea.texttitle = alinea.texttitle.replace("..","")
                alinea.texttitle = alinea.texttitle.replace(". .","")

                # NOTE: as we have not yet calculated the tree structure & the statictics (layered_summary),
                # we have no good KPI's at this point to decide which one is larger. If a big checpter
                # has no introduction text but many sections, its content will be empty and the content
                # of its reference in TOC is not, so we would shift the wrong one.

                # Without taking the children along, it is impossible to decide who is the largest one,
                # so we HAVE to take the first one. As after we calculated the summaries, we can no longer
                # change the textlevels, as that would altre the tree structure, which would need a
                # re-summary. So this is the best we can do.

            # Done.

    # --------------------------------------------------------------------------

    # Sometimes, directly succeeding enumerations of the same type do not hold
    # the same cascadelevel, which is obviously wrong. We manually correct for this:

    # loop over all textalineas:
    alineaindex = -1
    alinealength = len(self.textalineas)
    for alinea in self.textalineas:

        # increase the index:
        alineaindex = alineaindex + 1

        # Test if it is an enumeration:
        if (alinea.alineatype==texttype.ENUMERATION):

            # Then, see if we have to add dots:
            if not ("..." in alinea.texttitle):
                if (len(alinea.textcontent)>1):

                    # Then, we have to add them:
                    alinea.texttitle = alinea.texttitle + "..."

            # Next, see if we have to adapt levels:
            if (alineaindex>0):
                if (self.textalineas[alineaindex-1].enumtype==alinea.enumtype):

                    # Check whether they have the same level:
                    if (alinea.textlevel!=self.textalineas[alineaindex-1].textlevel):

                        # Verify that we are not dealing with an h-i-j issue:
                        if (not((contains_pointi_enumeration(alinea.texttitle))or(contains_pointI_enumeration(alinea.texttitle)))):

                            # Adapt:
                            alinea.textlevel = self.textalineas[alineaindex-1].textlevel

                        else:

                            # Only adapt in case the order is indeed h-i-j:
                            if (alineaindex<(alinealength-1)):

                                if (contains_pointi_enumeration(alinea.texttitle))and(contains_pointj_enumeration(self.textalineas[alineaindex+1].texttitle))and(contains_pointh_enumeration(self.textalineas[alineaindex-1].texttitle)):
                                    alinea.textlevel = self.textalineas[alineaindex-1].textlevel

                                if (contains_pointI_enumeration(alinea.texttitle))and(contains_pointJ_enumeration(self.textalineas[alineaindex+1].texttitle))and(contains_pointH_enumeration(self.textalineas[alineaindex-1].texttitle)):
                                    alinea.textlevel = self.textalineas[alineaindex-1].textlevel

    # -------------------------------------------------------------------------

    # Fix articles that are not propely marked as such:
    alinealength = len(self.textalineas)
    for k in range(0,alinealength-1):

        # Collect alineas:
        thisalinea = self.textalineas[k]
        nextalinea = self.textalineas[k+1]

        # See if the first one ends in an article:
        if (len(thisalinea.textcontent)>0):
            if equals_artikelregex(thisalinea.textcontent[len(thisalinea.textcontent)-1]):

                # Check that the second one is indeed a chapter:
                if (nextalinea.alineatype==texttype.HEADLINES):

                    # Then, change it to an article:
                    nextalinea.texttitle = thisalinea.textcontent[len(thisalinea.textcontent)-1] + " " + nextalinea.texttitle
                    nextalinea.textlevel = 1
                    nextalinea.typelevel = 0
                    thisalinea.textcontent.pop(len(thisalinea.textcontent)-1)



