
import secrets
import string

letters = string.ascii_letters
numbers = string.digits
punc = string.punctuation

usableChars = letters + numbers + punc


passwordLength = int(input("Enter password length: "))

def passGen(passwordLength, usableChars):
    return ''.join(secrets.choice(usableChars) for i in range(passwordLength))

print("Generated password:", passGen(passwordLength, usableChars))
