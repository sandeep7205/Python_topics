"""
1. What's the difference between try and except? 
    Ans: both handle execute thire respective code blocks, except handle the exceptions occures in try block
2. What happens when an exception occurs inside try?
    Ans: it jumps to except block
3. What's the difference between ValueError and TypeError?
    Ans: ValueError for any value exception and TypeError for Data Type exceptions
4. Why shouldn't we use this everywhere? ``` except Exception: ```
    Ans: there are different categories of exceptions are listed, exception does't handles all types
5. What does return do when a function successfully finishes?
    Ans: it returns the respective value to the calling function




Day 22
Time spent: 50min approx
What I learned: a little bit on how to add specific exception 
What I tried: by giving error data to get expection and add the except accordingly
Exception I found: KeyError, TypeError OSError, JSONDecoderError
How I handled it: by adding exception from input section to handle them
What confused me: what to put in clean_data() & process_data() as we handle before them or using if/else
idea: to concat the CSV data and write the total into json
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

    try:
        clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
        clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
        clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()

        get_clean_data = pe.clean_data(get_json_data['expenses'])
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