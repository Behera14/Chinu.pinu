def shopping_chatbot():
    print("🛍️ Welcome to ShopEasy Bot!")
    print("How can I assist you today?")
    print("Type 'exit' or 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "order" in user_input:
            print("Bot: You can check your order status in the 'My Orders' section on our website.")
        elif "return" in user_input:
            print("Bot: To return an item, go to 'My Orders', click on the item, and select 'Return'.")
        elif "refund" in user_input:
            print("Bot: Refunds are processed within 5-7 business days after item pickup.")
        elif "shipping" in user_input or "delivery" in user_input:
            print("Bot: Shipping usually takes 3-5 days. You can track it under 'My Orders'.")
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you today?")
        elif "thank" in user_input:
            print("Bot: You're welcome! 😊")
        elif user_input in ["exit", "bye"]:
            print("Bot: Thank you for chatting with ShopEasy. Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I didn't understand that. Please ask about orders, returns, shipping, or refunds.")

# Run the chatbot
shopping_chatbot()
