import re

def is_valid_email(email):
    # Define the email pattern
    email_pattern = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    # Use the pattern to search for a match
    if email_pattern.match(email):
        return True
    else:
        return False

# Test the function
emails = [
    "test@example.com",
    "invalid-email.com",
    "another.test@domain.co",
    "bad@domain@domain.com",
    "good.email+label@gmail.com"
]

for email in emails:
    print(f"{email}: {is_valid_email(email)}")
