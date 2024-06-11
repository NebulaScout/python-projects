#!python3
# dateDetection.py - Checks the validity of a date in dd/mm/yyyy format

import re

dateRegex = re.compile(r'''
                       ([0][1-31]|[1-31]{2})+ # date
                       /   # separator
                       ([0][1-12]|[1-12]{2})  # month
                       /    # separator
                       ([1-2][0-9]{3})  # year
                       ''', re.X)

while True:
    validateDate = input("Enter your date: ")
    try:
        mo = dateRegex.match(validateDate)
#        print(mo.groups())
        date, month, year = mo.groups()
    except AttributeError:
        print("\nThe date format is incorrect.\nThe correct format is dd/mm/yyyy.\n")
        continue
    break
#formats = mo.groups()
#date, month, year = mo.groups()
print(date)

#TODO: Add a 0 if date and month input is a single digit sub()
