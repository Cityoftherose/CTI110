# CTI-110
# P4HW2 - Salary Calculator
# Aletha Holmes
# 11/26/23
#

# Initialize variables
Overtime_total = 0
Regular_pay_total = 0
Gross_pay_total = 0
Num_employees = 0
Over_Time = 0
OverTime_Pay = 0
RegHrs_Pay = 0
Gross_Pay = 0

# Begin while loop
while True:
    #  user asked to enter employee name
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

    # If user enters done
    # Display number of employees enetered
    # Display Overtime total
    # Display Regular pay total
    # Display Gross pay total
    if employee_name == "Done":
        print()
        print("Total number of employees entered: ",Num_employees)
        print(f"Total amount paid for overtime: ${Overtime_total:.2f}")
        print(f"Total amount paid for regular hours: ${Regular_pay_total:.2f}")
        print(f"Total amount paid in gross: ${Gross_pay_total:.2f}")
        break
        print()

    # Ask user to enter number of hours employee worked
    hours_worked = float(input("How many hours did " + employee_name + " work? "))
    
    # Ask user to enter employee's pay rate
    pay_rate = float(input("What is " + employee_name + "'s pay rate? "))
       
    # Evaluating if employee has worked over time (more than 40 hrs)
    # if yes the program calculates how much the employee is owed for overtime hrs
    # calculate amount employee should be paid for reg hrs worked
    # calculate gross pay by adding reghrs_pay with over time
    if hours_worked > 40:
        Over_Time = hours_worked - 40
        OverTime_Pay = Over_Time * pay_rate * 1.5
        RegHrs_Pay = 40 * pay_rate
        Gross_Pay = RegHrs_Pay + OverTime_Pay
    else:
        RegHrs_Pay = hours_worked * pay_rate
        Gross_Pay = RegHrs_Pay + Over_Time

    # Add to total variables
    Overtime_total += OverTime_Pay
    Regular_pay_total += RegHrs_Pay
    Gross_pay_total += Gross_Pay
    Num_employees += 1


    #program displays (employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for reg hours and gross pay)
    print()

    print("Employee name:", employee_name)
    
    print()

    print('Hours Worked   Pay Rate     OverTime     OverTime Pay      RegHour Pay     Gross Pay       ')
    print('------------------------------------------------------------------------------------')
    
    print(f'{hours_worked:<15.1f} {pay_rate: <13.2f} {Over_Time:<10.1f} {OverTime_Pay:<18.2f} ${RegHrs_Pay:<15.2f} ${Gross_Pay:<15.2f}')
    print()
