# import math as m

# a = m.factorial(5)
# print(a)

# b = 16

# c = m.sqrt(b)
# print(c)

# d = m.cos(0)
# print(d)


# import random

# a = random.random()
# b = random.randint(100000,999999)
# c = random.randrange(0,20,3)


# d = ["apple","orange","grapes","cherry","melon"]

# e = random.choice(d)
# print(a)
# print(b)
# print(c)
# print(e)

import datetime as dt

# a = dt.datetime.today()# now() or today
# b= dt.date.today()

# c = dt.timedelta(hours=1000)
# print(a)
# print(b)
# print(a+c)


# today = dt.date.today()
# startdate = dt.date(2026,4,1)

# day = today - startdate

# print(day.days)


todaytime = dt.datetime.now()

print(todaytime.strftime("time=%H:%M:%S\ndate=%d-%m-%Y"))

