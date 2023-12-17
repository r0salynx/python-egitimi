#import calculator
#from calculator import *
#from calculator import toplama, carpma

import datetime
current_date = datetime.datetime.now()
print(current_date, type(current_date))
#2023-12-17 15:34:14.977785 <class 'datetime.datetime'>

print(current_date.hour)

print(current_date.strftime("%d-%m-%Y"))