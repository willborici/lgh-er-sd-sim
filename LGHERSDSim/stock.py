# Generic class to capture any stock object in a stock-and-flow model
# The stock has a name and a non-negative integer amount

class Stock:
    def __init__(self, name, initial_value=0):
        self.__name = name
        self.__value = initial_value

    # Get stock quantity
    @property
    def value(self):
        return self.__value

    # Update stock quantity
    @value.setter
    def value(self, amount):
        self.__value = amount

    # Get stock name
    @property
    def name(self):
        return self.__name

    # increase/ decrease stock quantity
    def increase(self, amount):
        self.__value += amount

    def decrease(self, amount):
        self.__value -= amount
