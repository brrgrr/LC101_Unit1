#1
## original
for i in range(1000):
    print("We like Python's turtles!")
## update
number_of_reps = int(input("How many repetitions of the message?"))
for i in range(number_of_reps):
    print("We like Python's turtles!")

#2
bottles = int(input("How many bottles?"))
line1a = "bottle"
line1b = "of beer"
line1c = "on the wall"
line2a = "Take one down and pass it around,"
line2b = "Go to the store and buy some more,"

for i in range(bottles,-1, -1):
    if i > 2:
        print(i, line1a+"s", line1b, line1c+",", i, line1a+"s", line1b+".")
        print(line2a, i - 1, line1a+"s", line1b, line1c+".")
    elif i == 2:
        print(i, line1a+"s", line1b, line1c+",", i, line1a+"s", line1b+".")
        print(line2a, i - 1, line1a, line1b, line1c+".")
    elif i == 1:
        print(i, line1a, line1b, line1c+",", i, line1a, line1b+"." )
        print(line2a, "no more", line1a+"s", line1b, line1c+".")
    elif i == 0:
        print("No more", line1a+"s", line1b, line1c+",", "no more", line1a+"s", line1b+".")
        print(line2b, bottles, line1a+"s", line1b, line1c+".")


#3
for i in range(0, 52, 2):
    print(i)

#4
for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']:
    print("One of the months of the year is", month)

#5
import turtle
import random

wn = turtle.Screen()
terry = turtle.Turtle()
terry.shape("turtle")
terry.pensize(3)
terry.speed(0)

for sides in [3,4,6,8]:
    terry.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    length = (800/sides)
    terry.up()
    terry.home()
    terry.goto(-(length/2),-(length/2))
    terry.down()
    terry.stamp()
    for i in range(sides):
        terry.forward(length)
        terry.left(360/sides)

wn.exitonclick()

#6
import turtle

wn = turtle.Screen()
axl = turtle.Turtle()
axl.shape("turtle")
axl.speed(10)

sides = int(input("How many sides?"))
length = int(input("What length for each side?"))
pen_color = input("What pen color?")
fill_color = input("What fill color?")

axl.color(pen_color,fill_color)

axl.begin_fill()
for i in range(sides):
    axl.forward(length)
    axl.left(360/sides)
axl.end_fill()

wn.exitonclick()

#7
import turtle

wn = turtle.Screen()
axl = turtle.Turtle()
axl.shape("turtle")
axl.speed(10)

axl.penup()
axl.goto(100,0)
axl.pendown()

for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    axl.left(angle)
    axl.forward(100)

wn.exitonclick()

#8
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(5)
tess.right(90)     # turn south
tess.left(3600)    # 10 full spins, still south
tess.right(-90)    # turn east
tess.left(3600)    # 10 full spins, still east
tess.forward(-100) # negative forward means backwards 


#9
import turtle

wn = turtle.Screen()
axl = turtle.Turtle()
axl.ht()
axl.speed(10)
axl.pensize(3)

for i in range(5):
    axl.forward(100)
    axl.left(216)

wn.exitonclick()

#10
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
axl = turtle.Turtle()
axl.shape("turtle")
axl.color("blue")
axl.pensize(3)
axl.speed(10)
axl.left(90)       #start at the top

for hour in range(12):
    axl.penup()
    axl.forward(120)
    axl.pendown()
    axl.forward(10)
    axl.penup()
    axl.forward(20)
    axl.stamp()
    axl.backward(150)
    axl.right(30)

axl.home()
wn.exitonclick()

#11
import turtle
import random

wn = turtle.Screen()
axl = turtle.Turtle()
axl.shape("turtle")
axl.speed(0)
axl.pensize(5)


for degree in range(360):
    axl.color(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    axl.forward(degree//2)
    axl.right(degree)
    

wn.exitonclick()


#12
import turtle

wn = turtle.Screen()
axl = turtle.Turtle()

print(type(axl))

#13
import turtle

wn = turtle.Screen()

sprite = turtle.Turtle()
sprite.hideturtle()
sprite.speed(10)
legs = int(input("How many legs should this sprite have?"))
angle = 360 / legs

for i in range(legs): 
    sprite.left(angle)
    sprite.forward(100)
    sprite.dot()
    sprite.forward(-100)

sprite.dot()

wn.exitonclick()

#14
import random
for i in range(10):
    print(random.randrange(1,100))

#15
import random
for i in range(10):
    print(random.randrange(25,35))

#16
import math

a = int(input("What is the length of the first side?"))
b = int(input("What is the length of the second side?"))

c = math.hypot(a,b)
print("The hypotenuse of the triangle is", c)

#17
import math

pi_approx = 22/7

print("One approximation of pi is", pi_approx)
print("The math module says pi is actually", math.pi)


#Weekly Graded Assignment
nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for a in nums:
    print(a)
    
for b in nums:
    print("The square of", b, "is", (b**2))

