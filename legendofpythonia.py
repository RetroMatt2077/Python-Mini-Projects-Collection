
"""
LEGENDS OF PYTHONIA - PHASE 4 DELUXE EDITION
Single-file retro text RPG for Python/Pydroid 3
"""

import random, json, os

SAVE_FILE = "pythonia_save.json"

MONSTERS = {
    "Forest": ["Goblin", "Wolf", "Bandit"],
    "Cave": ["Skeleton", "Spider", "Orc"],
    "Desert": ["Scorpion", "Raider", "Mummy"],
    "Swamp": ["Slime", "Witch", "Lizardman"],
    "Mountains": ["Troll", "Harpy", "Ogre"]
}

BOSSES = ["Dragon King", "Lich Lord", "Demon Knight"]

WEAPONS = {
    "Wood Sword": 0,
    "Iron Sword": 5,
    "Steel Sword": 10,
    "Dragon Slayer": 25
}

ARMOR = {
    "Cloth": 0,
    "Leather": 3,
    "Chainmail": 6,
    "Dragon Armor": 12
}


class Player:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.level = 1
        self.xp = 0
        self.gold = 100
        self.skill_points = 0
        self.location = "Town"
        self.achievements = []

        if cls == "Warrior":
            self.max_hp = self.hp = 140
            self.max_mana = self.mana = 40
            self.attack = 14
        elif cls == "Wizard":
            self.max_hp = self.hp = 90
            self.max_mana = self.mana = 120
            self.attack = 9
        else:
            self.max_hp = self.hp = 110
            self.max_mana = self.mana = 60
            self.attack = 11

        self.weapon = "Wood Sword"
        self.armor = "Cloth"

        self.inventory = {
            "Potion": 5,
            "Mana Potion": 3,
            "Herb": 0,
            "Iron Ore": 0
        }

        self.pet = None

        self.skills = {
            "Power Strike": False,
            "Fireball": False,
            "Backstab": False
        }

        self.quest = {
            "target": "Goblin",
            "goal": 5,
            "progress": 0,
            "reward": 150
        }


def save_game(p):
    with open(SAVE_FILE, "w") as f:
        json.dump(p.__dict__, f)
    print("Game saved!")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    p = Player(data["name"], data["cls"])
    p.__dict__.update(data)
    return p


def level_up(p):
    while p.xp >= p.level * 50:
        p.level += 1
        p.skill_points += 1
        p.max_hp += 20
        p.hp = p.max_hp
        p.attack += 3

        print(f"\nLEVEL UP! Level {p.level}")

        if p.level == 3 and not p.pet:
            p.pet = "Wolf"
            print("A Wolf Companion joins you!")

        if p.level >= 10 and "Veteran" not in p.achievements:
            p.achievements.append("Veteran")


def show_stats(p):
    print("\n===== HERO =====")
    print("Name:", p.name)
    print("Class:", p.cls)
    print("Level:", p.level)
    print("XP:", p.xp)
    print("Gold:", p.gold)
    print("HP:", p.hp, "/", p.max_hp)
    print("Mana:", p.mana, "/", p.max_mana)
    print("Weapon:", p.weapon)
    print("Armor:", p.armor)
    print("Pet:", p.pet)
    print("Location:", p.location)


def shop(p):
    while True:
        print("\n=== SHOP ===")
        print("1 Potion (10g)")
        print("2 Mana Potion (15g)")
        print("3 Iron Sword (50g)")
        print("4 Steel Sword (100g)")
        print("5 Leather Armor (50g)")
        print("0 Exit")

        c = input("> ")

        if c == "0":
            return

        elif c == "1" and p.gold >= 10:
            p.gold -= 10
            p.inventory["Potion"] += 1

        elif c == "2" and p.gold >= 15:
            p.gold -= 15
            p.inventory["Mana Potion"] += 1

        elif c == "3" and p.gold >= 50:
            p.gold -= 50
            p.weapon = "Iron Sword"

        elif c == "4" and p.gold >= 100:
            p.gold -= 100
            p.weapon = "Steel Sword"

        elif c == "5" and p.gold >= 50:
            p.gold -= 50
            p.armor = "Leather"


def use_potion(p):
    if p.inventory["Potion"] > 0:
        p.inventory["Potion"] -= 1
        p.hp = min(p.max_hp, p.hp + 40)
        print("Recovered HP!")


def battle(p):
    if p.level % 5 == 0:
        monster = random.choice(BOSSES)
        enemy_hp = 150 + p.level * 10
    else:
        monster = random.choice(MONSTERS.get(p.location, ["Goblin"]))
        enemy_hp = random.randint(40, 80)

    print(f"\nA {monster} appears!")

    while enemy_hp > 0 and p.hp > 0:
        print("\n1 Attack")
        print("2 Skill")
        print("3 Potion")

        choice = input("> ")

        if choice == "1":
            dmg = random.randint(p.attack, p.attack + 10)
            dmg += WEAPONS[p.weapon]
            enemy_hp -= dmg
            print("You deal", dmg)

        elif choice == "2":
            if p.mana >= 10:
                p.mana -= 10
                dmg = random.randint(25, 45)
                enemy_hp -= dmg
                print("Special skill deals", dmg)

        elif choice == "3":
            use_potion(p)

        if p.pet:
            enemy_hp -= 5

        if enemy_hp <= 0:
            break

        defense = ARMOR[p.armor]
        enemy_dmg = max(1, random.randint(8, 18) - defense)

        p.hp -= enemy_dmg
        print(monster, "hits for", enemy_dmg)

    if p.hp <= 0:
        print("You were defeated.")
        return False

    xp = random.randint(20, 40)
    gold = random.randint(15, 35)

    p.xp += xp
    p.gold += gold

    print(f"Victory! +{xp} XP +{gold} Gold")

    if monster == p.quest["target"]:
        p.quest["progress"] += 1

        if p.quest["progress"] >= p.quest["goal"]:
            print("Quest Complete!")
            p.gold += p.quest["reward"]
            p.quest["progress"] = 0

    level_up(p)
    return True


def travel(p):
    places = ["Town", "Forest", "Cave", "Desert", "Swamp", "Mountains"]
    print("\nTravel To:")

    for i, place in enumerate(places, start=1):
        print(i, place)

    try:
        p.location = places[int(input("> ")) - 1]
    except:
        pass


def crafting(p):
    print("\nCRAFTING")
    print("1 Iron Sword (5 Iron Ore)")

    if input("> ") == "1":
        if p.inventory.get("Iron Ore", 0) >= 5:
            p.inventory["Iron Ore"] -= 5
            p.weapon = "Iron Sword"
            print("Crafted Iron Sword!")
        else:
            print("Not enough ore.")


def fishing(p):
    fish = random.choice(["Minnow", "Bass", "Trout", "Golden Fish"])
    value = random.randint(5, 25)
    p.gold += value
    print(f"You caught {fish} and sold it for {value} gold!")


def achievements(p):
    print("\nAchievements")
    for a in p.achievements:
        print("-", a)


def main():
    print("=== LEGENDS OF PYTHONIA DELUXE ===")

    player = None

    if os.path.exists(SAVE_FILE):
        if input("Load save? y/n: ").lower() == "y":
            player = load_game()

    if not player:
        name = input("Name: ")
        cls = input("Class (Warrior/Wizard/Rogue): ")
        player = Player(name, cls)

    while True:
        print("\n=== MAIN MENU ===")
        print("1 Explore")
        print("2 Shop")
        print("3 Travel")
        print("4 Stats")
        print("5 Crafting")
        print("6 Fishing")
        print("7 Achievements")
        print("8 Save")
        print("9 Quit")

        c = input("> ")

        if c == "1":
            if not battle(player):
                break
        elif c == "2":
            shop(player)
        elif c == "3":
            travel(player)
        elif c == "4":
            show_stats(player)
        elif c == "5":
            crafting(player)
        elif c == "6":
            fishing(player)
        elif c == "7":
            achievements(player)
        elif c == "8":
            save_game(player)
        elif c == "9":
            break


if __name__ == "__main__":
    main()
