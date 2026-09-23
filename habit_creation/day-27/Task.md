🔥 **DAY 27 — LET'S SHOOT IT OUT, SKM.**

Yesterday we spotted something important in your `data_summary()`:

```python
del summary_data["clean_data"]
```

That changes the dictionary you passed into the function.

Today we're going to **feel what that actually means**.

# 🎯 Day 27 — Mutation vs New Data

This is a very important Python concept because as your pipelines get bigger, accidentally changing shared data can create some nasty bugs.

---

## ⏱️ Part 1 — 5 minutes: Predict first

Create a small test in your Day 27 `main.py`:

```python
data = {
    "name": "Sandeep",
    "skills": ["Python", "SQL"]
}

def change_data(input_data):
    input_data["name"] = "SKM"

change_data(data)

print(data)
```

### Before running it, predict:

What will this print?

And more importantly:

> **Why?**

Don't Google it yet.

---

## ⏱️ Part 2 — Another experiment

Now try:

```python
data = {
    "name": "Sandeep",
    "skills": ["Python", "SQL"]
}

def change_data(input_data):
    input_data = input_data.copy()
    input_data["name"] = "SKM"

change_data(data)

print(data)
```

Predict again.

Then run both.

### Compare:

```text
Experiment 1
→ ?

Experiment 2
→ ?
```

---

# 🧠 What we're trying to discover

When you pass a dictionary into a function:

```python
change_data(data)
```

Python doesn't magically create a completely independent dictionary for the function.

The function receives a reference to the same object.

So:

```text id="m0m8j8"
data
  │
  └──────────────┐
                 ↓
          same dictionary
                 ↑
                 │
        input_data
```

Therefore:

```python
input_data["name"] = "SKM"
```

can change the original `data`.

That's **mutation**.

---

# ⏱️ Part 3 — Apply it to YOUR pipeline

Now look back at your Day 26:

```python
def data_summary(summary_data):
    if "clean_data" in summary_data:
        del summary_data["clean_data"]
```

You already know what this means now.

The challenge:

### Make `data_summary()` NOT modify `get_clean_data`.

But don't ask me for the solution yet.

Think:

> "How can I give `data_summary()` its own dictionary to work with?"

You already used `.copy()` in today's experiment.

There is a connection.

---

# 🚨 One important limitation

Today we're only dealing with a **shallow dictionary**.

Don't go down the rabbit hole of:

```text
copy
deepcopy
nested objects
references
memory addresses
garbage collection
```

😂

Not today.

We only need:

```text
original dictionary
       ↓
function
       ↓
don't accidentally modify original
```

---

# 🔥 Bonus challenge

After fixing `data_summary()`, prove that it doesn't modify the original.

Do something like:

```text
Before summary:
Does clean_data exist? → YES

Run data_summary()

After summary:
Does clean_data exist? → YES
```

That proof is more important than the actual fix.

---

# 📋 Day 27 report

Send me:

```text
Day 27
Time spent:

Experiment 1:
Prediction:
Actual:

Experiment 2:
Prediction:
Actual:

What happened with data_summary():

How I fixed it:

Before:
After:

What I learned:
What confused me:
```

### Today's rule

Don't turn this into a 2-hour Python internals investigation. 😄

**15 minutes minimum.**

You already have a working pipeline.

We're just making your understanding of Python stronger.

🔥 **Go shoot Day 27.**