"""

"""


import traceback
import os
from dotenv import load_dotenv
import src.expense_pipeline as pe
import json
load_dotenv()
env_variavbles_arr = ["EXPENSE_JSON_FILE", "EXPENSE_OUTPUT_JSON_FILE", "EXPENSE_CSV_FILE"]
if pe.valid_config_files_paths(env_variavbles_arr, ''):
    json_file_path = os.getenv("EXPENSE_JSON_FILE")
    json_output_file_path = os.getenv("EXPENSE_OUTPUT_JSON_FILE")
    csv_file_path = os.getenv("EXPENSE_CSV_FILE")

    clean_json_data = {
        'developer': {},
        'category_expenses': {},
    }

    get_json_data = pe.read_json(json_file_path, 1)
    get_csv_data = pe.read_data(csv_file_path)
    try:
        clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
        clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
        clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()
        
        merge_csv_json_data = get_json_data['expenses'] + get_csv_data

        get_clean_data = pe.clean_data(merge_csv_json_data)

        get_process_category_data = pe.process_data(get_clean_data['clean_data'])
        clean_json_data['category_expenses'] = get_process_category_data

        get_process_source_data = pe.process_source_data(get_clean_data['clean_data'])
        clean_json_data['source_expenses'] = get_process_source_data

        pe.write_json(json_output_file_path, clean_json_data)

        get_json_data = pe.read_json(json_output_file_path, 0)
        print(json.dumps(get_json_data, indent=4))   

        pipeline_summary = pe.data_summary(get_clean_data)
        print(pipeline_summary)
    except KeyError as e:
        print(f"\nData missing from json file -> {e}.\n")
        traceback.print_exc()
    except TypeError as e:
        print(f"\nWrong Data type has given as input -> {e}.\n")
        traceback.print_exc()
    except NameError as e:
        print(f"\nWrong Name type -> {e}.\n")
        traceback.print_exc()
else:
    print("\n.env file missing from same file directory\n")
    traceback.print_exc()