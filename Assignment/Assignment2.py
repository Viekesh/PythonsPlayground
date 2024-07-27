import traceback

from typing import List

# Likely from a third-party library, remove if not used
# from bullet import Bullet, colors, utils


class PurchaseItem(object):
    def __init__(self, option):
        self.price = option.p
        self.name = str(option)


def get_total_order_amount(order: List[PurchaseItem]):
    """
    The total cost of all the items ordered
    """
    total_amount = 0
    for item in order:
        total_amount += item.price
    return total_amount


def get_service_charge(order_amount: float):
    """
    Calculates the service charge based on the order amount.
    Max service charge is 20%.
    """
    service_charge = 0
    if order_amount > 0:
        # Limit to max 20% or 600
        service_charge = min(order_amount * 0.2, 600)
    return service_charge


class Option(object):
    def __init__(self, n=None, pu=None, p=None, d=None):
        self.p = p
        self.n = n
        self.pu = pu
        if d:
            self.n = d.get("name")
            self.p = d.get("price")
        if self.p is None:
            self.p = 0
        if self.n is None:
            raise AttributeError
        self.pu = self.pu if self.pu else "Rs."

    def __str__(self):
        return f"{str(self.n)} {str(self.pu) + ' ' + str(self.p) if self.p else ''}"


MCDONALDS_FOOD_OPTIONS = [
    Option(d={"name": "Veg Burger", "price": 115.00}),
    Option(d={"name": "Veg Wrap", "price": 130.00}),
    Option(d={"name": "Veg Happy Meal", "price": 215.00}),
    Option(d={"name": "Chicken Burger", "price": 175.00}),
    Option(d={"name": "Chicken Wrap", "price": 195.00}),
    Option(d={"name": "No, that's all", "price": 0.00}),
]

MCDONALDS_BEVERAGES_OPTIONS = [
    Option(d={"name": "Sprite (M)", "price": 115.00}),
    Option(d={"name": "Sprite (L)", "price": 130.00}),
    Option(d={"name": "Mango Smoothie", "price": 215.00}),
    Option(d={"name": "Chocolate Smoothie", "price": 175.00}),
    Option(d={"name": "Chocolate Smoothie w/ Icecream", "price": 195.00}),
    Option(d={"name": "No, that's all", "price": 0.00}),
]


def get_option_from_result(result, options):
    for option in options:
        if str(option) == result:
            return option

    raise ValueError(f"Invalid option: {result}")  # Handle invalid options


def print_order(order):
    print()

    total_amount = get_total_order_amount(order)
    service_charge = get_service_charge(total_amount)

    print("Final Order")
    for i, item in enumerate(order):
        print(f"{i+1}. {item.name}")

    print(f"Order Amount: {total_amount:.2f}")
    print(f"Service Charge: {service_charge:.2f}")
    print(f"Final Amount: {(total_amount + service_charge):.2f}")


print()
print("Welcome to McDonalds on your shell :)")
print("Here you can place your order")
print("And then we will show you your bill")

print()

order = []

while True:
    options = list(map(lambda x: str(x), MCDONALDS_FOOD_OPTIONS))
    # Removed Bullet dependency (if not used)
