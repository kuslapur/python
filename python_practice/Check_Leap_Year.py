year = int(input("enter year "))

if (year % 4 == 0) and (year % 100 == 0):
    print("{0} is leap year ". format(year))

elif(year % 4 == 0) and ( year % 100 != 0):
    print("{0} is not leap year ". format(year))

else:
    print("{0} is not leap year ". format(year))
