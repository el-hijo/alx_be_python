num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
type_of_operation = input("Choose the type of operation (+, -, *, /): ")
match type_of_operation:
    case "+":
        print("The result is",str(num1 + num2)+".")
    case "-":
        print("The result is",str(num1 - num2)+".")
    case "*":
        print("The result is",str(num1 * num2)+".")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is",str(num1/num2)+".")

        