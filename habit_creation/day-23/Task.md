🔥 **DAY 23 — LET'S BURN IT, SKM.**

Today we're going to use **your own idea** from yesterday:

> **CSV + JSON → combine the data → calculate totals → write the result to JSON**

But we're going to do it in a controlled way. No rabbit holes. 😄

## 🎯 Day 23 Mission — Two Sources, One Pipeline

Right now you have two data sources:

```text
developer_expenses.json
        ↓
    clean_data()
        ↓
   process_data()
```

and separately:

```text
expenses.csv
        ↓
    clean_data()
        ↓
   process_data()
```

Today we're going to make them work together.

### Target architecture

```text
             ┌── JSON ──┐
             │          │
             ↓          ↓
           READ       READ
             │          │
             └────┬─────┘
                  ↓
             COMBINE DATA
                  ↓
              CLEAN DATA
                  ↓
             PROCESS DATA
                  ↓
              OUTPUT JSON
```

That's a tiny **ETL pipeline**.

---

# ⏱️ First 5 minutes — Think before coding

Open your CSV and JSON data.

Don't change anything yet.

Answer these questions in your `main.py` comments:

### 1. What does `read_json()` return?

Is it:

```text
dictionary?
list?
string?
```

### 2. What does `read_data()` return?

Same question.

### 3. What does `clean_data()` expect?

Look at this:

```python
clean_data(input_content)
```

What kind of object does `input_content` need to be?

### 4. What does `process_data()` expect?

And what does it return?

---

# ⏱️ Next 5 minutes — Find the bridge

This is the **important part**.

Your JSON currently looks conceptually like:

```text
{
    "developer": {...},
    "expenses": [
        {...},
        {...}
    ]
}
```

Your CSV reader gives you something conceptually like:

```text
[
    {...},
    {...},
    {...}
]
```

Notice something?

The JSON's:

```python
get_json_data['expenses']
```

is already a **list of expense dictionaries**.

And `read_data()` also returns a **list of dictionaries**.

💡 That's your bridge.

Your challenge is to figure out how to turn:

```text
JSON expenses
       +
CSV expenses
       ↓
ONE list of expenses
```

Don't ask me for the code yet.

**You should figure out the operation.**

---

# ⏱️ Final 5 minutes — Build it

Modify `main.py` so that:

### Step 1

Read JSON expenses.

### Step 2

Read CSV expenses.

### Step 3

Combine both lists.

### Step 4

Pass the combined list into:

```python
clean_data()
```

### Step 5

Pass the cleaned data into:

```python
process_data()
```

### Step 6

Write the final totals to your output JSON.

---

## 🚨 One important constraint

**Do NOT modify `clean_data()` or `process_data()` today.**

They already work.

We're testing whether you can **reuse the pipeline components you've already built**.

That's an important engineering skill:

> **Don't rewrite working components when you can compose them.**

---

# 🧪 Your test

After running it, show me:

```text
Day 23
Time spent:

JSON records:
CSV records:
Combined records:

Valid:
Invalid:

Final totals:

What I learned:
What confused me:
```

And one extra thing:

### 🔥 Tell me the exact line/operation you used to combine the two lists.

Don't just show the whole code.

I want you to know **why that line works.**

---

### Today's trap 😂

You may think:

> "Maybe I should create `merge_data()`, then `validate_source()`, then a generic pipeline class, then..."

**NOPE.**

Today:

```text
READ → COMBINE → CLEAN → PROCESS → WRITE
```

That's it.

**15-minute minimum.**

If you naturally hit 30–40 minutes because you're enjoying it, fine.

Now go burn Day 23. 🔥
