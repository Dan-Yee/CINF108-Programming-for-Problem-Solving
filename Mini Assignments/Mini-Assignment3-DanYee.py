# Dan Yee
# CINF 108 - Programming for Problem Solving
# Mini-Assignment #3 - While Loops

continueProgram = True                                                                              # flag variable for while loop condition

while continueProgram:                                                                              # while the flag variable is true, execute body
    firstNumber = float(input("Enter a real number: "))                                             # prompt the user to enter a real number and store it
    secondNumber = float(input("Enter another real number: "))                                      # prompt the user to enter another real number and store it

    sum = firstNumber + secondNumber                                                                # calculate and store the sum of both numbers
    print("\nThe sum of", firstNumber, "and", secondNumber, "is", format(sum, ",.2f"))              # display sum rounded to two decimal places

    if sum % 2 == 0:                                                                                # Only integers can be EVEN or ODD - convert to int and check remainder when divided by 2
        print("The added result, ", format(sum, ",.2f"), ", is even.", sep = "")
    else:                                                                                           # number is odd if the remainder when divided by 2 is not 0
        print("The added result, ", format(sum, ",.2f"), ", is odd.", sep = "")

    multipliedResult = sum * 15                                                                     # calculate and store sum * 15 as multiplied result

    if multipliedResult > 1500:                                                                     # if product is greater than 1500
        print("The multiplied result, ", format(multipliedResult, ",.2f"), ", is greater than 1500.", sep = "")
    elif multipliedResult < 1500:                                                                   # if product is less than 1500
        print("The multiplied result, ", format(multipliedResult, ",.2f"), ", is less than 1500.", sep = "")
    else:                                                                                           # if product is equal to 1500
        print("The multiplied result, ", format(multipliedResult, ",.2f"), ", is equal to 1500.", sep = "")

    runAgain = input("\nWould you like to run the program again? (y/n): ")                          # store the user to enter "y" or "n" to see if the program should run again
    if(runAgain == "n"):                                                                            # if user inputted "n", invalidate the loop condition by setting flag variable to False
        continueProgram = False
    print("")