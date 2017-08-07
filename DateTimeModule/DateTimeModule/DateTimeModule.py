#%b is the month abbreviation
#%B is the full month name
#%y is two digit year
#%Y is the full year
#%a is the day of the week abbreviated
#%A is the day of the week

#For a full list visit http://strftime.org 

import datetime
currentDate = datetime.date.today()

print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

print(currentDate.strftime("%b %d, %Y"))

print(currentDate.strftime("Please attend our event %A, %B %d, %Y"))


#For dealing with different languages visit http://babel.pocoo.org

#Take user input and convert string into datetime
userInput = input("Please enter your birthday: ")
birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y')
print(birthday)
