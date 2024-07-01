from stock import Stock


class BedStock(Stock):
    def __init__(self, name, initial_value=0):
        super().__init__(name, initial_value)
        self.__beds = initial_value

    @property
    def beds(self):
        return self.__beds

    @beds.setter
    def beds(self, value):
        self.__beds = value

    def add_bed(self):
        self.increase(1)

    def remove_bed(self):
        self.decrease(1)
