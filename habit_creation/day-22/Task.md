🔥 **LET'S SMOKE DAY 22, SKM.**

But we're keeping the rule: **15 minutes minimum.**
If you get into flow and want to go longer, great. But we're not *requiring* it.

# 🐍 Day 22 — Make Your Pipeline Reliable

Yesterday you built validation.

Today we take the next step:

> **What happens when something goes wrong while the pipeline is running?**

You've already used `try/except` for `ValueError`.

Today we're going to understand **where exceptions should be handled and where they should NOT be handled.**

### 🎯 Today's mission

Take your existing pipeline and identify **3 places where an error could realistically happen.**

For example:

```text
CSV/JSON file doesn't exist
        ↓
File can't be opened
        ↓
Invalid JSON structure
        ↓
Missing expected key
        ↓
Invalid data
        ↓
Processing
```

Don't write code yet.

### ⏱️ First 5 minutes — Recall

Without looking at your previous code, answer these:

1. What's the difference between `try` and `except`?
2. What happens when an exception occurs inside `try`?
3. What's the difference between `ValueError` and `TypeError`?
4. Why shouldn't we use this everywhere?

```python
except Exception:
```

5. What does `return` do when a function successfully finishes?

---

### ⏱️ Next 5 minutes — Think like a Data Engineer

Look at your current pipeline:

```text
read_json()
     ↓
clean_data()
     ↓
process_data()
     ↓
write_json()
```

For **each function**, ask:

> "What can realistically go wrong here?"

Example:

```text
read_json()
    └── ?

clean_data()
    └── ?

process_data()
    └── ?

write_json()
    └── ?
```

Write **one or two possible failures** beside each.

Don't worry about fixing them yet.

---

### ⏱️ Final 5 minutes — Your challenge

Pick **ONE** failure from `read_json()`.

Your job:

1. Make the failure happen intentionally.
2. Observe the exception.
3. Decide which exception type it produces.
4. Add the **smallest possible** handling for it.
5. Run the pipeline again.

**Don't try to make the entire pipeline bulletproof.**

That's today's trap. 😄

We're practicing:

> **One problem → understand it → handle it → move on.**

---

### 🧠 Day 22 rule

If you suddenly get an idea like:

> "Wait, I could build a generic exception framework with custom exceptions, decorators, logging, retry logic..."

😂

Write it down.

Then tell yourself:

> **"Cool idea. Day 22 doesn't need it."**

That's exactly the lesson we learned yesterday.

### 📋 When you're finished

Send me:

```text
Day 22
Time spent:
What I learned:
What I tried:
Exception I found:
How I handled it:
What confused me:
```

**No solution from me upfront. You drive the code; I'll review it.**

Now go. **15 minutes. 🔥**
