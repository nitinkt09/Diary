from tkinter import *
from datetime import datetime
from tkinter import messagebox

# Define the GUI window
root = Tk()
root.title("Chatbot Diary")

# Create a label and text box for the conversation
conversation_label = Label(root, text="Conversation:")
conversation_label.grid(row=0, column=0)
conversation_box = Text(root, height=10, width=50)
conversation_box.grid(row=1, column=0)

# Create a label and text box for the user's message
message_label = Label(root, text="Your message:")
message_label.grid(row=2, column=0)
message_box = Entry(root, width=50)
message_box.grid(row=3, column=0)

# Define a function to send the user's message and get the bot's response
def send_message():
    message_text = message_box.get().strip()
    if message_text:
        response_text = get_bot_response(message_text)
        conversation_box.insert(END, f"You: {message_text}\n")
        conversation_box.insert(END, f"Bot: {response_text}\n")
        message_box.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a message first.")

# Create a button to send the user's message
send_button = Button(root, text="Send", command=send_message)
send_button.grid(row=4, column=0)

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
save_button.grid(row=5, column=0)

# Define a function to get the bot's response
def get_bot_response(message_text):
    # Replace this with your own chatbot functionality
    # This is just a simple example that always responds with "Hello!"
    return "Hello!"

# Run the GUI window
root.mainloop()


