import random

def chatbot_response(text, user_data):
    text = text.lower()
    
    # Bot greeting responses
    greetings = ["hello", "hi", "hey", "sup", "yo"]
    greeting_responses = ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"]

    # Farewells
    farewells = ["bye", "goodbye", "see you", "later"]
    farewell_responses = ["Goodbye!", "See you later!", "Take care!"]

    # Questions about the bot
    bot_questions = ["how are you", "are you real", "who are you"]
    bot_responses = [
        "I'm just a program, so I don't have feelings, but I'm functioning properly!",
        "I'm virtual, not a real person.",
        "I'm a simple chatbot, here to assist you!"
    ]

    # Check and respond
    if text in greetings:
        return random.choice(greeting_responses)
    elif text in farewells:
        return random.choice(farewell_responses)
    elif any(bot_q in text for bot_q in bot_questions):
        return random.choice(bot_responses)
    elif "name" in text and "your" in text:
        return "I'm just a chatbot, but you can call me ChatGPT!"
    elif "my name is" in text:
        user_data["name"] = text.split("is")[-1].strip()
        return f"Nice to meet you, {user_data['name']}!"
    elif "remember my name" in text:
        if "name" in user_data:
            return f"Of course, your name is {user_data['name']}!"
        else:
            return "I'm sorry, I don't recall your name. What is it?"
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

def main():
    user_data = {}  # Store user-specific data like name
    print("Chatbot: Hello! If you want to exit, just say 'bye'.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input, user_data)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
