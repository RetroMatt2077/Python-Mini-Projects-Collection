"""
Retro Matt RPG Deluxe
Starter Framework

This file is intentionally structured so it can grow into a very large RPG.
"""

import random
import json
import os

player = {
    "name": "",
    "class": "",
    "hp": 100,
    "max_hp": 100,
    "mp": 30,
    "gold": 25,
    "xp": 0,
    "level": 1,
    "inventory": ["Wooden Sword", "Potion"],
}

areas = ["Town", "Forest", "Cave", "Mountains", "Castle"]

monsters = [
    {"name":"Goblin","hp":20,"atk":5,"gold":8,"xp":10},
    {"name":"Wolf","hp":25,"atk":6,"gold":10,"xp":12},
    {"name":"Skeleton","hp":35,"atk":8,"gold":15,"xp":18},
]

SAVE_FILE="savegame.json"

def save():
    with open(SAVE_FILE,"w") as f:
        json.dump(player,f,indent=2)
    print("Game saved.")

def load():
    global player
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            player=json.load(f)
        print("Game loaded.")
    else:
        print("No save found.")

def stats():
    print("\n==== PLAYER ====")
    for k,v in player.items():
        print(f"{k}: {v}")

def fight():
    m=random.choice(monsters).copy()
    print(f"\nA wild {m['name']} appears!")
    while m["hp"]>0 and player["hp"]>0:
        print("\n1) Attack  2) Potion  3) Run")
        c=input("> ")
        if c=="1":
            dmg=random.randint(8,15)
            m["hp"]-=dmg
            print(f"You hit for {dmg}.")
            if m["hp"]<=0:
                print("Victory!")
                player["gold"]+=m["gold"]
                player["xp"]+=m["xp"]
                if player["xp"]>=player["level"]*50:
                    player["level"]+=1
                    player["max_hp"]+=10
                    player["hp"]=player["max_hp"]
                    print("LEVEL UP!")
                return
            edmg=random.randint(1,m["atk"])
            player["hp"]-=edmg
            print(f"{m['name']} hits for {edmg}.")
        elif c=="2":
            if "Potion" in player["inventory"]:
                player["inventory"].remove("Potion")
                player["hp"]=min(player["max_hp"],player["hp"]+30)
                print("You used a Potion.")
            else:
                print("No potions.")
        else:
            print("You escaped.")
            return

def main():
    print("="*40)
    print("RETRO MATT RPG DELUXE")
    print("="*40)
    if not player["name"]:
        player["name"]=input("Name: ")
        player["class"]=input("Class: ")
    while True:
        print("\n1 Stats\n2 Explore\n3 Save\n4 Load\n5 Quit")
        c=input("> ")
        if c=="1":
            stats()
        elif c=="2":
            fight()
            if player["hp"]<=0:
                print("Game Over")
                break
        elif c=="3":
            save()
        elif c=="4":
            load()
        elif c=="5":
            break

if __name__=="__main__":
    main()

# Expansion ideas:
# - Quest system
# - Shops
# - Equipment
# - Crafting
# - Bosses
# - World map
# - Magic
# - Dialogue
# - Achievements
