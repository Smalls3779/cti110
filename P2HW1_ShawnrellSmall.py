# Code for travel expenses
# 3/1/2023
# CTI-110 P2HW1 - Travel
# Shawnrell Small

# Inputs values using string and float inputs where suitable

Budget = float(input('Enter Budget:'))

Location = str(input('Enter your travel destination: '))

Gas = float(input('How much do you think you will spend on gas?'))

Hotel = float(input('Approximately, how much will you need for accommodation/hotel?'))

Food = float(input('Last, how much do you need for food?'))

# Calculates balance after expenses
Balance = float(Budget - Gas - Hotel - Food)

# Prints values using string formatting for $'s where suitable
print('------------Travel Expenses------------')
print(f'Location:           {Location}')
print(f'Initial Budget:     ${Budget}')
print(f'Fuel:               ${Gas}')
print(f'Accommodations:     ${Hotel}')
print(f'Food:               ${Food}')
print('---------------------------------------')
# Prints remaining balance
print(f'Remaining Balance:  ${Balance}')
