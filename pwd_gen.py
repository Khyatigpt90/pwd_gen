import random
import string

def generate_password(length=12, include_digits=True, include_uppercase=True, include_special_chars=True):
    # Define character sets
    lower = string.ascii_lowercase # a-z
    upper = string.ascii_uppercase if include_uppercase else '' # A-Z
    digits = string.digits if include_digits else '' # 0-9
    special_chars = string.punctuation if include_special_chars else '' # Special characters
    # combine all the allowed characters
    all_chars = lower + upper + digits + special_chars
    if not all_chars:
        raise ValueError(" You must allow al least one type of characters.")
    # Randomly select characters to form the password 
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User input for password length and constraints
length = int(input("Enter the desired password length: "))
include_digits = input("include digits? (y/n): ").lower() == 'y'
include_uppercase = input("include uppercase letters? (y/n):").lower() == 'y'
include_special_chars = input("include special characters? (y/n): ").lower() == 'y'
# Generate and display the password
password = generate_password(length, include_digits, include_uppercase, include_special_chars)
print(f"Generate Password: {password}")
        
