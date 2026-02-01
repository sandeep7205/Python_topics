questions = [
    {
        "question": "What is 5 + 3?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    },
    {
        "question": "Which shape has 3 sides?",
        "options": ["Square", "Circle", "Triangle", "Rectangle"],
        "answer": "Triangle"
    },
    {
        "question": "Which number",
        "options": [" ", "9", "", "12"],
        "answer": "20"
    },
    {
        "question": "What number comes after 11?",
        "options": ["10", "12", "13", "14"],
        "answer": "12"
    },
    {
        "question": "If you have 5 apples and eat 2, how many are left?",
        "options": ["2", "3", "4", "7"],
        "answer": "3"
    },
    {
        "question": "Which number is the biggest?",
        "options": ["15", "9", "20", "12"],
        "answer": "20"
    },
    # Blank question field
    {
        "question": " ",
        "options": ["Square", "9", "12", "12"],
        "answer": "20"
    },
        # Blank options element field
    {
        "question": "Which number",
        "options": [" ", "9", "", "12"],
        "answer": "--"
    },
        # Blank options answer field
    {
        "question": "Which number",
        "options": [" Square", "9", "Square", "12"],
        "answer": " "
    },
        # Blank all fields question 
    {},
    # Missing question field
    {
        "options": ["True", "False"],
        "answer": "True"
    },
    # Missing options field
    {
        "question": "What is 10 - 5?",
        "answer": "5"
    },
    # Missing answer field
    {
        "question": "What color is the sky?",
        "options": ["Red", "Blue", "Green", "Yellow"]
    },
    # Empty options list
    {
        "question": "What is 2 + 2?",
        "options": [],
        "answer": "4"
    },
    # Only one option (less than 2)
    {
        "question": "Is water wet?",
        "options": ["Yes"],
        "answer": "Yes"
    },
    # Answer not in options
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    # Duplicate options
    {
        "question": "What is 3 x 3?",
        "options": ["6", "9", "9", "12"],
        "answer": "9"
    },
    # All empty options
    {
        "question": "Pick a number",
        "options": ["", "", "", ""],
        "answer": ""
    },
    # None question
    {
        "question": None,
        "options": ["A", "B", "C", "D"],
        "answer": "A"
    },
    # None options
    {
        "question": "What is your favorite color?",
        "options": None,
        "answer": "Blue"
    },
    # None answer
    {
        "question": "What is 7 + 8?",
        "options": ["14", "15", "16", "17"],
        "answer": None
    },
    # Non-list options (string instead)
    {
        "question": "Is this valid?",
        "options": "Yes, No, Maybe",
        "answer": "Yes"
    },
    # Non-string answer (integer)
    {
        "question": "What is 5 + 5?",
        "options": ["8", "9", "10", "11"],
        "answer": 10
    },
    # Non-string options (integers)
    {
        "question": "Pick a number",
        "options": [1, 2, 3, 4],
        "answer": "2"
    },
    # Extra unexpected fields
    {
        "question": "What is the answer?",
        "options": ["A", "B", "C", "D"],
        "answer": "B",
        "extraField": "This shouldn't be here",
        "anotherField": 123
    },
    # Question with only whitespace
    {
        "question": "   \n\t  ",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
    },
    # Empty string answer
    {
        "question": "What is the result?",
        "options": ["Yes", "No", "Maybe", ""],
        "answer": ""
    },
    # Too many options (if there's a maximum limit)
    {
        "question": "Pick one",
        "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "answer": "5"
    },
    # Case sensitivity issue - answer doesn't match case
    {
        "question": "What is the color of grass?",
        "options": ["Green", "Blue", "Red", "Yellow"],
        "answer": "green"
    },
    # Whitespace in answer
    {
        "question": "What is 1 + 1?",
        "options": ["1", "2", "3", "4"],
        "answer": " 2 "
    },
    # Special characters in fields
    {
        "question": "What is <script>alert('xss')</script>?",
        "options": ["Safe", "Unsafe", "🔥", "⚠️"],
        "answer": "Unsafe"
    },
    # Extremely long question
    {
        "question": "A" * 10000,
        "options": ["Yes", "No"],
        "answer": "Yes"
    },
    # Extremely long option
    {
        "question": "Choose one",
        "options": ["Short", "B" * 5000, "Normal", "OK"],
        "answer": "Short"
    },
    # Boolean values instead of strings
    {
        "question": "Is this true?",
        "options": [True, False],
        "answer": True
    },
    # Mixed types in options list
    {
        "question": "What is the answer?",
        "options": ["String", 42, None, True, {"nested": "dict"}],
        "answer": "String"
    },
    # Tuple instead of list for options
    {
        "question": "Pick one",
        "options": ("A", "B", "C", "D"),
        "answer": "A"
    },
    # Float answer
    {
        "question": "What is pi?",
        "options": ["3.14", "3.15", "3.16"],
        "answer": 3.14
    },
    # Dictionary in options
    {
        "question": "What is valid?",
        "options": [{"key": "value"}, "Normal", "String"],
        "answer": "Normal"
    },
    # List answer
    {
        "question": "What is the answer?",
        "options": ["A", "B", "C"],
        "answer": ["A", "B"]
    },
    # Nested dictionary as a question object
    {
        "question": "Valid question",
        "options": ["A", "B"],
        "answer": "A",
        "metadata": {
            "difficulty": "easy",
            "category": "math"
        }
    },
    # Empty string for all fields
    {
        "question": "",
        "options": ["", ""],
        "answer": ""
    },
    # Unicode characters
    {
        "question": "¿Cómo estás?",
        "options": ["Bien", "Mal", "Así así", "👍"],
        "answer": "Bien"
    },
    # Negative numbers as strings
    {
        "question": "What is -5?",
        "options": ["-5", "-4", "-3", "5"],
        "answer": "-5"
    },
    # Set instead of list
    {
        "question": "Pick one",
        "options": {"A", "B", "C", "D"},
        "answer": "A"
    },
    # options is string
    {
        "question": "Pick one",
        "options": "A",
        "answer": "A"
    },
    None,
    "not a dictionary",
    123,
    True,
    False,
    ["list", "instead", "of", "dict"],
    3.14,
    set(),
    {"question", "options", "answer"}  # Set literal
]

if not isinstance(questions, (list, tuple)):
    print("Invaild format: expeted list or tuple formart")

if len(questions) <= 0:
    print("expected data in dictinory format inside list or tuple")

option_keys = set(["question",  "options", "answer"])
# is_invalid = False
valid_questions = []
for index, question in enumerate(questions):
    # print("\n------------------------")
    # print(index, question)
    if not isinstance(question, dict):
        # print(f'Invalid format: at position {index} - expected a dictionary,"{question}".')
        # is_invalid = True
        continue
    if not set(question.keys()).issuperset(option_keys):
        # print(f'Invalid format: at position {index} -  missing and/or invalid keys,"{question}".')
        # is_invalid = True
        continue
    valid_questions.append(question)

for valid_index, valid_question in enumerate(valid_questions):
    print("\n\n", valid_index, ' - ', valid_question)

def if_valid_quizset(index, question, options, answer):
    print("\n---------------------------------------------")
    print(index, ' - question - ', question)
    print(index, ' - options - ', options)
    print(index, ' - answer - ', answer)
    print("---------------------------------------------")
    constrains = {
        'question': isinstance(question, str) and len(question) > 0,
        'options': isinstance(options, (list, tuple, set)) and len(question) > 0,
        'answer': isinstance(answer, str) and len(question) > 0
    }
    return constrains
index_input = 36
print(if_valid_quizset(index_input, **valid_questions[index_input]))
print("---------------------------------------------\n\n")