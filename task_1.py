import random
import string

def generate_password(length=12):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        length = 8

    # Generate the password with random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    print("Password Generator")
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))
    
    passwords = generate_multiple_passwords(num_passwords, password_length)
    
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
