print("Chatbot: Hello! How can I help you?")

while True:

    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user:
        print("Bot: I am a simple AI chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you!")

    elif "course" in user:
        print("Bot: I can help you with your studies.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")

