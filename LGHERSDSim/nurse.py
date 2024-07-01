# Nurse subclass
# TODO: This can later be a supertype for types of nurses (RN, NP, etc.).
from medical_staff import MedicalStaff


class Nurse(MedicalStaff):
    def __init__(self, name, efficiency):
        super().__init__(name, "Nurse")
        self.__efficiency = efficiency

    @property
    def efficiency(self):
        return self.__efficiency

    @efficiency.setter
    def efficiency(self, value):
        self.__efficiency = value
