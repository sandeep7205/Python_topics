SKM — **this is a solid Day 28 implementation.** You didn't just follow the hint; you actually figured out the nested dictionary structure yourself.

Your core function is correct:

```python
source_category_dict = {}

for data in clean_data:
    category = data['category']
    amount = data['amount']
    source = data['source'] if 'source' in data and data['source'] else 'no_source'

    if source not in source_category_dict:
        source_category_dict.update({source:{}})

    if category not in source_category_dict[source]:
        source_category_dict[source].update({category:amount})
    else:
        source_category_dict[source][category] += amount
```

### What you learned today

You went from:

```text
category → amount
```

to:

```text
source
   ↓
category
   ↓
amount
```

That's an important step.

Your resulting structure should look roughly like:

```json
{
    "json": {
        "Travel": 1546.24,
        "Food": 1259.25
    },
    "csv": {
        "Utilities": 400.0,
        "Mobile": 550.0
    }
}
```

Obviously your actual numbers depend on the valid records.

### One thing I want you to notice

You wrote:

```python
if source not in source_category_dict:
    source_category_dict.update({source:{}})
```

and then:

```python
if category not in source_category_dict[source]:
    source_category_dict[source].update({category:amount})
```

You are now **navigating a nested dictionary** rather than just working with a flat dictionary.

That's exactly the kind of thing I wanted you to practice.

---

### 🧐 One small improvement — don't change it yet

This:

```python
source = data['source'] if 'source' in data and data['source'] else 'no_source'
```

works, but eventually we'll make this cleaner.

And this:

```python
source_category_dict.update({source:{}})
```

works too, but there's a more natural Python way:

```python
source_category_dict[source] = {}
```

**Don't refactor it yet.** I want you to first understand what you wrote.

---

### One important thing I noticed in `main.py`

You have:

```python
clean_json_data['sorce_expenses'] = get_process_source_data
```

You wrote **`sorce_expenses`** instead of:

```python
source_expenses
```

Tiny typo, but this is exactly why output validation matters in a pipeline.

---

### And your biggest win today

You were **2 days late**.

But look at what happened:

> You came back → got the task → wrote a new ETL transformation → integrated it into `main.py`.

That's much more valuable for your long-term goal than maintaining a perfect 28-day streak.

**Day 28 = DONE ✅**

Don't add another feature today. Let this one settle.

Tomorrow, we'll take this result and start thinking like a data engineer about **validation and pipeline reliability**, rather than just making the code work.
