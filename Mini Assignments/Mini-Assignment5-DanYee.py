# Dan Yee
# CINF 108 - Programming for Problem Solving
# Mini-Assignment #5 - File I/O

# Function that returns true or false based on if a number is odd or not
def Is_Odd(number):
    if not(number % 2 == 0):
        return True
    else:
        return False

# Function that returns the result of number parameter times 15 compared to 1500
def Greater_Than(number):
    multipliedResult = number * 15                                                                 

    if multipliedResult > 1500:
        return "greater than"
    elif multipliedResult < 1500:
        return "less than"
    else:
        return "equal to"

# Main function that reads data from a file, processes the data and writes the results to another file
def main():
    inputFile = open("input.txt", "r")
    outputFile = open("output.txt", "w")

    for data in inputFile:
        readLine = data.split(" ", 1)                                                                   # split the data read in the line using space as the delimeter
        firstNumber = float(readLine[0])                                                                # read the first number from the line
        secondNumber = float(readLine[1])                                                               # read the second number from the line

        sum = firstNumber + secondNumber

        # print the sum of the two numbers
        # write the sum of the two numbers to file
        print("\nThe sum of", firstNumber, "and", secondNumber, "is", format(sum, ",.2f"))
        outputFile.write("The sum of " + str(firstNumber) + " and " + str(secondNumber) + " is " + str(format(sum, ",.2f")) + ".\n")

        # call Is_Odd function and print results
        # write results of Is_Odd function to file
        if Is_Odd(sum):
            print("The added result, ", format(sum, ",.2f"), ", is odd.", sep = "")
            outputFile.write("The added result, " + str(format(sum, ",.2f")) + ", is odd.\n")
        else:
            print("The added result, ", format(sum, ",.2f"), ", is even.", sep = "")
            outputFile.write("The added result, " + str(format(sum, ",.2f")) + ", is even.\n")

        multipliedResult = sum * 15

        # display the result of Greater_Than function as part of the String
        # write result of Greater_Than function to file
        print("The multiplied result, ", format(multipliedResult, ",.2f"), ", is ", Greater_Than(sum), " 1500.", sep = "")
        outputFile.write("The multiplied result, " + str(format(multipliedResult, ",.2f")) + ", is " + Greater_Than(sum) + " 1500.\n")
        outputFile.write("\n")

    print("\nData written to file: output.txt")
    inputFile.close()
    outputFile.close()
main()