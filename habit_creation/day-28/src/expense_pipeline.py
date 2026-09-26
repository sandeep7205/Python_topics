import json
import csv
from pathlib import Path
from dotenv import find_dotenv, dotenv_values
import sys
import traceback

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
        try:
            csv_read = csv.DictReader(csv_file)   
            for csv_data in csv_read:
                csv_data.update({"source":"csv"})   
                get_content.append(csv_data)
        except csv.Error as e:
            get_content = []
    return get_content

def clean_data(input_content):
    return_dict = {
        "clean_data": [],
        "valid_data_cnt": 0,
        "invalid_data_cnt": 0,
        "json_cnt": 0,
        "csv_cnt": 0,
        "total_data": 0
    }
    for input_data in input_content:
        return_dict['total_data'] += 1
        if "source" in input_data:
            if input_data['source'] == "json":
                return_dict['json_cnt'] += 1
            elif input_data['source'] == 'csv':
                return_dict['csv_cnt'] += 1

       # handle invalid/missing data
        if "category" not in input_data:
            category_validation = False
        elif input_data['category'] is None:
            category_validation = False
        elif not isinstance(input_data['category'], str):
            category_validation = False
        else:
            category = input_data['category'].strip()
            if not category:
                category_validation = False
            elif category.lower() in ['null', 'none', 'nan']:
                category_validation = False
            else: 
                category_validation = True

        if "amount" not in input_data:
            amount_validation = False
        elif input_data['amount'] is None:
            amount_validation = False
        elif isinstance(input_data['amount'], (bool)):
            amount_validation = False
        elif isinstance(input_data['amount'], str):
            amount = input_data['amount'].strip()
            if not amount:
                amount_validation = False
            elif amount.lower() in ['null', 'none', 'nan', 'infinity', '-infinity']:
                amount_validation = False
            else: 
                amount_validation = True
        else: 
            amount_validation = True

        try:
            if category_validation and amount_validation:
                # remove unwanted spaces
                # normalize category names
                input_data['category'] = category.title()
                # convert amount to float
                input_data['amount'] = float(input_data['amount'])
                return_dict['clean_data'].append(input_data)
                return_dict['valid_data_cnt']+= 1
            else:
                return_dict['invalid_data_cnt']+= 1
        except ValueError:
            # traceback.print_exc()
            return_dict['invalid_data_cnt']+= 1

    return return_dict

def process_data(clean_content):
    #Calculate category totals.
    category_dict_amount = {}
    for clean_data in clean_content:
        category = clean_data['category']
        amount = clean_data['amount']
        source = clean_data['source']
        if category not in category_dict_amount:
            category_dict_amount.update({category:amount})
        else:
            category_dict_amount[category] += amount
    return category_dict_amount

def process_source_data(clean_data):
    source_category_dict = {}
    for data in clean_data:
        # print(json.dumps(data, indent=4))
        category = data['category']
        amount = data['amount']
        source = data['source'] if 'source' in data and data['source'] else 'no_source'

        if source not in source_category_dict:
            source_category_dict.update({source:{}})
        
        if category not in source_category_dict[source]:
            source_category_dict[source].update({category:amount})
        else:
            source_category_dict[source][category] += amount
            
    return source_category_dict 

def read_json(json_file_path, add_source_flag):
    # Read from json file
    with open(json_file_path, "r") as read_file:
        try:
            get_data = json.load(read_file)
            if add_source_flag == 1:
                get_data['expenses'] = list(map(lambda d: d | {"source":"json"}, get_data['expenses']))
        except json.JSONDecodeError as e:
            get_data = {}
    return get_data


def write_json(json_file_path, dict_data):
    # write dict data into from json file
    with open(json_file_path, "w") as write_file:
        try:
            json.dump(dict_data, write_file,indent=4)
        except TypeError as e:
            sys.exit(f"TypeError: Data contains non-serializable objects -> {e}")
        except OSError as e:
            sys.exit(f"File Error: Could not write to file path -> {e}")

def add_value(data_type, datas, value):
    updated_data = []
    if data_type == 'dict':
        # for data in datas:
        #     data.update(value)        
        updated_data = list(map(lambda d: d | value, datas))
    return updated_data


def data_summary(summary_data):
    summary_str = "\n\n========== PIPELINE SUMMARY =========="
    summary_data = summary_data.copy() # creates a copy and assign to local variable with same name
    if "clean_data" in summary_data:
        del summary_data["clean_data"] # delete from the local variable & the original data got unchanged
        
    if 'total_data' in summary_data and summary_data["total_data"] >=0:
        summary_str += f"\n\n Total records : {summary_data["total_data"]}"
    if 'valid_data_cnt' in summary_data and summary_data["valid_data_cnt"] >=0:
        summary_str += f"\n Valid records : {summary_data["valid_data_cnt"]}"
    if 'invalid_data_cnt' in summary_data and summary_data["invalid_data_cnt"] >=0:
        summary_str += f"\n Invalid records : {summary_data["invalid_data_cnt"]}"
    if 'json_cnt' in summary_data and summary_data["json_cnt"] >=0:
        summary_str += f"\n\n JSON records : {summary_data["json_cnt"]}"
    if 'csv_cnt' in summary_data and summary_data["csv_cnt"] >=0:
        summary_str += f"\n CSV records : {summary_data["csv_cnt"]}\n\n"

    return summary_str




