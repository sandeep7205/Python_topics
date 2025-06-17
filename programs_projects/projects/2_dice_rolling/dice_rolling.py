import random
import sys


print("\nWelcome to the Dice Rolling Simulator!")
print("\nPress 'r' to roll the dice, or 'q' to quit.")

roll_keys = ['r', 'q']
try:
    while True:
        user_choice = input("\nEnter your choice: ").lower()
        if user_choice in roll_keys:
            if user_choice == 'q':
                print("\nThanks for playing! See you next time.")
                raise KeyboardInterrupt 
            else:
                num_dice = int(input("\nHow many dice would you like to roll? (Enter a number, e.g., 1, 2, 3): "))
                if num_dice <= 0:
                    print("\nYou need to roll at least one die! Please enter a positive number.")
                    continue
                else:
                    for d in range(1, (num_dice+1)):
                        roll_result = random.randint(1, 6)
                        print(f"\nDie {d}: {roll_result}")
        else:
            print("\nInvalid input. Please enter 'r' to roll or 'q' to quit.")
                    
except KeyboardInterrupt:
    sys.exit(0)