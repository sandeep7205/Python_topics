SKM — **this is a real Day 13 win.** Not because the code is perfect, but because you actually crossed the important line today: you took yesterday's logic and turned it into a **3-stage pipeline**.

And yes, going over an hour is fine today. You said you were frustrated **but enjoyed the process** — that's actually a useful signal. You weren't just consuming tutorials; you were debugging, searching, and figuring things out.

## 🔥 First: your Day 13 concept answers

A few corrections:

### `csv.DictReader`

Your answer:

> "it shows each lines of the file in value where the header is the key"

Close. More precisely:

> `DictReader` reads each CSV row as a dictionary-like object where the column headers become the keys.

Good understanding. ✅

### `.strip()`

Correct. ✅

It removes whitespace from the **beginning and end** of a string. A newline is whitespace too.

### `int()`

Correct. ✅

Although today you chose `float()` instead, which makes sense if your expense data can contain values like `250.50`.

### What does a function return?

This one needs correction.

You wrote:

> "it is a reusable block of code"

That's a **function**, not `return`.

Think:

```text
Function = reusable block of code

return = sends a result/value back to whoever called the function
```

For example, conceptually:

```text
result = read_data(...)
```

`read_data()` does its work and **returns** the data, which gets stored in `result`.

That's an important distinction. Remember it.

---

# 🏗️ Now let's review your pipeline

You built:

```text
read_data()
     ↓
clean_data()
     ↓
process_data()
     ↓
print()
```

That's exactly what I wanted.

### 1. `read_data()` — ✅ Good

```python
def read_data(input_csv_file):
    import csv
    get_content = []
    with open(input_csv_file, "r") as csv_file:
        csv_read = csv.DictReader(csv_file)   
        for csv_data in csv_read:
            get_content.append(csv_data)
    return get_content
```

The important part isn't the syntax.

It's this design:

```text
filename
   ↓
read_data()
   ↓
list of rows
```

You correctly separated **reading** from everything else.

And you specifically said:

> "what confused me: how to get data from with open"

That's actually worth paying attention to.

You discovered that:

```python
with open(...) as csv_file:
```

gives you a **file object**, and then:

```python
csv.DictReader(csv_file)
```

uses that file object to read the CSV.

That's a good connection to make.

---

# 2. `clean_data()` — ⚠️ Good idea, one important problem

You wrote:

```python
if input_data['Category'] and input_data['Amount'] and float(input_data['Amount'].strip()):
```

This works for many cases, but there's a hidden issue.

Suppose:

```text
Amount = "0"
```

Then:

```python
float("0")
```

becomes:

```text
0.0
```

And:

```python
if 0.0:
```

is **False**.

So an amount of `0` gets treated as invalid.

More importantly, you're doing the conversion **inside the condition**:

```python
float(input_data['Amount'].strip())
```

That means validation and transformation are being mixed together.

Don't fix it yet.

Just understand the problem.

That's exactly the kind of thing you'll start catching naturally as your Python skills improve.

---

## Another good decision 👇

You changed:

```python
int(...)
```

to:

```python
float(...)
```

That's actually better for an expense tracker if amounts can contain decimals:

```text
250
250.50
99.99
```

So your reasoning was good.

---

# 3. `process_data()` — ✅ Strong

This part is clean:

```python
category = clean_data['Category']
amount = clean_data['Amount']
```

Then:

```python
if category not in category_dict_amount:
    category_dict_amount.update({category:amount})
else:
    category_dict_amount[category] += amount
```

You've now reused something you learned several days ago.

That's important.

You're not learning isolated syntax anymore.

You're **connecting concepts**.

And this:

```python
for key, value in category_dict_amount.items():
```

shows that `.items()` is becoming natural for you.

---

# ⭐ One thing I particularly like

This:

```python
get_csv_data = read_data(input_file)
get_clean_data = clean_data(get_csv_data)
get_process_data = process_data(get_clean_data)
```

You can literally read it like a pipeline:

```text
get CSV data
      ↓
get clean data
      ↓
get processed data
```

That's the beginning of how you'll eventually think about:

```text
Extract → Transform → Load
```

We're not jumping into ETL yet.

But you're already building the mental model.

---

# 🧠 And here's the biggest Day 13 lesson

You said:

> "What I learned: every single line of code that i wrote, debug, search"

**That's exactly how you should be learning right now.**

Not:

> Watch 5 hours of Python → feel like you understand Python.

Instead:

> Build → break → investigate → fix → understand.

That's much closer to real engineering.

---

# One thing I want you to change mentally

Don't measure today as:

> "I spent more than an hour."

Measure it as:

> **"I stayed with the problem until I understood enough to make it work."**

That's a different skill.

But there's one warning:

**Don't let today's >1 hour become tomorrow's expectation.**

Your minimum is still:

**15 minutes.**

If tomorrow you only have 15 minutes, that's enough.

If you naturally go for 45 minutes, great.

No pressure to "beat" today's time.

---

## 🏁 Day 13 verdict

| Area                | Verdict                        |
| ------------------- | ------------------------------ |
| Functions           | ✅                              |
| Parameters          | ✅                              |
| Return values       | 🟡 Minor conceptual correction |
| CSV reading         | ✅                              |
| Data cleaning       | ✅                              |
| Data processing     | ✅                              |
| Function separation | ✅                              |
| Pipeline thinking   | ✅                              |
| Debugging mindset   | 🔥                             |

**Day 13: COMPLETE.**

And SKM, notice something: a few weeks ago, "how do I get data from a CSV?" was the problem.

Today you built:

```text
CSV
 ↓
DictReader
 ↓
read_data()
 ↓
clean_data()
 ↓
process_data()
 ↓
category totals
```

That's meaningful progress.

**Tomorrow we don't need to make things dramatically harder. We make the pipeline a little more robust.**
