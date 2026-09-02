"""
🔥 **Day 12 — let's go, SKM.**

Today we're doing something much closer to what happens in actual Data Engineering.

Yesterday you learned to **read structured data** with `csv.DictReader`.

Today you'll learn the uncomfortable truth:

> **Real data is messy.**

Your job isn't only to read data. You need to make it consistent before trusting it.

# 🟢 Day 12 — Data Cleaning & Normalization

### 🎯 Today's goal

Take messy CSV data:

```text
Date,Category,Amount
Monday, food ,250
Tuesday,FOOD,300
Wednesday,Food,150
Thursday, travel ,100
Friday,TRAVEL,450
Saturday,Shopping, 800
Sunday, entertainment ,450
```

and make Python treat:

```text
food
FOOD
 Food
food 
```

as the **same category**.

Today's pipeline:

```text
CSV
 ↓
Read
 ↓
Clean
 ↓
Convert
 ↓
Validate
 ↓
Calculate
```

---

# ⏱️ Minute 0–3 — Recall

Without opening Day 11, answer:

1. What's the difference between `csv.reader()` and `csv.DictReader()`?
2. What does `.strip()` do?
3. Why do we convert `Amount` using `int()`?
4. What does `row["Category"]` mean?
5. Why is a dictionary useful for category totals?
6. What happens when you do `total += amount`?

Short answers are enough.

---

# ⏱️ Minute 3–5 — Create dirty data

Create:

```text
day-12/
├── day-12.py
└── messy_expenses.csv
```

Put around **8–10 records** inside.

Deliberately make the data inconsistent.

For example:

```text
Date,Category,Amount
Monday, food ,250
Tuesday,FOOD,300
Wednesday,Food,150
Thursday, travel ,100
Friday,TRAVEL,450
Saturday, Shopping,800
Sunday,entertainment ,450
Monday, FOOD,200
```

Don't clean the CSV manually.

### Python has to clean it.

---

# ⏱️ Minute 5–10 — Challenge 1: Clean categories

Use:

```text
csv.DictReader
```

Read each row.

Then clean the category.

You already know:

```text
.strip()
```

Now discover a string method that can normalize capitalization.

Your target is something consistent like:

```text
food          → Food
FOOD          → Food
 food         → Food
Food          → Food

TRAVEL        → Travel
 travel       → Travel
```

Don't search for the whole solution.

Search only for something like:

> Python string capitalization methods

Experiment.

---

# ⏱️ Minute 10–12 — Challenge 2: Clean amount

Your CSV may contain:

```text
"250"
" 300"
"800 "
```

Clean the whitespace and convert the amount to an integer.

Think:

```text
raw value
   ↓
strip
   ↓
convert
   ↓
number
```

Then calculate the overall total.

---

# 🔥 Challenge 3 — Aggregate the cleaned data

Now reuse your Day 11 knowledge.

Create a dynamic dictionary:

```text
Food → ₹900
Travel → ₹550
Shopping → ₹800
Entertainment → ₹450
```

The important test:

### `"Food"`, `"FOOD"` and `" food "` must become ONE category.

If your output contains:

```text
Food → ₹400
FOOD → ₹300
food → ₹200
```

your cleaning hasn't worked yet.

Debug it.

---

# ⭐ Bonus — Bad records

Only if you're still interested after the main task.

Add one intentionally bad record:

```text
Tuesday,Food,
```

or:

```text
Tuesday,,300
```

Then ask yourself:

> **Should my pipeline process this row?**

Try detecting:

* missing category
* missing amount

You don't need sophisticated error handling yet.

A simple condition is enough.

Conceptually:

```text
Is required data missing?
        ↓
      YES → skip
        ↓
       NO → process
```

If you solve that, print something like:

```text
Skipping invalid row
```

---

# 🧠 The important concept today

There are really two different things happening.

### Cleaning

Fix the representation:

```text
" food " → "food"
```

### Normalization

Make equivalent values consistent:

```text
"food"
"FOOD"
"Food"

      ↓

"Food"
```

Then aggregation becomes reliable:

```text
Clean data
    ↓
Category grouping
    ↓
Totals
```

This is much more important than simply learning another Python method.

---

# 🚨 One rule today

Don't over-engineer this.

I don't want:

* pandas
* classes
* complex exception systems
* external libraries
* giant validation frameworks

You have everything necessary with:

**`csv` + strings + conditions + loops + dictionaries**

Use the fundamentals.

---

# 📝 Your Day 12 report

When you're finished, send me:

```text
Day 12 ✅

Memory:
1.
2.
3.
4.
5.
6.

I learned:

I built:

I understood:

I got stuck on:

I discovered:

Invalid-data experiment:

Time spent:

Habit battle today:
```

Paste your code and output too.

---

## One habit reminder tonight

It's later than your usual 8 PM session today.

That doesn't make Day 12 a failure.

The dangerous thought would be:

> "It's already late. I'll do it tomorrow."

No.

Your system is:

> **Late → do the minimum → continue tomorrow normally.**

And because it is late, **don't turn tonight into a 40-minute requirement just because your recent sessions happened to run that long.**

If you give Day 12 a focused **15 minutes**, you've kept the promise.

**Tonight we're cleaning messy data, not trying to have a perfect day. Day 12 — go own it. 🔥**

"""


# -----------------------------------------------------------------------------------

"""
Day 12 ✅ (yesterday's task)

Memory:
1.What's the difference between csv.reader() and csv.DictReader()? reader returns the list and dictreader returns the dictinoary where the header is the key
2.What does .strip() do? it erase the whitespace accross the elemnt including newline
3.Why do we convert Amount using int()? so we can do mathmatical  operations any integer numeric amount
4.What does row["Category"] mean? category key of row dictionary
5.Why is a dictionary useful for category totals? using keyname  we can retrive the values 
6.What happens when you do total += amount? its total = total + amount

I learned: handle the missing data nd clean it

I built: expense tracker

I understood: use of muliti function at once like .strip().title()

I got stuck on: not quite

I discovered: use of muliti function at once like .strip().title()

Invalid-data experiment: handle successfully

Time spent: 24 min but yester day i did not spent time i slept without finish

Habit battle today: yesterday i didnot win but totay i want to do the day-13 as punishment to myself,

"""

import csv

category_dict_amount = {}
with open("habit_creation/day-12/expenses.csv", "r") as csv_file:
    get_content = csv.DictReader(csv_file)
    #Read each row.
    for content in get_content:
        if content['Category'] and content['Amount']:
            #string method that can normalize capitalization.
            category = content['Category'].strip().title()
            #Clean the whitespace and convert the amount to an integer.
            amount = int(content['Amount'].strip())

            #Create a dynamic dictionary:
            if category not in category_dict_amount:
                category_dict_amount.update({category:amount})
            else:
                category_dict_amount[category] += amount
        else:
            print("Skipping invalid row")
        
print(category_dict_amount)