# Python calculator that accepts user input

# We will first prompt the user to enter their name
# We will then prompt them to enter the type of operator they wish to use to perform an operation
# We will finally display the result of operation, their name and a goodbye message

# Let's get started

name = input("Enter your name: ")

# Looping calculator program
while True:
    # Prompt user for an operator
    operator = input("Enter an operator (+, -, *, /) or 'exit' to quit: ")

    if operator.lower() == 'exit': #we are using the lower() method just incase the user types in caps
        break  # Exit the loop without printing anything here

    # Check if operator is valid
    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator. Please try again.")
        continue

    # Get two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number. Please enter numeric values.")
        continue

    # Perform the operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            continue

    # Print the result
    print("Result:", result)

# Final thank you message after exiting the loop
print(f"Thank you {name}. Goodbye for now.")
