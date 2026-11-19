# Email Automation Configuration

import os
from dotenv import load_dotenv

load_dotenv()

SIMULATION_MODE = False

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

REMINDER_STATUS_PENDING = "Pending"
REMINDER_STATUS_PROCESSED = "Processed"
REMINDER_STATUS_FAILED = "Failed"