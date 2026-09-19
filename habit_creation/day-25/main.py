"""
1. What do you think this does?  import traceback   -> it trace where every lines got tracked
2. What do you think this does?  traceback.print_exc()  ->  it prints only the exceptions
3. What's the difference between:
        id="g1"
        print(e)
    and:
        id="g2"
        traceback.print_exc()
-> e dosn't give anything as there is no exception type mentioned & traceback.print_exc() may gives success message of asigned as there no exception



Day 25
Time spent:

Prediction:
1. it trace where every lines got tracked
2. it prints only the exceptions
3. e dosn't give anything as there is no exception type mentioned & traceback.print_exc() may gives success message of asigned as there no exception

KeyError:
File: "d:\my_study\Python_topics\habit_creation\day-25\main.py" , "d:\my_study\Python_topics\habit_creation\day-25\src\expense_pipeline.py"
Line: 44, 118
Statement: KeyError: 'source'



ValueError:
File: \my_study\Python_topics\habit_creation\day-25\src\expense_pipeline.py"
Line:  102
Statement: ValueError: could not convert string to float: 'abc123'




TypeError:
File: "d:\my_study\Python_topics\habit_creation\day-25\main.py"
Line: 34
Statement: TypeError: list indices must be integers or slices, not str




What I learned: how to track and read the error
What confused me: i have send traceback as argument in clean_data for child to use, so i am curious how to use same module as the child file is also import in parent file, so don't need to import twice
    
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
    except KeyError as e:
        print(f"\nData missing from json file -> {e}.\n")
        traceback.print_exc()
    except TypeError as e:
        print(f"\nWrong Data type has given as input -> {e}.\n")
        traceback.print_exc()
else:
    print("\n.env file missing from same file directory\n")
    traceback.print_exc()