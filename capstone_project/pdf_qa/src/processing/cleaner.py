

import re
def clean_page(text: str) -> str:
    """
    Clean extracted PDF page text by removing null characters,
    replacing multiple whitespace characters with a single space,
    and trimming leading and trailing whitespace.

    Args:
        text (str): Raw text extracted from a PDF page.

    Returns:
        str: Cleaned text, or an empty string if the input is empty
        or contains only whitespace.
    """

    if not text:
        return ""
    text = text.replace("\x00", "")
    text = re.sub(r'\s+', ' ', text).strip()    
    
    return text



if __name__ == "__main__":
    sample = " \n1 \nSample PDF \n \nCreated for testing PDFObject \n \n"
    print(repr(clean_page(sample)))