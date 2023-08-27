"""
main.py

Main entry point of the application.
"""

from click import echo, prompt
from database import Database
from sms import SMS
from call import Call
from appointment import Appointment


class CLI:
    def __init__(self, database: Database, sms: SMS, call: Call):
        """
        Initialize a CLI object with the given database, SMS, and call instances.
        """
        self.database = database
        self.sms = sms
        self.call = call

    def schedule_appointment(self):
        """
        Schedule a new appointment.
        """
        echo("Scheduling a new appointment...")
        patient_name = prompt("Enter patient name")
        date = prompt("Enter appointment date (YYYY-MM-DD)")
        time = prompt("Enter appointment time (HH:MM)")
        status = "Scheduled"
        notes = prompt("Enter appointment notes")
        appointment = Appointment(None, patient_name, date, time, status, notes)
        self.database.add_appointment(appointment)
        echo("Appointment scheduled successfully!")

    def view_appointments(self):
        """
        View all appointments.
        """
        echo("Viewing all appointments...")
        appointments = self.database.get_appointments()
        for appointment in appointments:
            echo(appointment)
            echo("")

    def manage_appointments(self):
        """
        Manage appointments (update or delete).
        """
        echo("Managing appointments...")
        appointment_id = prompt("Enter appointment ID")
        appointment = self.database.get_appointment(appointment_id)
        if appointment is None:
            echo("Appointment not found!")
            return
        echo(appointment)
        echo("")
        action = prompt("Enter action (update/delete)")
        if action == "update":
            patient_name = prompt("Enter patient name", default=appointment.patient_name)
            date = prompt("Enter appointment date (YYYY-MM-DD)", default=appointment.date)
            time = prompt("Enter appointment time (HH:MM)", default=appointment.time)
            status = prompt("Enter appointment status", default=appointment.status)
            notes = prompt("Enter appointment notes", default=appointment.notes)
            appointment.patient_name = patient_name
            appointment.date = date
            appointment.time = time
            appointment.status = status
            appointment.notes = notes
            self.database.update_appointment(appointment)
            echo("Appointment updated successfully!")
        elif action == "delete":
            self.database.delete_appointment(appointment_id)
            echo("Appointment deleted successfully!")
        else:
            echo("Invalid action!")

    def exit(self):
        """
        Exit the CLI interface.
        """
        echo("Exiting...")

    def run(self):
        """
        Run the CLI interface.
        """
        while True:
            echo("Main Menu:")
            echo("1. Schedule Appointment")
            echo("2. View Appointments")
            echo("3. Manage Appointments")
            echo("4. Exit")
            choice = prompt("Enter your choice", type=int)
            if choice == 1:
                self.schedule_appointment()
            elif choice == 2:
                self.view_appointments()
            elif choice == 3:
                self.manage_appointments()
            elif choice == 4:
                self.exit()
                break
            else:
                echo("Invalid choice!")


if __name__ == "__main__":
    db_file = "appointments.db"
    database = Database(db_file)
    database.create_tables()
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    from_number = "YOUR_TWILIO_PHONE_NUMBER"
    sms = SMS(account_sid, auth_token, from_number)
    call = Call(account_sid, auth_token, from_number)
    cli = CLI(database, sms, call)
    cli.run()
