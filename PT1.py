def find_new_salary(current_salary,job_level):
    # write your logic here
    if job_level == 3:
        new_salary = current_salary + (current_salary*0.15)
    elif job_level == 4:
        new_salary = current_salary + (current_salary*0.07)
    elif job_level == 4:
        new_salary = current_salary + (current_salary*0.05)
    else:
        return current_salary



    return new_salary



# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print("New Salary : ",new_salary)