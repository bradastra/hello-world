import random

class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello! What's your name?", "Hi there! May I know your name?"],
            "hello": ["Hello! What's your name?", "Hi! Can you tell me your name?"],
            "default": ["I'm not sure how to respond to that.", "Can you rephrase that?"],
            "name_known": ["Nice to meet you, {}! How can I assist you today?", "Hello, {}! What can I do for you?"]
        }
        self.user_name = None

    def get_response(self, message):
        if self.user_name:
            if "name" in message or "who am i" in message:
                return f"You're {self.user_name}! How can I assist you today?"
        
        if message in ["hi", "hello"]:
            return random.choice(self.responses[message])

        if "my name is" in message or "i am" in message or "call me" in message:
            # Extract the user's name from the message
            self.user_name = message.split()[-1]
            return random.choice(self.responses["name_known"]).format(self.user_name)

        return random.choice(self.responses["default"])

if __name__ == "__main__":
    bot = Chatbot()
    print("Chatbot: Hi there! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")
