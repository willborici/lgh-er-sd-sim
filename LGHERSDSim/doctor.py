# Physician subclass
# TODO: for more complex sim, this class can serve a supertype for specialties
from medical_staff import MedicalStaff


class Doctor(MedicalStaff):
    def __init__(self, name, specialty):
        super().__init__(name, "Doctor")
        self.__specialty = specialty

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, value):
        self.__specialty = value
