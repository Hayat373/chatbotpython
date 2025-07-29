import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Download NLTK data
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

# Create GUI
window = tk.Tk()
window.title("GrokBot")
window.geometry("400x500")

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=20, width=40)
chat_area.pack(padx=10, pady=10)
chat_area.config(state="disabled")

# Input field
input_field = tk.Entry(window, width=40)
input_field.pack(padx=10, pady=10)

# Send button
def send_message():
    user_input = input_field.get()
    if user_input:
        chat_area.config(state="normal")
        chat_area.insert(tk.END, f"You: {user_input}\n")
        if user_input.lower() == "exit":
            chat_area.insert(tk.END, "GrokBot: Goodbye!\n")
            window.quit()
        else:
            response = chatbot.respond(user_input)
            chat_area.insert(tk.END, f"GrokBot: {response}\n")
        chat_area.config(state="disabled")
        input_field.delete(0, tk.END)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

# Run GUI
window.mainloop()