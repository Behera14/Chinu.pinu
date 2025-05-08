def bookstore_chatbot():
    print("📚 Welcome to BookBuddy - Your Online Bookstore Assistant!")
    print("Type 'exit' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("Bot: Thank you for visiting BookBuddy. Have a great day!")
            break

        elif 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello! How can I help you today?")

        elif 'available' in user_input or 'have' in user_input:
            print("Bot: Yes, we have a wide collection of books. What genre are you interested in?")

        elif 'order' in user_input and 'status' in user_input:
            print("Bot: Please provide your order ID to check the status.")

        elif 'return' in user_input:
            print("Bot: You can return any book within 7 days of delivery. Would you like to initiate a return?")

        elif 'contact' in user_input or 'support' in user_input:
            print("Bot: You can reach our support at support@bookbuddy.com or call 1800-BOOK-123.")

        else:
            print("Bot: I'm sorry, I didn't understand that. Could you please rephrase your question?")

# Run the chatbot
bookstore_chatbot()
