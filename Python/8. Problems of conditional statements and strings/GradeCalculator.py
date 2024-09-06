#Create a program that takes the marks of a student in different subjects as input. Calculate the total marks and average, and then display the corresponding grade based on the average.

'''
Sample input = Marks in Math: 85, Marks in Science:90, Marks in English: 78

Sample output = Total Marks: 253, Average Marks: 84.33
'''

m = int(input("Marks in Math: "))
s = int(input("Marks in Science: "))
e = int(input("Marks in English: "))

total_marks = m+s+e
average = total_marks / 3

percentage = (total_marks / 300) * 100
grade = " "

if percentage > 90:
    grade = "A"
elif percentage > 80:
    grade = "B"
elif percentage > 70:
    grade = "C"
else:
    grade = "P"
    
print(f"Total Marks: {total_marks} \nAverage Marks: {average} \nGrade: {grade}")