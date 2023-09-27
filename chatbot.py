import random

user_data = {}
greetings_responses = ["Hello!", "Hi there!", "Hey!", "Hi!"]
questions_responses = [
    "Would you like to tell me more about your favorite things?",
    "Do you have any hobbies?",
    "What's a fun fact about you?"
]

def get_name():
    name = input("First, please tell me your name: ")
    user_data["name"] = name

def get_favorite_color():
    color = input("What's your favorite color? ")
    user_data["color"] = color

def known_topics():
    print("Here are some topics I understand:")
    print("1. Greetings (e.g., hello, hi)")
    print("2. Colors (e.g., What's your favorite color?)")
    print("3. Exit (e.g., bye)")

if not user_data.get("name"):
    get_name()
print(f"Hello, {user_data['name']}!")

if not user_data.get("color"):
    get_favorite_color()
print(f"That's cool! {user_data['color']} is a nice color.")

while True:
    user_message = input(f"{user_data['name']}, type your message: ")
    
    if "hello" in user_message.lower():
        print(random.choice(greetings_responses))
    elif "color" in user_message.lower() or "favourite" in user_message.lower() or "favorite" in user_message.lower():
        if user_data.get("color"):
            print(f"Your favorite color is {user_data['color']}, right?")
        else:
            get_favorite_color()
    elif "bye" in user_message.lower():
        print("Goodbye!")
        break
    else:
        print("I'm sorry, I didn't understand that.")
        print(random.choice(questions_responses))
        known_topics()
