import random

answers = [
    "Yes!",
    "No!",
    "Maybe...",
    "Ask again later.",
    "Definitely!",
    "Very unlikely."
]

question = input("Ask a question: ")
print("🔮", random.choice(answers))