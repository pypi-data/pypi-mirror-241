def summarize_private_huggingface_textsplitter(self, text: str, verbose_option: int) -> str:
    """
    This function takes a certain amount of text and uses a private LLM
    to summarize that tekst. The purpose is to prevent sending data
    from the documents across the internet.
    
    # Parameters: 
    text: str: the text that has to be summarized (possible a long string).
    verbose_option: int: 0: then nothing will be printed. higher numbers will print in-between stages in the terminal.
    # Return: str: the summary of the text.
    """
    
    # --------------------------------------------------------------------------

    # TODO: Develop this code:
    Answer = "The possibility to generate private summaries with LaMini-Flan-T5-248M does not yet exist in pdftextsplitter version " + str(self.VERSION)
    
    # Then, we can now return the answer:
    return Answer
