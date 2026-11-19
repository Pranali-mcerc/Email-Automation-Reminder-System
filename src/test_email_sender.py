from email_sender import create_email, preview_email


email = create_email(
    name="Rahul Sharma",
    email_address="rahul.sharma@example.com",
    subject="Meeting Reminder",
    message="Your team meeting is scheduled for tomorrow."
)

preview_email(email)