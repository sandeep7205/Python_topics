"""
1. Where should we add the source information?  -> in read_data() and read_json()
2. What should the source value be? "json" & "csv" Would you use uppercase? Lowercase? -> in actual data it might mention or not if mention then which format don't know but i will use Lowercase

3. Do we need to modify process_data()? Think carefully.
    - Your current process_data() calculates:
        category → amount
    - But now we eventually want something more like:
        category
            ├── json
            └── csv

    - Should process_data() know about the source?    ->  nice idea, We can add an other calculation with existing one by adding source condition but need to make chanegs in return part


Day 24
Time spent: 1hour above (you check)

Where I added source: i experiment 2 or 3 thing by create a new function add_value() then added into read_data() and read_json()

CSV source: 14 || JSON source: 51 || Combined records: 65

Final totals:65 'valid_data_cnt': 39, 'invalid_data_cnt': 26

What I learned: i create a new function to add value as it can be reuse
What confused me: the exception {e} dos't give me exact error line or function or anyother details

"""



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
    # print("\n\n get_process_data ->->->-> ", get_process_data)
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
        # print("\n\n get_clean_data ->->->-> ", get_clean_data)
        clean_json_data['expenses'] = get_process_data
        pe.write_json(json_output_file_path, clean_json_data)

        get_json_data = pe.read_json(json_output_file_path, 0)
        
        print(get_json_data)
    except KeyError as e:
        print(f"\nData missing from json file -> {e}.\n")
    except TypeError as e:
        print(f"\nWrong Data type has given as input -> {e}.\n")
else:
    print("\n.env file missing from same file directory\n")