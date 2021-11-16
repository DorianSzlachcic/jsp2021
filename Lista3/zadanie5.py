import re

password = input("Podaj hasło: ")
MinPasswordLength = 6
MaxPasswordLength = 16

if len(password)>MinPasswordLength and len(password)<MaxPasswordLength:
    isValid = True
    if re.search(r"[a-z]",password) == None:
        isValid = False
    if re.search(r"[A-Z]",password) == None:
        isValid = False
    if re.search(r"[0-9]",password) == None:
        isValid = False
    if re.search(r"[$#@]",password) == None:
        isValid = False
    
    if isValid:
        print("Hasło jest prawidłowe")
    else:
        print("Hasło jest nieprawidłowe")
else:
    print("Twoje hasło ma złą długość")