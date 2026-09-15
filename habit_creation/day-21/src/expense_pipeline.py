import json
import csv
from pathlib import Path
from dotenv import find_dotenv, dotenv_values
import sys

def valid_config_files_paths(variable_name_arr, env_path):
    if env_path == '':
        discovered_path = find_dotenv()
        if discovered_path:
            env_path = Path(discovered_path)
        else:
            sys.exit("Dynamic .env file does not exist.")

    if not env_path.is_file():
        sys.exit(".env file does not exist.")
    else:
        config_file_value = dotenv_values(env_path)

        if not variable_name_arr:
            sys.exit(f"Error: Invalid Variable Name ")

        for variable_name in variable_name_arr:
            if variable_name not in config_file_value:
                sys.exit(f"Variable '{variable_name}' is missing from the .env file.")
            else:
                if not config_file_value[variable_name]:
                    sys.exit(f"Error: Config Variable can't be blank.")
                else:
                    file_path = Path(config_file_value[variable_name])
                    if not file_path.exists():
                        sys.exit(f"file not found: [{config_file_value[variable_name]}]")
    return True

def read_data(input_csv_file):
    #Open the CSV and get the data.
    get_content = []
    with open(input_csv_file, "r") as csv_file:
        csv_read = csv.DictReader(csv_file)   
        for csv_data in csv_read:
            get_content.append(csv_data)
    return get_content

def clean_data(input_content):
    return_dict = {
        "clean_data": [],
        "valid_data_cnt": 0,
        "invalid_data_cnt": 0
    }
    for input_data in input_content:

        category_validation = "category" in input_data and input_data['category'] is not None and input_data['category'].strip() != ''
        amount_validation = "amount" in input_data and input_data['amount'] is not None

        # handle invalid/missing data
        try:
            if category_validation and amount_validation:
                # remove unwanted spaces
                # normalize category names
                input_data['category'] = input_data['category'].strip().title()
                # convert amount from string → integer
                input_data['amount'] = float(input_data['amount'].strip()) if isinstance(input_data['amount'], str) else input_data['amount'] 

                return_dict['clean_data'].append(input_data)
                
                return_dict['valid_data_cnt']+= 1
            else:
                return_dict['invalid_data_cnt']+= 1
        except ValueError:
            return_dict['invalid_data_cnt']+= 1
        except AttributeError:
            return_dict['invalid_data_cnt']+= 1
    return return_dict

def process_data(clean_content):
    #Calculate category totals.
    category_dict_amount = {}
    for clean_data in clean_content:
        category = clean_data['category']
        amount = clean_data['amount']
        if category not in category_dict_amount:
            category_dict_amount.update({category:amount})
        else:
            category_dict_amount[category] += amount
    return category_dict_amount

def read_json(json_file_path):
    # Read from json file
    with open(json_file_path, "r") as read_file:
        get_data = json.load(read_file)
    return get_data


def write_json(json_file_path, dict_data):
    # write dict data into from json file
    with open(json_file_path, "w") as write_file:
        json.dump(dict_data, write_file,indent=4)