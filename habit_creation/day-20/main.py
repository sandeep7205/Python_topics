"""
1. What does this represent? data = {"Food": 1200,"Travel": 550}  -> data has stored dictionary values.
2. If you have:data = {"Food": 1200}  how do you access 1200?   ->  data['Food']
3. What's the difference between: json.load() and: json.dump() -> 1st one load the json data and 2ns one dump the json data 
4. Why did appending directly to a JSON file with "a" cause problems? not in formart which give error in json file

"""
import os
from dotenv import load_dotenv
import src.expense_pipeline as pe

load_dotenv()

json_file_path = os.getenv("EXPENSE_JSON_FILE")
json_output_file_path = os.getenv("EXPENSE_output_JSON_FILE")
app_name = os.getenv("APP_NAME")


clean_json_data = {
    'developer': {},
    'expenses': {},
}

get_json_data = pe.read_json(json_file_path)

clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()


get_clean_data = pe.clean_data(get_json_data['expenses'])

get_process_data = pe.process_data(get_clean_data['clean_data'])
clean_json_data['expenses'] = get_process_data

pe.write_json(json_output_file_path, clean_json_data)

get_json_data = pe.read_json(json_output_file_path)
print(get_json_data)