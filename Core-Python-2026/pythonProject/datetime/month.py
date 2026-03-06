import  datetime

for i  in range(1,13):
     month_name = datetime.date(2026, i, 1).strftime('%B')
     print(f'Month {i}: {month_name}')