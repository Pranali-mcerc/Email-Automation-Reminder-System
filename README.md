# 📧 Email Automation & Reminder System

A Python-based automation project that manages reminders and sends personalized emails automatically using Gmail SMTP. The system reads reminder data from CSV files, identifies due reminders, sends emails, updates statuses, and logs activities.

## 🚀 Features

- Automated reminder management using CSV
- Detects pending and due reminders
- Personalized email generation
- Gmail SMTP integration
- Simulation mode for safe testing
- Automated scheduling
- Status tracking (Pending, Processed, Failed)
- Logging and error handling
- Secure credential management using environment variables

## 🛠️ Technologies Used

- Python
- Pandas
- SMTP
- Schedule
- Yagmail
- Python-dotenv
- CSV
- Git & GitHub

## 📁 Project Structure

```text
Email-Automation-Reminder-System/
│
├── config.py
├── .env
├── .gitignore
├── README.md
│
├── data/
│   ├── contacts.csv
│   └── reminders.csv
│
├── logs/
│
├── src/
│   ├── main.py
│   ├── email_sender.py
│   ├── reminder_manager.py
│   ├── logger.py
│   └── test files
│
└── venv/
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Pranali-mcerc/Email-Automation-Reminder-System.git
```

2. Navigate to the project directory.

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate it on Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install pandas schedule python-dotenv yagmail
```

## 🔐 Configuration

Create a `.env` file in the root folder:

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

Use a Gmail App Password instead of your normal Gmail password.

## ▶️ Running the Project

```bash
python src/main.py
```

The system checks reminders and processes those that are due.

## 📊 Workflow

1. Load reminders from CSV.
2. Check reminder dates.
3. Filter pending reminders.
4. Generate personalized emails.
5. Send emails through Gmail SMTP.
6. Update reminder status.
7. Record logs.
8. Run automatically according to schedule.

## 🔒 Security

- Credentials stored in `.env`
- `.env` excluded from GitHub using `.gitignore`
- Simulation mode available for testing

## 👩‍💻 Author

**Pranali Golesar**  
BE Artificial Intelligence & Data Science