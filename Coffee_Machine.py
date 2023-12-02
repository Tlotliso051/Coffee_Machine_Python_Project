
# global values of the values to calculate
water, milk, coffee, money = 1000, 1000, 500, 2.4

latte = {"water": 100,"milk": 50,"coffee": 76,"money": 1.50}
espresso =  {"water": 150,"milk": 50,"coffee": 76,"money": 2.70}
cappuccino = {"water": 200,"milk": 50,"coffee": 76,"money": 4.50}

def user_input_for_coffee():
    '''
    The function requests the user to choose the coffee of their own choice.
    '''
    user_input = input("please Choose coffee of your choice (espresso, latte, cappuccino): ").lower()
    return user_input


def validate_the_input(user_input):
    '''
    The function validates if the input from the user is valid
    '''
    list_of_valid_prompts = ["off", "report", "espresso", "latte","cappuccino"]
    while True:
        if user_input == list_of_valid_prompts[0]:
            turn_off_machine()
            exit()
        elif user_input == list_of_valid_prompts[1]:
            print_report()
            exit()
        elif user_input.isalpha() == False or user_input == '':
            print("Please write the name without numeric/empty values.")
            continue
        else:
            if user_input in list_of_valid_prompts[2:]:
                return user_input


            
def check_resources(choosen_coffee):
    '''
    The function checks if there are enough resources to make choosen coffee
    '''
    global water, milk, coffee,latte,espresso,cappuccino

    if choosen_coffee == "latte" and (latte["water"] < water and latte["milk"] < milk and latte["coffee"] < coffee):
        output(choosen_coffee)

    elif choosen_coffee == "espresso" and (espresso["water"] < water and espresso["milk"] < milk and espresso["coffee"] < coffee):
        output(choosen_coffee)
            
    elif choosen_coffee == "cappuccino" and (cappuccino["water"] < water and cappuccino["milk"] < milk and cappuccino["coffee"] < coffee):
        output(choosen_coffee)

    else:
        print("Sorry there is not enough water.")


def output(choosen_coffee):
    '''
    The function works to print out the message about progressed coffee or information
    if there aren't enough resources to make coffee.
    '''
    print(f"Your {choosen_coffee.capitalize()} is in progress...")
    print("Please wait for a few minutes.")
     

def turn_off_machine():
    '''
    The function switches of the Machine
    '''
    print("Machine switching off...")
        

def print_report():
    '''
    This function prints the report.
    '''
    global water, milk, coffee, money
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def get_user_coins(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input[0].lower() in ('y', 'n'):
            return user_input[0].lower()
        else:
            print("Invalid input. Please enter 'y'/'yes or 'n'/'no'.")


def insert_coin():
    print("Coffee ready, do you want to make the payment?")

    user_response = get_user_coins("Enter 'y'/'yes', 'n'/'no' : ")

    if user_response == 'n':
        print("Thank you, come back for purchase later.")
        exit()

    print("Purchase Step".center(30, "-"))

    try:
        quarters = int(input("Insert quarters coins: "))
        dimes = int(input("Insert dimes: "))
        nickels = int(input("Insert nickels: "))
        pennies = int(input("Insert pennies: "))
    except ValueError:
        print("Please enter only numeric values.")
        exit()

    return quarters, dimes, nickels, pennies

            
        
def process_coins():
    '''
    The function process and converts coins to the right monetary value
    '''
    global water, milk, coffee, money
    
    monetary_values = 0.25 *quarters + 0.10 * dimes + 0.05 * nickles + 0.001 * pennies
    return round(monetary_values,2)


def process_coffee_transaction(coffee_type, inserted_amount):
    '''
    This functions process the transactions and checks if the coins added are enough to purchase the coffee.
    '''
    global money, latte, espresso, cappuccino

    if coffee_type["money"] == inserted_amount:
        money += coffee_type["money"]
    elif inserted_amount > coffee_type["money"]:
        change = round(inserted_amount - coffee_type["money"], 2)
        money += coffee_type["money"]
        print(f"Here is ${change} change.")
    else:
        print("Sorry, that's not enough money. Money refunded.")


def transaction(inserted_amount, name_of_coffee):
    '''
    This function check the type of the coffee selected and process it.
    '''
    global money, latte, espresso, cappuccino

    if name_of_coffee == 'latte':
        process_coffee_transaction(latte, inserted_amount)
    elif name_of_coffee == 'espresso':
        process_coffee_transaction(espresso, inserted_amount)
    elif name_of_coffee == 'cappuccino':
        process_coffee_transaction(cappuccino, inserted_amount)



        


if __name__ == "__main__":

    name_of_coffee = user_input_for_coffee()
    input_validation = validate_the_input(name_of_coffee)
    check_the_resources = check_resources(input_validation)
    quarters, dimes, nickles, pennies = insert_coin()
    process_the_coins = process_coins()
    transactions_of_coffee = transaction(process_the_coins,name_of_coffee)