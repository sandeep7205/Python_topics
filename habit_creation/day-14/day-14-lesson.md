SKM, **Day 14 is complete — and this was a useful 22 minutes.** Your pipeline now survives bad data instead of immediately falling over. That's exactly what we wanted.

One important thing first: your **habit battle being low** is actually the bigger win. You're starting to sit down without the same internal fight. That's the habit becoming normal.

## 🧠 Your Day 14 answers

### 1. `return` vs `print()`

You wrote:

> return some value else NaN, print is function to print something in terminal

You're halfway there.

The important distinction is:

```text
return → sends a value back to the caller
print  → displays something on the screen
```

`return` does **not** automatically mean `NaN` when there is no value.

For example, a function with no explicit `return` actually returns `None`.

---

### 2. `float("250.50")`

Correct. ✅

Technically the result is:

```text
250.5
```

The trailing zero isn't stored as part of the numeric value.

---

### 3. `float("abc")`

Correct. ✅

It raises:

```text
ValueError
```

---

### 4. Why isn't `if input_data['Amount']` enough?

You said:

> it gives error

Close, but there's a deeper reason.

This:

```text
"abc"
```

is **truthy**.

So:

```text
if "abc":
```

passes.

But `"abc"` still cannot be converted into a number.

That's why:

```text
checking whether data exists
```

and

```text
checking whether data is valid
```

are two different things.

**That's an important Data Engineering lesson.**

---

# 🔥 Your actual code

This is the most important change you made:

```python
try:
    ...
except ValueError:
```

You're beginning to separate:

```text
Expected data
     ↓
Try processing
     ↓
Bad data?
     ↓
Handle it
```

Good.

---

## But there's one bug you should notice

Look at this:

```python
if input_data['Category']:
    input_data['Category'] = input_data['Category'].strip().title()
    input_data['Amount'] = float(input_data['Amount'].strip())
```

You're checking whether **Category exists**, but you're not checking whether **Amount exists** before doing:

```python
input_data['Amount'].strip()
```

Your CSV contains:

```text
Tuesday,Food,
```

and:

```text
,Shopping,
```

So `Amount` can be an empty string.

In your current code, that eventually causes:

```text
ValueError
```

Your `except` catches it, so the program survives. ✅

But there's an interesting distinction:

### Your program currently says:

> "Try converting the amount. If it fails, I'll catch the error."

That's valid.

But robust data cleaning often thinks:

> "Is this data valid **before** I try to process it?"

We'll improve that later.

**Don't change it right now.** I want you to recognize the distinction first.

---

# ⚠️ Another thing I want you to notice

You have:

```python
except ValueError:
```

That's good for:

```text
float("abc")
```

But not every possible problem is a `ValueError`.

For example, if your dictionary didn't contain:

```text
'Category'
```

you could get a different exception:

```text
KeyError
```

Don't start catching every exception with:

```python
except Exception:
```

That's a common beginner mistake.

You want to catch **specific problems you actually expect**.

---

# 🧹 Your output counter

This was a good addition:

```python
valid_data_cnt += 1
invalid_data_cnt += 1
```

And:

```text
Valid rows: X
Invalid rows: Y
```

That's more useful than silently skipping bad records.

You now have a tiny form of **data quality reporting**.

---

# 🏆 Day 14 verdict

| Skill                    | Result |
| ------------------------ | ------ |
| `try/except`             | ✅      |
| `ValueError`             | ✅      |
| Missing data awareness   | 🟡     |
| Validation vs conversion | 🟡     |
| Cleaning                 | ✅      |
| Error handling           | ✅      |
| Data-quality counter     | ✅      |
| Pipeline structure       | ✅      |

### Day 14: **COMPLETE ✅**

And I want you to notice your progression:

```text
Day 8
Read a file
   ↓
Day 9
Count data
   ↓
Day 10
Parse CSV manually
   ↓
Day 11
Use DictReader
   ↓
Day 12
Clean data
   ↓
Day 13
Build functions
   ↓
Day 14
Handle bad data
```

That's a **logical progression**, not random Python exercises.

Tomorrow, we'll take the next small step: **make your pipeline return structured results instead of mixing processing with presentation.**

That will make your code feel much more like something you'd actually find in a real data-processing project.
