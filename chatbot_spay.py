from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy

# Load spacy model
nlp = spacy.load("en_core_web_sm")

# Create chatbot
chatbot = ChatBot("MyFirstBot")
trainer = ListTrainer(chatbot)
training_data = [
    "Hello", "Hi there!",
    "How are you?", "I'm doing great, thanks!",
    "What's your name?", "I'm MyFirstBot, nice to meet you!",
    "Bye", "Goodbye, see you soon!"
]
trainer.train(training_data)

# Process input with spacy
def process_input(user_input):
    doc = nlp(user_input)
    entities = [ent.text for ent in doc.ents]
    if entities:
        return f"I noticed you mentioned {entities}. Can you tell me more?"
    return None

# Start conversation
print("Type something to talk to MyFirstBot (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    spacy_response = process_input(user_input)
    if spacy_response:
        print(f"Bot: {spacy_response}")
    else:
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")