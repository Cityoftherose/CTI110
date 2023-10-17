#Revised Calculating Travel Expenses
#10-15-23
# CTI-110 P2HW1 - Travel
#Aletha Holmes
#
#User is asked to input budget
#User is asked to input travel destination
#User is asked to input gas expenses
#User is asked to input accomodation expenses
#User is asked to input food expenses
#convert user entries to float
#Calculate the sum of gas, accomodations, and food
#Calculate the remaining balance by subtracting expenses from budget
#Display Location
#Add dollar sign to travel expenses and remaining balance
#Display Budget
#Display fuel expenses 
#Display accomodation expenses 
#Display food expenses
#Display remaining_balance

print('This program calculates and displays travel expenses')
Budget = float(input('Enter Budget: '))
Location = input('Enter your travel destination: ')
Gas = float(input('How much do you think you will spend on gas? '))
Accomodations = float(input('Approximately, how much will you need for accomodation/hotel? '))
Food = float(input('Last, how much do you need for food? '))
Expenses = int(Gas + Accomodations + Food)
Remaining_balance = int(Budget - Expenses)

print("")
print("------------Travel Expenses------------")
print("Location:          ",Location)
print(f'Initial Budget:     ${Budget:.1f}')
print(f'Fuel:               ${Gas:.1f}')
print(f'Accomodation:       ${Accomodations:.1f}')
print(f'Food:               ${ Food:.1f}')
print('---------,------------------------------')
print(f'Remaining_balance:  ${Remaining_balance:.1f}')

