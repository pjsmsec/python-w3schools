import datetime

x = datetime.datetime.now()
print(x)
# A date contains year, month, day, hour, minute, second, and microsecond.

print()

print(x.year)
print(x.strftime("%A"))

print()

# Creating date objects
# The datetime() class requires three parameters to create a date: year, month, day
x = datetime.datetime(2020, 5, 17)

print(x)

print()

# Additional parameters

# The strftime() method
# Formats datetime objects.
# Takes one parameter - format
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
