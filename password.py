# Checking Validity of Password

# Validation Criteria :

# 1) At least 1 letter between [a-z]
# 2) At least 1 letter between [A-Z]
# 3) At least 1 number between [0-9]
# 4) At least 1 character from [@#$]
# 5) Minimum length 6 characters
# 6) Maximum length 16 characters

import re
input = raw_input
p = input("Enter Password: ")
x = True

while x:
    if (len(p) < 6 or len(p) > 16):
        break
    elif not re.search("[a-z]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[0-9]", p):
        breakpoint
    elif not re.search("[@#$]", p):
        break
    else:
        print("Password is valid!")
        x = False
        break
if x:
    print("invalid Password!")
