import time
import datetime
now=datetime.datetime.now()
print("a)Current date and time:",now)
print("b)Current year:",now.year)
print("c)Month of the year:",now.month)
print("d)Week number of the year:",now.isocalendar()[1])
print("e)Weekday of the week(number):",now.isoweekday())
print("f)Day of year:",now.timetuple().tm_yday)
print("g)Day of month:",now.day)
print("h)Day of week(name):",now.strftime("%A"))
