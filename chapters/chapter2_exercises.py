#1
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

#2
print( 2 + (3 - 1) * 10 / 5 * (2 + 3) )
print( 2 + (2 * 10) / 5 * 5 )
print( 2 + (20 / 5) * 5 )
print( 2 + (4 * 5) )
print( 2 + 20 )

#3
current_time = int(input("What is the current time (in hours)?"))
wait_time = int(input("How many hours to wait for alarm?"))

alarm_time = (current_time + wait_time) % 24

print("The hour on the clock will be", alarm_time, "when the alarm goes off.")

#4
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

#5
print( "6 * 1 - 2 ==", (6 * 1 - 2) )
print( "6 * (1 - 2) ==", (6 * (1 - 2)) )

#6
P = 10000
n = 12
r = .08
t = int(input("Compounded for how many years?"))

A = P * ( (1 + (r / n)) ** (n * t) )    

print("The final amount after", t, "years is", A)

#7  
radius = float(input("What is the radius of your circle?"))
pi = 3.14

area = pi * (radius ** 2)

print(area)

#8
width = int(input("Width?"))
height = int(input("Height?"))

area = width * height

print("The area of the rectangle is", area)

#9
miles = float(input("How many miles have you driven?"))
gallons = float(input("How many gallons have you used?"))

MPG = int(miles / gallons)               
print("Your car gets", MPG, "miles per gallon.")

#10
deg_C = int(input("What is the temperature in Celsius?"))
deg_F = deg_C * (9/5) + 32

print(deg_C, "degrees Celsius is", deg_F, "degrees Fahrenheit." )

#11
deg_F = int(input("What is the temperature in Fahrenheit?"))
deg_C = (deg_F - 32) / (9/5)

print(deg_F, "degrees Fahrenheit is", deg_C, "degrees Celsius." )

