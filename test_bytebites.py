from models import FoodItem, Menu, Transaction, Customer


def make_menu():
    burger = FoodItem("Spicy Burger", 10.00, "Food", 4.5)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 3.8)
    cake = FoodItem("Chocolate Cake", 6.50, "Desserts", 4.9)
    tea = FoodItem("Iced Tea", 3.00, "Drinks", 4.1)
    return Menu([burger, soda, cake, tea])


def test_order_total_with_multiple_items():
    # A $10 burger and a $5 soda should total $15
    order = Transaction()
    order.add_item(FoodItem("Spicy Burger", 10.00, "Food", 4.5))
    order.add_item(FoodItem("Large Soda", 5.00, "Drinks", 3.8))
    assert order.calculate_total() == 15.00


def test_empty_order_total_is_zero():
    # An order with no items should total $0
    assert Transaction().calculate_total() == 0


def test_filter_by_category_returns_only_that_category():
    # Filtering by "Drinks" should return only drinks
    drinks = make_menu().filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)


def test_filter_by_category_ignores_case():
    # Searching "drinks" in lowercase should still find "Drinks" items
    drinks = make_menu().filter_by_category("drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]


def test_sort_by_popularity_puts_highest_first():
    # The highest-rated item should come first after sorting
    sorted_items = make_menu().sort_by_popularity()
    assert sorted_items[0].name == "Chocolate Cake"
    assert sorted_items[-1].name == "Large Soda"


def test_record_purchase_adds_to_history():
    # Recording a purchase should add that transaction to the customer's history
    customer = Customer("Cody")
    order = Transaction()
    customer.record_purchase(order)
    assert customer.purchase_history == [order]
