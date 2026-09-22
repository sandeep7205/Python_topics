"""
Day 26
Time spent:

My answers:

1. Where does the information for: Look at your clean_data() return dictionary.
    valid_records  =  records which are reday to process
    invalid_records = records which gives error/expception while process or invalid output
    json_records = records comes from json source
    csv_records = records comes from csv source

2. Do we really need to calculate these again in main.py? Or does clean_data() already know them?   -> clean_data() knows 

3. What should: total_records be?    Would you calculate:  valid + invalid    or:    json + csv    or something else?    -> if source not exists  or blank then data may miss, iguess i may go with valid + invalid or i will count inside loop for more betterment


========== PIPELINE SUMMARY ==========

 Total records : 65
 Valid records : 39
 Invalid records : 26

 JSON records : 51
 CSV records : 14

What I learned: how to mange the code 
What confused me: not in this
"""


import traceback
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

    get_json_data = pe.read_json(json_file_path, 1)
    get_csv_data = pe.read_data(csv_file_path)
    try:
        clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
        clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
        clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()
        
        # expense_json = pe.add_value('dict', get_json_data['expenses'], {"source":"json"})
        # expense_csv = pe.add_value('dict', get_csv_data, {"source":"csv"})

        merge_csv_json_data = get_json_data['expenses'] + get_csv_data

        get_clean_data = pe.clean_data(merge_csv_json_data)
        get_process_data = pe.process_data(get_clean_data['clean_data'])
        clean_json_data['expenses'] = get_process_data
        pe.write_json(json_output_file_path, clean_json_data)

        get_json_data = pe.read_json(json_output_file_path, 0)
        
        print(get_json_data)

        pipeline_summary = pe.data_summary(get_clean_data)
        print(pipeline_summary)
    except KeyError as e:
        print(f"\nData missing from json file -> {e}.\n")
        traceback.print_exc()
    except TypeError as e:
        print(f"\nWrong Data type has given as input -> {e}.\n")
        traceback.print_exc()
else:
    print("\n.env file missing from same file directory\n")
    traceback.print_exc()