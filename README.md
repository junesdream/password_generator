# Simple Password Generator

## Description
This is a simple, interactive password generator written in Python. It allows users to create custom passwords based on their preferences for length and character types.

## Features
- Customizable password length (minimum 8 characters)
- Option to include or exclude:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Error handling for invalid inputs
- Ensures at least one character type is selected

## Requirements
- Python 3.x

## Usage
1. Run the script in a Python environment.
2. Follow the prompts to specify your password preferences:
   - Enter the desired password length (must be at least 8 characters)
   - Choose whether to include lowercase letters, uppercase letters, numbers, and special characters
3. The generated password will be displayed on the screen

## Code Structure
The main function `create_password()` handles all the logic:
- It defines character sets for different types of characters
- Prompts the user for password length and character type preferences
- Constructs a character set based on user preferences
- Generates a random password using the constructed character set

## Example
- How long should the password be? (at least 8 characters): 12
- Use lower case letters? (y/n): y
- Use upper case letters?? (y/n): y
- Use numbers? (y/n): y
- Use special characters? (y/n): n
- Your generated password is: aB3cDe4fG5hI

## Customization
- You can easily modify the character sets or adjust the script to suit your specific needs. For example, you can add more special characters, or enforce stricter rules about password complexity.

## Contributions
Feel free to fork this project and submit pull requests for any improvements or additional features you'd like to see!

## License
