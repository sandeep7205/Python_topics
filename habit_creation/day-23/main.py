"""
1. What does read_json() return?
    Is it:  dictionary? ||  list? ||  string?   -> dictionary

2. What does read_data() return?   -> dictionary

3. What does clean_data() expect? Look at this: clean_data(input_content) What kind of object does input_content need to be?    -> List[{dict}]

4. What does process_data() expect? And what does it return?    -> both dictionary



Day 23
Time spent: 32 min

JSON records: 15
CSV records: 50
Combined records: 65

Valid: 39
Invalid: 26

Final totals: 26

What I learned: how to concat lists
What confused me: luckily not today


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

    get_json_data = pe.read_json(json_file_path)
    get_csv_data = pe.read_data(csv_file_path)

    try:
        clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
        clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
        clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()

        merge_csv_json_data = get_json_data['expenses'] + get_csv_data
        get_clean_data = pe.clean_data(merge_csv_json_data)

        get_process_data = pe.process_data(get_clean_data['clean_data'])
        clean_json_data['expenses'] = get_process_data

        pe.write_json(json_output_file_path, clean_json_data)

        get_json_data = pe.read_json(json_output_file_path)
       
        print(get_json_data)
    except KeyError as e:
        print(f"\nData missing from json file -> {e}.\n")
    except TypeError as e:
        print(f"\nWrong Data type has given as input -> {e}.\n")
else:
    print("\n.env file missing from same file directory\n")