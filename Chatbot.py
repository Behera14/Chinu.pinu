import random

class FoodieBot:
    def __init__(self):
        self.cart = []
        self.booking = None
        self.menu = {
            "starters": ["Spring Rolls", "Garlic Bread", "Chicken Wings"],
            "main course": ["Butter Chicken", "Paneer Tikka", "Veg Biryani", "Pasta Alfredo"],
            "desserts": ["Gulab Jamun", "Brownie", "Ice Cream"],
            "drinks": ["Lassi", "Mojito", "Coke"]
        }

    def greet(self):
        name = input("What's your name? ")  # Ask for the user's name
        print(f"Hi {name}! Welcome to Foodie's Paradise Restaurant!")
        print("I am FoodieBot, your virtual assistant.")
        print("You can ask about the menu, place orders, book tables, or type 'help' for all options.")

    def show_menu(self):
        print("Here's our menu:")
        for category, items in self.menu.items():
            print(f"  - {category.title()}: {', '.join(items)}")

    def show_menu_by_category(self, category):
        items = self.menu.get(category)
        if items:
            print(f"{category.title()} Options: {', '.join(items)}")
        else:
            print("Sorry, we don't have that category. Try starters, main course, desserts or drinks.")

    def book_table(self):
        name = input("Your name: ")
        people = input("Number of guests: ")
        time = input("Preferred time: ")
        self.booking = {"name": name, "people": people, "time": time}
        print(f"Table booked for {people} people under '{name}' at {time}.")

    def cancel_booking(self):
        if self.booking:
            print(f"Booking for {self.booking['name']} has been cancelled.")
            self.booking = None
        else:
            print("No booking found.")

    def order_item(self):
        item = input("Enter item name to order: ").title()
        if any(item in cat for cat in self.menu.values()):
            self.cart.append(item)
            print(f"'{item}' added to your order.")
        else:
            print("Item not found in menu.")

    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your current order:")
            for i, item in enumerate(self.cart, 1):
                print(f"  {i}. {item}")

    def clear_cart(self):
        self.cart.clear()
        print("Your cart has been cleared.")

    def show_special(self):
        category = random.choice(list(self.menu.keys()))
        item = random.choice(self.menu[category])
        print(f"Today's Special: {item} from our {category.title()} section.")

    def help_menu(self):
        print("""
You can type:
- show menu
- show starters / main course / desserts / drinks
- order item
- show cart
- clear cart
- book table
- cancel booking
- show special
- hours / timings
- location
- exit
""")

    def respond(self, user_input):
        user_input = user_input.lower()

        if user_input in ['hi', 'hello']:
            print("Hello! This is FoodieBot. How can I help you today?")
        elif 'menu' in user_input:
            self.show_menu()
        elif any(cat in user_input for cat in self.menu.keys()):
            category = next(cat for cat in self.menu.keys() if cat in user_input)
            self.show_menu_by_category(category)
        elif 'book' in user_input or 'reserve' in user_input:
            self.book_table()
        elif 'cancel' in user_input and 'booking' in user_input:
            self.cancel_booking()
        elif 'order' in user_input:
            self.order_item()
        elif 'cart' in user_input:
            self.show_cart()
        elif 'clear' in user_input and 'cart' in user_input:
            self.clear_cart()
        elif 'special' in user_input:
            self.show_special()
        elif 'hours' in user_input or 'timing' in user_input:
            print("We are open daily from 11 AM to 11 PM.")
        elif 'location' in user_input or 'where' in user_input:
            print("We are located at 123, Food Street, Flavor Town.")
        elif 'thank' in user_input:
            print("You're welcome!")
        elif 'help' in user_input:
            self.help_menu()
        elif user_input in ['exit', 'bye', 'quit']:
            print("Thank you for chatting with FoodieBot. Have a great day!")
            return False
        else:
            print("Sorry, I didn’t understand that. Try something else or type 'help'.")
        return True

    def run(self):
        self.greet()
        while True:
            user_input = input("\nYou: ")
            if not self.respond(user_input):
                break

# Run FoodieBot
if __name__ == "__main__":
    bot = FoodieBot()
    bot.run()


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



