Budget = float(input('Enter Budget:'))

Location = str(input('Enter your travel destination: '))

Gas = float(input('How much do you think you will spend on gas?'))

Hotel = float(input('Approximately, how much will you need for accommodation/hotel?'))

Food = float(input('Last, how much do you need for food?'))

Balance = float(Budget - Gas - Hotel - Food)


print('------------Travel Expenses------------')
print('Location:', Location)
print('Initial Budget:', Budget)

print('Fuel:', Gas)
print('Accommodation:', Hotel)
print('Food:', Food)

print('Remaining Balance:', Balance)
