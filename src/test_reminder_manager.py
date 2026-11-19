from reminder_manager import load_reminders, get_due_reminders


# Load reminders
reminders = load_reminders()

# Display all reminders
print("\nALL REMINDERS:")
print(reminders)

# Find due reminders
due_reminders = get_due_reminders(reminders)

# Display due reminders
print("\nDUE REMINDERS:")
print(due_reminders)

print(f"\nTotal Due Reminders: {len(due_reminders)}")