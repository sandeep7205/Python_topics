SKM, **this was a very good Day 22.** 🔥

And 50 minutes is fine. You started with a 15-minute minimum, then stayed because you were actually working through the problem. That's different from forcing yourself to study for 50 minutes.

More importantly, you didn't just copy the concept—you **intentionally broke the pipeline and observed the exceptions.** That's exactly the exercise.

## First: your answers

### 1. `try` vs `except`

Your answer is basically correct.

A cleaner mental model:

```text
try
 └── "Run this code and watch for an exception."

except
 └── "If that particular exception happens, handle it here."
```

---

### 2. What happens when an exception occurs?

Correct. 👍

Python stops executing the remaining statements in the `try` block and looks for a matching `except`.

---

### 3. `ValueError` vs `TypeError`

You're **mostly right**, but there's an important distinction.

Don't memorize:

> ValueError = any value exception

Instead:

**`ValueError`**

> The type is acceptable, but the actual value isn't acceptable for that operation.

Example:

```python
float("hello")
```

It's a string, and `float()` accepts strings—but `"hello"` isn't a valid numeric value.

**`TypeError`**

> The operation doesn't support that type.

Example:

```python
"hello" + 10
```

Python doesn't know how to add a string and integer.

So:

```text
ValueError → right type, bad value
TypeError  → wrong/incompatible type
```

That's the distinction I want you to remember.

---

### 4. `except Exception`

Your answer needs correction here.

You said:

> exception doesn't handle all types

Actually, **`except Exception:` catches almost all normal exceptions.**

That's precisely why we don't blindly use it.

If you do:

```python
except Exception:
    print("Something went wrong")
```

you've potentially hidden the *real* problem.

For example:

```text
KeyError
TypeError
ValueError
OSError
JSONDecodeError
...
       ↓
except Exception
       ↓
"Something went wrong"
```

You lose useful information about what actually happened.

Your instinct to catch **specific exceptions** is correct.

---

# Now let's review your actual code

There are some genuinely good improvements here.

### 👍 Good: specific handling

You added:

```python
except KeyError as e:
    ...
except TypeError as e:
    ...
```

That's much better than:

```python
except Exception:
```

because your program now communicates **what kind of problem occurred**.

---

## 👍 Good: you noticed `JSONDecodeError`

You correctly discovered:

```python
json.JSONDecodeError
```

But there's an interesting issue in your `read_json()`:

```python
def read_json(json_file_path):
    with open(json_file_path, "r") as read_file:
        try:
            get_data = json.load(read_file)
        except json.JSONDecodeError as e:
            get_data = {}
    return get_data
```

You're catching the error **inside `read_json()`**.

That means your `main.py` never gets to know that malformed JSON occurred.

Instead:

```text
Bad JSON
   ↓
read_json()
   ↓
JSONDecodeError
   ↓
caught here
   ↓
return {}
   ↓
main.py
```

And then `main.py` might encounter:

```python
get_json_data['developer']
```

and produce:

```text
KeyError: 'developer'
```

So the original problem was **bad JSON**, but the error you see later is **missing key**.

That's an important Data Engineering lesson.

> **Where you catch an exception changes what the rest of your pipeline knows about the failure.**

---

# Your biggest question: `clean_data()` and `process_data()`

You asked:

> what to put in clean_data() & process_data() as we handle before them or using if/else

Excellent question.

And here's where I want you to **stop for today**.

Don't add more exception handling yet.

Because your current architecture already has two different kinds of protection:

```text
                    VALIDATION
                        ↓
Raw data → clean_data() → valid cleaned data
                              ↓
                        process_data()
```

### `clean_data()`

Its job is already:

> **"Is this individual expense acceptable?"**

That's why your `if/else` validation makes sense there.

For example:

```text
category missing → invalid
amount missing   → invalid
bad amount       → invalid
valid            → clean
```

That's **data validation**, not exception handling.

### `process_data()`

Its job is:

> **"I have clean data. Now calculate something."**

So you shouldn't randomly add `try/except` just because exceptions exist.

That's the key lesson.

---

# 🔥 Your CSV idea

You wrote:

> idea: to concat the CSV data and write the total into json

**YES.**

That's actually a very good next step.

You already have:

```text
JSON → clean → process → JSON
```

And you already have:

```text
CSV → clean → process
```

Now you're thinking:

```text
             ┌── JSON ──┐
             │          ↓
CSV → clean → process → combined totals → JSON
```

That's much closer to an actual ETL-style exercise.

But **don't start it tonight.**

You've already done enough.

---

# 🧠 Day 22 lesson

Today you learned three different layers:

```text
1. VALIDATION
   "Is this data acceptable?"

2. EXCEPTION HANDLING
   "Something unexpected happened while executing."

3. PIPELINE LOGIC
   "What should we do with valid data?"
```

Those are **not the same thing**.

And I think this is exactly why you got confused today.

You were asking:

> "If I already validate everything, why do I need exceptions?"

Because validation handles **expected bad data**.

Exceptions handle **unexpected execution problems**.

For example:

```text
amount = "abc"
        ↓
Expected bad input
        ↓
Validation
```

versus:

```text
JSON file suddenly becomes malformed
        ↓
Execution cannot continue normally
        ↓
Exception
```

That's the distinction.

---

## One correction I'd make tomorrow

Don't immediately start building the CSV + JSON combination.

First, we'll spend a few minutes cleaning up the exception architecture you created today.

Then we'll build your **CSV + JSON → combined result → JSON** idea.

That's a much better Day 23.

And SKM — **today's frustration was useful.**

You pushed far enough to discover a real architectural question instead of just completing a toy exercise.

That's exactly the kind of question I want you asking as you move toward Data Engineering.

**Day 22 🟢 COMPLETE.**

Go enjoy your evening. You've earned it. 🔥
