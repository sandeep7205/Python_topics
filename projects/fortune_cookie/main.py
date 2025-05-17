import json
import random
import os
import sys   # for a clean exit

# ───────────────────────────────────────────────────────────
# 1.  Helper: show one random fortune from a category
# ───────────────────────────────────────────────────────────
def show_fortune(quotes_dict: dict, category: str) -> None:
    """Pick and print a random fortune from the chosen category."""
    print(f"\n🧧 Fortune from '{category.capitalize()}' category:")
    print("────────────")
    print(random.choice(quotes_dict[category]))
    print("────────────")

# ───────────────────────────────────────────────────────────
# 2.  Load JSON from file
# ───────────────────────────────────────────────────────────
FILE_PATH = "projects/fortune_cookie/fortunes.json"

if not os.path.exists(FILE_PATH):
    sys.exit("\n❌ File not found.\n")

with open(FILE_PATH, "r") as file:
    fortunes = json.load(file)

if not fortunes or "quotes" not in fortunes:
    sys.exit("\n⚠️ Content not found in JSON.\n")

quotes = fortunes["quotes"]          # dict of categories → list[str]
categories = list(quotes.keys())     # list of category names

# ───────────────────────────────────────────────────────────
# 3.  Main loop – wrapped to catch Ctrl+C
# ───────────────────────────────────────────────────────────
print("🥠 Welcome to the Fortune Cookie Program!")

YES = {"y", "yes"}         # accepted “yes” answers
again = "y"

try:
    while again in YES:
        # ── list categories ────────────────────────────────
        print("\n📚 Available Categories:")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat.capitalize()}")

        # ── get category choice ────────────────────────────
        try:
            prompt = f"\n🎯 Choose a category (1‑{len(categories)}): "
            choice = int(input(prompt))
            if not (1 <= choice <= len(categories)):
                raise ValueError
        except ValueError:
            print("⚠️ Invalid input. Try again.")
            continue

        category_selected = categories[choice - 1]
        show_fortune(quotes, category_selected)

        # ── ask if the user wants more ─────────────────────
        while True:
            again = input("\n🔁 Want another fortune? (y/n): ").strip().lower()
            if again not in YES:
                raise KeyboardInterrupt

            same_cat = input("🎯 From the same category? (y/n): ").strip().lower()
            if same_cat in YES:
                show_fortune(quotes, category_selected)
            else:
                break

except KeyboardInterrupt:
    print("\n👋 Bye Bye! Stay inspired.")
    sys.exit(0)
