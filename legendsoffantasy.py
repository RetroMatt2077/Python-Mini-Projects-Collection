"""
===========================================================
                LEGENDS OF FANTASY
                    Version 2.0

              Developed by Matt Swartz

A text-based fantasy RPG built while learning Python.
===========================================================
"""

import os
import time
import random

# ----------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------

def clear():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def slow_print(text, delay=0.03):
    """Print text one character at a time."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ----------------------------------------------------------
# Title Screen
# ----------------------------------------------------------

def title_screen():
    clear()

    print(r"""
 __        ______   _____  _____ _   _ ____  ____
 \ \      / / __ \ / ____|/ ____| \ | |  _ \|  _ \
  \ \ /\ / / |  | | (___ | |    |  \| | | | | |_) |
   \ V  V /| |  | |\___ \| |    | . ` | | | |  _ <
    \_/\_/ | |__| |____) | |____| |\  | |_| | |_) |
            \____/|_____/ \_____|_| \_|____/|____/

           L E G E N D S   O F   F A N T A S Y
    """)

    print("=" * 55)
    print("          A Classic Text Adventure RPG")
    print("=" * 55)
    print("\n1. New Game")
    print("2. Credits")
    print("3. Quit")


# ----------------------------------------------------------
# Intro Story
# ----------------------------------------------------------

def intro_story():
    clear()

    story = [
        "Thousands of years ago...",
        "",
        "The Five Kingdoms lived in peace.",
        "",
        "Then darkness spread across the land.",
        "",
        "The Crystal of Creation shattered...",
        "",
        "Ancient monsters returned.",
        "",
        "Cities burned.",
        "",
        "Heroes vanished.",
        "",
        "Hope faded.",
        "",
        "Yet one prophecy remains...",
        "",
        "A new champion shall rise."
    ]

    for line in story:
        slow_print(line)
        time.sleep(0.5)

    pause()


# ----------------------------------------------------------
# Character Creation
# ----------------------------------------------------------

classes = {
    "1": "Warrior",
    "2": "Paladin",
    "3": "Rogue",
    "4": "Ranger",
    "5": "Mage",
    "6": "Sorcerer",
    "7": "Necromancer",
    "8": "Bard"
}


def create_character():
    clear()

    print("=== CHARACTER CREATION ===\n")

    name = input("Enter your hero's name: ")

    print("\nChoose your class:\n")

    for number, hero_class in classes.items():
        print(f"{number}. {hero_class}")

    choice = ""

    while choice not in classes:
        choice = input("\nSelection: ")

    hero_class = classes[choice]

    player = {
        "name": name,
        "class": hero_class,
        "level": 1,
        "xp": 0,
        "gold": 100,
        "hp": 100,
        "max_hp": 100,
        "mana": 50,
        "max_mana": 50,
        "strength": 10,
        "defense": 10,
        "dexterity": 10,
        "intelligence": 10,
        "luck": 10,
        "inventory": [],
        "weapon": "Wooden Sword",
        "armor": "Traveler's Clothes"
    }

    return player


# ----------------------------------------------------------
# Hero Summary
# ----------------------------------------------------------

def show_character(player):
    clear()

    print("=" * 40)
    print("        HERO CREATED")
    print("=" * 40)

    for key, value in player.items():
        print(f"{key.title():15}: {value}")

    pause()


# ----------------------------------------------------------
# Main Menu
# ----------------------------------------------------------

def main():

    while True:

        title_screen()

        choice = input("\nChoose an option: ")

        if choice == "1":
            intro_story()
            player = create_character()
            show_character(player)

        elif choice == "2":
            clear()
            print("Legends of Fantasy")
            print("Version 2.0")
            print("\nDeveloped by Matt Swartz")
            pause()

        elif choice == "3":
            clear()
            print("Thank you for playing!")
            break

        else:
            print("\nInvalid choice.")
            time.sleep(1)


# ----------------------------------------------------------
# Program Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
    
    # ============================================================
# PLAYER CLASS
# ============================================================

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class

        # Level System
        self.level = 1
        self.experience = 0
        self.exp_to_next = 100

        # Health & Mana
        self.max_hp = 100
        self.hp = self.max_hp

        self.max_mp = 50
        self.mp = self.max_mp

        # Combat Stats
        self.strength = 10
        self.defense = 10
        self.dexterity = 10
        self.intelligence = 10
        self.luck = 10

        # Currency
        self.gold = 100

        # Equipment
        self.weapon = "Wooden Sword"
        self.armor = "Traveler's Clothes"
        self.helmet = "None"
        self.accessory = "None"

        # Inventory
        self.inventory = [
            "Potion",
            "Potion",
            "Ether"
        ]

    # ----------------------------------------
    # Display Character Sheet
    # ----------------------------------------
    def show_stats(self):
        print("\n==============================")
        print("      CHARACTER SHEET")
        print("==============================")
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Level: {self.level}")
        print(f"EXP: {self.experience}/{self.exp_to_next}")
        print()
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"MP: {self.mp}/{self.max_mp}")
        print()
        print(f"Strength:     {self.strength}")
        print(f"Defense:      {self.defense}")
        print(f"Dexterity:    {self.dexterity}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Luck:         {self.luck}")
        print()
        print(f"Gold: {self.gold}")
        print()
        print("Equipment")
        print(f" Weapon:    {self.weapon}")
        print(f" Armor:     {self.armor}")
        print(f" Helmet:    {self.helmet}")
        print(f" Accessory: {self.accessory}")
        print()
        print("Inventory")
        for item in self.inventory:
            print(f" - {item}")
        print("==============================")
        
        # ============================================================
# CHARACTER CREATION
# ============================================================

def create_character():
    print("\nWelcome, Hero!")

    name = input("Enter your character's name: ")

    print("\nChoose your class:")
    print("1. Warrior")
    print("2. Paladin")
    print("3. Rogue")
    print("4. Ranger")
    print("5. Mage")
    print("6. Sorcerer")
    print("7. Necromancer")
    print("8. Bard")

    while True:
        choice = input("\nClass Number: ")

        if choice == "1":
            player = Player(name, "Warrior")
            player.max_hp = 140
            player.hp = 140
            player.max_mp = 20
            player.mp = 20
            player.strength = 18
            player.defense = 15
            player.weapon = "Iron Sword"
            break

        elif choice == "2":
            player = Player(name, "Paladin")
            player.max_hp = 130
            player.hp = 130
            player.max_mp = 40
            player.mp = 40
            player.strength = 15
            player.defense = 18
            player.weapon = "Blessed Hammer"
            break

        elif choice == "3":
            player = Player(name, "Rogue")
            player.max_hp = 100
            player.hp = 100
            player.max_mp = 25
            player.mp = 25
            player.dexterity = 20
            player.luck = 18
            player.weapon = "Twin Daggers"
            break

        elif choice == "4":
            player = Player(name, "Ranger")
            player.max_hp = 110
            player.hp = 110
            player.max_mp = 30
            player.mp = 30
            player.dexterity = 18
            player.strength = 14
            player.weapon = "Oak Bow"
            break

        elif choice == "5":
            player = Player(name, "Mage")
            player.max_hp = 80
            player.hp = 80
            player.max_mp = 120
            player.mp = 120
            player.intelligence = 22
            player.weapon = "Magic Staff"
            break

        elif choice == "6":
            player = Player(name, "Sorcerer")
            player.max_hp = 90
            player.hp = 90
            player.max_mp = 140
            player.mp = 140
            player.intelligence = 24
            player.weapon = "Ancient Wand"
            break

        elif choice == "7":
            player = Player(name, "Necromancer")
            player.max_hp = 95
            player.hp = 95
            player.max_mp = 130
            player.mp = 130
            player.intelligence = 21
            player.luck = 15
            player.weapon = "Bone Staff"
            break

        elif choice == "8":
            player = Player(name, "Bard")
            player.max_hp = 105
            player.hp = 105
            player.max_mp = 60
            player.mp = 60
            player.dexterity = 15
            player.luck = 22
            player.weapon = "Enchanted Lute"
            break

        else:
            print("Invalid choice. Try again.")

    print("\n================================")
    print("Character Created Successfully!")
    print("================================")

    player.show_stats()

    input("\nPress ENTER to continue...")

    return player
    
    # ============================================================
# MAIN MENU
# ============================================================

def main_menu(player):
    while True:
        print("\n" + "=" * 50)
        print("            LEGENDS OF FANTASY")
        print("=" * 50)
        print(f"Hero : {player.name}")
        print(f"Class: {player.player_class}")
        print(f"Level: {player.level}")
        print(f"HP: {player.hp}/{player.max_hp}")
        print(f"MP: {player.mp}/{player.max_mp}")
        print(f"Gold: {player.gold}")
        print("=" * 50)

        print("1. Begin Adventure")
        print("2. Character Sheet")
        print("3. Inventory")
        print("4. Equipment")
        print("5. Save Game")
        print("6. Load Game")
        print("7. Settings")
        print("8. Credits")
        print("9. Exit Game")

        choice = input("\nChoose an option: ")

        if choice == "1":
            world_map(player)

        elif choice == "2":
            player.show_stats()
            input("\nPress ENTER to return to the menu...")

        elif choice == "3":
            print("\n========== INVENTORY ==========")

            if len(player.inventory) == 0:
                print("Inventory is empty.")
            else:
                for index, item in enumerate(player.inventory, start=1):
                    print(f"{index}. {item}")

            input("\nPress ENTER to return...")

        elif choice == "4":
            print("\n========== EQUIPMENT ==========")
            print(f"Weapon    : {player.weapon}")
            print(f"Armor     : {player.armor}")
            print(f"Helmet    : {player.helmet}")
            print(f"Accessory : {player.accessory}")

            input("\nPress ENTER to return...")

        elif choice == "5":
            print("\nSave system coming in Version 2.1!")
            input("Press ENTER...")

        elif choice == "6":
            print("\nLoad system coming in Version 2.1!")
            input("Press ENTER...")

        elif choice == "7":
            print("\n========== SETTINGS ==========")
            print("1. Text Speed")
            print("2. Sound (Coming Soon)")
            print("3. Difficulty (Coming Soon)")
            print("4. Back")

            input("\nPress ENTER to return...")

        elif choice == "8":
            print("\n========== CREDITS ==========")
            print("Legends of Fantasy")
            print("Version 2.0")
            print()
            print("Created by Matt Swartz")
            print("Built with Python")
            print()
            print("Thank you for playing!")

            input("\nPress ENTER...")

        elif choice == "9":
            print("\nMay your legend live forever...")
            break

        else:
            print("\nInvalid selection.")
            
            # ============================================================
# WORLD MAP
# ============================================================

world_locations = {
    "1": {
        "name": "King's Village",
        "description": "A peaceful village where new heroes begin their journey."
    },
    "2": {
        "name": "Whispering Forest",
        "description": "A mysterious forest filled with monsters and hidden treasures."
    },
    "3": {
        "name": "Goblin Cave",
        "description": "A dark cave rumored to contain dangerous goblins."
    },
    "4": {
        "name": "Crystal Lake",
        "description": "A beautiful lake said to possess magical healing powers."
    },
    "5": {
        "name": "Ancient Ruins",
        "description": "The remains of a forgotten civilization."
    },
    "6": {
        "name": "Dragon Peak",
        "description": "A towering mountain where dragons once ruled."
    }
}


# ============================================================
# WORLD MAP MENU
# ============================================================

def world_map(player):

    while True:

        print("\n" + "=" * 50)
        print("               WORLD MAP")
        print("=" * 50)

        for key, location in world_locations.items():
            print(f"{key}. {location['name']}")

        print("7. Return to Main Menu")

        choice = input("\nWhere would you like to travel? ")

        if choice == "7":
            return

        elif choice in world_locations:

            location = world_locations[choice]

            print("\n" + "=" * 50)
            print(location["name"])
            print("=" * 50)

            print(location["description"])

            visit_location(player, location["name"])

        else:
            print("Invalid choice.")
            
            # ============================================================
# LOCATION HANDLER
# ============================================================

def visit_location(player, location):

    while True:

        print("\n--------------------------------")
        print(location)
        print("--------------------------------")

        print("1. Explore")
        print("2. Search for Treasure")
        print("3. Rest")
        print("4. Return to World Map")

        choice = input("\nChoose an action: ")

        if choice == "1":
            print("\nYou carefully explore the area...")
            print("Nothing happens...for now.")

            input("\nPress ENTER...")

        elif choice == "2":

            print("\nYou search the surroundings...")

            print("You found 15 Gold!")

            player.gold += 15

            print(f"Gold: {player.gold}")

            input("\nPress ENTER...")

        elif choice == "3":

            player.hp = player.max_hp
            player.mp = player.max_mp

            print("\nYou feel completely refreshed.")

            input("\nPress ENTER...")

        elif choice == "4":
            return

        else:
            print("Invalid choice.")