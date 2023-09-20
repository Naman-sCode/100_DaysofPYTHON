MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# COINS
def process_coins():
    """Returns the total amount of coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?:")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    money_received = quarters + dimes + nickles + pennies
    return money_received


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    # if money_received < MENU[coffee_type]["cost"]:
    #     print("Sorry that's not enough money. Money refunded.")
    # elif money_received >= MENU[coffee_type]["cost"]:
    #     change = money_received - MENU[coffee_type]["cost"]
    #     print(f"Here is {change} in change.")
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️")


is_on = True

while is_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_type == "off":
        is_on = False
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee_type]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_type, drink["ingredients"])
