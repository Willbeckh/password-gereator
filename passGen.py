# python 101
# random password generator
import random, string

CHARS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = string.punctuation

#combine data literals and asign them to a variable
combinedChars = DIGITS + CHARS + SYMBOLS
 
length = 8 #length of password.

password = ''
for c in range(length):
  #random.choice will iterate my combinedChar variable 
  # and append the result to password variable
  password += random.choice(combinedChars) 

print(f'Your passcode is: {password}')
