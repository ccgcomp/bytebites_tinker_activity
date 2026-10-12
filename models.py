# ByteBites backend models
#
# Classes (see bytebites_design.md for the UML):
#   Customer    - a customer's name and their past purchase history
#   FoodItem    - one item we sell: name, price, category, popularity rating
#   Menu        - the full collection of items, can filter by category
#   Transaction - the items a customer picked, and computes the total cost


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items):
        self.items = items

    def filter_by_category(self, category):
        # Return a new list of only the items whose category matches (ignoring case)
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self):
        # Return a new list of the items sorted by popularity rating, highest first
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item):
        # Add a picked FoodItem to this transaction
        self.items.append(item)

    def calculate_total(self):
        # Add up the prices of every item in this transaction
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def record_purchase(self, transaction):
        # Add a finished Transaction to this customer's purchase history
        self.purchase_history.append(transaction)
