import  datetime

today =datetime.date.today()

formated = today.strftime("%d-%m-%y")


print("Formatted date:", formated)