"""
Day 27

Experiment 1
my ans -> name : SKM, the name got update from sandeep to skm
after run -> {'name': 'SKM', 'skills': ['Python', 'SQL']}


Experiment 2
my ans -> name : SKM
after run -> {'name': 'Sandeep', 'skills': ['Python', 'SQL']}


Day 27
Time spent:

Experiment 1:
Prediction: name : SKM, the name got update from sandeep to skm
Actual: {'name': 'SKM', 'skills': ['Python', 'SQL']}

Experiment 2:
Prediction: name : SKM
Actual:  {'name': 'Sandeep', 'skills': ['Python', 'SQL']}

What happened with data_summary():

How I fixed it: 
 summary_data = summary_data.copy() # creates a copy and assign to local variable with same name
    if "clean_data" in summary_data:
        del summary_data["clean_data"] # delete from the local variable & the original data got unchanged

Before summary: Does clean_data exist? → YES
After summary: Does clean_data exist? → YES

What I learned: got a basic knowladge of mutation 
What confused me: got cleared


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
        
        # print(get_json_data)
        if "clean_data" in get_clean_data:
            print(f"\n Before summary: Does clean_data exist? → YES")
    
        pipeline_summary = pe.data_summary(get_clean_data)
        if "clean_data" in get_clean_data:
            print(f"\n After summary: Does clean_data exist? → YES")
        # print(pipeline_summary)
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