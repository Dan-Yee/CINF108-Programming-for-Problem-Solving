# Dan Yee
# CINF 108 - Programming for Problem Solving
# Assignment #5 - Compound Interest Calculator using Loops, Functions, File I/O and Exceptions

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
    outputFile = open("output.txt", "w")
    validInput = False

    while not(validInput):
        try:
            fileName = input("Enter the file name with extension: ")
            inputFile = open(fileName, "r")
            print("File Opened:", fileName, "\n")
            outputFile.write("File Opened: " + fileName + "\n\n")
            validInput = True;
        except FileNotFoundError:
            # Note file name error
            print("File Name:", fileName)
            print("FileNotFoundError: Please check file name and extension")
            print("")

    for data in inputFile:
        try:
            # read and process data read from line
            principalAmount = float(data.split(" ")[0])
            interestRate = float(data.split(" ")[1])
            compoundFrequency = float(data.split(" ")[2])
            compoundYears = float(data.split(" ")[3])
        except ValueError:
            # Note the data error and move to the next line of data
            print("ValueError: Invalid numeric data was entered from line:", data, end = "")
            outputFile.write("ValueError: Invalid numeric data was entered from line: " + data)
            print("Moving to next line of data...")
            outputFile.write("Moving to next line of data...\n")
            print("========================================")
            outputFile.write("========================================\n")
            continue
        
        # display each piece of information read from file
        print("Principal Amount: $", format(principalAmount, ",.2f"), sep = "")
        outputFile.write("Principal Amount: $" + str(format(principalAmount, ",.2f")) + "\n")
        print("Interest Rate: ", format(interestRate, ",.2f"), "%", sep = "")
        outputFile.write("Interest Rate: " + str(format(interestRate, ",.2f")) + "%\n")
        print("Compounding Periods Per Year:", compoundFrequency)
        outputFile.write("Compounding Periods Per Year: " + str(compoundFrequency) + "\n")
        print("Compounding Periods:", compoundYears, "years")
        outputFile.write("Compounding Periods: " + str(compoundYears) + " years\n\n")

        adjustedInterestRate = adjust_rate(principalAmount, interestRate)                                                                   # get the adjusted interest rate based on incentives

        print("\nYear \t Amount")
        outputFile.write("Year \t Amount\n")
        for numYears in range(1, (int(compoundYears) + 1)):                                                                                 # print simplified amortization table
            print(numYears, " \t $", format(calculate_Amount(principalAmount, adjustedInterestRate, compoundFrequency, numYears), ",.2f"), sep = "")
            outputFile.write(str(numYears) + "\t $" + str(format(calculate_Amount(principalAmount, adjustedInterestRate, compoundFrequency, numYears), ",.2f")) + "\n")
        outputFile.write("\n")

        accumulatedValue = calculate_Amount(principalAmount, adjustedInterestRate, compoundFrequency, compoundYears)                        # calculates and stores the accumulated balance after compound interest and any extra incentive rates
        accumulatedValue += incentive_one(principalAmount, interestRate, compoundYears)                                                     # adds 1% incentive bonus if applicable or 0
        accumulatedValue += incentive_two(interestRate)                                                                                     # adds 75 bonus if applicable or 0 to final accumulated value
        print("\nAt the end of ", compoundYears, " years, you will have $", format(accumulatedValue, ",.2f"), sep = "")                     # display the accumulated value after compound interest rounded to 2 decimal places
        outputFile.write("At the end of " + str(compoundYears) + " years, you will have $" + str(format(accumulatedValue, ",.2f")) + "\n")
        print("========================================")
        outputFile.write("========================================\n")
    inputFile.close()
    outputFile.close()
main()