SKM ❤️ **that's exactly the sentence I wanted to hear:**

> **"2 days late, but not discontinuing."**

That's the habit.

Not *never miss*.
Not *perfect streak*.
**Miss → return → continue.**

So we don't spend Day 26 paying for the two missed days. They're gone. We're back on the road.

# 🔥 DAY 26 — Make the Pipeline Tell You What Happened

We've built quite a bit now:

```text
JSON ──┐
       ├──→ Combine → Clean → Process → JSON
CSV ───┘
```

And we've learned:

* validation
* exception handling
* metadata/source tracking
* tracebacks

Today we're going to connect those ideas.

## 🎯 Mission

Right now your pipeline can tell you:

```text
Valid: 39
Invalid: 26
```

But imagine this:

```text
Pipeline completed
------------------
Total records : 65
Valid         : 39
Invalid       : 26

JSON records  : 51
CSV records   : 14
```

That's much more useful.

### Today's goal:

Create a **pipeline summary**.

Not a fancy logging framework.

Not a class.

Not a database.

Just a clean summary dictionary.

Something conceptually like:

```python
{
    "total_records": 65,
    "valid_records": 39,
    "invalid_records": 26,
    "json_records": 51,
    "csv_records": 14
}
```

---

# ⏱️ Part 1 — 5 minutes: Think

Before coding, answer these in your Day 26 file.

### 1.

Where does the information for:

```text
valid_records
invalid_records
json_records
csv_records
```

currently exist?

Look at your `clean_data()` return dictionary.

---

### 2.

Do we really need to calculate these again in `main.py`?

Or does `clean_data()` already know them?

---

### 3.

What should:

```text
total_records
```

be?

Would you calculate:

```python
valid + invalid
```

or:

```python
json + csv
```

or something else?

There is a subtle reason both currently give you the same number.

Find it.

---

# ⏱️ Part 2 — 5 minutes: Design

Your current `clean_data()` returns something like:

```python
{
    "clean_data": [...],
    "valid_data_cnt": 39,
    "invalid_data_cnt": 26,
    "json_cnt": 51,
    "csv_cnt": 14
}
```

Ask yourself:

> **Should `clean_data()` itself create the final pipeline summary?**

Or should `main.py` create the summary from the information it receives?

Don't immediately change the function.

Think about **responsibility**.

Remember our earlier lesson:

> Don't make a function responsible for things outside its job.

---

# ⏱️ Part 3 — 10 minutes: Build

Create a summary and print it.

Your output should be roughly:

```text
========== PIPELINE SUMMARY ==========

Total records : 65
Valid records : 39
Invalid records : 26

JSON records  : 51
CSV records   : 14
```

### Constraint 🚨

**Do not change your existing validation rules.**

Your pipeline should still produce:

```text
39 valid
26 invalid
```

We're only changing **how we report what happened**.

---

# 🧠 Bonus challenge — only if you finish early

You currently have:

```python
print(...)
```

inside `clean_data()`:

```python
print(f"""
CSV source: ...
JSON source: ...
Combined records: ...
""")
```

Think about this:

> **Should a reusable function print results, or should it return data and let `main.py` decide how to display it?**

Don't necessarily change it today.

Just think about it.

This connects directly to something you learned around **Day 15**:

> **Separate data from presentation.**

You've actually encountered this principle before. Today we're coming back to it.

---

# 🔥 Day 26 rule

You are **2 days late**.

So there is absolutely no:

> "I need to do extra today to compensate."

Nope.

Today's minimum:

### **15 minutes.**

If you naturally spend 30 minutes, great.

If you finish in 15, **also great.**

We're not paying interest on missed days. 😂

---

## 📋 Send me this when you're done

```text
Day 26
Time spent:

My answers:
1.
2.
3.

Pipeline summary:

Total:
Valid:
Invalid:
JSON:
CSV:

What I learned:
What confused me:
```

And one thing I especially want today:

> **Tell me why you decided to calculate/create the summary where you did.**

Don't just show me the code.

I want the engineering reasoning.

🔥 **Welcome back, SKM. Day 26 starts now.**
