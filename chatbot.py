import random

user_data = {}
greetings_responses = ["Hello!", "Hi there!", "Hey!", "Hi!"]
questions_responses = [
    "Would you like to tell me more about your favorite things?",
    "Do you have any hobbies?",
    "What's a fun fact about you?"
]

topics_responses = {
    "hello": lambda: print(random.choice(greetings_responses)),
    "color": lambda: handle_color_topic(),
    "favourite": lambda: handle_color_topic(),
    "favorite": lambda: handle_color_topic(),
    "bye": lambda: "exit"
}

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

def handle_color_topic():
    if user_data.get("color"):
        print(f"Your favorite color is {user_data['color']}, right?")
    else:
        get_favorite_color()

def handle_input(user_message):
    for keyword, action in topics_responses.items():
        if keyword in user_message.lower():
            result = action()
            if result == "exit":
                print("Goodbye!")
                return False
            return True
    print("I'm sorry, I didn't understand that.")
    print(random.choice(questions_responses))
    known_topics()
    return True

if not user_data.get("name"):
    get_name()
print(f"Hello, {user_data['name']}!")

if not user_data.get("color"):
    get_favorite_color()
print(f"That's cool! {user_data['color']} is a nice color.")

keep_going = True
while keep_going:
    user_message = input(f"{user_data['name']}, type your message: ")
    keep_going = handle_input(user_message)
