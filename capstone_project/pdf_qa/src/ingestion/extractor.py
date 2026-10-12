from pathlib import Path
import pymupdf
import json
def extract_pdf(file_path):
    get_text = {
        "page_count": 0,
        "filename": "",
        "page": []
    }
    try:
        file_dir = Path(file_path)
        if file_dir.is_file():
            with pymupdf.open(file_path) as pdf_file:
                total_cnt = len(pdf_file)
                get_text['page_count'] = total_cnt
                get_text['filename'] = file_dir.stem

                page_number = 0
                for index in range(total_cnt):
                    page_number = index + 1
                    get_text['page'].append({'text' : pdf_file[index].get_text(), 'page_number' : page_number})
        else:
            print("The file does not exist (or it is a directory).")        
    except FileNotFoundError:
        print("The file does not exist.")
    return get_text



pdf_data = extract_pdf("c:/Users/Sandeep Kumar Mishra/Downloads/sample-local-pdf.pdf")
print(json.dumps(pdf_data, indent=4))