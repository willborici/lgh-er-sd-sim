# Modeling the LGH ER area
# TODO: encapsulate!
class ERRoom:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_patients = []

    def admit_patient(self, patient):
        if len(self.current_patients) < self.capacity:
            self.current_patients.append(patient)
            return True
        return False

    def discharge_patient(self, patient):
        if patient in self.current_patients:
            self.current_patients.remove(patient)
