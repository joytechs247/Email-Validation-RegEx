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

def main():
    # Prompt the user to enter an email address
    email = input("Enter an email address: ")
    
    # Check if the email is valid
    if is_valid_email(email):
        print(f"The email address '{email}' is valid.")
    else:
        print(f"The email address '{email}' is invalid.")

if __name__ == "__main__":
    main()
