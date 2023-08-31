import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

with open('./dataset/cybersecurity.json') as f:
    intents_data = json.load(f)

intents = intents_data["intents"]
intent_tags = [intent["tag"] for intent in intents]
patterns = [pattern for intent in intents for pattern in intent["patterns"]]
responses = {intent["tag"]: intent["responses"] for intent in intents}
X_train = patterns
y_train = [intent["tag"] for intent in intents for _ in intent["patterns"]]
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)


def get_intent(message):
    return model.predict([message])[0]

class Model:
    def respond(message):
        intent = get_intent(message)
        if intent in responses:
            # return "hello world!"
            return random.choice(responses[intent])
        else:
            return "I don't understand. Please rephrase your question." 







# print("Bot: Hi there! Ask me something about the college.")
# while True:
#     user_input = input("You: ")
#     print("Bot:", respond(user_input))