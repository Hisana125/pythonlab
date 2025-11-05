import calendar
year=int(input("Enter a year:"))
if calendar.isleap(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")
