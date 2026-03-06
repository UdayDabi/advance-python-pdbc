
try:
    # Code jisme error aasakta hai
    a = 10
    b = u
    c = a / b
    print('division:', c)
except ZeroDivisionError as e:
    # Error aane par ye chalega
    print('exception:', e)
except ValueError:
     print("Please number hi daalna tha")
except Exception as e:
    print('exception:', e)
else:
    # Jab try me koi error NA aaye to ye chalega
    print('else block executed')
finally:
    # Chahe error aaye ya nahi, ye hamesha chalega
    print('finally block executed')




# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File nahi mili")
# else:
#     print("File successfully read")
# finally:
#     print("Cleanup complete")  # ✅ ye hamesha chalega






# try:
#     num = int(input("Enter a number: "))
#     print("Square is:", num * num)
# except ValueError:
#      print("Please number hi daalna tha")
# finally:
#     print("Program end")  # ✅ Always
