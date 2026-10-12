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


class Transaction:
    def __init__(self, items=None):
        self.items = items if items is not None else []


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []
