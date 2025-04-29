def simple_chatbot():
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! How can I help you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        elif user_input == "how are you?":
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif user_input == "what is your name?":
            print("Chatbot: I am a simple chatbot created to assist you!")
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

simple_chatbot()
