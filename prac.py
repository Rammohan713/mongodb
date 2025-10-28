import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
a=dt.datetime.now()
print(a)
# To calculate current  hour
current_hour = a.now().hour
print(current_hour)

p=a+timedelta(days= 2)
# print(p)
# ps = p.strftime('%Y:%m:%d: %H:00')
# print(ps)
# print(type(ps))
pm = a-relativedelta(months=2)
print(pm)