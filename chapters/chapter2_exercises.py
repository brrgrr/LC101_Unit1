# 1
"""
Evaluate the following numerical expressions in your head, then use the active code window to check your results:

5 ** 2
9 * 5
15 / 12
12 / 15
15 // 12
12 // 15
5 % 2
9 % 5
15 % 12
12 % 15
6 % 6
0 % 7
"""
print("5 ** 2 ==", 5 ** 2)
print("9 * 5 ==", 9 * 5)
print("15 / 12 ==", 15 / 12)
print("12 / 15 ==", 12 / 15)
print("15 // 12 ==", 15 // 12)
print("12 // 15 ==", 12 // 15)
print("5 % 2 ==", 5 % 2)
print("9 % 5 ==", 9 % 5)
print("15 % 12 ==", 15 % 12)
print("12 % 15 ==", 12 % 15)
print("6 % 6 ==", 6 % 6)
print("0 % 7 ==", 0 % 7)

# 2
"""
What is the order of the arithmetic operations in the following expression? Evaluate the expression by hand and then check your work.

2 + (3 - 1) * 10 / 5 * (2 + 3)
"""
print(2 + (3 - 1) * 10 / 5 * (2 + 3))
print(2 + (2 * 10) / 5 * 5)
print(2 + (20 / 5) * 5)
print(2 + (4 * 5))
print(2 + 20)

# 3
"""
Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).

If it is currently 13 and you set your alarm to go off in 50 hours, the hour will be 15 (3pm). Write a program to solve the general version of the above problem. Ask the user for the current time (in hours), and then ask for the number of hours to wait for the alarm.

Your program should output what the hour will be on the clock when the alarm goes off.
"""
current_time = int(input("What is the current time (in hours)?"))
wait_time = int(input("How many hours to wait for alarm?"))

alarm_time = (current_time + wait_time) % 24

print("The hour on the clock will be", alarm_time, "when the alarm goes off.")

# 4
"""
Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.
"""
word1 = "All"
word2 = "work"
word3 = "and"
word4 = "no"
word5 = "play"
word6 = "makes"
word7 = "Jack"
word8 = "a"
word9 = "dull"
word10 = "boy."
print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

sentence = "All work and no play makes Jack a dull boy."
lst = sent.split()
for word in lst:
    print(word + " ", end="")

print("\n"+" ".join(lst))
# 5
"""
Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
"""
print("6 * 1 - 2 ==", (6 * 1 - 2))
print("6 * (1 - 2) ==", (6 * (1 - 2)))

# 6
"""
The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
    ## formula for compound interest ##
Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
"""
P = 10000
n = 12
r = .08
t = int(input("Compounded for how many years?"))

A = P * ((1 + (r / n)) ** (n * t))

print("The final amount after", t, "years is", A)

# 7
"""
Write a program that will compute the area of a circle. Prompt the user to enter the radius, and then print the answer, like this:

What is the radius of your circle?
>>> 7.8
191.0376
"""
radius = float(input("What is the radius of your circle?"))
pi = 3.14

area = pi * (radius ** 2)

print(area)

# 8
"""
Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.
"""
width = int(input("Width?"))
height = int(input("Height?"))

area = width * height

print("The area of the rectangle is", area)

# 9
"""
Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer, like this:

How many miles have you driven?
>>> 150
How many gallons have you used?
>>> 5
Your car gets 30 miles per gallon.
"""
miles = float(input("How many miles have you driven?"))
gallons = float(input("How many gallons have you used?"))

MPG = int(miles / gallons)
print("Your car gets", MPG, "miles per gallon.")

# 10
"""
Write a program that will convert degrees Celsius to degrees Fahrenheit.
"""
deg_C = int(input("What is the temperature in Celsius?"))
deg_F = deg_C * (9 / 5) + 32

print(deg_C, "degrees Celsius is", deg_F, "degrees Fahrenheit.")

# 11
"""
Write a program that will convert degrees Fahrenheit to degrees Celsius, like this:

What is the temperature in Fahrenheit?
>>> 32
32.0 degrees Fahrenheit is 0.0 degrees Celsius.
"""
deg_F = int(input("What is the temperature in Fahrenheit?"))
deg_C = (deg_F - 32) / (9 / 5)

print(deg_F, "degrees Fahrenheit is", deg_C, "degrees Celsius.")
