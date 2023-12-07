#Even numbers
"""
def even_numbers(arg):
    evened = list(filter(lambda x : x % 2 == 0, arg))
    return evened


print(even_numbers([1,2,3,4,5,6,7,8,9,10]))
"""
import random

#Square Elements
"""
def square_all(arg):
    def square_them(arg):
        return arg * arg
    squared_list = list(map(square_them, arg))
    return squared_list

print(square_all([1,2,3,4,5,6,7,8,9,10]))
"""

#Squared Even Numbers
"""
def square_even(arg):
    filtered = list(filter(lambda x : x % 2 == 0, arg))

    def square_them(arg):
        return arg * arg

    squared_list = list(map(square_them, filtered))
    return squared_list


print(square_even([1,2,3,4,5,6,7,8,9,10]))
"""

#Find certain numbers
"""
def find_numbers(min, max):
    all_numbers = list(range(min, max))

    filtered_seven = list(filter(lambda x: x % 7 == 0, all_numbers))
    filtered_not_five = list(filter(lambda x: x % 5 != 0, filtered_seven))

    print(filtered_not_five)


find_numbers(4,100)
"""

#Online Shop
"""
orders = [

    {
        'id': 'order_001',
        'item': 'Introduction to Python',
        'quantity': 1,
        'price_per_item': 32,
    },
    {
        'id': 'order_002',
        'item': 'Advanced Python',
        'quantity': 3,
        'price_per_item': 40,
    },
    {
        'id': 'order_003',
        'item': 'Python web frameworks',
        'quantity': 2,
        'price_per_item': 51,
    },
]

def compute_totals(arg):
    new_list = []
    for order in arg:
        if order["price_per_item"] * order["quantity"] < 100:
            order["total_price"] = order["price_per_item"] * order["quantity"] + 10
            changed_tuple = (order["id"], order["total_price"])
            new_list.append(changed_tuple)
        else:
            order["total_price"] = order["price_per_item"] * order["quantity"]
            unchanged_tuple = (order["id"], order["total_price"])
            new_list.append(unchanged_tuple)

    new_tuple = tuple(new_list)

    return new_tuple


totals = compute_totals(orders)
print(totals)
"""

#Restaurant

class Dish:
    def __init__(self, name, ingredients, client_price):
        self.name = name
        self.ingredients = ingredients
        self.costs = 0
        self.client_price = client_price

    def __str__(self):
        return self.name

    def cost(self):
        total = 10
        for el in self.ingredients:
            total += el.price
        self.costs += total

    def profit(self):
        profit = self.client_price - self.costs
        print(profit)

class Ingredients:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}.-"

class Restaurant:
    def __init__(self):
        self.orders = {}

    def order_dish(self, client, dish):
        if client not in self.orders:
            self.orders[client] = []
        self.orders[client].append(dish)

    def print_orders(self):
        for client, client_orders in self.orders.items():
            print(f"Client: {client}")
            for index, el in enumerate(client_orders):
                print(f"Order #{index}: {el}")
            print()

    def print_check(self, client):
        total_check = 0
        if client in self.orders:
            print(f"Client: {client}")
            for index, el in enumerate(self.orders[client]):
                total_check += el.client_price
                print(f"Order #{index}: {el}, price: {el.client_price}")
            print(f"Total for {client}: {total_check}")
        else:
            print(f"No orders found for {client}")

class Client:
    def __init__(self, name):
        self.name = name

    def order(self, restaurant, dish):
        restaurant.order_dish(self.name, dish)

    def checkout(self, restaurant):
        restaurant.print_check(self.name)


# Ingredients
sauce = Ingredients("Sauce", 5)
dough = Ingredients("Dough", 2)
leaf = Ingredients("Leaf", 1)

# Dishes
pizza = Dish("Pizza", [sauce, dough], 30)
salad = Dish("Salad", [leaf], 20)

# Restaurant
pizzeria = Restaurant()

# Clients
donald = Client("Donald")
kebab = Client("Kebab")

# Orders
donald.order(pizzeria, pizza)
donald.order(pizzeria, salad)
donald.checkout(pizzeria)

kebab.order(pizzeria, salad)
kebab.checkout(pizzeria)

# Print Orders