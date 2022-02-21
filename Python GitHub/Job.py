level3Hike = 15/100 #percentage

level4Hike = 7/100  #percentage

level5Hike = 5/100  #percentage

jobLevel = int(input("Enter Job Level : "))

currentSalary = float(input("Enter current salary: "))

salaryHike=0.0

if jobLevel == 3:

    salaryHike = (currentSalary*level3Hike)

elif jobLevel == 4:

    salaryHike = (currentSalary*level4Hike)

elif jobLevel == 5:

    salaryHike = (currentSalary*level5Hike)

else:
    salaryHike = 0

newSalary = currentSalary + salaryHike

print("New Salary After Hike : "+ str(newSalary) )