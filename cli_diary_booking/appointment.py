"""
appointment.py
This file contains the implementation of the Appointment class, which represents appointment objects.
"""

class Appointment:
    def __init__(self, id: int, patient_name: str, date: str, time: str, status: str, notes: str):
        """
        Initialize an Appointment object with the given attributes.
        """
        self.id = id
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.status = status
        self.notes = notes

    def __str__(self) -> str:
        """
        Return a string representation of the Appointment object.
        """
        return f"Appointment ID: {self.id}\nPatient Name: {self.patient_name}\nDate: {self.date}\nTime: {self.time}\nStatus: {self.status}\nNotes: {self.notes}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Appointment object.
        """
        return f"Appointment(id={self.id}, patient_name='{self.patient_name}', date='{self.date}', time='{self.time}', status='{self.status}', notes='{self.notes}')"
