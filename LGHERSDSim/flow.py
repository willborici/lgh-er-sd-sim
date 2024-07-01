# Collection of flow-related logic
# TODO: expand with studied differential equations, like treatment_flow, etc.
def triage_flow(patients_waiting, patients_in_triage, nurse_efficiency):
    num_triaged = min(len(patients_waiting.patients), nurse_efficiency)
    for _ in range(num_triaged):
        patient = patients_waiting.patients.pop(0)
        patients_in_triage.add_patient(patient)
    patients_waiting.decrease(num_triaged)
