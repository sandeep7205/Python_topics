from pathlib import Path
import pymupdf
import json
from dotenv import load_dotenv
import os
import hashlib

def _compute_hash(file_path: Path) -> str:
    """
    Calculate the SHA-256 hash of a file.

    Args:
        file_path (Path): Path to the file.

    Returns:
        str: SHA-256 hash as a hexadecimal string.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be read due to insufficient permissions.
    """

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""): # reads 8KB at a time
            sha256.update(chunk)
    return sha256.hexdigest()



def extract_pdf(file_path: Path) -> dict:
    """
    Extract text and metadata from a PDF file.

    Args:
        file_path (Path): Path to the PDF file.

    Returns:
        dict: A dictionary containing:
            - file_path (str): Absolute path to the PDF file.
            - filename (str): Name of the PDF file.
            - file_size (int): File size in bytes.
            - file_hash (str): SHA-256 hash of the file.
            - page_count (int): Total number of pages.
            - pages (list[dict]): Extracted text for each page, containing
              the page number and its text.

    Raises:
        FileNotFoundError: If the file does not exist or is not a regular file.
    """

    file_dir = Path(file_path)
    if not file_dir.is_file():
        raise FileNotFoundError("The file does not exist (or it is a directory).")    

    get_text = {
        "file_path": str(file_dir.resolve()),  # absolute path
        "filename": "",
        "file_size": file_dir.stat().st_size,  # returns bytes
        "file_hash": _compute_hash(file_path),  # SHA256
        "page_count": 0,
        "pages": []
    }
    with pymupdf.open(file_path) as pdf_file:
        total_cnt = len(pdf_file)
        get_text['page_count'] = total_cnt
        get_text['filename'] = file_dir.name

        for index in range(total_cnt):
            page_number = index + 1
            get_text['pages'].append({'text' : pdf_file[index].get_text(), 'page_number' : page_number})
    return get_text



if __name__ == "__main__":
    try:
        load_dotenv()
        input_file = os.getenv("FILE_PATH")

        result = extract_pdf(input_file)
        print(json.dumps(result, indent=4))
    except FileNotFoundError as e:
        print(f"Error: {e}")