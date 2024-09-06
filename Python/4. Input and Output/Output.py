#Output Statements
'''
a = int(input("Give a value: "))
b = int(input("Give a value: "))

print(a,b,a,b,sep = ", ", end = "Ended Here")
'''

#Ex-1: String Input and Output
'''
expected input: "John"
expected output: "Hello, John!"

name = input("enter name: ")
print("Hello",name,sep = ", ",end = "!") 
'''

#Ex-2: Integer Input & Output
'''
expected Input: 5
expected Output: "You entered: 5"

num = int(input("Give value of num: "))
print("You entered:",num)
'''

#Ex-3: Float Input and Output
'''
expected Input: 3.14
expected Output: "value of Pi: 3.14"

pi = float(input("Give value of pi: "))
print("value of Pi:",pi,sep="")
'''

#Ex-4: Taking Multiple Inputs in a single line
'''
expected Input: 10 20 30
expected Output: "Sum of Inputs: 60"

a = input()
x,y,z = a.split(" ")
sum = int(x) + int(y) + int(z)
print(sum)
print("Sum of Inputs: ",sum)
'''

#Ex-5: Specifying separator in Output
'''
expected Input: "John",25
expected Output: "Name:John,Age:25"

b = input("Enter name and age: ")
name,age = b.split(",")

print("Name:",name,",Age:",age,sep = "")
'''

#Ex-6: End Parameter in Output
'''
expected Input: 5
expected Output: "Countdown: 5 4 3 2 1 Blast Off!"

n = int(input("Enter n: "))
print("Countdown: 5 4 3 2 1 ",sep = "", end = "Blast Off!")
'''


#Ex-7: Arithmetic Operators
'''
expected Input: 10, 5
expected Output: "Addition:15, Subtraction:5,Multiplication:50, Division:2.0

x,y = input("Enter a and b values: ").split(",")
a = int(x)
b = int(y)
print("Addition:",a+b,"Subtraction:", a-b, "Multiplication:",a*b,"Division:", a/b,sep = "")
'''

#Ex-8: Comparison Operators
'''
expected Input: 10,5
expected Output: "10>5: True, 10<5: False, 10==5: False, 10!=5: True"

x,y = input("Enter a and b values: ").split(",")
a = int(x)
b = int(y)
print("10>5:",True,"10<5:",False,"10==5:",False,"10!=5:",True, sep=" ")
'''

#Ex-9: Logical Operators
''' 
expected Input: True, False
expected Output: True and False: False, True or False: True, not True: False"

x,y = input("Enter values: ").split(",")
print("True and False:",False,"True or False:",True,"not True:",False)
'''

#Ex-10: Taking Yes/No Input and Handling Case Sensitivity
''' 
expected Input: Yes (or yes, YES, yEs, etc.)
expected Output: "You entered:Yes"

a = input("Give name: ")
print("You entered:", yes)
'''

#Ex-11: Formatting Output using f-strings
'''
expected Input: "Alice",25
expected Output: "Name: Alice, Age:25 years"
'''
x,y = input("Give value:").split(",")
print(f"Name:{x}Age:{y}",sep = " ")

