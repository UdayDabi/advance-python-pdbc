list = [10, 11, 5, 13, 17, 88]
number = 17

count = 0

for i in list:
    if i == number:
        count += 1

if number in list:
    print("number exist")
else:
    print("number not exist")
