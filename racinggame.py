import random
import time

player = 0
computer = 0

while player < 20 and computer < 20:
    player += random.randint(1, 4)
    computer += random.randint(1, 4)

    print("🚗 You:", player)
    print("🤖 CPU:", computer)
    print()

    time.sleep(1)

if player >= 20:
    print("🏆 You win!")
else:
    print("💀 CPU wins!")