# Name: HAIBIN YIN
# Section: Part 1, Barista.py
# Barista.py: This program defines a Barista class. It models a barista with attributes
# such as name, specialty, rate per hour, and working hours. The class includes functionalities
# to track work hours, reset hours for a new month, and calculate the monthly cost of employing the barista.

class Barista:
    def __init__(self, name, specialty=None, rate_per_hour=15, hours_per_month=80):
        """
        Initializes a new Barista object with the given attributes.

        Parameters:
        name (str): The name of the barista.
        specialty (str, optional): The specialty of the barista. Default is None.
        rate_per_hour (float, optional): The hourly rate of the barista. Default is 15.
        hours_per_month (int, optional): The number of hours the barista works per month. Default is 80.
        """
        self.name = name
        self.rate_per_hour = rate_per_hour
        self.hours_per_month = hours_per_month
        self.available_minutes = hours_per_month * 60  # Total available minutes in a month
        self.hours_per_month_to_pay = 120
        self.specialty = specialty

    def work(self, minutes_needed):
        """
        Deducts the minutes needed from the barista's available minutes if they have enough minutes to work.

        Parameters:
        minutes_needed (int): The number of minutes the barista needs to work.

        Returns:
        bool: True if the barista can work for the specified minutes, False otherwise.
        """
        if self.available_minutes >= minutes_needed:
            self.available_minutes -= minutes_needed
            return True
        return False

    def reset_hours(self):
        """
        Resets the barista's available minutes to the maximum for a new month.
        """
        self.available_minutes = self.hours_per_month * 60

    def monthly_cost(self):
        """
        Calculates the monthly cost to employ the barista based on their hourly rate and hours per month.

        Returns:
        float: The monthly cost of employing the barista.
        """
        return self.rate_per_hour * self.hours_per_month_to_pay


# example usage
# jack = Barista("jack")
# print(jack.monthly_cost())
# print(jack.available_minutes)
# jack.work(100)
