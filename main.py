from menu import MENU, resources

profit = 0

# TODO: 4. Check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    """This returns true when order can be made, false if ingredients are insufficient"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


# TODO: 5. Process coins
def process_coins():
    """This returns the total calculated from coins inserted into the coffee machine."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# TODO: 6. Check if transaction is successful
def is_transaction_successful(money_received, cost_of_drink):
    """This returns true when order can be made (payment is accepted), false if money is sufficient."""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print(f"Sorry, there is not enough ${money_received}. Money refunded.")
        return False

# TODO: 7. Make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources of the coffee machine."""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name} coffee ☕️. Enjoy!")

is_on = True

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        is_on = False

    # TODO: 3. Print report of the coffee machine
    elif user_choice == "report":
       print(f"Water:{resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
