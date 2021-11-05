# Dan Yee
# CINF 108 - Programming for Problem Solving
# Assignment #4 - Compound Interest Calculator with Loops using Functions

# Function that calculates the accumulated value of a principal after interest
def calculate_Amount(principal, rate, cpy, years):
    return principal * ((1 + ((rate / 100) / cpy))) ** (cpy * years)

# Function that returns an adjusted interest rate based on the principal balance
def adjust_rate(principal, rate):
    if principal >= 5100 and principal <= 11000:
        rate += 0.5
    elif principal >= 11001 and principal <= 60000:
        rate += 0.75
    elif principal > 60000:
        rate += 1.25
    return rate

# Function that returns a bonus amount based on compounding years and interest rate
def incentive_one(principal, rate, years):
    if years >= 12 and rate >= 6:
        return (principal * 0.1) * years
    else:
        return 0

# Function that returns a bonus amount based on the original interest rate
def incentive_two(rate):
    if rate > 11:
        return 75
    else:
        return 0

# Function that accepts user inputs and outputs a simplified amortization table as well as the final accumulated value
def main():
    runAgain = True

    while runAgain:
        # prompt the user for inputs
        principalAmount = float(input("Enter the principal balance: "))
        interestRate = float(input("Enter the interest rate as a percent: "))
        compoundFrequency = float(input("How many times per year is the interest compounded? "))
        compoundYears = float(input("How many years will the account earn interest? "))

        adjustedInterestRate = adjust_rate(principalAmount, interestRate)                                                                   # get the adjusted interest rate based on incentives

        print("\nYear \t Amount")
        for numYears in range(1, (int(compoundYears) + 1)):                                                                                 # print simplified amortization table
            print(numYears, " \t $", format(calculate_Amount(principalAmount, adjustedInterestRate, compoundFrequency, numYears), ",.2f"), sep = "")                                                                                                          # reset yearly value to bonus to reset value for next year

        accumulatedValue = calculate_Amount(principalAmount, adjustedInterestRate, compoundFrequency, compoundYears)                        # calculates and stores the accumulated balance after compound interest and any extra incentive rates
        accumulatedValue += incentive_one(principalAmount, interestRate, compoundYears)                                                     # adds 1% incentive bonus if applicable or 0
        accumulatedValue += incentive_two(interestRate)                                                                                     # adds 75 bonus if applicable or 0 to final accumulated value
        print("\nAt the end of ", compoundYears, " years, you will have $", format(accumulatedValue, ",.2f"), sep = "")                     # display the accumulated value after compound interest rounded to 2 decimal places

        userInput = input("\nWould you like to run the calculations again on another set of data? (y/n) [Not Case Sensitive]: ")            # ask the user if they want to run again
        while not((userInput.lower() == "y") or (userInput.lower() == "n")):                                                                # perform input validation
                print("Invalid Input! Valid Inputs are \"Y\", \"y\", \"N\", or \"n\"")
                userInput = input("Would you like to run the calculations again on another set of data? (y/n): ")
        if(userInput.lower() == "n"):                                                                                                       # terminate the program through loop invalidation
            runAgain = False
        print("")
main()