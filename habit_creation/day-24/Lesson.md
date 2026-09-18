SKM 🔥 **Day 24 is DONE — and you went deeper than the task.**

You said **1 hour above**, and based on the timestamps in this conversation, you were working from roughly **7:59 PM to 9:38 PM**, so that's about **1h 39m elapsed**. There may have been pauses, so I wouldn't call all of that study time. Your honest report of **"1 hour above"** is the better number to record.

And I want to highlight something: **you experimented instead of blindly following my suggested implementation.** That's exactly what I want.

---

# 🔥 What you built

You created:

```python
def add_value(data_type, datas, value):
```

and experimented with:

```python
updated_data = list(map(lambda d: d | value, datas))
```

That's a legitimate reusable transformation.

You then used the same idea for both sources:

```text
JSON → add source=json
CSV  → add source=csv
```

Result:

```text
JSON = 51
CSV  = 14
--------------
Total = 65
```

And your cleaning still produced:

```text
Valid   = 39
Invalid = 26
```

So you added metadata **without breaking the existing pipeline.**

That's a solid result. 🟢

---

# One thing I want you to notice

You actually discovered an important design principle:

### Before

```text
read_json()
read_data()
```

were doing two things:

```text
READ DATA
+
MODIFY DATA
```

Now you've experimented with separating:

```text
READ
 ↓
ADD METADATA
 ↓
CLEAN
 ↓
PROCESS
```

That's closer to the separation-of-responsibilities thinking we want.

---

# About this part

You added:

```python
source = clean_data['source']
```

inside `process_data()`.

But then you don't use `source`.

That's okay **for today's experiment**, but it's a clue.

You were thinking yesterday:

> category → json / csv

But your current `process_data()` still does:

```text
category → total amount
```

So `source` is currently just **carried through the pipeline**, not actually used for calculation.

And that's fine.

In fact, this is a nice place to stop rather than forcing a new feature.

---

# 🧠 Your biggest question today: `{e}`

You said:

> the exception `{e}` doesn't give me exact error line or function or any other details

**Correct observation.**

When you do:

```python
except KeyError as e:
    print(e)
```

`e` contains the **exception information/message**, not the complete debugging context.

For example:

```python
print(e)
```

might give:

```text
'developer'
```

That's useful, but it doesn't tell you:

```text
which function?
which file?
which line?
what was the call chain?
```

### That's where traceback comes in.

Python has a module specifically for this:

```python
import traceback
```

and:

```python
traceback.print_exc()
```

That gives you the traceback showing the path the exception took, including the relevant line.

Conceptually:

```text
main.py
   ↓
read_json()
   ↓
some_function()
   ↓
ERROR
   ↓
line number
```

This is exactly the thing you were looking for.

**But don't add it tonight.**

We've identified the next concept.

---

# ⚠️ One correction to your Day 24 thinking

You wrote:

> Should process_data() know about the source? Nice idea, we can add another calculation with existing one by adding source condition...

That's a good thought, but don't automatically add it.

Ask:

> **"Does the output requirement actually need source-level totals?"**

If yes:

```text
Travel
 ├── JSON → 996.24
 └── CSV  → 550.00
```

then `process_data()` needs to understand source.

If no:

```text
Travel → 1546.24
```

then `process_data()` doesn't need source at all.

That's an important engineering habit:

> **Don't make a component more complicated just because you have more data available.**

Use information when the requirement needs it.

---

# And your Day 24 lesson is bigger than `map()`

You learned:

```text
Data
 ↓
attach metadata
 ↓
preserve metadata
 ↓
process data
```

That concept will matter later when you encounter things like:

```text
source_system
ingestion_time
file_name
batch_id
record_id
```

You don't need to learn those yet.

Today it was simply:

```text
source = "json"
source = "csv"
```

That's enough.

---

# 🟢 Day 24 Scorecard

| Area                          | Result |
| ----------------------------- | ------ |
| Understand data structures    | ✅      |
| Combine multiple sources      | ✅      |
| Add metadata                  | ✅      |
| Reusable transformation       | ✅      |
| Preserve existing pipeline    | ✅      |
| Experiment independently      | ✅      |
| Identify traceback limitation | ✅      |

And one habit point:

**You showed up again.**

Day 21 → Day 22 → Day 23 → **Day 24**

That's the streak that matters.

Not whether every session is exactly 15 minutes.

---

## 🔥 Day 24 COMPLETE.

**Tomorrow's Day 25 will be about the exact problem you discovered today:**

> **How do I actually debug an exception and find the exact line where things went wrong?**

We'll learn **tracebacks**, but keep it practical and small.

For tonight:

**Close the laptop. You're done.** 😄🔥
