print("LEAP YEAR")


year = int(input("Enter the year of your Choice : "));
if (year%400 == 0 ) and (year %100 ==0):
    print("{} is a Leap year".format(year))
elif (year%4== 0 ) and (year %100!=0):
    print("{} is a leap year".format(year))
else:
    print("{} is Non Leap Year".format(year))