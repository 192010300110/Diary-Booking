"""
This file contains the implementation of the Database class, which is responsible for managing appointments in SQLite.
"""

import sqlite3
from typing import List

from appointment import Appointment


class Database:
    def __init__(self, db_file: str):
        """
        Initialize a Database object with the given database file.
        """
        self.db_file = db_file
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """
        Create the necessary tables in the database if they do not exist.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                date TEXT,
                time TEXT,
                status TEXT,
                notes TEXT
            )
            """
        )
        self.connection.commit()

    def get_appointments(self) -> List[Appointment]:
        """
        Retrieve all appointments from the database.
        """
        self.cursor.execute("SELECT * FROM appointments")
        rows = self.cursor.fetchall()
        appointments = []
        for row in rows:
            appointment = Appointment(*row)
            appointments.append(appointment)
        return appointments

    def get_appointment(self, appointment_id: int) -> Appointment:
        """
        Retrieve an appointment from the database by its ID.
        """
        self.cursor.execute("SELECT * FROM appointments WHERE id = ?", (appointment_id,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        appointment = Appointment(*row)
        return appointment

    def add_appointment(self, appointment: Appointment):
        """
        Add a new appointment to the database.
        """
        self.cursor.execute(
            "INSERT INTO appointments (patient_name, date, time, status, notes) VALUES (?, ?, ?, ?, ?)",
            (appointment.patient_name, appointment.date, appointment.time, appointment.status, appointment.notes),
        )
        self.connection.commit()

    def update_appointment(self, appointment: Appointment):
        """
        Update an existing appointment in the database.
        """
        self.cursor.execute(
            "UPDATE appointments SET patient_name = ?, date = ?, time = ?, status = ?, notes = ? WHERE id = ?",
            (appointment.patient_name, appointment.date, appointment.time, appointment.status, appointment.notes, appointment.id),
        )
        self.connection.commit()

    def delete_appointment(self, appointment_id: int):
        """
        Delete an appointment from the database by its ID.
        """
        self.cursor.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
        self.connection.commit()
