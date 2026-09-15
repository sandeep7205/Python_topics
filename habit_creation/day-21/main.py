import os
from dotenv import load_dotenv
import src.expense_pipeline as pe
load_dotenv()
env_variavbles_arr = ["EXPENSE_JSON_FILE", "EXPENSE_OUTPUT_JSON_FILE", "EXPENSE_CSV_FILE"]
if pe.valid_config_files_paths(env_variavbles_arr, ''):
    json_file_path = os.getenv("EXPENSE_JSON_FILE")
    json_output_file_path = os.getenv("EXPENSE_OUTPUT_JSON_FILE")
    csv_file_path = os.getenv("EXPENSE_CSV_FILE")

    clean_json_data = {
        'developer': {},
        'expenses': {},
    }

    get_json_data = pe.read_json(json_file_path)

    clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
    clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
    clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()


    get_clean_data = pe.clean_data(get_json_data['expenses'])

    print(get_clean_data)

    get_process_data = pe.process_data(get_clean_data['clean_data'])
    clean_json_data['expenses'] = get_process_data

    pe.write_json(json_output_file_path, clean_json_data)

    get_json_data = pe.read_json(json_output_file_path)
    print(get_json_data)
else:
    print(".env file missing from same file directory")