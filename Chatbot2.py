import random

class FoodieBot:
    def __init__(self):
        self.cart = []
        self.booking = None
        self.menu = {
            "starters": ["Spring Rolls", "Garlic Bread"],
            "main": ["Butter Chicken", "Paneer Tikka"],
            "desserts": ["Gulab Jamun", "Ice Cream"],
            "drinks": ["Lassi", "Coke"]
        }

    def greet(self):
        name = input("What's your name? ")
        print(f"Hi {name}, welcome to Foodie's Paradise!")
        print("Type 'help' to see what I can do.")

    def show_menu(self, category=None):
        if category and category in self.menu:
            print(f"{category.title()}: {', '.join(self.menu[category])}")
        else:
            for cat, items in self.menu.items():
                print(f"{cat.title()}: {', '.join(items)}")

    def book_table(self):
        name = input("Name: ")
        people = input("Guests: ")
        time = input("Time: ")
        self.booking = (name, people, time)
        print(f"Booked for {people} under {name} at {time}.")

    def order_item(self):
        item = input("Item to order: ").title()
        if any(item in items for items in self.menu.values()):
            self.cart.append(item)
            print(f"{item} added to cart.")
        else:
            print("Item not found.")

    def show_cart(self):
        print("Cart:", ', '.join(self.cart) if self.cart else "Empty")

    def respond(self, msg):
        msg = msg.lower()
        if msg == "help":
            print("Options: menu, starters, main, desserts, drinks, order, cart, book, special, exit")
        elif msg in ["menu", "starters", "main", "desserts", "drinks"]:
            self.show_menu(msg if msg != "menu" else None)
        elif msg == "order":
            self.order_item()
        elif msg == "cart":
            self.show_cart()
        elif msg == "book":
            self.book_table()
        elif msg == "special":
            cat = random.choice(list(self.menu))
            item = random.choice(self.menu[cat])
            print(f"Today's Special: {item} ({cat})")
        elif msg in ["exit", "bye", "quit"]:
            print("Goodbye! Enjoy your meal.")
            return False
        else:
            print("Didn't get that. Type 'help'.")
        return True

    def run(self):
        self.greet()
        while True:
            if not self.respond(input("\nYou: ")):
                break

# Run the bot
if __name__ == "__main__":
    FoodieBot().run()


"""FoodieBot: Overview
FoodieBot is a Python-based virtual assistant for a restaurant that can:

Show menu: Displays food categories (starters, main course, desserts, drinks).

Order items: Allows users to order from the menu.

Manage cart: Shows current orders and clears the cart.

Book/cancel table: Allows users to reserve or cancel table bookings.

Special of the day: Randomly picks and shows a special menu item.

Help: Provides a list of commands the user can type for assistance.

Key Methods:
greet(): Welcomes the user and introduces FoodieBot.

show_menu(): Displays the entire menu.

show_menu_by_category(category): Shows items in a specific category (e.g., starters).

book_table(): Takes details for table reservation.

cancel_booking(): Cancels an existing booking.

order_item(): Adds an item to the cart.

show_cart(): Displays items in the cart.

clear_cart(): Empties the cart.

show_special(): Shows a random special item from the menu.

help_menu(): Lists commands the user can use.

respond(): Processes user input and calls the appropriate function.

run(): Starts the bot and handles user interactions in a loop.

Interaction Example:
User: "Hi"

Bot: "Hello! This is FoodieBot. How can I help you today?"

User: "Show menu"

Bot: Lists the full menu.

User: "Book a table"

Bot: Takes booking details and confirms.

Summary:
FoodieBot simulates a virtual assistant for a restaurant, handling 
menu queries, orders, bookings, and special offers with simple text input.
"""



