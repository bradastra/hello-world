import random

def simple_bot(user_input):
    responses = {
        "hello": ["Hi!", "Hey!", "Hello!"],
        "how are you": ["I'm just a program, so I don't have feelings, but 
I'm functioning optimally!", 
                        "Running at full capacity!", 
                        "Good, thanks for asking!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"]
    }

    user_input = user_input.lower()
    
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    print("Simple Bot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Simple Bot: Goodbye!")
            break
        response = simple_bot(user_input)
        print(f"Simple Bot: {response}")
