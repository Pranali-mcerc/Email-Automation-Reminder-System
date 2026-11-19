import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def create_email(name, email_address, subject, message):
    email = MIMEMultipart()
    email["From"] = os.getenv("EMAIL_USER")
    email["To"] = email_address
    email["Subject"] = subject

    personalized_message = f"""
Hello {name},

{message}

Best Regards,
Email Automation System
"""
    email.attach(MIMEText(personalized_message, "plain"))
    return email


def preview_email(email):
    print("\n" + "=" * 60)
    print("EMAIL PREVIEW")
    print("=" * 60)
    print(f"Sender: {email['From']}")
    print(f"Recipient: {email['To']}")
    print(f"Subject: {email['Subject']}")
    print("-" * 60)
    print(email.get_payload()[0].get_payload())
    print("=" * 60)


def send_email(email):
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(email)

        print(f"Email sent successfully to {email['To']}")
        return True

    except Exception as e:
        print(f"Email sending failed: {e}")
        return False