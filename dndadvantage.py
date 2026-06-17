import random

while True:

    print("\n1. Normal")
    print("2. Advantage")
    print("3. Disadvantage")
    print("4. Quit")

    choice = input("> ")

    if choice == "4":
        break

    if choice == "1":
        roll = random.randint(1, 20)
        print("🎲", roll)

    elif choice == "2":
        a = random.randint(1, 20)
        b = random.randint(1, 20)

        print(f"🎲 {a} and {b}")
        print("Best:", max(a, b))

    elif choice == "3":
        a = random.randint(1, 20)
        b = random.randint(1, 20)

        print(f"🎲 {a} and {b}")
        print("Worst:", min(a, b))