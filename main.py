# Gives an instruction to input numbers for the calculation.
print ( 'Input some numbers to calculate their sum and average. Input 0 to exit.')

# Setting up count, sum and number.
count = 0
sum = 0.0
number = 1

# This while loop it gives the input if there are no numbers written.
while number != 0:
    number = int(input(''))

    # It adds the numbers to the sum, so it calculate the total sum.
    sum = sum + number

    # It increases the count of added numbers
    count = count + 1

# It checks if no numbers were entered
if count == 0:
    print('Input some numbers')
else:
    # Calculates the average and the sum and prints them.
    print('The average and the sum of the numbers is', sum/(count-1), sum)






