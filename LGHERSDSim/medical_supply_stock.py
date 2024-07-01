from stock import Stock


class MedicalSupplyStock(Stock):
    def __init__(self, name, initial_value=0):
        super().__init__(name, initial_value)
        self.__supplies = initial_value

    @property
    def supplies(self):
        return self.__supplies

    @supplies.setter
    def supplies(self, value):
        self.__supplies = value

    def add_supply(self, amount):
        self.increase(amount)

    def remove_supply(self, amount):
        self.decrease(amount)
