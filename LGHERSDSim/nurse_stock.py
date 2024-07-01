from stock import Stock
from nurse import Nurse


class NurseStock(Stock):
    def __init__(self, name, initial_value=0):
        super().__init__(name, initial_value)
        self.__nurses = []

    @property
    def nurses(self):
        return self.__nurses

    def add_nurse(self, nurse):
        if isinstance(nurse, Nurse):
            self.__nurses.append(nurse)
            self.increase(1)

    def remove_nurse(self, nurse):
        if nurse in self.__nurses:
            self.__nurses.remove(nurse)
            self.decrease(1)
