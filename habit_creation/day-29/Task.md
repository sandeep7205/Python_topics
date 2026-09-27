🔥 **Let's rock and roll, SKM. Day 29.**

You've now built enough pieces that we should start shifting from:

> **“Can I make this work?”**

toward:

> **“Can I trust what this pipeline produces?”**

## 🟢 Day 29 — Pipeline Validation

Today we're going to introduce a very small but important Data Engineering concept:

### **Data quality checks**

Your pipeline currently processes data and produces results.

But imagine this happens:

```text
65 records
   ↓
clean_data()
   ↓
39 valid
26 invalid
   ↓
process_data()
```

How do you know the pipeline didn't accidentally lose a valid record?

That's today's challenge.

---

### 🎯 Your mission

Create a function:

```python
def validate_pipeline_summary(summary_data):
    ...
```

It should check this relationship:

```text
total_data = valid_data_cnt + invalid_data_cnt
```

For your current data:

```text
65 = 39 + 26
```

So the validation should pass.

But if something goes wrong:

```text
65 != 38 + 26
```

the function should tell you that something is inconsistent.

---

### 💡 Hints — not the solution

Think about these questions:

**1. What values do you need?**

You already have them inside:

```python
get_clean_data
```

Look at:

```text
total_data
valid_data_cnt
invalid_data_cnt
```

---

**2. What should your function return?**

Keep it simple.

Maybe:

```python
True
```

when everything is consistent, and:

```python
False
```

when something is wrong.

---

**3. What should happen if a required key doesn't exist?**

For example:

```python
{
    "total_data": 65,
    "valid_data_cnt": 39
}
```

What happens when `invalid_data_cnt` is missing?

Don't immediately reach for `try/except`.

Think first about **validation**.

---

### 🧪 Your test cases

Don't test only the happy path.

Create three small test dictionaries.

#### Test 1 — Valid

```text
total = 65
valid = 39
invalid = 26
```

Expected:

```text
True
```

#### Test 2 — Invalid

```text
total = 65
valid = 40
invalid = 26
```

Expected:

```text
False
```

#### Test 3 — Missing field

Remove one of the three values.

Ask yourself:

> Should my function return `False`, or should it raise an exception?

**You decide.**

That's part of today's exercise.

---

### 🚫 Today's rule

Don't touch:

* pandas
* databases
* classes
* logging
* Streamlit
* your PDF chatbot

And don't rewrite the existing pipeline.

We're building **one small piece of reliability**.

### ⏱️ 15-minute target

**5 min:** design the logic on paper
**7 min:** write the function
**3 min:** test the three cases

Then paste your function + test results here.

I'll review it **without giving you the solution upfront**.

And one more thing: yesterday you came back after two missed days. Today you're here again.

That's the behavior we're trying to build. **Keep the streak in your head secondary; keep returning primary.** 💪
