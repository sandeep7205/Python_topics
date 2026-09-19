SKM 🔥 **Day 25 is complete.** And you actually found the traceback you were looking for.

You correctly identified:

* `KeyError`
* `TypeError`
* `ValueError`
* file paths
* line numbers
* the failing operation

That's the real skill today.

## First, let's fix your three predictions

### 1. `import traceback`

You said:

> "it trace where every lines got tracked"

Close, but slightly off.

`import traceback` **imports Python's traceback module**. It gives you tools for working with and displaying the traceback of an exception.

It doesn't continuously track every line of your program.

Think:

```text
traceback
    ↓
exception happens
    ↓
show me the path Python took before reaching the error
```

---

### 2. `traceback.print_exc()`

You said:

> "it prints only the exceptions"

This is the biggest correction for today.

It prints the **current exception's full traceback**, not just the exception.

That's why you got:

```text
File → line → statement → exception
```

For example:

```text
Traceback (most recent call last):
  File "...main.py", line 34, in <module>
    ...
  File "...expense_pipeline.py", line 102, in clean_data
    ...
ValueError: could not convert string to float: 'abc123'
```

That's exactly what you wanted yesterday.

---

### 3. `print(e)` vs `traceback.print_exc()`

Your prediction here was off, but this is a useful mistake.

`e` **does contain the exception object**.

For example:

```python
except ValueError as e:
    print(e)
```

might produce:

```text
could not convert string to float: 'abc123'
```

Whereas:

```python
except ValueError:
    traceback.print_exc()
```

gives you the **full traceback path**.

So:

```text
print(e)
   ↓
"What went wrong?"

traceback.print_exc()
   ↓
"What went wrong + where + how we got there?"
```

That's the mental model I want you to keep.

---

# 🔥 Your three experiments

### KeyError

You found:

```text
main.py
line 44

expense_pipeline.py
line 118

KeyError: 'source'
```

Excellent.

And notice something important:

**You got two files in the traceback.**

That's because the error travelled through your program:

```text
main.py
   ↓
expense_pipeline.py
   ↓
failure
```

That's the power of a traceback.

---

### ValueError

You found:

```text
expense_pipeline.py
line 102

ValueError:
could not convert string to float: 'abc123'
```

Perfect.

And this is particularly useful because your `clean_data()` is intentionally handling that exception.

So you can see:

```text
bad data
   ↓
float("abc123")
   ↓
ValueError
   ↓
except ValueError
   ↓
invalid_data_cnt += 1
```

That's a real data-cleaning scenario.

---

### TypeError

You found:

```text
main.py
line 34

TypeError:
list indices must be integers or slices, not str
```

Again, excellent.

You're now reading the **actual meaning** of Python's errors instead of just seeing "program crashed."

---

# 🚨 Now your interesting question

You asked:

> "I have send traceback as argument in clean_data for child to use... don't need to import twice?"

**Yes — you noticed something important.**

You currently have:

```python
import traceback
```

in `main.py`.

Then:

```python
get_clean_data = pe.clean_data(
    merge_csv_json_data,
    traceback
)
```

and:

```python
def clean_data(input_content, traceback):
```

This technically works.

But **I don't recommend doing this.**

You're passing a whole module into a function just so the function can call:

```python
traceback.print_exc()
```

That's unnecessary coupling.

### Better mental model

If `expense_pipeline.py` needs the `traceback` module, it should simply import it itself:

```text
main.py
   └── traceback

expense_pipeline.py
   └── traceback
```

That's perfectly normal.

Python doesn't say:

> "Oops, traceback was already imported somewhere else."

Each module has its own namespace.

And importing the same module in different files is normal Python practice.

So you don't need:

```python
clean_data(input_content, traceback)
```

You can eventually have:

```python
def clean_data(input_content):
```

and let `expense_pipeline.py` import what it needs.

**But don't change it tonight.**

You've already completed the lesson.

---

# One more thing I noticed

You have:

```python
except ValueError:
    traceback.print_exc()
    return_dict['invalid_data_cnt'] += 1
```

This means you're now printing a traceback for an **expected invalid input** like:

```text
abc123
```

That's technically useful while debugging.

But in a production data pipeline, you probably wouldn't want a huge traceback printed every time a normal bad record appears.

This gives us another important distinction:

```text
Development/debugging
        ↓
Full traceback is useful

Expected bad data
        ↓
Usually record/report the bad data
        ↓
Don't necessarily dump a traceback
```

We'll revisit that later.

---

# 🧠 Day 25 takeaway

You now have three levels of information:

```text
print(e)
    ↓
Exception message

traceback.print_exc()
    ↓
Exception message
+ file
+ line
+ call path

Debugger/logging
    ↓
Even more context
```

You don't need the third one yet.

For now:

> **Learn to read the traceback before trying to fix the traceback.**

That's a very good developer habit.

---

## 🟢 DAY 25 COMPLETE

And look at your progression:

**Day 21:** Data validation
**Day 22:** Exception handling
**Day 23:** Multiple data sources
**Day 24:** Data lineage metadata
**Day 25:** Debugging with tracebacks

That's a pretty meaningful five-day progression.

And you did something I really like today:

**You made wrong predictions before testing.**

That's actually a powerful learning technique.

You predicted → ran it → saw reality → corrected your mental model.

That's how you build understanding instead of memorizing Python syntax.

🔥 **Park Day 25.**

Tomorrow we ride into **Day 26.**
