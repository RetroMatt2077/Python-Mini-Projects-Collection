import random

choices = ["friendly", "hostile"]

alien = random.choice(choices)

if alien == "friendly":
    print("👽 The alien gives you technology!")
else:
    print("💥 The alien attacks!")