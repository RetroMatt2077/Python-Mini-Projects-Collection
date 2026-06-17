"""
Rock, Paper, Scissors Deluxe Edition
Author: Retro Matt / ChatGPT
"""

import random
import os

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Dummy:
        RED=GREEN=YELLOW=CYAN=MAGENTA=""
        RESET_ALL=""
    Fore=Style=Dummy()

SCORE_FILE="rps_highscore.txt"
CHOICES=["rock","paper","scissors"]

def load_best():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE) as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def save_best(best):
    with open(SCORE_FILE,"w") as f:
        f.write(str(best))

wins=losses=ties=0
streak=0
best=load_best()

print(Fore.CYAN + "="*40)
print(Fore.YELLOW + " ROCK • PAPER • SCISSORS DELUXE ")
print(Fore.CYAN + "="*40)
print("Commands: rock, paper, scissors, help, quit")

while True:
    print(f"\nBest Win Streak: {best}")
    choice=input(Fore.GREEN+"Your move: ").lower().strip()

    if choice in ("quit","exit","q"):
        break
    if choice=="help":
        print("Beat the computer. Rock>Scissors, Scissors>Paper, Paper>Rock.")
        continue
    if choice not in CHOICES:
        print(Fore.RED+"Invalid choice!")
        continue

    cpu=random.choice(CHOICES)
    print(f"Computer: {cpu}")

    if choice==cpu:
        print(Fore.YELLOW+"Tie!")
        ties+=1
    elif (choice=="rock" and cpu=="scissors") or \
         (choice=="paper" and cpu=="rock") or \
         (choice=="scissors" and cpu=="paper"):
        print(Fore.GREEN+"You WIN!")
        wins+=1
        streak+=1
        if streak>best:
            best=streak
            save_best(best)
            print(Fore.MAGENTA+"*** NEW BEST WIN STREAK! ***")
    else:
        print(Fore.RED+"Computer wins!")
        losses+=1
        streak=0

    total=wins+losses+ties
    pct=(wins/total*100) if total else 0

    print("-"*40)
    print(f"Wins   : {wins}")
    print(f"Losses : {losses}")
    print(f"Ties   : {ties}")
    print(f"Streak : {streak}")
    print(f"Win %  : {pct:.1f}%")
    print("-"*40)

print("\nThanks for playing!")
print(f"Final Record: {wins}-{losses}-{ties}")
print(f"Best Win Streak: {best}")
