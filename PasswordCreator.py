import secrets
import string

letters = string.ascii_letters
numbers = string.digits
punc = string.punctuation

usableChars = letters

allowedInput = ['Y', 'y', 'N', 'n']


useNums = input("Use numbers? (Y/N): ")
while useNums not in allowedInput:
    print(useNums, "is an invalid input.")
    useNums = input("Use numbers? (Y/N): ")
     
if useNums == 'Y' or useNums == 'y':
    usableChars += numbers



usePunc = input("Use punctuation? (Y/N): ")
while usePunc not in allowedInput:
    print(usePunc, "is an invalid input.")
    usePunc = input("Use punctuation? (Y/N): ")
     
if useNums == 'Y' or useNums == 'y':
   usableChars += punc



passwordLength = int(input("Enter password length: "))



def passGen(passwordLength, usableChars):
    return ''.join(secrets.choice(usableChars) for i in range(passwordLength))

print("Generated password:", passGen(passwordLength, usableChars))
