# Generic class to model all medical staff (scalability reasons)
class MedicalStaff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    def __str__(self):
        return f"{self.__role}: {self.__name}"
