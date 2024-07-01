# TODO: add a patient_id -- to be used as a business-friendly ref.
# TODO: encapsulate!
class Patient:
    def __init__(self, arrival_time, severity):
        self.arrival_time = arrival_time
        self.severity = severity  # simple 1 = low, 10 = emergency scale
        self.treatment_time = None
        self.departure_time = None

    def set_treatment_time(self, treatment_time):
        self.treatment_time = treatment_time

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
