# Dan Yee
# CINF 108 - Programming for Problem Solving
# Assignment #1(mini)

firstNumber = float(input("Please enter a real number: "))                # prompts the user to enter a real number, typecasts from str to float and stores it in 'firstNumber'
secondNumber = float(input("Please enter another real number: "))         # prompts the user to enter a second real number, typecasts from str to float and stores it in 'secondNumber'

sum = firstNumber + secondNumber                                          # calculates the sum of the two user inputted real numbers and stores the value in 'sum'

# prints the sum of the two numbers and formats the number to only display two significant figures
print("The sum of", firstNumber, "and", secondNumber, "(rounded to two significant figures) is", format(sum, '.2f'))