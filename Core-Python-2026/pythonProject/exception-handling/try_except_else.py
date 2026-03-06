from operator import index

a = 10
b = 0

try:
    c = a / a
    print('division:', c)
except IndexError as e:
    print('TypeError exception:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError exception:', e)
except Exception as e:
    print('Exception:', e)
else:
    print('in else block')
finally:
    print('in finally block')
