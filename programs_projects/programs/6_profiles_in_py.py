# ---------------------
# 1. Using cProfile (Standard Python Tool)

# Run in Terminal - python -m cProfile  my_script.py

# What this shows:
# ncalls: Number of times function was called
# tottime: Time spent in the function itself
# cumtime: Time spent in this function and all sub-functions


import time

def slow_function():
    time.sleep(2)

def fast_function():
    time.sleep(0.5)

def main():
    slow_function()
    fast_function()

if __name__ == "__main__":
    main()

# ---------------------
print("------------------------------------")
# ---------------------

#  2. Using cProfile in your script (with pstats)

import cProfile
import pstats

def slow_function():
    import time; time.sleep(2)

def fast_function():
    import time; time.sleep(0.5)

def main():
    slow_function()
    fast_function()

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumtime').print_stats()
# ---------------------

