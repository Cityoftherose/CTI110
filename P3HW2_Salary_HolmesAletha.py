# CTI-110
# P3HW2 - Salary
# Aletha Holmes
# 11/3/23
#

#user is asked to enter name of employee
#user is asked to enter the number of hours employee worked
#user is asked to enter employee's pay rate
Employee_Name = input("Enter employee's name: ")
Hours_Work = float(input("Enter number of hours worked: "))
Pay_Rate = float(input("Enter employee's pay rate: "))

#evaluating if employee has worked over time (more than 40 hrs)
#if yes the program calculates how much the employee is owed for overtime hrs
#calculate amount employee should be paid for reg hrs worked
#display gross pay by adding reghrs_pay with over time

Over_Time = 0.0
OverTime_Pay = 0.0

if Hours_Work > 40:
 Over_Time = Hours_Work - 40
 OverTime_Pay = Over_Time * Pay_Rate * 1.5
 RegHrs_Pay = 40 * Pay_Rate
 Gross_Pay = RegHrs_Pay + OverTime_Pay

else:
 RegHrs_Pay = Hours_Work * Pay_Rate
 Gross_Pay = RegHrs_Pay + Over_Time

#program displays (employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for reg hours and gross pay)

print('---------------------------------------')
print('Employee name:  ', Employee_Name)
print('') 
print('Hours Worked   Pay Rate     OverTime     OverTime Pay      RegHour Pay     Gross Pay       ')
print('-----------------------------------------------------------------------------------------------')
print(f'{Hours_Work:<15.1f}{Pay_Rate:<13.1f}{Over_Time:<13.1f}{OverTime_Pay:<18.2f}${RegHrs_Pay:<15.2f}${Gross_Pay:<15.2f}')
