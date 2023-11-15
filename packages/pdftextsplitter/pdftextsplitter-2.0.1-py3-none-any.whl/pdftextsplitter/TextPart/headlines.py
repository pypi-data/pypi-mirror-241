# Python functionality:
import re

# Package functionality:
from thefuzz import fuzz

# Textpart imports:
from .textpart import textpart
from .CurrentLine import CurrentLine
from .regex_expressions import remove_nonletters
from .regex_expressions import contains_artikelregex
from .regex_expressions import equals_artikelregex
from .regex_expressions import contains_chapterregex
from .regex_expressions import contains_sectionregex
from .regex_expressions import contains_subsectionregex
from .regex_expressions import contains_subsubsectionregex
from .regex_expressions import contains_tablecontentsregex
from .regex_expressions import contains_headlines_regex
from .regex_expressions import contains_headlines_nochapter_regex
from .regex_expressions import contains_bigroman_enumeration
from .regex_expressions import contains_smallroman_enumeration
from .regex_expressions import contains_bigletter_enumeration
from .regex_expressions import contains_smallletter_enumeration
from .regex_expressions import contains_digit_enumeration
from .regex_expressions import contains_signmark_enumeration
from .regex_expressions import contains_some_enumeration
from .enum_type import enum_type

class headlines(textpart):
    """
    This class is a specific textual element that inherits from textpart.
    It is meant to identify the headlines (chaper-tuiles, etc.) of a given document, using its
    own (overwritten) rule-function. All other functionality comes from 
    the parent-class.
    
    # For bold text: Plan_Velo:  41970 /13375 characters. ratio = 0.318680
    #                Cellar:    155903 / 1612 characters. ratio = 0.010340
    #                Copernicus: 16735 /  310 characters. ratio = 0.018524
    
    """

    # Definition of the default-constructor:
    def __init__(self):
        super().__init__() # First initiates all elements of textpart
        super().set_labelname("Headlines") # Then, change the label to reflext that this is about the headlines.
        self.hierarchy = []                # Duplicate of the same item in enumeration.
    
    # Definition of the specific headlines-rule that filters out the title:
    def rule(self, thisline: CurrentLine) -> tuple[bool,int]:
        """
        This function identifies headlines in the document, such as chapters, sections, etc.

        # Parameters: thisline: CurrentLine-object, an object holding all the needed information on the specific textline.
        # Returns: bool: whether the textline is a headline or not.
        # Returns: int: the textual level of the headline, if it is one (1-=chapter, 2=section, etc.)
        """

        # The standard-rules that assume there is no meta-data available:
        # We ONLY use headlines that match all three of the following conditions: 
        # 1) it is preceded by either another headline, or a large whiteline
        # 2) it is either bold/highlighted, or a large fontsize, or it has a large whiteline below.
        # 3) It contains sufficient textual characters.
        
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("--------------------------------------------------------------------")
            print(" ==> HEADLINES decision process for <" + str(thisline.textline) + ">")
        
        # Textual characters condition:
        Full_linelength = len(thisline.textline)
        pure_letters = remove_nonletters(thisline.textline)
        Nr_spaces = thisline.textline.count(" ")
        Letter_Length = len(pure_letters)
        Nospace_length = Full_linelength - Nr_spaces
        
        # Calculate ratio:
        letter_ratio = 1.0
        if (Nospace_length>0):
            letter_ratio = Letter_Length/Nospace_length
        Letter_condition = False
        if (letter_ratio>=0.60): # This threshold is a very specific value needed.
            Letter_condition = True
        
        # Now, if the fontsize is large, we do not need to worry about this:
        if self.fontsize_biggerthenregular(thisline.fontsize):
            Letter_condition = True
        
        # Pass Plan-Velo:
        if contains_signmark_enumeration(thisline.textline):
            Letter_condition = True
        
        # Prevent short-character titles:
        if (Full_linelength>=0)and(Full_linelength<=3):
            if (Full_linelength<=1):
                Letter_condition = False
            elif re.compile(r'^(\d+)$').search(thisline.textline):
                Letter_condition = False

        # Do not pass up on separate enumeration-marks:
        if (self.textextractionmethod=="pymupdf"):
            if re.compile(r'^(\d+)(\.)$').search(thisline.textline):
                Letter_condition = True

        # Eliminate titles with a lot of spaces:
        if (Full_linelength>0):
            if ((Nr_spaces/Full_linelength)>0.45):
                if not re.compile(r'^(\d+)(\ )(\d+) ').search(thisline.textline):
                    Letter_condition = False
        
        # Take care of single-digit starters & SOME of the big romans (if we do all, we hit other problems like with C.or D. chapter titles...)
        # NOTE: we cannot allow single-digits because that will screw up article 413 of civillian law.
        if re.compile(r'^(\d+)(\.)(\d+)(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^I(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^II(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^IV(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^V(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^VI(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^IX(\.)$').search(thisline.textline): Letter_condition = True
        if re.compile(r'^X(\.)$').search(thisline.textline): Letter_condition = True

        # Give some output to show the decision process:
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("Total number of characters in the line: " + str(Full_linelength))
            print("Number of spaces in the line:           " + str(Nr_spaces))
            print("Number of characters (no spaces):       " + str(Nospace_length))
            print("Number of pure letters in the line:     " + str(Letter_Length))
            print("Ratio for testing:                      " + str(letter_ratio))
            print("Full Letter Condition = " + str(Letter_condition))
            print("")
        
        # Condition above:
        Above_Condition = False
        if thisline.previous_IsHeadline: Above_Condition = True # preceded by another headline
        if self.whiteline_isbig(thisline.previous_whiteline): Above_Condition = True # preceded by a a large whiteline.
        if equals_artikelregex(thisline.previous_textline): Above_Condition = True # preceded by an artikcle.
        
        # However, if a new chapter accidentally starts at the top of the page, we must not dismiss it:
        if (Above_Condition==False)and(abs(thisline.vertical_position - self.headerboundary)<(0.5*self.findregularfontregion().get_value())):
            # Then, we want to allow this. But if the layout did not mark this line appropriately,
            # we must check the regex as additional safety:
            Above_Condition = False
            if (contains_tablecontentsregex(thisline.textline)): Above_Condition = True
            if (contains_headlines_regex(thisline.textline)): Above_Condition = True
            if (contains_some_enumeration(thisline.textline)): Above_Condition = True
            if self.fontsize_biggerthenregular(thisline.fontsize): Above_Condition = True
            # This is to make sure that we pass SplitDoc-tests.
        
        # If it is the top of the document:
        if (Above_Condition==False)and((abs(thisline.previous_whiteline+2.0)<1e-3)or(abs(thisline.previous_whiteline+1.0)<1e-3)):
            # Then, we want to allow this. But if the layout did not mark this line appropriately,
            # we must check the regex as additional safety:
            Above_Condition = False
            if (contains_tablecontentsregex(thisline.textline)): Above_Condition = True
            if (contains_headlines_regex(thisline.textline)): Above_Condition = True
            if (contains_some_enumeration(thisline.textline)): Above_Condition = True
            # This is to make sure that we pass SplitDoc-tests.
        
        # Next, the very first line of the document gets a special treatment:
        if (abs(thisline.previous_whiteline+1.0)<1e-3):
            Above_Condition = True
            # This is to make sure that we pass SplitDoc-tests.
            
        # Also, if a lot of other conditions are satisfied, we skip the above-condition:
        if (contains_headlines_regex(thisline.textline)):
            if (thisline.is_highlighted):
                Above_Condition = True
            if self.fontsize_biggerthenregular(thisline.fontsize):
                if (thisline.next_whiteline>1.75*self.findregularlineregion().get_value()):
                    Above_Condition = True

        if (contains_some_enumeration(thisline.textline)):
            if (thisline.is_highlighted):
                Above_Condition = True

        # Sometimes we have to just add an exception if a document just is damaged:
        if (thisline.textline=="Zeespiegelstijging"): Above_Condition = True
                
        # Give some output to show the decision process:
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("Vertical position:         " + str(thisline.vertical_position))
            print("Header boundary:           " + str(self.headerboundary))
            print("Footer boundary:           " + str(self.footerboundary))
            print("Previous Line Is Headline: " + str(thisline.previous_IsHeadline))
            print("Previous Line-Text:        " + str(thisline.previous_textline))
            print("Previous WhiteLine Is Big: " + str(self.whiteline_isbig(thisline.previous_whiteline)) + "; value = " + str(thisline.previous_whiteline))
            print("Thisline in Table of Contents (Regex): " + str(contains_tablecontentsregex(thisline.textline)))
            print("Thisline in Headline (Regex):          " + str(contains_headlines_regex(thisline.textline)))
            print("Full Above Condition = " + str(Above_Condition))
            print("")
     
        # Condition below:
        Below_condition = False
        if self.whiteline_isbig(thisline.next_whiteline): Below_condition = True # followed by a large whiteline
        if self.fontsize_biggerthenregular(thisline.fontsize): Below_condition = True # Large fontsize.
        
        # Do textual layout like bold fonts, highlight, etc. separately:
        Layout_Condition = False
        if (thisline.is_bold)and(self.boldchars_ratio<self.boldratio_threshold): Layout_Condition = True # bold font style; if bold is suffiently scarse that it has meaning for headlines.
        if (thisline.is_italic)and(self.italicchars_ratio<self.italicratio_threshold): Layout_Condition = True # italic font style; if it is sufficiently scarse that it has meaning.
        if (thisline.is_highlighted): Layout_Condition = True # Highlighted font-style (textmarker).
        if Layout_Condition: Below_condition = True
        
        # However, we do NOT just want to start a new headline if we have regular tekst that just happens
        # to be a single line. On the other hand, not everyone marks headlines by fontsizes or styles.
        # So, adapt Below_condition based on regex:
        if self.whiteline_isbig(thisline.next_whiteline):
            if not Layout_Condition:
                if not self.fontsize_biggerthenregular(thisline.fontsize):
                    
                    # Then, in this case we demand that at least some regex has to fire (not the chapter-one; that one is too specific...)
                    Below_condition = False
                    if (contains_headlines_nochapter_regex(thisline.textline)): Below_condition = True
                    # NOTE: as the chapterregex is usually a lot less specific then the section/subsection/subsubsection, that one
                    # is sensitive to generate mistakes (single lines that are misidentified as chapter-titles). As chapters are
                    # usually the least likely to have no more styling then just a single line, while there mistakes are the worst
                    # for the users, it is better to specifically exclude them here.
                    
                    # But, if the regex fires, make sure that it was not yet detected as an enumeration before (Copernicus):
                    if Below_condition:
                        if (contains_bigroman_enumeration(thisline.textline))and(enum_type.BIGROMAN in self.hierarchy): Below_condition = False
                        if (contains_smallroman_enumeration(thisline.textline))and(enum_type.SMALLROMAN in self.hierarchy): Below_condition = False
                        if (contains_bigletter_enumeration(thisline.textline))and(enum_type.BIGLETTER in self.hierarchy): Below_condition = False
                        if (contains_smallletter_enumeration(thisline.textline))and(enum_type.SMALLLETTER in self.hierarchy): Below_condition = False
                        if (contains_digit_enumeration(thisline.textline,self.whiteline_isbig(thisline.next_whiteline)))and(enum_type.DIGIT in self.hierarchy): Below_condition = False
                        if (contains_signmark_enumeration(thisline.textline))and(enum_type.SIGNMARK in self.hierarchy): Below_condition = False
                        
                    # In case we missed an enumeration because it is the first element in the hierarchy:
                    if re.compile(r':$').search(thisline.textline): Below_condition = False
        
        # Give some output to show the decision process:
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("Bold ratio in document:       " + str(self.boldchars_ratio) + " (threshold = " + str(self.boldratio_threshold) + ")")
            print("Italic ratio in document:     " + str(self.italicchars_ratio) + " (threshold = " + str(self.italicratio_threshold) + ")")
            print("Next WhiteLine Is Big:        " + str(self.whiteline_isbig(thisline.next_whiteline)) + "; value = " + str(thisline.next_whiteline))
            print("This textline is Bold:        " + str(thisline.is_bold))
            print("This textline is Italic:      " + str(thisline.is_italic))
            print("This textline is Highlighted: " + str(thisline.is_highlighted))
            print("This Fontsize is Big:         " + str(self.fontsize_biggerthenregular(thisline.fontsize)) + "; value = " + str(thisline.fontsize))
            print("TOC regex fired =             " + str(contains_tablecontentsregex(thisline.textline)))
            print("Chapter regex fired =         " + str(contains_chapterregex(thisline.textline)))
            print("Non-chapter headlines regex = " + str(contains_headlines_nochapter_regex(thisline.textline)))
            print("Full Below Condition =        " + str(Below_condition))
            print("")
        
        # Next, Unify the conditions:
        Headline_Condition = (Above_Condition)and(Below_condition)and(Letter_condition)

        # in some specific situations:
        if re.compile(r'Figure:').search(thisline.textline): Headline_Condition = False
        if ("3.1 Design parameters of Grand Raiden; table used with permission [64]" in thisline.textline): Headline_Condition = False
        
        # Now, if the previous line is a headline and an article and this one is a digit enumeration,
        # this one cannot be a headlines:
        if (thisline.previous_IsHeadline==True):
            if (contains_artikelregex(thisline.previous_textline)==True):
                if (contains_digit_enumeration(thisline.textline,self.whiteline_isbig(thisline.next_whiteline))==True):
                    Headline_Condition = False
        
        # Give some output to show the decision process:
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("Full HEADLINE Condition = " + str(Headline_Condition))
            print("")
        
        # Next, attempt to come up with a reasonable guess for the cascadelevel.
        # As an initial guess, we start wth one higher the body text:
        cascadelevel = self.findregularfontregion().get_cascadelevel()-1
        if (cascadelevel<=0): cascadelevel = 1
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("Blind-guess cascadelevel:        " + str(cascadelevel))
        
        # We only need to improve this information, if we actually found a headline:
        if Headline_Condition: 

            # If found a headline, attempt to match it with available content in the TOC
            # to determine the cascade level:
            Found_Cascade_Using_TOC = False
            if (len(self.copied_native_TOC)>0):

                # then, we loop though the list of native TOCs and we identify the best match:
                Best_match_ratio = 0.0
                Best_match_index = -1
                toc_index = -1

                # Loop:
                for toc_element in self.copied_native_TOC:

                    # increase index:
                    toc_index = toc_index + 1

                    # Compute the fuzzy match:
                    textline_to_test = thisline.textline
                    textline_to_test = textline_to_test.replace("’","'")
                    textline_to_test = textline_to_test.replace("‘","`")

                    tocline_to_test = toc_element.title
                    tocline_to_test = tocline_to_test.replace("’","'")
                    tocline_to_test = tocline_to_test.replace("‘","`")

                    fuzzymatch = fuzz.ratio(textline_to_test,tocline_to_test)

                    # Calculate maximum:
                    if (fuzzymatch>Best_match_ratio):
                        Best_match_ratio = fuzzymatch
                        Best_match_index = toc_index

                # Now, if the maximum is good enough (85 was established; not higher), use that cascade:
                if (Best_match_ratio>80.0):
                    cascadelevel = self.copied_native_TOC[Best_match_index].cascadelevel+1
                    Found_Cascade_Using_TOC = True

                if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
                    print("Recognised line  = " + thisline.textline)
                    print("Matched TOC-line = " + self.copied_native_TOC[Best_match_index].title)
                    print("Fuzzy_match      = " + str(Best_match_ratio))

                # NOTE: We deliberatly do NOT use the TOC to establish the headline-condition
                # itself. If we would JUST decide that some textline is a headline only because
                # it closely matches to the TOC, that is too risky; a body textline that contains
                # a headlines-title just because the text refers to that headline, would then also
                # be marked as a headline; we cannot have that. By requiring that the headline-condition
                # already fired, we avoid that and require that there has to be some layout to identify the headline.

                # NOTE: We also do not require that no other headlines can be found then the ones in the TOC;
                # otherwise we would eliminate some potentially very valuable structure that we did recognise.
                # As such, the resulting use of the TOC is JUST to improve the cascade levels once we
                # already established that something is a headline by our own rules. When we want to
                # continue further in the use of the TOC, we should do something with identifying
                # which inputs do/don't lead to a true headline condition based on TOC. But that is
                # no longer a rule-based algorithm; that would be rudimentary ML. So this is as far as
                # we can go using the TOC in the headline-identification.
            
            # NOTE: We want to keep our ability to determine cellar correctly without the TOC:
            if (self.documentname.lower()=="cellar"): Found_Cascade_Using_TOC = False

            if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
                print("cascadelevel after using TOC:        " + str(cascadelevel))

            # Then, if there is no TOC to help us: We primarily attempt to appoint cascade level based on font size:
            if not Found_Cascade_Using_TOC:
                if self.fontsize_biggerthenregular(thisline.fontsize):
                    cascadelevel = self.selectfontregion(thisline.fontsize).get_cascadelevel()

                if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
                    print("cascadelevel after using fontsize:        " + str(cascadelevel))

                # Next, improve our guesses using regex:
                if (contains_tablecontentsregex(thisline.textline)):
                    cascadelevel = 1
            
                if (contains_chapterregex(thisline.textline)):
                    cascadelevel = 1
                
                if (contains_sectionregex(thisline.textline)):
                    cascadelevel = 2
            
                if (contains_subsectionregex(thisline.textline)):
                    cascadelevel = 3
                
                if (contains_subsubsectionregex(thisline.textline)):
                    cascadelevel = 4

                if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
                    print("cascadelevel after using regex:        " + str(cascadelevel))

                # Now, if we actually fired on a regex, we know that for this document that
                # particular headline is always marked with a regex, so we should elmininate
                # that textlevel from the fontsizes. Then, if we find an unmarked headline
                # further down the document, we know that that headlines is NOT marked the
                # same as a headline we already know how to identify using regex.
                if ((contains_headlines_regex(thisline.textline))or(contains_tablecontentsregex(thisline.textline))):

                    # sort the array according to decending fontsizes:
                    self.fontregions = sorted(self.fontregions, key=lambda x: x.value, reverse=True)

                    # Find the index of the regular region:
                    index = 0
                    for k in range(0,len(self.fontregions)):
                        if (self.fontregions[k].get_isregular()==True):
                            index = k

                    # Now, loop over the regions with font sizes larger then the regular region:
                    if (index>0):
                        for k in range(0,index):
                            thisregion = self.fontregions[k]

                            # See if this region matches the appointed cascade:
                            if thisregion.get_cascadelevel()==cascadelevel:

                                # Then, this cascadelevel is erased and overwritten by
                                # the font region further in the chain:
                                if (k<index):
                                    for m in range(k,index):
                                        self.fontregions[m].cascadelevel = self.fontregions[m+1].cascadelevel

                                # Now, this loop started at thisregion itself, which is the cascadelevel
                                # we wanted to erase in the firts place, so that is good. But it ended
                                # placing the body-cascade level in region index-1. This is not good:
                                if ((index-1)>0):
                                    self.fontregions[index-1].cascadelevel = 4

                                # This will make sure that the smallest fontregion bigger then regular is
                                # kept at 4 (subsubsection). This then leaks through to new font regions
                                # every new time a regex expression is used to detect a textlevel, so that
                                # ultimately all fonts larger then regular but without any regex, are
                                # appointed subsections.

                                # But when, for example, sections are marked and other textlevels are not,
                                # this procedure will cause the largest region to appoint chapter and
                                # the second-to-largest to subsections (while regex will appoint sections).
                                # This is the procedure we wanted.
            
                                # Done.

                if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
                    print("cascadelevel after rearranging fontregions:        " + str(cascadelevel))
            
            # --------- (directly under if Headline_Condition) -------------------------------------

            # However, if the previous line was also a headline, we must NEVER change cascade levels;
            # NOTE: Keep thsi code in-sync with breakdown!

            # Calculate the fontregions of the different lines:
            previous_fontregion = self.selectfontregion(thisline.previous_fontsize)
            current_fontregion = self.selectfontregion(thisline.fontsize)
            fontregion_difference = previous_fontregion.get_value() - current_fontregion.get_value()
            fontsize_difference = thisline.previous_fontsize - thisline.fontsize

            # Calculate whether there is a shift in either bold, italic of fontsize:
            fontsize_shift = (abs(fontregion_difference)>1e-3)

            bold_shift = False
            if ((thisline.previous_is_bold)and(not(thisline.is_bold)))or((not(thisline.previous_is_bold))and(thisline.is_bold)): bold_shift = True
            if (self.boldchars_ratio>=self.boldratio_threshold): bold_shift = False

            italic_shift = False
            if ((thisline.previous_is_italic)and(not(thisline.is_italic)))or((not(thisline.previous_is_italic))and(thisline.is_italic)): italic_shift = True
            if (self.italicchars_ratio>=self.italicratio_threshold): italic_shift = False

            # Combine the three conditions in a layout-shift:
            layout_shift = (bold_shift)or(italic_shift)or(fontsize_shift)

            # Calculate whether there is a special regex:
            contains_special_regex = (contains_headlines_regex(thisline.textline))or(contains_some_enumeration(thisline.textline))
            contains_previousspecial_regex = (contains_headlines_regex(thisline.previous_textline))or(contains_some_enumeration(thisline.previous_textline))

            # Finetune layout_shift based on regexes:
            if (not(contains_special_regex)and(contains_previousspecial_regex)):
                if not fontsize_shift:
                    layout_shift = False

            # Now, decide if we have to keep the previous cascade level:
            if (not((thisline.previous_IsHeadline==False)or(layout_shift==True)or(contains_special_regex==True))):
                cascadelevel = thisline.previous_Headlines_cascade

            if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
                print("cascadelevel after syncing with previous headlines: " + str(cascadelevel))

        # To implement BNC-Fiches correctly:
        if self.is_fiche:
            if (not(contains_headlines_regex(thisline.textline))):
                if contains_smallletter_enumeration(thisline.textline):
                    if (not(thisline.is_bold))and(not(thisline.is_highlighted))and(not(self.fontsize_biggerthenregular(thisline.fontsize))):
                        Headline_Condition = True
                        cascadelevel = 2
            if (contains_headlines_regex(thisline.textline))and(not(contains_artikelregex(thisline.textline))):
                if contains_digit_enumeration(thisline.textline):
                    if (thisline.is_bold):
                        Headline_Condition = True
                        cascadelevel = 1

        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("cascadelevel after BNC-Fiche correction:        " + str(cascadelevel))
            print("Full HEADLINE Condition after BNC-Fiche correction: " + str(Headline_Condition))
            print("")
        
        # Give some output to show the decision process:
        if (self.ruleverbosity>0)and(self.verbosetextline in thisline.textline):
            print("Length of the TOC-metadata:        " + str(len(self.copied_native_TOC)))
            print("Thisline in TOC (Regex):           " + str(contains_tablecontentsregex(thisline.textline)))
            print("Thisline in Chapter (Regex):       " + str(contains_chapterregex(thisline.textline)))
            print("Thisline in Section (Regex):       " + str(contains_sectionregex(thisline.textline)))
            print("Thisline in SubSection (Regex):    " + str(contains_subsectionregex(thisline.textline)))
            print("Thisline in SubSubSection (Regex): " + str(contains_subsubsectionregex(thisline.textline)))
            for region in self.fontregions:
                if self.fontsize_biggerthenregular(region.get_value()):
                    region.printregion()
            print("Calculated Cascade Level: " + str(cascadelevel))
            print("")

        # See if we can improve our answer using meta-data from the document, if the document is
        # equipped with such data. We test this by determining if copied_native_TOC is empty or not:

        # Return the final answer:
        return Headline_Condition,cascadelevel
