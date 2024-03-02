# Name: HAIBIN YIN
# Section: Part 1, Supplier.py
# Supplier.py: This program defines a Supplier class. It represents a supplier with default prices
# for ingredients like milk, beans, and spices. It includes functionality to calculate the cost of
# ingredients based on quantity.

class Supplier:
    """
    Default prices for various ingredients.
    """

    default_prices = {
        'milk': 0.30,
        'beans': 0.10,
        'spices': 0.05,
    }

    def __init__(self, name, prices=None):
        """
        Initializes a new Supplier object with the given name and prices.
        If no prices are provided, uses default prices.

        Parameters:
        name (str): The name of the supplier.
        prices (dict, optional): A dictionary of prices for ingredients. Default is None, which uses default prices.
        """
        self.name = name
        self.prices = prices if prices is not None else Supplier.default_prices

    def get_cost(self, ingredient, quantity):
        """
        Calculates the cost of a specified quantity of an ingredient.

        Parameters:
        ingredient (str): The ingredient for which cost is being calculated.
        quantity (float): The quantity of the ingredient.

        Returns:
        float: The total cost for the specified quantity of the ingredient.
        """
        return self.prices[ingredient] * quantity

# Example usage
# supplier = Supplier("Hasty")
# print(supplier.get_cost('beans', 3))
