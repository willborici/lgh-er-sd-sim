from stock import Stock


class EquipmentStock(Stock):
    def __init__(self, name, initial_value=0):
        super().__init__(name, initial_value)
        self.__equipment = []

    @property
    def equipment(self):
        return self.__equipment

    def add_equipment(self, equipment):
        self.__equipment.append(equipment)
        self.increase(1)

    def remove_equipment(self, equipment):
        self.__equipment.remove(equipment)
        self.decrease(1)
