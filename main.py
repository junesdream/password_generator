import random

def create_password():
    # Define lists of character types for password components
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # As the user for the desired password length
    while True:
        try:
            length = int(input("How long should the password be? (at least 8 characters): "))
            if length < 8:
                print("The password should be at least 8 characters long.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user which types of characters to include
    use_lowercase = input("Use lower case letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Use upper case letters?? (y/n): ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Use special characters? (y/n): ").lower() == 'y'

    # Create a character set based on user selections
    charset = ''
    if use_lowercase:
        charset += lowercase
    if use_uppercase:
        charset += uppercase
    if use_numbers:
        charset += numbers
    if use_symbols:
        charset += symbols

    # Ensure at least one type of character is selected
    if not charset:
        print("You must select at least one character type. Lower case letters are used by default.")
        charset = lowercase

    # Generate the password from the selected character set
    password = ''.join(random.choice(charset) for i in range(length))

    return password


# Create and display the new password
if __name__ == "__main__":
    new_password = create_password()
    print(new_password)
