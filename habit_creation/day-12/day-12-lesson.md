SKM — **Day 12: ✅ Recovered and completed.**

First, I want to correct one thing in your thinking:

> **"Day 13 as punishment to myself."**

No.

**We do not use studying as punishment.**

You missed yesterday because you slept. Today you came back and completed the task. That's a recovery, not a debt.

If you turn this into:

> missed Day 12 → punish myself with extra work

you'll eventually make learning feel like something painful, and your brain will start avoiding it.

Our rule is:

> **Missed day → resume. No punishment. No catching up.**

And that's exactly what you did today.

---

# 🧠 Your Day 12 code review

Your solution is clean for your current level.

This is particularly good:

```python
if content['Category'] and content['Amount']:
```

You're checking whether the required fields exist before processing them.

Then:

```python
category = content['Category'].strip().title()
```

You've combined two transformations:

```text
" food "
   ↓ strip()
"food"
   ↓ title()
"Food"
```

That's a very useful pattern.

---

# ⭐ You successfully handled dirty data

Suppose the CSV contains:

```text
 food 
FOOD
Food
 food
```

Your code normalizes them to:

```text
Food
```

Then your dictionary can correctly aggregate them.

That's the entire point of today's exercise.

---

# One important correction

You wrote:

> "`csv.reader()` returns list and `DictReader` returns dictionary"

That's **mostly correct at the row level**, but let's make the mental model precise.

### `csv.reader`

Each row behaves like a list:

```text
['Monday', 'Food', '250']
```

### `csv.DictReader`

Each row behaves like a dictionary:

```text
{
    'Date': 'Monday',
    'Category': 'Food',
    'Amount': '250'
}
```

Good enough for now.

---

# Your missing-data handling is good

You wrote:

```python
if content['Category'] and content['Amount']:
```

Otherwise:

```python
print("Skipping invalid row")
```

That's exactly what I wanted from the bonus.

Your pipeline now has:

```text
CSV
 ↓
Read
 ↓
Validate
 ↓
Clean
 ↓
Convert
 ↓
Aggregate
```

That's becoming a real little data pipeline.

---

# One thing to think about

You are currently doing:

```python
amount = int(content['Amount'].strip())
```

What if the amount is:

```text
"abc"
```

The field isn't empty, so:

```python
if content['Amount']:
```

passes.

But `int("abc")` will fail.

Don't fix this yet.

**That's our next level of validation.**

You've just discovered an important distinction:

### Missing data

```text
Amount = ""
```

### Invalid data

```text
Amount = "abc"
```

They're not the same problem.

That's a very useful Data Engineering concept.

---

# Your memory is getting stronger

Your answers are becoming faster and more accurate.

Especially:

> `total += amount` → `total = total + amount`

That's exactly the kind of thing I want to become automatic.

You're no longer spending your mental energy remembering basic syntax as much.

That means we can gradually start focusing on **problem solving**.

---

# 📊 Day 12

| Area                         |    Result |
| ---------------------------- | --------: |
| Recall                       |  **9/10** |
| Data cleaning                |  **9/10** |
| Validation                   |  **8/10** |
| CSV handling                 |  **9/10** |
| Problem solving              |  **9/10** |
| Independence                 |  **9/10** |
| Recovery after missing a day | **10/10** |

And **24 minutes** is perfect.

You didn't force yourself to make up the previous day.

You simply came back.

That's the behavior we want.

---

# 🔵 Day 13 — What we're doing next

Tomorrow we're going to focus on:

## **Functions + Data Pipeline**

You've been writing the same types of operations repeatedly:

```text
read CSV
clean category
convert amount
validate
aggregate
```

Now we're going to start separating these responsibilities into functions.

Something conceptually like:

```text
read_data()
     ↓
clean_data()
     ↓
process_data()
     ↓
show_result()
```

This is an important step toward writing code that isn't one giant block.

And **you already learned functions on Day 7**, so we're bringing that knowledge back.

---

### One rule for Day 13

Don't try to compensate for missing Day 12.

No 1-hour punishment session.

No "I need to finish two days today."

Just:

> **Day 13 → 15-minute minimum → normal progress.**

You missed one day.

**You came back. That's the important part.**

Day 12 is officially closed. 🟢

Tomorrow we ride Day 13. 🔥
