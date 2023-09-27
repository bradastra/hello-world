import datetime

def greeting():
    """Generate a greeting based on the current hour."""
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

def main():
    """Main function to execute the chatbot functionalities."""
    user_name = input("Hi! What's your name? ")
    print(f"{greeting()}, {user_name}! How can I assist you today?")

    # This is a basic loop for the chatbot to respond until user decides to quit
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, so I don't have feelings, but I'm running as expected!")
        else:
            print("Chatbot: Sorry, I don't understand that. I'm still learning!")

if __name__ == "__main__":
    main()
