####################################################################################################
# Author: Jack Conley
#
# Purpose: This program creates a random password with user defined parameters.
# 
# Method: By using the secrets module, this program randomly and securely generates a password
# that can be adapted by user defined parameters.
####################################################################################################

# Import secrets module to use for secure randomization
import secrets
# string module has lists of characters useful to the program
import string

# Instantiates string characters as more usable names to work with
letters = string.ascii_letters
numbers = string.digits
punc = string.punctuation

# Sets default characters as letters
usableChars = letters

# List of input choices allowed by the program
allowedInput = ['Y', 'y', 'N', 'n']

# Asks if user wants to use numbers
useNums = input("Use numbers? (Y/N): ")
# Error handling to make sure a string is entered
while useNums not in allowedInput:
    print(useNums, "is an invalid input.")
    useNums = input("Use numbers? (Y/N): ")

# If the user chooses to use numbers  
if useNums == 'Y' or useNums == 'y':
    usableChars += numbers


# Asks if user wants to use punctuation
usePunc = input("Use punctuation? (Y/N): ")
# Error handling to make sure a string is entered
while usePunc not in allowedInput:
    print(usePunc, "is an invalid input.")
    usePunc = input("Use punctuation? (Y/N): ")

# If the user chooses to use puncutation
if useNums == 'Y' or useNums == 'y':
   usableChars += punc


# Error handling to make sure input is a number over 0
while True:
    try:
        passwordLength = int(input("Enter password length (recommended size > 6): "))
        if passwordLength > 0: break
        else: print("Please enter an integer larger than 0.")
    except ValueError:
      print("Please enter an integer.")


# passGen function that takes in password length and the usable characters as parameters
def passGen(passwordLength, usableChars):
    # Secure randomization algorithm that randomly picks a character and adds it to the password that is being generated
    return ''.join(secrets.choice(usableChars) for i in range(passwordLength))

# Function call and output
print("Generated password:", passGen(passwordLength, usableChars))

