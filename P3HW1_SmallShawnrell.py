# Correct the Code
# 3/21/2023
# CTI-110-P3HW1
# Shawnrell Small


# This program takes a number grade, determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

Grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(Grades)
high = max(Grades)
totals = sum(Grades)
avg = totals/len(Grades)
print ('')
print ('------------Results----------------')
print (f'lowest Grade:      {low:.1f}')
print (f'Highest Grade:     {high:.1f}')
print (f'Sum of Grades:     {totals:.1f}')
print (f'Average:           {avg:.2f}')
print ('------------------------------------------------')


# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg <= 89:
    print('Your grade is: B')
elif avg <= 79:
    print('Your grade is: C')
elif avg <= 69:
    print('Your grade is: D')
elif avg <= 64:
    print('Your grade is: F')

 # TO DO: finished





