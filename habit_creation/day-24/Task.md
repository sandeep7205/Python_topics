🔥 **DAY 24 — LET'S ACQUIRE IT, SKM.**

Yesterday you successfully combined:

```text
JSON + CSV
    ↓
ONE dataset
    ↓
clean
    ↓
process
    ↓
JSON
```

Today we're going to answer a question that real data pipelines constantly need to answer:

> **"Where did this record come from?"**

That's called **data lineage / provenance**.

And we're going to learn it without turning this into a huge framework.

---

# 🎯 Day 24 — Track the Data Source

Currently, after combining your data, you can't tell whether:

```python
{"category": "Travel", "amount": 100}
```

came from:

```text
JSON?
CSV?
```

Today, we're going to preserve that information.

Our target is conceptually:

```text
JSON record
    ↓
{"category": "Travel", "amount": 100, "source": "json"}

CSV record
    ↓
{"category": "Travel", "amount": 200, "source": "csv"}
```

Then your pipeline can answer:

> "How much Travel expense came from each source?"

---

## ⏱️ First 5 minutes — Think

Before coding, answer these in comments:

### 1. Where should we add the source information?

Option A:

```text
read_json()
```

Option B:

```text
read_data()
```

Option C:

```text
clean_data()
```

Think about **what each function's responsibility is**.

---

### 2. What should the source value be?

For example:

```text
"json"
"csv"
```

Would you use uppercase? Lowercase?

There's no hidden correct answer here. **Define a convention and stay consistent.**

---

### 3. Do we need to modify `process_data()`?

Think carefully.

Your current `process_data()` calculates:

```text
category → amount
```

But now we eventually want something more like:

```text
category
   ├── json
   └── csv
```

Should `process_data()` know about the source?

**Don't change it yet. Just reason about it.**

---

# ⏱️ Next 10 minutes — Build the simplest version

I want you to modify your pipeline so that **every expense knows its source before the lists are combined.**

Your flow should become:

```text
             JSON
              ↓
        add source=json
              ↓
           JSON list
              │
              │
              ├────── COMBINE
              │
              │
           CSV list
              ↑
        add source=csv
              ↑
             CSV
```

Then:

```text
Combined list
      ↓
clean_data()
      ↓
process_data()
```

### Important constraint 🚨

**Don't redesign `clean_data()` yet.**

Try to preserve the existing pipeline as much as possible.

You're learning how to add information to existing data without breaking the pipeline.

---

# 🧪 Your test

After you've added the source, **print the combined data before cleaning.**

I want to see something like:

```text
JSON:
{'category': 'Travel', 'amount': 45.99, 'source': 'json'}

CSV:
{'date': 'Monday', 'category': 'Utilities', 'amount': '250', 'source': 'csv'}
```

Your exact output will obviously depend on your implementation.

Then run the complete pipeline and verify that your final totals **haven't changed**.

That's important:

> Adding metadata should not accidentally change the actual expense calculations.

---

# 🧠 Today's concept

Think of `source` as **metadata**.

The actual business data is:

```text
category
amount
```

Metadata describes the data:

```text
source
date
file
timestamp
pipeline_run_id
```

Eventually, in real Data Engineering, you'll see a lot of this.

For example:

```text
record
├── customer_id       ← actual data
├── amount            ← actual data
├── transaction_date  ← actual data
│
├── source_system     ← metadata
├── ingestion_time    ← metadata
└── batch_id          ← metadata
```

You don't need all of that today.

**Today = just `source`.**

---

## ⚠️ And I know your brain now 😂

You're probably going to think:

> "Wait... what if JSON has source + filename + timestamp + record ID + checksum..."

STOP. 😂

Write those ideas down.

Today's mission is:

```text
JSON → source=json
CSV  → source=csv
       ↓
   combine
       ↓
    clean
       ↓
   process
```

**15 minutes minimum.**

If you naturally go longer, great.

Then send me:

```text
Day 24
Time spent:

Where I added source:

JSON source:
CSV source:

Combined records:

Final totals:

What I learned:
What confused me:
```

🔥 **Go acquire Day 24.**
