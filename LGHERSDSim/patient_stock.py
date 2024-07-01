# Define the patient stock subclass
from stock import Stock


class PatientStock(Stock):
    def __init__(self, name, initial_value=0):
        super().__init__(name, initial_value)
        self.__patients = []

    # Display the patients in stock
    @property
    def patients(self):
        return self.__patients

    def add_patient(self, patient):
        self.__patients.append(patient)
        self.increase(1)

    def remove_patient(self, patient):
        self.__patients.remove(patient)
        self.decrease(1)
