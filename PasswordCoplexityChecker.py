import re

def password_complexity_checker(password):

    # Check for minimum length of 8 characters
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all checks pass, the password is complex
    return True

# Prompt the user to enter a password
password = input("Please enter a password: ")

# Check the complexity of the entered password
if password_complexity_checker(password):
    print("The password is complex.")
else:
    print("The password is not complex. Please try again.")