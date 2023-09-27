import random

# Dictionary to store responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I assist you?"],
    "how are you": ["I'm just a program, so I don't have feelings, but I'm running smoothly!", "As good as a chatbot can be!", "Operating at full capacity!"],
    "default": ["I'm sorry, I don't understand that.", "Could you please rephrase that?", "I'm not sure how to respond to that."]
}

# Dictionary to store user data for personalization
user_data = {
    "name": None,
    "favorite_color": None,
    "favorite_book": None,
    "favorite_movie": None
}

def respond_to_user(user_input, user_data):
    if user_input in responses:
        return random.choice(responses[user_input])
    
    # Handle the user's name
    if "my name is" in user_input:
        user_name = user_input.split("is")[-1].strip()
        user_data["name"] = user_name
        return f"Nice to meet you, {user_name}!"
    if user_data["name"] and ("remember my name" in user_input or "do you know me" in user_input):
        return f"Of course, {user_data['name']}!"
    
    # Handle the user's favorite color
    if "favorite color" in user_input:
        user_data["favorite_color"] = user_input.split("is")[-1].strip()
        return f"Got it! I'll remember your favorite color is {user_data['favorite_color']}."
    if "remember my favorite color" in user_input:
        return f"Your favorite color is {user_data['favorite_color']}!" if user_data["favorite_color"] else "You haven't told me your favorite color yet."
    
    # Default response
    return random.choice(responses["default"])

def main():
    print("Hello! How can I assist you today?")
    while True:
        user_input = input().lower()
        if user_input in ["exit", "quit", "bye"]:
            print("Goodbye! Talk to you later.")
            break
        response = respond_to_user(user_input, user_data)
        print(response)

if __name__ == "__main__":
    main()
