# Stage 1 — Draw your pipeline

- Pipeline have 2 sources
    - JSON files
    - CSV files
- The Source & Destination Path comes from env files
- For Path/Variable Validation which recives the path details and file names and return the boolen if the path is tur or false  
    - valid_config_files_paths()
- To read & get the content from the input files path and return as dictonary along with it's type
    - JSON: read_json()
    - CSV: read_data()

- Merging both the JSON & CSV source data to make it one 
- To filterout the clean or valid source data, where we also log the counts for future summarization by taking and resturning the dictonary
    - clean_data()
- after filterout the data, it goes for summary calculations by taking and resturning the dictonary
    - process_data()
    - process_source_data()

- after processing & calculating we save the output into destination file with no returns
    - write_json()



---

# Stage 2 — Break your pipeline

## Test A — Missing category

Take:

{
    "amount": "100"
}

What should happen?
{'amount': '100', 'source': 'json'}
NoneType: None
{
    "developer": {
        "name": "Sandeep Kumar Mishra",
        "role": "Developer",
        "experience": "4.5 Years"
    },
    "category_expenses": {},
    "source_expenses": {}
}


Value matched



========== PIPELINE SUMMARY ==========

 Total records : 1
 Valid records : 0
 Invalid records : 1

 JSON records : 1
 CSV records : 0


## Test B — Invalid amount

Take:
{
    "category": "Food",
    "amount": "abc123"
}

What should happen?


{'category': 'Food', 'amount': 'abc123', 'source': 'json'}
Traceback (most recent call last):
  File "d:\my_study\Python_topics\habit_creation\day-29\src\expense_pipeline.py", line 107, in clean_data
    input_data['amount'] = float(input_data['amount'])
                           ~~~~~^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'abc123'
{
    "developer": {
        "name": "Sandeep Kumar Mishra",
        "role": "Developer",
        "experience": "4.5 Years"
    },
    "category_expenses": {},
    "source_expenses": {}
}


Value matched



========== PIPELINE SUMMARY ==========

 Total records : 1
 Valid records : 0
 Invalid records : 1

 JSON records : 1
 CSV records : 0




## Test C — Broken summary

Create something like:

{
    "total_data": 65,
    "valid_data_cnt": 39,
    "invalid_data_cnt": 10,
    "json_cnt": 51,
    "csv_cnt": 14
}


{'valid_data_cnt': 34, 'invalid_data_cnt': 21, 'json_cnt': 41, 'csv_cnt': 14, 'total_data': 55}

Data missing from json file -> 'clean_data'.

Traceback (most recent call last):
  File "d:\my_study\Python_topics\habit_creation\day-29\main.py", line 33, in <module>
    get_process_category_data = pe.process_data(get_clean_data['clean_data'])
                                                ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
KeyError: 'clean_data'




# Stage 3 — Code review yourself

## KEEP
    - instead read_json(), i can use read_data() with file_type_flag to read given file like json & csv
    - instead write_json(), i can create write_data() with file_type_flag to write given file like json & csv
    - data_summary()
    - clean_data()
## CHANGE
    - validate_pipeline_summary()
    - add_value() - flag base add source type
## REMOVE
    - read_json()
    - write_json()
## IMPROVE
    - clean_data()
    - exception handling And proper validations
    - adding comments



# Stage 4 — The final question

## Before Day 1:
What could you do in Python?
    - write code but nt with meaningfull and organized way

## Today:
What can you do in Python that you couldn't do 30 days ago?
    -  write code with meaningfull and optimized way


## And finally:

What is the biggest thing you still don't understand?
    - OOP
    - CRUD with DB
    - Exception handle  