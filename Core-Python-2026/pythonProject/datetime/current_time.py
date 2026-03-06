import datetime

d=datetime.datetime.now()
print("Current hour is:", d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
print(d.strftime("%Y-%m-%d %H:%M:%S"))
print(d.strftime("%A, %B %d, %Y"))
print(d.min)
print(d.max)

