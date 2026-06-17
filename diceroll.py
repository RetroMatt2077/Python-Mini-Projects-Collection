import random

while True:
    roll = random.randint(1, 6)
    print("🎲 You rolled:", roll)

    again = input("Roll again? (y/n): ")
    if again.lower() != "y":
        break