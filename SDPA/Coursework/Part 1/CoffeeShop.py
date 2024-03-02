# Name: HAIBIN YIN
# Section: Part 1, CoffeeShop.py
# CoffeeShop.py: This class defines a CoffeeShop class, which models the operations of a coffee shop.
# It includes managing cash balance, suppliers, baristas, stock of ingredients, and processing coffee sales.

class CoffeeShop:
    def __init__(self, cash_balance, supplier):
        """
        Initializes a new CoffeeShop object with cash balance, supplier, and initial setup of baristas,
        ingredients stock, and other essential attributes.

        Parameters:
        cash_balance (float): The initial cash balance of the coffee shop.
         supplier (Supplier): The supplier for the coffee shop.
        """

        self.cash_balance = cash_balance
        self.supplier = supplier
        self.baristas = []
        self.ingredients_stock = {'milk': 300, 'beans': 20000, 'spices': 4000}  # current stock of ingredients
        self.max_ingredients = {'milk': 300, 'beans': 20000, 'spices': 4000}  # maximum stock of ingredients
        self.demand = {'Espresso': 500, 'Americano': 200, 'Filter': 300, 'Macchiato': 400, 'Flat White': 600,
                       'Latte': 1000}
        self.sales_prices = {'Espresso': 1.5, 'Americano': 2.5, 'Filter': 1.5, 'Macchiato': 3.0, 'Flat White': 3.5,
                             'Latte': 4.0}
        self.coffee_prep_time = {'Espresso': 3, 'Americano': 2, 'Filter': 1, 'Macchiato': 4, 'Flat White': 5,
                                 'Latte': 6}
        self.rent = 1500
        self.pantry_costs = {'milk': 0.1, 'beans': 0.001, 'spices': 0.001}
        self.depreciation_rate = {'milk': 0.4, 'beans': 0.1, 'spices': 0.1}
        self.recipes = {
            'Espresso': {'milk': 0, 'beans': 8, 'spices': 0},
            'Americano': {'milk': 0, 'beans': 6, 'spices': 0},
            'Filter': {'milk': 0, 'beans': 4, 'spices': 0},
            'Macchiato': {'milk': 0.1, 'beans': 8, 'spices': 2},
            'Flat White': {'milk': 0.2, 'beans': 8, 'spices': 1},
            'Latte': {'milk': 0.3, 'beans': 8, 'spices': 3}
        }

    def add_barista(self, barista):
        """
        Adds a barista to the coffee shop.

        Parameters:
        barista (Barista): The barista to be added.
        """

        self.baristas.append(barista)

    def remove_barista(self, barista_name):
        """
        Removes a barista from the coffee shop.

        Parameters:
        barista_name (str): The name of the barista to be removed.
        """

        self.baristas = list(filter(lambda barista: barista.name != barista_name, self.baristas))

    def sell_coffee(self, coffee_type, amount):
        """
        Attempts to sell a specified amount of a type of coffee. Checks for sufficient ingredients,
        available barista labor, and demand before making a sale.

        Parameters:
        coffee_type (str): The type of coffee to sell.
        amount (int): The amount of coffee to sell.

        Returns:
        bool: True if the sale is successful, False otherwise.
        """

        # Define total_time_needed at the beginning
        total_time_needed = self.coffee_prep_time[coffee_type] * amount

        # Calculate the maximum amount of coffee that can be made with the current stock
        max_capacities = []

        for ingredient, required in self.recipes[coffee_type].items():
            if required > 0:
                # Calculate the maximum amount of coffee that can be made with the current stock for each ingredient
                max_capacity_for_ingredient = self.ingredients_stock[ingredient] // required
                max_capacities.append(max_capacity_for_ingredient)

        # find the minimum value of the maximum capacities
        max_capacity_ingredients = min(max_capacities)

        # Calculate the maximum amount of coffee that can be made with the current labour
        total_available_time = sum(barista.available_minutes for barista in self.baristas)
        max_capacity_labour = total_available_time // self.coffee_prep_time[coffee_type]

        # Check if enough ingredients are available
        if max_capacity_ingredients < amount:
            print(f"Insufficient ingredients. Maximum capacity for {coffee_type}: {max_capacity_ingredients}")
            return False

        # Check if there is enough labour
        if max_capacity_labour < amount:
            print(f"Insufficient labour. Maximum capacity for {coffee_type}: {max_capacity_labour}")
            return False

        # check if amount to sell is less than demand
        if amount > self.demand[coffee_type]:
            print(f"Maximum demand for {coffee_type} is {self.demand[coffee_type]}")
            return False

        # Deduct the hours from specialized baristas first
        specialized_baristas = list(filter(lambda b: b.specialty == coffee_type, self.baristas))
        regular_baristas = list(filter(lambda b: b.specialty != coffee_type, self.baristas))

        time_deducted = False
        for barista in specialized_baristas:
            time_needed_for_specialist = total_time_needed / 2
            if barista.available_minutes >= time_needed_for_specialist:
                barista.work(time_needed_for_specialist)
                total_time_needed -= time_needed_for_specialist
                time_deducted = True
                break

        # If no specialized barista or time not fully deducted, use regular baristas
        if not time_deducted:
            for barista in regular_baristas:
                if barista.available_minutes >= total_time_needed:
                    barista.work(total_time_needed)
                    break

        # deduct ingredients and update cash balance
        for ingredient, required in self.recipes[coffee_type].items():
            self.ingredients_stock[ingredient] -= required * amount

        self.cash_balance += self.sales_prices[coffee_type] * amount

        return True

    def buy_ingredients(self):
        """
        Buys ingredients from the supplier to replenish stock, based on cash balance and need.
        """

        for ingredient, max_qty in self.max_ingredients.items():
            if self.ingredients_stock[ingredient] < max_qty:
                required_qty = max_qty - self.ingredients_stock[ingredient]
                cost = self.supplier.get_cost(ingredient, required_qty)
                if self.cash_balance >= cost:
                    self.ingredients_stock[ingredient] += required_qty
                    self.cash_balance -= cost
                else:
                    print(f"Not enough cash to purchase more {ingredient}.")

    def pay_expenses(self):
        """
         Pays the monthly expenses of the coffee shop, including barista salaries and rent.
        """

        for barista in self.baristas:
            self.cash_balance -= barista.monthly_cost()
        self.cash_balance -= self.rent

    def apply_depreciation(self):
        """
        Applies depreciation to the ingredients stock.
        """

        for ingredient, rate in self.depreciation_rate.items():
            self.ingredients_stock[ingredient] -= -(-self.ingredients_stock[ingredient] * rate // 1)

    def pay_pantry_cost(self):
        """
        Pays the monthly pantry cost of the coffee shop, based on the ingredients stock.
        """

        for ingredient, quantity in self.ingredients_stock.items():
            self.cash_balance -= quantity * self.pantry_costs[ingredient]

    def display_status(self):
        """
        Displays the status of the coffee shop, including cash balance, barista status, and ingredients in stock.
        """

        print(f"Cash balance: £{self.cash_balance:.2f}")
        print("Baristas:")
        for barista in self.baristas:
            print(f" - {barista.name}: {barista.available_minutes} minutes available, specialty: {barista.specialty}")
        print("Ingredients in stock:")
        for ingredient, quantity in self.ingredients_stock.items():
            print(f" - {ingredient}: {quantity} g or L")

    # reset barista hours to full
    def reset_barista_hours(self):
        """
        Resets the hours of all baristas to the maximum for a new month.
        """

        for barista in self.baristas:
            barista.reset_hours()

    # check if the shop is bankrupt
    def is_bankrupt(self):
        """
        Checks if the coffee shop is bankrupt.
        """

        if self.cash_balance < 0:
            return True
        else:
            return False
