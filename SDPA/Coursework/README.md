# Part 1: Coffee Shop Simulation
## Overview
This project simulates the operations of a coffee shop, including barista management, sales status display, coffee selling, financial processing, and checking for bankruptcy over a specified number of months.

## File Structure
- `main.py`: The main script to initiate and run the entire coffee shop simulation.
- `CoffeeShop.py`: Defines the `CoffeeShop` class to model various operations of a coffee shop.
- `Barista.py`: Defines the `Barista` class representing a barista in the coffee shop.
- `Supplier.py`: Defines the `Supplier` class representing a supplier providing raw materials.

## `main.py`
### Features
- Simulates the operation of a coffee shop.
- Manages baristas, handles coffee sales, and processes finances.
- Checks for bankruptcy over given months.

### Design
- Incorporates the `Supplier`, `Barista`, and `CoffeeShop` classes.
- Utilizes exception handling to ensure valid user inputs.

## `CoffeeShop.py`
### Class `CoffeeShop`
#### Features
- Manages cash balance, suppliers, baristas, and ingredients stock.
- Processes coffee sales.

#### Methods
- `add_barista`, `remove_barista`: To add and remove baristas.
- `sell_coffee`: To sell coffee, checking for sufficient ingredients and labor.
- `buy_ingredients`: To purchase ingredients.
- `pay_expenses`: To handle monthly expenses.
- `apply_depreciation`: To apply depreciation to ingredients.
- `pay_pantry_cost`: To handle pantry costs.
- `display_status`: To display the current status of the coffee shop.
- `reset_barista_hours`: To reset the working hours of baristas.
- `is_bankrupt`: To check for bankruptcy.

## `Barista.py`
### Class `Barista`
#### Features
- Represents a barista, including their name, specialty, hourly rate, and work hours.

#### Methods
- `work`: Deducts the required working minutes.
- `reset_hours`: Resets working hours for a new month.
- `monthly_cost`: Calculates the monthly cost of employing the barista.

## `Supplier.py`
### Class `Supplier`
#### Features
- Represents a supplier with ingredient pricing.

#### Methods
- `get_cost`: Calculates the cost for a specified quantity of an ingredient.

## Design Decisions
During the design phase, an object-oriented approach was chosen to clearly separate and encapsulate different functionalities. For instance, operations of baristas, suppliers, and the coffee shop are encapsulated in distinct classes, enhancing the readability and maintainability of the code. This approach allows each class to focus on its specific responsibilities, with the main script `main.py` coordinating their interactions.

## Usage
Run the main script `main.py` to start the simulation. The script will prompt the user to enter the number of months to simulate and the number of baristas to hire. The simulation will then run for the specified number of months, displaying the status of the coffee shop at the end of each month. The simulation will terminate if the coffee shop goes bankrupt or if the specified number of months is reached.

---

# Part 2: NBA Data Analysis

### Overview
Part 2 of the project includes detailed documentation and implementation of some datasets about NBA games analyses in a Jupyter Notebook. This section provides guidelines on how to navigate and use the Jupyter Notebook for this part of the project.

### Additional Libraries

The following libraries are required to run the Jupyter Notebook:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `sklearn`
- `nba_api` : used to retrieve NBA data from the [nba wibsite](https://www.nba.com/stats/)

You can install these libraries using `pip`:
```
pip install -r requirements.txt
```

---
GitHub URL: https://github.com/Slliki/UOBum23937_EMATM0048.git
