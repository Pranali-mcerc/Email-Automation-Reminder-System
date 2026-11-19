import pandas as pd
from datetime import datetime


def load_reminders(file_path="data/reminders.csv"):

    try:
        reminders = pd.read_csv(file_path)

        print(f"Successfully loaded {len(reminders)} reminders.")

        return reminders

    except FileNotFoundError:

        print("Reminder file not found!")

        return pd.DataFrame()


def get_due_reminders(reminders):

    today = datetime.today().date()

    reminders["reminder_date"] = pd.to_datetime(
        reminders["reminder_date"]
    ).dt.date

    due_reminders = reminders[
        (reminders["reminder_date"] <= today) &
        (reminders["status"] == "Pending")
    ]

    return due_reminders
def update_reminder_status(
    reminders,
    email_address,
    new_status,
    file_path="data/reminders.csv"
):

    reminders.loc[
        reminders["email"] == email_address,
        "status"
    ] = new_status

    reminders.to_csv(file_path, index=False)

    print(f"Status updated for {email_address}: {new_status}")