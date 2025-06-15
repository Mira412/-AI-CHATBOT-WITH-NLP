import nltk
import spacy

nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")

responses = {
    "hello": "Hi there! How can I help?",
    "you are?": "I'm just a chatbot, but I'm here to assist you!",
    "bye": "Goodbye! Have a great day!",
    "ai": "I'm your AI assistant, here to help!",
    "how does machine learning work": "Machine learning helps computers learn patterns from data and make predictions!",
    "what is an API": "An API (Application Programming Interface) lets different programs talk to each other!",
    "explain NLP": "Natural Language Processing (NLP) helps computers understand human language.",
}

def chatbot_response(user_input):
    user_input = user_input.lower().strip()  
    return responses.get(user_input, "I'm still learning! Can you ask differently?")

print("Chatbot is ready! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    print("Chatbot:", chatbot_response(user_input))
