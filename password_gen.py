import random
import string

# Define a function to generate a password.
def generate_password(min_length, numbers=True, special_characters=True):
    # Define character sets for letters, digits, and special characters.
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Initialize the characters variable with letters.
    characters = letters

    # Include digits if numbers parameter is True.
    if numbers:
        characters += digits

    # Include special characters if special_characters parameter is True.
    if special_characters:
        characters += special

    # Initialize an empty string to store the password.
    pwd = ""

    # Initialize flags to track if the password contains numbers and special characters.
    has_num = False
    has_spl = False

    # Continue adding characters to the password until it meets the criteria.
    while len(pwd) < min_length or (numbers and not has_num) or (special_characters and not has_spl):
        # Choose a random character from the defined character set.
        new_char = random.choice(characters)

        # Add the selected character to the password.
        pwd += new_char

        # Update flags if the character is a digit or special character.
        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_spl = True

    # Return the generated password.
    return pwd

# Prompt the user to enter the minimum length of the password.
min_length = int(input("Enter minimum length: "))

# Prompt the user to specify if they want numbers in the password (y/n).
has_number = input("Do you want to have numbers? (y/n)").lower() == "y"

# Prompt the user to specify if they want special characters in the password (y/n).
has_spl = input("Do you want to have special characters? (y/n)").lower() == "y"

# Generate a password using the specified parameters.
password = generate_password(min_length, has_number, has_spl)

# Print the generated password.
print(password)