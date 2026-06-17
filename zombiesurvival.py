health = 10

while health > 0:
    action = input("Run or Fight? ").lower()

    if action == "fight":
        health -= 2
        print("You survived!")
    elif action == "run":
        print("You escaped!")
        break

    print("Health:", health)

if health <= 0:
    print("🧟 The zombies got you!")