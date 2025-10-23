# Simple Calculator

while True:
    operation = input("Choose an operation (add, subtract, multiply, divide, modulus, power, floor) or type 'exit' to quit:").lower()

    if operation == "exit":
        print("Exiting the calculator. Goodbye!")
        break

    num1 = float(input("Enter Your First Number: "))
    num2 = float(input("Enter Your Second Number: "))


    if operation == "add":
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")

    elif operation == "subtract":
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is: {result}")

    elif operation == "multiply":
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")

    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")

    elif operation == "modulus":
        result = num1 % num2
        print(f"The result of modulus {num1} by {num2} is: {result}")

    elif operation == "power":
        result = num1 ** num2
        print(f"The result of {num1} raised to the power of {num2} is: {result}")

    elif operation == "floor":
        result = num1 // num2
        print(f"The result of floor division of {num1} by {num2} is: {result}")
        
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, divide, modulus, power, floor or type 'exit' to quit.")
