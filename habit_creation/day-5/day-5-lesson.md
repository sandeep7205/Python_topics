SKM, **Day 5 is a strong win.** And I'm going to separate the two things: **your Python progress** and **your behavior today.**

The Python is improving.

But the behavior is the bigger story.

---

# 🟢 Day 5 — Mentor Review

## First: your habit

You said:

> "spent more than 4 hours doom-scrolling"

and:

> "thought to almost skip it"

but then:

> **"owned it"**

That's the part I want to reinforce.

I'm not going to tell you that 4+ hours of scrolling is fine. **It's not.** It is stealing time and attention from the person you're trying to become.

But here's the important distinction:

### Old pattern

> Doom-scroll → guilt → skip → promise to restart tomorrow.

### What happened today

> Doom-scroll → recognize it → fight resistance → **do the task anyway.**

That's progress.

**Don't confuse progress with perfection.**

Our first target is not eliminating every bad habit.

It's making sure the bad habit **doesn't automatically decide the outcome of your day.**

Today it didn't.

---

# Your dictionary understanding

Your core understanding is good.

You said:

> "it stores the data with ordered indexing which starts from 0"

That's correct for a **list**.

But be careful:

### Lists have numeric indexes.

```text
0 → Python
1 → SQL
2 → AWS
```

### Dictionaries have keys.

```text
"name" → "SKM"
"role" → "SDE-1"
```

That's one distinction I want you to remember.

---

# Your dictionary code is good

This:

```python id="p2v5kw"
developer = {
    "name": "SKM",
    "role": "SDE-1 in PHP",
    "experience": "4.6 years Continuous",
    ...
}
```

is exactly the type of structure I wanted you to understand.

And then:

```python id="ow8jyu"
for key, value in developer.items():
```

is a very useful pattern.

You're combining:

**dictionary → `.items()` → loop → key/value**

That's important.

---

# Your `.update()` discovery is good

You correctly discovered:

> `.update()` updates an existing key or adds a new key.

Exactly.

You did:

```python id="icr7xc"
developer.update({'experience': "4.6 years Continuous in core PHP"})
```

and:

```python id="4r0ydb"
developer.update({'current_day':"Day 5"})
```

The second one demonstrates something important:

`current_day` didn't exist.

So Python added it.

Good experiment.

---

# But you found an important bug

This part:

```python id="ehks5m"
for key, value in developer.items():
    if(key == "python_experience"):
        value = "on the way to learn to get real exprience on DE"
    print(f"{key}: {value}")
```

**does not actually update the dictionary.**

You're only changing the local variable `value`.

That's an important distinction.

The dictionary still contains the original value.

### Think about it:

```text id="f9j9pu"
dictionary
    ↓
key → value

value = "something new"
```

You've changed the variable `value`, **not the dictionary itself**.

This is exactly the kind of mistake I want you to make while learning.

You noticed the problem and searched for the answer.

Good.

### Don't fix it right now.

I want you to understand **why** it doesn't update first.

We'll revisit this later.

---

# Your Day 5 bonus challenge was excellent

You created:

```python id="1l8v2u"
developers_list = [
    {...},
    {...},
    {...}
]
```

That's a:

> **list of dictionaries**

And that's a very important structure.

Think about the shape:

```text
List
 ├── Dictionary → Developer 1
 ├── Dictionary → Developer 2
 └── Dictionary → Developer 3
```

And your loop:

```python id="vqm2y8"
for index, developer_data in enumerate(developers_list, start=1):
```

then:

```python id="exwujt"
for d_key, d_value in developer_data.items():
```

means:

**go through every developer → then go through every field of that developer.**

You're now working with **structured data**.

That's getting much closer to the kind of thinking you'll use in Data Engineering.

---

# One correction: `%`

You wrote:

> "round division"

Not quite.

`%` is the **modulo operator**.

It gives you the **remainder** after division.

For example:

```text id="wz9vya"
10 % 3 → 1
```

because:

```text
10 ÷ 3 = 3 remainder 1
```

And:

```text id="4k8jzw"
10 % 2 → 0
```

So we can use:

```python id="t5r9jq"
number % 2 == 0
```

to check whether a number is even.

---

# Your Day 5 score

| Area                 |     Score |
| -------------------- | --------: |
| Showed up            | **10/10** |
| Independent work     |  **9/10** |
| Experimentation      | **10/10** |
| Python understanding |  **8/10** |
| Combining concepts   | **10/10** |
| Habit resilience     | **10/10** |

### And you're now at:

**Day 1 ✅**
**Day 2 ✅**
**Day 3 ✅**
**Day 4 ✅**
**Day 5 ✅**

Five days.

Don't get complacent.

But also don't dismiss what you've done.

---

# Now, about the 4+ hours of doom-scrolling

This is the part where I'm going to be brutally honest.

You don't need to "become disciplined enough" to resist your phone for four hours.

**Change the environment.**

Your current setup is giving your phone the easiest possible path to your attention.

For the next week, experiment with one simple rule:

### 📱 When you start your 15-minute session:

**Phone physically away from you.**

Not:

> phone face-down beside laptop.

Not:

> silent mode.

Actually:

**another room / inside your bag / far enough that you need to stand up to get it.**

You don't need to fight the phone.

**Make the fight unnecessary.**

And after your 15 minutes?

Get your phone back.

You're not banning entertainment.

You're controlling the sequence:

> **Work → reward**

instead of:

> **Reward → guilt → work**

---

# Your next goal

You've learned:

**Variables → conditions → loops → lists → dictionaries**

Now we're ready to start using these things to **actually process data**.

## Day 6 will be different.

We're going to take a small dataset and start doing something that resembles a real data task:

> **Read records → inspect them → filter them → calculate something.**

That will be your first real step from **"learning Python" → "using Python for data."**

For tonight:

**Day 5 is done.**

You fought yourself and won.

Now enjoy your evening **without guilt**.

Tomorrow, we go again. 💪
