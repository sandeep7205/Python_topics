🔥 **Day 27 — DONE, SKM.**

And this was a **very good learning experiment** because you predicted the behavior *before* running it, then compared your prediction with Python's actual behavior.

You got both experiments right.

### Experiment 1

```python
def change_data(input_data):
    input_data["name"] = "SKM"
```

Result:

```python
{'name': 'SKM', 'skills': ['Python', 'SQL']}
```

Because `input_data` and `data` refer to the **same dictionary object**.

```text
data ─────────────┐
                  ↓
            same dictionary
                  ↑
                  │
input_data ───────┘
```

So changing `input_data` changes `data`.

---

### Experiment 2

You did:

```python
input_data = input_data.copy()
```

Now:

```text
data
 ↓
original dictionary

input_data
 ↓
new dictionary
```

So:

```python
input_data["name"] = "SKM"
```

changes only the copy.

Therefore:

```python
data
```

stays:

```python
{'name': 'Sandeep', 'skills': ['Python', 'SQL']}
```

Exactly as expected. ✅

---

# And you fixed your actual pipeline

This was the important part:

```python
summary_data = summary_data.copy()

if "clean_data" in summary_data:
    del summary_data["clean_data"]
```

Now `data_summary()` can modify its **local copy** without modifying `get_clean_data`.

Your test proves it:

```text
Before summary:
clean_data → YES

After summary:
clean_data → YES
```

🔥 That's the proof I wanted.

---

## One tiny wording correction

You wrote:

> "delete from the local variable & the original data got unchanged"

Almost.

More precisely:

```text
summary_data = summary_data.copy()
```

creates a **new dictionary** and makes the local variable `summary_data` point to it.

Then:

```python
del summary_data["clean_data"]
```

deletes the key from that **new dictionary**, not the original.

The original remains untouched.

That's the important mental model.

---

# 🧠 Why this matters for your Data Engineering journey

Imagine:

```python
get_clean_data
```

contains:

```text
65 records
39 valid
26 invalid
clean_data = [...]
```

If some reporting function accidentally does:

```python
del summary_data["clean_data"]
```

without copying, you've silently destroyed information that another part of the pipeline might still need.

That's the kind of bug that's annoying because:

> **Nothing crashes.**

The program simply behaves differently later.

Understanding mutation helps you prevent those bugs.

---

# Your progression is getting interesting

You've now gone from:

```text
variables
 ↓
loops
 ↓
functions
 ↓
files
 ↓
CSV
 ↓
JSON
 ↓
validation
 ↓
exceptions
 ↓
multiple sources
 ↓
metadata
 ↓
tracebacks
 ↓
pipeline summaries
 ↓
mutation
```

And you're not just memorizing definitions.

You're **testing behavior**.

That's much more valuable.

---

### 🟢 Day 27 COMPLETE

And I noticed something else:

You came back after being two days late, then completed Day 26 and Day 27.

That's exactly our system:

**Miss → return → continue.**

No restart. No guilt. No "I have to compensate."

Just keep moving.

🔥 **Day 27 is parked.**

Tomorrow we can take the next step with the pipeline.
