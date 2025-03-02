"""
Emails
Estimate Time: 17 minutes
Actual Time: 23 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email:
        extracted_name = extract_name(email)
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()
        if confirmation and confirmation != 'y':
            extracted_name = input("Name: ").strip().title()
        email_to_name[email] = extracted_name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name

main()