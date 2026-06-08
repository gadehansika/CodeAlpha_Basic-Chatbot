def get_response(user_input):
    # Convert input to lowercase
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you?":
        return "I'm doing great! Thanks for asking."
    elif user_input == "what's your name?":
        return "I'm a simple chatbot."
    elif user_input == "who made you?":
        return "I was created by a Python developer."
    elif user_input == "what can you do?":
        return "I can chat with you and answer simple questions."
    elif user_input == "good morning":
        return "Good morning! Hope you have a great day!"
    elif user_input == "good night":
        return "Good night! Sleep well!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Try asking something else."


def run_chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_message = input("You: ")

        bot_reply = get_response(user_message)

        print("ChatBot:", bot_reply)

        if user_message.lower().strip() == "bye":
            break


def main():
    run_chatbot()


if __name__ == "__main__":
    main()
    