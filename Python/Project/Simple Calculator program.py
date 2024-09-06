'''
1. Create a basic calculator program that performs addition, subtraction, multiplication, division.
2. Ask the user to enter two numbers and choose an operation.
3. Display the result accordingly.
4. Handle potential errors gracefully.'''

num1 = int(input("Give 1st number: "))
num2 = int(input("Give 2nd number: "))
operator = input("Give operator: ")

if operator == "+":
    print(f"Addition of two numbers is{num1 + num2}")
elif operator == "-":
    print(f"Subtraction of two numbers is{num1 - num2}")
elif operator == "*":
    print(f"Multiplication of two numbers is{num1 * num2}")
elif operator == "/":
    print(f"Division of two numbers is{num1 / num2}")
else:
    print("Invalid operator")