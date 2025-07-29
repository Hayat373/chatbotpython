import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define conversation pairs
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you", ["I'm doing great, thanks!", "I'm just a bot, but I'm happy!"]],
    [r"what is your name", ["I'm GrokBot, nice to meet you!"]],
    [r"bye|goodbye", ["See you later!", "Goodbye!"]],
    [r"what's the weather like", ["I don't have weather data, but it's always sunny in AI land!"]],
    [r"tell me a joke", ["Why did the computer go to school? To improve its 'byte'!"]],
    [r"(.*)", ["Sorry, I didn't understand that. Try something like 'hi' or 'how are you'."]],
    [r"what is ai", ["AI is artificial intelligence, like me! I'm a program that tries to understand and respond to your questions."]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Type something to talk to GrokBot (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("GrokBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"GrokBot: {response}")