"""
# 🚀 Day 14 — Let's Make Your Pipeline Robust

SKM, today we're going one small step beyond Day 13.

Yesterday you built:

```text
CSV
 ↓
read_data()
 ↓
clean_data()
 ↓
process_data()
 ↓
result
```

Today we're going to deal with something **very real in Data Engineering**:

> **What happens when the data is bad?**

Real-world data is messy. Files can contain missing values, invalid numbers, extra spaces, unexpected formats, etc.

So today's focus is **error handling + data validation**.

---

## 🎯 Today's goal

By the end of today, your pipeline should be able to encounter something like:

```text
Category,Amount
Food,250
Travel,abc
Shopping,
 food ,500
,300
```

…and **not crash just because one row is bad**.

Instead, your pipeline should recognize the bad row and skip it.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching your code, answer these:

1. What is the difference between `return` and `print()`?
2. What does `float("250.50")` produce?
3. What happens if you execute `float("abc")`?
4. Why might `if input_data['Amount']` not be enough to validate an amount?
5. What problem does `try/except` solve?

Don't worry if #4 or #5 isn't clear yet.

---

# 🔨 3–5 min — Understand `try/except`

You've probably seen Python crash with something like:

```text
ValueError
```

For example, conceptually:

```text
"250" → float → ✅
"250.50" → float → ✅
"abc" → float → ❌
```

The problem is:

```text
one bad row
    ↓
exception
    ↓
entire program stops
```

We want:

```text
one bad row
    ↓
exception
    ↓
skip/report row
    ↓
continue processing remaining rows
```

That's where `try/except` comes in.

---

# 🛠️ 5–12 min — Your challenge

**Modify your Day 13 `clean_data()` function.**

Don't rewrite the whole project.

Your job is to make this part robust:

```text
Category
Amount
```

### Your cleaning function should:

**1. Check that Category exists**

```text
missing category → invalid
```

**2. Check that Amount exists**

```text
missing amount → invalid
```

**3. Clean whitespace**

```text
" food " → "Food"
```

**4. Convert Amount to `float`**

```text
"250.50" → 250.5
```

**5. Handle invalid amounts**

```text
"abc"
```

should **not crash your program**.

Instead, skip that row.

---

## 🧩 One important challenge

Remember the problem I pointed out yesterday?

You had:

```python
if input_data['Category'] and input_data['Amount'] and float(...):
```

Think about why that's not ideal.

I want you to separate:

```text
VALIDATION
     ↓
CONVERSION
```

rather than doing everything inside one `if`.

That's the main thinking exercise today.

---

# ⭐ Bonus — only if you finish early

Add a counter:

```text
Valid rows: 8
Invalid rows: 2
```

So your pipeline doesn't just silently throw bad data away.

That's a tiny step toward **data quality monitoring**.

---

# 🚫 Don't do this today

Don't jump into:

* pandas
* NumPy
* AWS
* Airflow
* databases
* advanced exception handling

Not yet.

We're building the foundation properly.

---

## 📝 Your Day 14 report

When you're done, send:

```text
Day 14:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

I'll review it without immediately giving you the corrected version.

### Today's mindset:

> **Don't try to write perfect code. Try to understand what happens when your code meets imperfect data.**

That's where the Data Engineer mindset starts. 🔥

"""

# ========================================================================================================================================================

"""
What is the difference between return and print()? return some value else NaN, print is function to print something in terminal
What does float("250.50") produce? 250.50 in float value
What happens if you execute float("abc")? valuerror
Why might if input_data['Amount'] not be enough to validate an amount? it gives error
What problem does try/except solve? if try block gives error then except block handles the exceptions


Day 14:
Time: 22min
Habit battle: didnot battle much
What I built: hanndling the exception in expense calculation
What confused me: to handle category '' as it not give error
What I learned: not fully but how to use try except

"""


def read_data(input_csv_file):
    #Open the CSV and get the data.
    import csv
    get_content = []
    with open(input_csv_file, "r") as csv_file:
        csv_read = csv.DictReader(csv_file)   
        for csv_data in csv_read:
            get_content.append(csv_data)
    return get_content

def clean_data(input_content):
    # remove unwanted spaces
    # normalize category names
    # convert amount from string → integer
    # handle invalid/missing data
    clean_data = []
    valid_data_cnt = 0
    invalid_data_cnt = 0
    for input_data in input_content:
        try:
            if input_data['Category']:
                input_data['Category'] = input_data['Category'].strip().title()
                input_data['Amount'] = float(input_data['Amount'].strip())
                clean_data.append(input_data)
                valid_data_cnt+=1
            else:
                invalid_data_cnt+=1
        except ValueError:
            invalid_data_cnt+=1
            print('Skip the invalid data')
    print(f"Valid rows: {valid_data_cnt}\nInvalid rows: {invalid_data_cnt}")
    return clean_data

def process_data(clean_content):
    #Calculate category totals.
    category_dict_amount = {}
    for clean_data in clean_content:
        category = clean_data['Category']
        amount = clean_data['Amount']
        if category not in category_dict_amount:
            category_dict_amount.update({category:amount})
        else:
            category_dict_amount[category] += amount

    category_str = '\n'
    for key, value in category_dict_amount.items():
        category_str += f"{key} → {value}\n"
    return category_str


input_file = "habit_creation/day-14/expenses.csv"
get_csv_data = read_data(input_file)
get_clean_data = clean_data(get_csv_data)
get_process_data = process_data(get_clean_data)
print(get_process_data)