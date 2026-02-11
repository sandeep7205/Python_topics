# ============================================================
# Medical Records Format Validator
# ============================================================
#
# Description:
# This script validates a collection of medical records to
# ensure that each record follows a strict data format.
#
# Each medical record must:
# - Be a dictionary
# - Contain the exact required keys
# - Follow validation rules for values such as IDs, age,
#   gender, diagnosis, medications, and visit IDs
#
# The script uses regular expressions and type checks to
# identify formatting issues and reports detailed errors
# without stopping execution prematurely.
#
# ============================================================

import re


# ------------------------------------------------------------
# Sample Medical Records Dataset
# ------------------------------------------------------------
# Each record represents a patient visit and must conform
# to predefined validation rules.
# ------------------------------------------------------------

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


# ------------------------------------------------------------
# Field-Level Validation Function
# ------------------------------------------------------------
# This function checks individual fields in a medical record
# against defined constraints and returns the names of fields
# that fail validation.
# ------------------------------------------------------------

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """
    Validation rules:
    - patient_id: string matching 'p' followed by digits
    - age: integer >= 18
    - gender: 'male' or 'female' (case-insensitive)
    - diagnosis: string or None
    - medications: list of strings
    - last_visit_id: string matching 'v' followed by digits

    Notes on regex usage:
    - r'...' ensures raw string handling
    - \d correctly represents digit matching
    - re.IGNORECASE allows case-insensitive matching
    """

    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),

        'age': isinstance(age, int) and age >= 18,

        'gender': isinstance(gender, str)
        and gender.lower() in ('male', 'female'),

        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),

        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }

    # Return a list of field names that failed validation
    return [key for key, value in constraints.items() if not value]


# ------------------------------------------------------------
# Dataset-Level Validation Function
# ------------------------------------------------------------
# This function validates an entire dataset of medical records.
# It checks:
# - Input structure (list or tuple)
# - Record type (dictionary)
# - Required keys
# - Field-level validity using find_invalid_records
# ------------------------------------------------------------

def validate(data):
    # Ensure the input is a sequence
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False

    # Required keys for every medical record
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # Iterate through each record in the dataset
    for index, dictionary in enumerate(data):

        # Validate record type
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Validate record keys
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} '
                f'has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        # Validate individual fields
        invalid_records = find_invalid_records(**dictionary)

        for i in invalid_records:
            print(
                f"Unexpected format '{i}: {dictionary[i]}' "
                f"at position {index}."
            )
            is_invalid = True

    # Final validation result
    if is_invalid:
        return False

    print('Valid format.')
    return True


# ------------------------------------------------------------
# Validation Execution
# ------------------------------------------------------------
# Run validation against the sample medical records dataset
# ------------------------------------------------------------

validate(medical_records)
