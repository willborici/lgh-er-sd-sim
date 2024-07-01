from patient_stock import PatientStock
from nurse_stock import NurseStock
from equipment_stock import EquipmentStock
from physician_stock import PhysicianStock
from bed_stock import BedStock
from medical_supply_stock import MedicalSupplyStock
from nurse import Nurse
from doctor import Doctor
from flow import triage_flow
import numpy as np
import matplotlib.pyplot as plt
from patient import Patient
from er_room import ERRoom


def simulate_er(simulation_time, nurse_efficiency):
    patients_waiting = PatientStock("Patients Waiting for Triage")
    patients_in_triage = PatientStock("Patients in Triage")
    patients_waiting_for_treatment = PatientStock("Patients Waiting for Treatment")
    patients_being_treated = PatientStock("Patients Being Treated")

    nurses_on_duty = NurseStock("Registered Nurses on Duty", initial_value=7)
    medical_equipment = EquipmentStock("Available Medical Equipment", initial_value=6)
    physicians_on_duty = PhysicianStock("Physicians on Duty", initial_value=4)
    beds_available = BedStock("Beds Available", initial_value=12)
    medical_supplies = MedicalSupplyStock("Medical Supplies", initial_value=9)

    # Initialize medical staff
    for i in range(13):
        nurses_on_duty.add_nurse(Nurse(f"Nurse {i + 1}", efficiency=3))
    for i in range(4):
        physicians_on_duty.add_physician(Doctor(f"Doctor {i + 1}", specialty="General"))

    # Initialize patients -- can change severity to a random dist between 1 and 10
    for _dummy in range(290):
        patients_waiting.add_patient(Patient(arrival_time=0, severity=5))

    for time in range(simulation_time):
        triage_flow(patients_waiting, patients_in_triage, nurse_efficiency)
        # TODO: Add more flows and logic as this grows

    print(f"Patients waiting for triage: {patients_waiting.value}")
    print(f"Patients in triage: {patients_in_triage.value}")
    print(f"Nurses on duty: {nurses_on_duty.value}")
    print(f"Medical equipment available: {medical_equipment.value}")
    print(f"Physicians on duty: {physicians_on_duty.value}")
    print(f"Beds available: {beds_available.beds}")
    print(f"Medical supplies: {medical_supplies.supplies}")


# Experiment with another sim
def simulate_er2(num_patients2, er_capacity2, simulation_time2):
    er = ERRoom(er_capacity2)
    # TODO: update patient arrival time based on LGH observed distribution:
    patients2 = ([Patient(arrival_time=np.random.randint(0, simulation_time2),
                  severity=np.random.randint(1, 10))
                  for _dummy in range(num_patients2)])

    for time in range(simulation_time2):
        for patient in patients2:
            if patient.arrival_time == time:
                admitted = er.admit_patient(patient)
                if admitted:
                    # Random treatment time
                    # TODO: update per corresponding differential equation
                    patient.set_treatment_time(time + np.random.randint(1, 10))
                else:
                    print(f"Patient {patient} could not be admitted at time {time}")

        # TODO: encapsulate ER attributes to avoid shallow copies like here:
        for patient in er.current_patients[:]:
            if patient.treatment_time and patient.treatment_time <= time:
                patient.set_departure_time(time)
                er.discharge_patient(patient)

    return patients2


def plot_results(patients2):
    arrival_times = [p.arrival_time for p in patients2]
    departure_times = [p.departure_time for p in patients2 if p.departure_time]

    plt.hist(arrival_times, bins=range(0, max(arrival_times) + 1), alpha=0.5, label='Arrival Times')
    plt.hist(departure_times, bins=range(0, max(departure_times) + 1), alpha=0.5, label='Departure Times')
    plt.legend(loc='upper left')
    plt.xlabel('Hour')
    plt.ylabel('Number of Patients')
    plt.title('Hospital ER Simulation')
    plt.show()


if __name__ == "__main__":
    # first sim expr.
    simulate_er(simulation_time=24, nurse_efficiency=5)

    # Second sim expr.
    num_patients = 290
    er_capacity = 72
    simulation_time = 24  # 24 hours, let's say

    patients = simulate_er2(num_patients, er_capacity, simulation_time)
    plot_results(patients)
