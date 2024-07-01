from stock import Stock
from doctor import Doctor


class PhysicianStock(Stock):
    def __init__(self, name, initial_value=0):
        super().__init__(name, initial_value)
        self.__physicians = []

    @property
    def physicians(self):
        return self.__physicians

    def add_physician(self, physician):
        if isinstance(physician, Doctor):
            self.__physicians.append(physician)
            self.increase(1)

    def remove_physician(self, physician):
        if physician in self.__physicians:
            self.__physicians.remove(physician)
            self.decrease(1)
