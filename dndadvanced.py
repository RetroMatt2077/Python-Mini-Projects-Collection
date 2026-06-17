import random

print("🎲 D&D Dice Roller")

while True:

    dice = input(
        "\nChoose a die (4,6,8,10,12,20,100) or q to quit: "
    )

    if dice.lower() == "q":
        break

    try:
        sides = int(dice)

        roll = random.randint(1, sides)

        print(f"\n🎲 d{sides} rolled: {roll}")

        if sides == 20:
            if roll == 20:
                print("🔥 NATURAL 20!")
            elif roll == 1:
                print("💀 NATURAL 1!")

    except:
        print("Invalid die.")