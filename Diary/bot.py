from tkinter import *
from tkinter import messagebox
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import datetime

# Define the chatbot
bot = ChatBot("Diary Bot")

# Train the chatbot on the English corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Define the GUI window
root = Tk()
root.title("Chatbot Diary")

# Create a label and text box for the conversation
conversation_label = Label(root, text="Conversation:")
conversation_label.pack()
conversation_box = Text(root, height=10, width=50)
conversation_box.pack()

# Create a label and text box for the user's message
message_label = Label(root, text="Your message:")
message_label.pack()
message_box = Entry(root, width=50)
message_box.pack()

# Define a function to send the user's message and get the bot's response
def send_message():
    message_text = message_box.get().strip()
    if message_text:
        response_text = bot.get_response(message_text)
        conversation_box.insert(END, f"You: {message_text}\n")
        conversation_box.insert(END, f"{bot.name}: {response_text}\n")
        message_box.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a message first.")

# Create a button to send the user's message
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Create a button to save the conversation as a diary entry
def save_entry():
    date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_text = conversation_box.get("1.0", END).strip()
    if conversation_text:
        filename = f"diary_{date_string}.txt"
        with open(filename, "w") as f:
            f.write(conversation_text)
        messagebox.showinfo("Success", "Diary entry saved!")
        conversation_box.delete("1.0", END)
    else:
        messagebox.showwarning("Warning", "There is nothing to save.")

save_button = Button(root, text="Save Entry", command=save_entry)
save_button.pack()

# Run the GUI window
root.mainloop()

""" When you run this program, a GUI window will appear with a label, a conversation text box, a message text box, and two buttons. You can type a message in the message text box and click the "Send" button to send it to the bot. The bot will respond with a message, which will be displayed in the conversation text box. You can continue chatting with the bot and the conversation will be logged in the text box.

When you're finished chatting, you can click the "Save Entry" button to save the conversation as a diary entry. The text file will be named "diary_DATE_TIME.txt" and will be saved in the same directory as the Python program. If you try to save an empty diary entry, a warning message will appear. If you successfully save a diary entry, a success message will appear, and the conversation text box will be cleared so you can start a new conversation.
"""