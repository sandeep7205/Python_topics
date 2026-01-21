'''
## **Build a Terminal Based Quiz App**

In this lab you will practice Python fundamentals by building a terminal-based quiz application that asks questions, accepts user input, and calculates a final score.

### **Objective**

Fulfill the user stories below and get all the tests to pass to complete the lab.

---
### **User Stories:**

* You should define a function named `quiz_app`.
* The `quiz_app` function should take a single parameter `questions`.
* `questions` should be a list of dictionaries.
* Each dictionary should contain:

  * `question` (string)
  * `options` (list of strings)
  * `answer` (string – the correct option)
* The quiz should run in the terminal using `print()` and `input()`.
* For each question:

  * The question should be displayed.
  * All options should be displayed with numbering (1, 2, 3, …).
  * The user should be asked to enter the option number.
* If the user selects the correct option, the score should increase by 1.
* If the user selects a wrong option, the score should not increase.
* If the user enters invalid input (non-integer or out-of-range value), display an error message and move to the next question.
* After all questions are answered, the final score should be displayed in the format:
  `Your score: X/Y`
* The function should return the final score as an integer.
* If `questions` is not a list, the function should return
  `Questions must be provided as a list.`
* If the list is empty, the function should return
  `No questions available for the quiz.`

---

### **Tests**

1. You should have a `quiz_app` function.
2. The `quiz_app` function should have one parameter named `questions`.
3. `quiz_app` should accept a list of question dictionaries.
4. Each question should be displayed in the terminal.
5. All options should be displayed with numbering.
6. The quiz should accept user input using `input()`.
7. The score should increase by 1 for each correct answer.
8. The score should not increase for wrong answers.
9. Invalid input should be handled gracefully.
10. The final score should be displayed as `Your score: X/Y`.
11. The function should return the final score as an integer.
12. The function should return `Questions must be provided as a list.` for invalid input type.
13. The function should return `No questions available for the quiz.` when the list is empty.

'''
import sys

def sys_exit():
    print("Bye Bye")
    sys.exit()


# def current_qs_options(qs_index, question):
#     qs_str = f"{qs_index}. {question['question']}\n"
#     optn_str = ''
#     option_index_arr = []
#     for op_index, options in enumerate(question['options'], 1):
#         op_index = str(op_index)
#         option_index_arr.append(op_index)
#         optn_str +=  f"\t{op_index}. {options}\n"

#     question_format = ("\n" + qs_str + optn_str + "\n")
#     print(question_format)

#     options_str = "/".join(option_index_arr)
#     qs_answer = user_input(option_index_arr, f"\nWrite your option [{options_str}]: ")
#     return qs_answer

def user_input(option_index_arr, message):
    options_str = "/".join(option_index_arr)
    qs_answer = input(message)
    if qs_answer not in option_index_arr:
       qs_answer = user_input(option_index_arr, f"\nAnswer should be with in the options \n Write your option [{options_str}]: ")
    return qs_answer

def quiz_app(questions):
    try:
        if not isinstance(questions, list):
            print("Questions must be provided as a list.")
            sys_exit()
        elif len(questions) <= 0:
            print("No questions available for the quiz.")
            sys_exit()
       
        print ("Welcome to the Quiz Game.")
       
        total_qs = len(questions)
        correct_points = 0
        for qs_index, question in enumerate(questions, 1):
            if  not isinstance(question, dict) or len(question) <= 0:
                print(f"question set {qs_index} is not available or in valid formart for the quiz.")
                sys_exit()

            qs_index = str(qs_index)
            if not question['question']:
                print(f"Add question for set {qs_index} and restart the gmae")
                sys_exit()
            elif len(question['options']) <= 0:
                print(f"Add all options for set {qs_index} and restart the gmae")
                sys_exit()
            elif not question['answer']:
                print(f"Answer is blank for verification")
                sys_exit()

            # qs_answer = current_qs_options(qs_index, question)
            qs_str = f"{qs_index}. {question['question']}\n"
            optn_str = ''
            option_index_arr = []
            for op_index, options in enumerate(question['options'], 1):
                op_index = str(op_index)
                option_index_arr.append(op_index)
                optn_str +=  f"\t{op_index}. {options}\n"

            question_format = ("\n" + qs_str + optn_str + "\n")
            print(question_format)

            options_str = "/".join(option_index_arr)
            qs_answer = user_input(option_index_arr, f"\nWrite your option [{options_str}]: ")
            
            print('\n Your Answer - ', qs_answer)
            if (question['options'][(int(qs_answer) - 1)]) == question['answer']:
                correct_points += 1
                print('\n Correct Answer')
            else:
                print(f"\n Your Answer is Wrong, Correct Answer is [{question['answer']}]\n")

        return (f"Out of {total_qs} Your score is {correct_points}")
    except KeyboardInterrupt:
        sys_exit()
        

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
    }
]


quiz_score = quiz_app(questions)
print(quiz_score)
sys_exit()