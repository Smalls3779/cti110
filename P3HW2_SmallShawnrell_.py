
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0

# start loop for entering employee information
while True:
    # ask user for employee name
    name = input("Enter employee name (or 'Done' to exit): ")

    # check if user wants to exit
    if name == "Done":
        break

    # ask user for pay rate and hours worked
    pay_rate = float(input("Enter employee pay rate: "))
    hours_worked = float(input("Enter employee hours worked: "))

    # calculate regular pay and overtime pay
    if hours_worked > 40:
        over_pay = (hours_worked - 40) * (pay_rate * 1.5)
        reg_pay = 40 * pay_rate
        gross_pay = over_pay + reg_pay
    else:
        over_pay = 0
        reg_pay = hours_worked * pay_rate
        gross_pay = reg_pay

    # increment variables
    num_employees += 1
    overtime_total += over_pay
    regular_pay_total += reg_pay
    gross_pay_total += gross_pay

    # display employee's salary information
# initialize variables
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0

# start loop for entering employee information
while True:
    # ask user for employee name
    name = input("Enter employee name (or 'Done' to exit): ")

    # check if user wants to exit
    if name == "Done":
        break

    # ask user for pay rate and hours worked
    pay_rate = float(input("Enter employee pay rate: "))
    hours_worked = float(input("Enter employee hours worked: "))

    # calculate regular pay and overtime pay
    if hours_worked > 40:
        over_pay = (hours_worked - 40) * (pay_rate * 1.5)
        reg_pay = 40 * pay_rate
        gross_pay = over_pay + reg_pay
    else:
        over_pay = 0
        reg_pay = hours_worked * pay_rate
        gross_pay = reg_pay

    # increment variables
    num_employees += 1
    overtime_total += over_pay
    regular_pay_total += reg_pay
    gross_pay_total += gross_pay

    # display employee's salary information
    print(f"{name}")
    print('-------------------------------------------------------------------------------')
    print(f"Hours Worked    Pay Rate       Overtime   Overtime Pay")
    print(f'{hours_worked} {reg_pay:.2f}  {overtime_total}  {over_pay}')
# display totals for all employees
print(f"\nTotal overtime pay: ${overtime_total:.2f}")
print(f"Total regular pay: ${regular_pay_total:.2f}")
print(f"Total gross pay: ${gross_pay_total:.2f}")
print(f"Number of employees entered: {num_employees}")
