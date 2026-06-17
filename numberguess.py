import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess == secret:
        print("🎉 You got it!")
        break
    else:
        print("❌ Try again!")