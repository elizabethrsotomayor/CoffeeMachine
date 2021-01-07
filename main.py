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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

money = 0


def generate_report(current_resources):
    return f"Water: {current_resources['water']}mL\nMilk: {current_resources['milk']}mL\nCoffee: {current_resources['coffee']}mL\nMoney: ${current_resources['money']:.2f}"


def check_user_choice(choice):
    """Returns the amount paid based on coins inserted"""
    amount_paid = 0.0
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    amount_paid = (quarters / 4) + (dimes * .10) + (nickels * 0.05) + (pennies * 0.01)

    return amount_paid


def modify_resources(item):
    if item == 'espresso' and resources['water'] >= 50 and resources['coffee'] >= 18:
        resources['water'] -= 50
        resources['coffee'] -= 18
        resources['money'] += 1.5
        return True
    elif item == 'latte' and resources['water'] >= 200 and resources['coffee'] >= 24 and resources['milk'] >= 150:
        resources['water'] -= 200
        resources['coffee'] -= 24
        resources['milk'] -= 150
        resources['money'] += 2.5
        return True
    elif item == 'cappuccino' and resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 100:
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 100
        resources['money'] += 3
        return True
    else:
        return False


def calculate_refund(item, amount):
    if item == 'espresso' and amount >= 1.5:
        refund = amount - 1.5
        if amount > 1.5:
            print("Here is ${:0.2f} in change.".format(refund))
    elif item == 'latte' and amount >= 2.50:
        refund = amount - 2.5
        if amount > 2.5:
            print("Here is ${:0.2f} in change.".format(refund))
    elif item == 'cappuccino' and amount >= 3:
        refund = amount - 3
        if amount > 3:
            print("Here is ${:0.2f} in change.".format(refund))
    else:
        # TODO: 6. Check transaction successful
        print("Sorry, that's not enough money. Money refunded.")
        return
    return refund


def game():
    game_should_continue = True
    while game_should_continue:
        # TODO: 1. Prompt user by asking what they would like
        user_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. Turn off the coffee machine by entering "off" to the prompt
        if user_choice == 'off':
            game_should_continue = False
        # TODO: 3. print report
        elif user_choice == 'report':
            print(generate_report(resources))
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            # TODO: 4. Check resources sufficient
            if modify_resources(user_choice):
                # TODO: 5. Process coins
                amount = check_user_choice(user_choice)
                refund = calculate_refund(user_choice, amount)
                if (user_choice == 'espresso' and amount >= 1.5) or (user_choice == 'latte' and amount >= 2.5) or (user_choice == 'cappuccino' and amount >= 3):
                    # TODO: 7. Make coffee
                    print(f"Here is your {user_choice} ☕ Enjoy!")
            else:
                print("Sorry, there is not enough water.")


game()
