import random

responses = {
    "hello": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! How's your day going?"
    ],
    "how are you": [
        "I'm just a program, so I don't have feelings, but I'm functioning optimally!",
        "Running at full capacity!",
        "As good as a bunch of code can be!"
    ],
    "bye": [
        "Goodbye! If you have more questions, just ask.",
        "See you later!",
        "Bye! Have a great day!"
    ],
    "what's your name": [
        "I'm ChatGPT, a simple chatbot. Nice to meet you!",
        "People call me ChatGPT. What about you?",
        "I go by ChatGPT. What's your name?"
    ]
}

print("Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input in responses:
        print("ChatGPT:", random.choice(responses[user_input]))
    elif "my name is" in user_input:
        name = user_input.split("is")[1].strip()
        print(f"ChatGPT: Nice to meet you, {name}!")
        responses["what's your name"].append(f"I remember now! You're {name}, right?")
    elif user_input == 'bye':
        print("ChatGPT: Goodbye! Have a great day!")
        break
    else:
        print("ChatGPT: I'm sorry, I don't understand that.")
