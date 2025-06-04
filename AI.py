# 1. Import Libraries
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.naive_bayes import MultinomialNB # type: ignore

# 2. Create Training Data
training_data = [
    # Greetings
    ("hi", "greeting"),
    ("hello", "greeting"),
    ("hey", "greeting"),
    ("good morning", "greeting"),
    ("good afternoon", "greeting"),
    ("good evening", "greeting"),
    ("howdy", "greeting"),
    ("how are you", "greeting"),
    ("what's up", "greeting"),
    ("hows it going", "greeting"),
    ("yo", "greeting"),
    ("hi there", "greeting"),
    ("hey there", "greeting"),
    ("greetings", "greeting"),
    ("sup", "greeting"),
    ("hello there", "greeting"),

    # Goodbye
    ("bye", "goodbye"),
    ("see you later", "goodbye"),
    ("good night", "goodbye"),
    ("take care", "goodbye"),
    ("catch you later", "goodbye"),
    ("see ya", "goodbye"),
    ("talk to you later", "goodbye"),
    ("farewell", "goodbye"),
    ("i have to go", "goodbye"),
    ("goodbye", "goodbye"),
    ("see you soon", "goodbye"),
    ("i'm leaving", "goodbye"),
    ("peace out", "goodbye"),
    ("gotta go", "goodbye"),
    ("later", "goodbye"),
    ("ciao", "goodbye"),
    # Name Queries
    ("what's your name", "name_query"),
    ("who are you", "name_query"),
    ("can you tell me your name", "name_query"),
    ("may I know your name", "name_query"),
    ("do you have a name", "name_query"),
    ("what do people call you", "name_query"),
    ("who am I talking to", "name_query"),
    ("who is this", "name_query"),
    ("what should I call you", "name_query"),
    ("your name?", "name_query"),
    ("tell me your name", "name_query"),
    ("are you a bot", "name_query"),
    ("are you human", "name_query"),
    ("do you have an identity", "name_query"),
    ("what are you", "name_query"),
    ("name please", "name_query"),
    ("bot name?", "name_query"),
    ("who made you", "name_query"),
    ("identify yourself", "name_query"),
    ("tell me who you are", "name_query"),

    # Help Request
    ("can you help me", "help_request"),
    ("i need help", "help_request"),
    ("help me", "help_request"),
    ("assist me", "help_request"),
    ("i need assistance", "help_request"),
    ("could you help", "help_request"),
    ("please help", "help_request"),
    ("i want help", "help_request"),
    ("need your help", "help_request"),
    ("can i get some help", "help_request"),
    ("help", "help_request"),
    ("i need support", "help_request"),
    ("can you assist me", "help_request"),
    ("i could use some help", "help_request"),
    ("give me a hand", "help_request"),
    ("help required", "help_request"),
    ("may I get help", "help_request"),
    ("some assistance please", "help_request"),
    ("i'm stuck", "help_request"),
    ("please assist", "help_request"),

    # Capabilities
    ("what can you do", "capabilities"),
    ("tell me your functions", "capabilities"),
    ("what are your skills", "capabilities"),
    ("how can you help me", "capabilities"),
    ("what services do you offer", "capabilities"),
    ("what are you capable of", "capabilities"),
    ("tell me what you can do", "capabilities"),
    ("how do you work", "capabilities"),
    ("show me your features", "capabilities"),
    ("what can you help me with", "capabilities"),
    ("explain your features", "capabilities"),
    ("what tasks can you perform", "capabilities"),
    ("list your capabilities", "capabilities"),
    ("what functions do you serve", "capabilities"),
    ("how can you assist me", "capabilities"),

    # Thanks
    ("thanks", "thanks"),
    ("thank you", "thanks"),
    ("thanks a lot", "thanks"),
    ("much appreciated", "thanks"),
    ("thanks buddy", "thanks"),
    ("thanks man", "thanks"),
    ("thanks for the help", "thanks"),
    ("cheers", "thanks"),
    ("many thanks", "thanks"),
    ("thx", "thanks"),
    ("thanks a bunch", "thanks"),
    ("thank you very much", "thanks"),
    ("i appreciate it", "thanks"),
    ("thanks for assisting", "thanks"),


    # Apology
    ("I'm sorry", "apology"),
    ("My apologies", "apology"),
    ("I didn't mean to", "apology"),
    ("Please forgive me", "apology"),
    ("Sorry about that", "apology"),

    # Compliment
    ("You're amazing", "compliment"),
    ("Great job", "compliment"),
    ("Well done", "compliment"),
    ("You're the best", "compliment"),
    ("I appreciate you", "compliment"),

    # Frustration
    ("This is annoying", "frustration"),
    ("I'm so frustrated", "frustration"),
    ("Why isn't this working?", "frustration"),
    ("I'm angry", "frustration"),
    ("This makes me mad", "frustration"),

    # Sadness
    ("I'm feeling down", "sadness"),
    ("I'm sad", "sadness"),
    ("I feel lonely", "sadness"),
    ("This is depressing", "sadness"),
    ("I'm heartbroken", "sadness"),

    # Happiness
    ("I'm so happy", "happiness"),
    ("This is wonderful", "happiness"),
    ("I'm excited", "happiness"),
    ("Yay!", "happiness"),
    ("Best day ever", "happiness"),

    # Confusion
    ("I'm confused", "confusion"),
    ("I don't get it", "confusion"),
    ("Can you explain?", "confusion"),
    ("What do you mean?", "confusion"),
    ("I'm lost", "confusion"),

    # Jokes
    ("Tell me a joke", "joke"),
    ("Make me laugh", "joke"),
    ("Got any jokes?", "joke"),
    ("Funny stuff", "joke"),
    ("You're hilarious", "joke"),

    # Sarcasm
    ("Oh, great", "sarcasm"),
    ("Just what I needed", "sarcasm"),
    ("Fantastic...", "sarcasm"),
    ("Yeah, right", "sarcasm"),
    ("Wonderful news", "sarcasm"),

    # Flirtation
    ("You're cute", "flirtation"),
    ("I like you", "flirtation"),
    ("You're charming", "flirtation"),
    ("Are you single?", "flirtation"),
    ("You're attractive", "flirtation"),

    # Gratitude
    ("Thank you", "gratitude"),
    ("Thanks a lot", "gratitude"),
    ("Much appreciated", "gratitude"),
    ("I'm grateful", "gratitude"),
    ("Thanks!", "gratitude"),
]


# Split input and output
X = [item[0] for item in training_data]
y = [item[1] for item in training_data]


# 3. Vectorize Text
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X)

# 4. Train the Classifier
model = MultinomialNB()
model.fit(X_vectors, y)

# 5. Define Prediction Function
def predict_intent(user_input):
    input_vector = vectorizer.transform([user_input])
    return model.predict(input_vector)[0]

# 6. Define Responses
responses = {
    "greeting": "Hi there! How can I help you today?",
    "goodbye": "Goodbye! Have a great day!",
    "name_query": "I'm a chatbot, created by Arnav.",
    "help_request": "Sure, I'm here to help! Tell me what you need.",
    "capabilities": "I can answer your questions, help with tasks, and chat with you!",
    "thanks": "You're welcome!",
    "confused": "I'm sorry, I didn't quite catch that. Could you rephrase?",
    "apology": "No worries, it's all good!",
    "compliment": "Thank you! You're too kind.",
    "frustration": "I'm sorry you're feeling frustrated. How can I assist?",
    "sadness": "I'm here for you. Want to talk about it?",
    "happiness": "That's fantastic! I'm glad to hear it.",
    "confusion": "Let me try to explain it differently.",
    "joke": "Why did the computer show up at work late? It had a hard drive!",
    "sarcasm": "I sense some sarcasm. Care to elaborate?",
    "flirtation": "You're making me blush!",
    "gratitude": "You're welcome! Happy to help.",
}



# 7. Chat Loop
if __name__ == "__main__":
    print("Chatbot: Hey there! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        intent = predict_intent(user_input)
        print("Chatbot:", responses.get(intent, "Sorry, I didn't understand that."))