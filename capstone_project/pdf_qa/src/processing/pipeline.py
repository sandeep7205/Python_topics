from src.ingestion.extractor import extract_pdf
from src.processing.cleaner import clean_page

from dotenv import load_dotenv
import os
import json

def run_pipeline(file_path) -> dict:
    """
    Extract and clean text from a PDF file.

    Extracts page-level text and file metadata, cleans the text of each
    page, and excludes pages that contain no meaningful text.

    Args:
        file_path (Path): Path to the PDF file.

    Returns:
        dict: PDF metadata and cleaned page data, including file path,
        file name, file size, file hash, page count, and a list of
        pages containing the page number and cleaned text.

    Raises:
        FileNotFoundError: If the PDF file does not exist or is not
        a regular file.
    """

    cleaned_pages = []

    extract_data = extract_pdf(file_path)

    for i, raw_text in enumerate(extract_data['pages']):
        clean_data = clean_page(raw_text['text'])
        if clean_data:
            cleaned_pages.append({'text': clean_data, 'page_number': raw_text['page_number']})

    extract_data['pages'] = cleaned_pages
    
    return extract_data


if __name__ == "__main__":
    try:
        load_dotenv()
        input_file = os.getenv("FILE_PATH")

        result = run_pipeline(input_file)

        print(json.dumps(result, indent=4))
    except FileNotFoundError as e:
        print(f"Error: {e}")