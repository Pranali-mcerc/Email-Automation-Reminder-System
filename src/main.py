import schedule
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reminder_manager import load_reminders, get_due_reminders, update_reminder_status
from email_sender import create_email, preview_email, send_email
from logger import log_info, log_warning, log_error
from config import SIMULATION_MODE


def run_automation():
    print("\nEMAIL AUTOMATION & REMINDER SYSTEM")
    print("-" * 40)

    log_info("Automation started")

    reminders = load_reminders()

    if reminders.empty:
        print("No reminders available.")
        log_warning("No reminders found")
        return

    due_reminders = get_due_reminders(reminders)

    print(f"Total reminders: {len(reminders)}")
    print(f"Due reminders: {len(due_reminders)}")

    for _, reminder in due_reminders.iterrows():
        try:
            email = create_email(
                name=reminder["name"],
                email_address=reminder["email"],
                subject=reminder["subject"],
                message=reminder["message"]
            )

            if SIMULATION_MODE:
                preview_email(email)
                print("SIMULATION MODE: Email not sent.")
                success = True

            else:
                success = send_email(email)

            if success:
                update_reminder_status(
                    reminders,
                    reminder["email"],
                    "Processed"
                )
                log_info(f"Reminder processed for {reminder['email']}")

            else:
                update_reminder_status(
                    reminders,
                    reminder["email"],
                    "Failed"
                )
                log_error(f"Email failed for {reminder['email']}")

        except Exception as e:
            log_error(f"Error processing {reminder['email']}: {e}")
            print(f"Error: {e}")

    print("\nAutomation completed!")
    log_info("Automation completed")


if __name__ == "__main__":
    print("Email Reminder Scheduler Started")
    print("Automation will run daily at 9:00 AM")

    schedule.every(1).minutes.do(run_automation)

    while True:
        schedule.run_pending()
        time.sleep(60)