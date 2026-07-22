print("==========================")
print(" EMPLOYEE SALARY CALCULATOR")
print("==========================")
choice=input("Do you want to continue?: ")
while choice=="yes":
 name=input("Enter Employee name:")
 salary=int(input("Enter Basic salary:"))
 bonus=0
 tax=0
 if salary>=50000:
    bonus=salary*20/100
    print("Bonus:",bonus)
 elif salary>=30000:
    bonus=salary*10/100
    print("Bonus:",bonus)
 else:
    bonus=salary*5/100
    print("Bonus:",bonus)
 gross_salary=salary+bonus
 print("Gross_Salary:",gross_salary)
 if gross_salary>=60000:
    tax=gross_salary*15//100
    print("Tax:",tax)
 elif gross_salary>=40000:
    tax=gross_salary*10//100
    print("Tax:",tax)
 else:
    tax=gross_salary*5//100
    print("Tax:",tax)
 net_salary=gross_salary-tax
 print("Net_Salary:",net_salary)
