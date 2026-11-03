#Python Programming Assignment 5
#Checking if a string contains a-z, A-Z and 0-9 using re module

import re

text=input("Enter string to check: ")

if re.match(r"^[a-zA-Z0-9]+$", text):
    print("Valid, contains a-z, A-Z, and 0-9.")
else:
    print("Invalid, contains other characters.")


