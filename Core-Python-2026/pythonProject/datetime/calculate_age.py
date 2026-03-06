import datetime

dob = datetime.date(2004, 4, 13)
today = datetime.date.today()

age = today.year - dob.year


# Day name of DOB
day_name = dob.strftime("%A")

print("Your age is:", age)
print("You were born on:", day_name)
