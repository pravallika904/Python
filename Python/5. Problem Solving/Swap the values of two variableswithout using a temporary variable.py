'''  
input: a = 10, b = 20
output: after swapping--> a = 20, b = 10
'''

a = int(input("Give a: "))
b = int(input("Give b: ")) 
b = b + a
a = b - a
b = b - a

print(f"value of a is: {a}")
print(f"value of b is: {b}")
