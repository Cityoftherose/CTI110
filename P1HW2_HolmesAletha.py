#Calculating Travel Expenses
#9-26-23
#CTI-110 P1HW2-Travel Expense
#Aletha Holmes
#
#User is asked to input budget
#User is asked to input travel destination
#User is asked to input gas expenses
#User is asked to input accomodation expenses
#User is asked to input food expenses
#Calculate the sum of gas, accomodations, and food
#Calculate the remaining balance by subtracting expenses from budget
#Display Location
#Display Budget
#Display fuel expenses
#Display accomodation expenses
#Display food expenses
#Display remaining_balance

print('This program calculates and displays travel expenses')
Budget = int(input('Enter Budget: '))
Location = input('Enter your travel destination: ')
Gas = int(input('How much do you think you will spend on gas? '))
Accomodations = int(input('Approximately, how much will you need for accomodation/hotel? '))
Food = int(input('Last, how much do you need for food? '))
Expenses = int(Gas + Accomodations + Food)
Remaining_balance = int(Budget - Expenses)

print("")
print("------------Travel Expenses------------")
print("Location: ",Location)
print("Initial Budget: ",Budget)
print("")
print("Fuel: ",Gas)
print("Accomodation: ",Accomodations)
print("Food: ",Food)
print("")
print("Remaining Balance: ",Remaining_balance)
