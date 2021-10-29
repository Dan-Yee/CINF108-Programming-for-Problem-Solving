# Dan Yee
# CINF 108 - Programming for Problem Solving
# Mini-Assignment #4 - Functions

def Is_Odd(number):
    if number % 2 != 0:                                                                                 # if remainder when divided by 2 is not 0, the number is odd
        return True
    else:                                                                                               # else the number is even
        return False

def Greater_Than(number):
    multipliedResult = number * 15                                                                      # multiplied result is parameter * 15                                                                  

    if multipliedResult > 1500:                                                                         # if multiplied result is greater than 1500
        return "greater than"
    elif multipliedResult < 1500:                                                                       # if multiplied result is less than 1500
        return "less than"
    else:                                                                                               # else multiplied result is equal to 1500
        return "equal to"

def main():
    continueProgram = True                                                                              # flag variable for while loop condition

    while continueProgram:                                                                              # while the flag variable is true, execute body
        firstNumber = float(input("Enter a real number: "))                                             # prompt the user to enter a real number and store it
        secondNumber = float(input("Enter another real number: "))                                      # prompt the user to enter another real number and store it

        sum = firstNumber + secondNumber                                                                # calculate and store the sum of both numbers
        print("\nThe sum of", firstNumber, "and", secondNumber, "is", format(sum, ",.2f"))              # display sum rounded to two decimal places

        if Is_Odd(sum):                                                                                 # if Is_Odd returned True, number is odd
            print("The added result, ", format(sum, ",.2f"), ", is odd.", sep = "")
        else:                                                                                           # else the number is even
            print("The added result, ", format(sum, ",.2f"), ", is even.", sep = "")

        multipliedResult = sum * 15                                                                     # calculate and store sum * 15 as multiplied result

        # display the result of Greater_Than function as part of the String
        print("The multiplied result, ", format(multipliedResult, ",.2f"), ", is ", Greater_Than(sum), " 1500.", sep = "")

        runAgain = input("\nWould you like to run the program again? (y/n): ")                          # store the user to enter "y" or "n" to see if the program should run again
        if(runAgain.lower() == "n"):                                                                    # if user inputted "n" or "N", invalidate the loop condition by setting flag variable to False
            continueProgram = False
        print("")
main()