def main():

    firstNumber = input("first number: ")
    secondNumber = input("second number: ")

    print("what would you like to do")
    calculation = input("add, subtract, times, or divide: ")

    if calculation == "add":
        result = (int(firstNumber) + int(secondNumber))
    elif calculation == "subtract":
        result = (int(firstNumber) - int(secondNumber))
    elif calculation == "divide":
        result = (int(firstNumber) / int(secondNumber))
    elif calculation == "times":
        result = (int(firstNumber) * int(secondNumber))

    print(result)

    restart = input("do you wish to do a new calculation: ")
    if restart == "yes":
        main()

    else:
        exit()
main()
