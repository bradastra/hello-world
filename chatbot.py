import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')  # for tokenization

user_data = {}
greetings_responses = ["Hello!", "Hi there!", "Hey!", "Hi!"]
questions_responses = [
    "Would you like to tell me more about your favorite things?",
    "Do you have any hobbies?",
    "What's a fun fact about you?"
]

corpus = {
    "hello": greetings_responses,
    "color": ["What's your favorite color?", "Do you have a preferred color?", "Which color do you like?"],
    "bye": ["Goodbye!", "See you later!", "Farewell!"],
    "calculate": ["Can you compute this for me?", "What's the result of this calculation?", "Solve this math problem for me."]
}

def get_name():
    name = input("First, please tell me your name: ")
    user_data["name"] = name

def get_favorite_color():
    color = input("What's your favorite color? ")
    user_data["color"] = color

def known_topics():
    print("Here are some topics I understand:")
    for topic in corpus:
        print(f"- {topic.capitalize()}")

def calculate_expression(expr):
    try:
        return eval(expr)
    except:
        return "Sorry, I couldn't understand or evaluate that expression."

def respond_to_input(user_input):
    responses = []
    for key, value in corpus.items():
        for v in value:
            responses.append(v)
    
    tfidf_vectorizer = TfidfVectorizer().fit_transform([user_input] + responses)
    cosine_vals = cosine_similarity(tfidf_vectorizer[0:1], tfidf_vectorizer[1:]).flatten()
    best_match_idx = cosine_vals.argmax()
    response = responses[best_match_idx]

    if "calculate" in response:
        expr = input("Please enter the mathematical expression: ")
        return calculate_expression(expr)
    else:
        return response

if not user_data.get("name"):
    get_name()
print(f"Hello, {user_data['name']}!")

if not user_data.get("color"):
    get_favorite_color()
print(f"That's cool! {user_data['color']} is a nice color.")

while True:
    user_message = input(f"{user_data['name']}, type your message: ")

    if "bye" in user_message.lower():
        print("Goodbye!")
        break
    else:
        response = respond_to_input(user_message)
        print(response)
