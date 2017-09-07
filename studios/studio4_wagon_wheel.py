#version1

import turtle

def draw_square(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)
    
def draw_foursquare(t, s):
    for i in range(2):
        draw_square(t,s)
        draw_square(t,-s)
        t.left(90)
    t.left(180)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    axl = turtle.Turtle()
    axl.color('blue')
    axl.pensize(2)
    axl.speed(10)
    for i in range(5):
        draw_foursquare(axl,100)
        axl.left(90/5)
 
    wn.exitonclick()

if __name__ == "__main__":
    main()

#version2
import turtle

def draw_square(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    axl = turtle.Turtle()
    axl.color('blue')
    axl.pensize(2)
    axl.speed(0)
    axl.ht()
    for i in range(20):
        draw_square(axl,100)
        axl.left(90/5)
 
    wn.exitonclick()

if __name__ == "__main__":
    main()

#bonus1
def square(x):
    running_total = 0          # initialize the accumulator!
    for counter in range(x):
        running_total = running_total + x

    return running_total

def power(x,y):
    running_total = square(x)          # initialize the accumulator!
    for counter in range(2,y):
        running_total = running_total * x

    return running_total


num = 2
exp = 8
result = power(num,exp)
print("The result of", num, "to the power of", exp, "is", result)

if num ** exp == result:
    print("Pass")
else:
    print("Fail")

	
#bonus2 - Fibonacci
	def fib(n):
    if n < 0:
        return "ERROR: Out of range."
    elif n == 0 or n == 1:
        return (n)
    else:
        return ( fib(n-2) + fib(n-1) )
    
for i in range(27):
    print(i, fib(i) )
        