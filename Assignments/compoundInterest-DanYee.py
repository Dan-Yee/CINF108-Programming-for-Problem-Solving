# Dan Yee
# CINF 108 - Programming for Problem Solving
# Assignment #1 - Compound Interest Calculator

principalAmount = float(input("Enter the principal balance: "))                                                                     # prompt the user for the principal balance and stores it in a variable
interestRate = float(input("Enter the interest rate as a percent: "))                                                               # prompt the user for the interest rate and stores it in a variable
compoundFrequency = float(input("How many times per year is the interest compounded? "))                                            # prompt the user for the compound frequency and stores it in a variable
compoundYears = float(input("How many years will the account earn interest? "))                                                     # prompt the user for the interest time and stores it in a variable

accumulatedValue = principalAmount * ((1 + ((interestRate / 100)) / compoundFrequency) ** (compoundFrequency * compoundYears))      # calculates and stores the accumulated balance after compound interest in a variable

print("\nAt the end of ", format(compoundYears, ".2f"), " years, you will have $", format(accumulatedValue, ",.2f"), sep = "")      # display the accumulated value after compound interest rounded to 2 decimal places