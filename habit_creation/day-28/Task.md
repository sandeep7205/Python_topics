Yes. And honestly, **the most important thing about Day 28 is not the code. It's that you're here again.**

You missed 2 days. Fine. No catch-up, no guilt, no “I need to compensate with 2 hours today.”

**Miss → return → continue.** That's the habit we're actually training.

### My suggestion for Day 28

Keep today's session to **15–25 minutes**.

Yesterday we learned:

> A function can accidentally mutate data it receives.

Today we'll use that lesson in a small but very real ETL problem:

### 🎯 Day 28 — Group data by `source` + `category`

You already have:

```text
JSON → Food → amount
JSON → Travel → amount
CSV  → Food → amount
CSV  → Travel → amount
```

Your existing `process_data()` only answers:

> “How much did I spend in each category?”

Today we'll make a **second function** that can answer:

> “How much did I spend in each category, separated by where the data came from?”

Something conceptually like:

```text
{
    "json": {
        "Food": ...,
        "Travel": ...
    },
    "csv": {
        "Food": ...,
        "Travel": ...
    }
}
```

Don't copy that into your code yet. **Design it yourself first.**

### Your Day 28 task

**Step 1 — 5 min**

Take 4–5 records from your cleaned data and manually write what the expected output should look like.

**Step 2 — 10 min**

Create a new function. Don't touch your existing `process_data()`.

Think about:

```python
def process_source_data(clean_data):
    ...
```

Ask yourself:

* How do I get `source`?
* How do I get `category`?
* What should happen if that source doesn't exist yet?
* Where should I add the amount?

**Step 3 — 5 min**

Test it with a tiny manually-created list first.

Don't immediately throw all 65 records at it.

---

### One mentor suggestion

**Do not try to “make up” the two missed days.**

That's exactly how your old cycle worked:

> miss → guilt → make huge plan → get overwhelmed → miss again.

We're deliberately breaking that pattern.

Today, **15 minutes counts as a complete Day 28.**

If you naturally go for 40 minutes, great. But the win condition is simply:

> **I showed up and moved the project forward.**

When you've written your first attempt, paste **only your function** here. I'll review it like a mentor—I'll point out what's wrong and give you hints rather than immediately handing you the answer.
