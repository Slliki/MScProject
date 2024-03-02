# Name: HAIBIN YIN
# Section: Part 1, main.py
# Description: This script simulates the operation of a coffee shop, handling barista management, display status,
# coffee selling, financial processing, and checking for bankruptcy over a given number of months.

# import classes
from Supplier import Supplier
from Barista import Barista
from CoffeeShop import CoffeeShop

# Prompt the user for the number of months to simulate
# Prompt the user for the number of baristas to add or remove
# Prompt the user for the amount of each coffee type to sell
# Pay expenses, including rent and barista salaries
# Pay pantry cost,assume that the ingredients will depreciate after paying the pantry cost
# Display the status of the coffee shop
# Apply depreciation to the ingredients
# Buy ingredients
# Check if the coffee shop is bankrupt


def main():
    """
    Simulates the operation of a coffee shop, handling barista management, display status,
    coffee selling, financial processing, and checking for bankruptcy over a given number of months.
    """

    # initialising the coffee shop and supplier
    supplier = Supplier('Hasty')
    shop = CoffeeShop(cash_balance=10000, supplier=supplier)

    # set valid coffee types
    valid_coffee_types = ["Expresso", "Americano", "Filter", "Macchiatto", "Flat White", "Latte"]

    # check if the input is a positive integer for months to run
    while True:
        user_input = input("Please enter number of months: ")

        # if user input is null, run for 6 months
        if user_input == "":
            months_to_run = 6
            break

        try:
            months_to_run = int(user_input)
            if months_to_run > 0:
                break
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Simulation
    for month in range(1, months_to_run + 1):
        print(f"\n===== SIMULATING month {month} =====")

        while True:
            try:
                # prompt for barista change
                barista_change = int(
                    input("Baristas: To hire-->enter positive, to fire-->enter negative, no chang-->enter 0: "))
                new_barista_count = len(shop.baristas) + barista_change

                # check if the new barista count is valid
                if new_barista_count > 4:
                    print("Maximum number of baristas should be 4.")
                    continue
                elif new_barista_count < 1:
                    print("Minimum number of baristas should be 1.")
                    continue

                # add baristas
                if barista_change > 0:
                    for _ in range(barista_change):
                        barista_added = False
                        while not barista_added:
                            barista_name = input("Enter new barista name: ")
                            if any(barista.name == barista_name for barista in shop.baristas):
                                print(f"Barista name '{barista_name}' already exists. Please enter a different name.")
                                continue

                            # check if the input is null
                            if not barista_name:
                                print("Invalid name. Please enter a valid name.")
                                continue

                            # prompt the user for the specialty of the barista
                            specialty_prompt = input(
                                f"Does {barista_name} have a specialty? (yes/no): ").strip().lower()
                            # if yes, prompt the user for the specialty coffee type
                            if specialty_prompt == 'yes':
                                while True:
                                    specialty_coffee = input(
                                        f"What coffee type does {barista_name} specialize in?: ").strip()
                                    if specialty_coffee in valid_coffee_types:
                                        shop.add_barista(Barista(name=barista_name, specialty=specialty_coffee))
                                        barista_added = True
                                        break
                                    else:
                                        print(f"Invalid coffee type. Valid types are: {', '.join(valid_coffee_types)}")

                            # if no, add the barista without specialty
                            else:
                                shop.add_barista(Barista(name=barista_name))
                                barista_added = True

                # remove baristas, check if the barista name exists
                elif barista_change < 0:
                    for _ in range(-barista_change):
                        while True:
                            barista_name = input("Enter barista name to remove: ")
                            if any(barista.name == barista_name for barista in shop.baristas):
                                shop.remove_barista(barista_name)
                                break
                            else:
                                print(f"No barista found with the name '{barista_name}'. Please enter a valid name.")
                break

            except ValueError:
                print("Please enter an integer.")

        # display barista info
        print("\nBarista Info:")
        for barista in shop.baristas:
            print(f"{barista.name} has {barista.available_minutes} minutes available, specialty: {barista.specialty}")

        # prompt for selling coffee
        # check if the input is a positive integer for amount to sell (negative number is not allowed)
        for coffee_type in shop.sales_prices:

            while True:
                try:
                    amount_to_sell = int(input(f"{coffee_type} demand {shop.demand[coffee_type]}, how much to sell: "))
                    if amount_to_sell >= 0:
                        if shop.sell_coffee(coffee_type, amount_to_sell):
                            break
                    else:
                        print("Invalid input, please enter a positive number.")

                except ValueError:
                    print("Invalid input, please enter a positive number.")

        # pay expenses
        shop.pay_expenses()
        print(f"\nExpenses paid, cash balance: £{shop.cash_balance:.2f}")

        # pay pantry costs
        shop.pay_pantry_cost()
        print(f"Pantry costs paid, cash balance: £{shop.cash_balance:.2f}")

        # display status
        print('\nCurrent status:')
        shop.display_status()

        # apply depreciation
        shop.apply_depreciation()
        print(f"\nDepreciation applied, current pantry:{shop.ingredients_stock}")

        # buy ingredients
        shop.buy_ingredients()
        print(f"Ingredients bought, cash balance: £{shop.cash_balance:.2f}")

        # check if bankrupt
        if shop.is_bankrupt():
            print("You are bankrupt!")
            break

        # reset barista hours
        shop.reset_barista_hours()

    print("Simulation ends.")


if __name__ == '__main__':
    main()
