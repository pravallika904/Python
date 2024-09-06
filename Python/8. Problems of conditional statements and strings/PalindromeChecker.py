#Write a program that takes a string input from the user and check if it is a palindrome or not. A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as forward.

''' 
Sample input: "radar"
Sample output: It is a palindrome.
'''

'''
s = "RADAR"

print(s[ : : -1])
'''

s = input("Give a string: ")

reverse = s[ : : -1]

if reverse == s:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")