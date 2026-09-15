test_data = [
    {"category": "Food", "amount": "120.50"},
    {"category": None, "amount": "50"},
    {"category": "", "amount": "50"},
    {"category": "   ", "amount": "50"},
    {"category": "Travel", "amount": None},
    {"category": "Food", "amount": ""},
    {"category": "Shopping", "amount": "abc"},
    {"category": "Food", "amount": "100.25"},
    {"category": "Food", "amount": 0},
]

print




{"category": "Food", "amount": "120.50"} -> Valid
{"category": None, "amount": "50"} -> InValid
{"category": "", "amount": "50"} -> InValid
{"category": "   ", "amount": "50"} -> InValid
{"category": "Travel", "amount": None} -> InValid
{"category": "Food", "amount": ""} -> InValid
{"category": "Shopping", "amount": "abc"} -> InValid
{"category": "Food", "amount": "100.25"} -> Valid
{"category": "Food", "amount": 0} -> Valid"}