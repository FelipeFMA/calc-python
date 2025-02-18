num1 = int(input("\nEnter an integer: "))
op = (input("Enter an operator (+, -, * or /): "))
num2 = int(input("Enter another integer: "))

if(op == "+"):
    print("\nYou chose to add, the result is...")
    print(num1+num2, "\n")
elif(op == "-"):
    print("\nYou chose to subtract, the result is...")
    print(num1-num2, "\n")
elif(op == "*"):
    print("\nYou chose to multiply, the result is...")
    print(num1*num2, "\n")
elif(op == "/"):
    print("\nYou chose to divide, the result is...")
    print(num1/num2, "\n")
else:
    print("\nEnter a valid operator!\n")
