numbers = [100, 10, 11, 5, 13, 17, 88]

highest = 0
second_highest = 0

for num in numbers:
    if num > highest:

        second_highest = highest
        highest = num

    elif num > second_highest and num != highest:
        second_highest = num

print("Highest number is:", highest)
print("Second highest number is:", second_highest)



# numbers = [100, 10, 11, 5, 13, 17, 88]

# highest = numbers[0]   # pehle element ko hi highest maan lo

# for num in numbers:
#     if num > highest:
#         highest = num

# print("Highest number is:", highest)
