#1
exp = [(3 == 3), (3 != 3), (3 >= 4), (not (3 < 4))]
eval = [True, False, False, False]
err = len(eval)-len(exp)
if err == 0: 
    for i in range(len(exp)):
        if exp[i] == eval [i]:
            result = "Great Job"
        else:
            result = "Try Again"
        print(str(i+1)+".", result) 
elif err < 0:
    print("You have not evaluated all the expressions.", err)
else: #err > 0
	print("You have", err, "too many evaluations.")
	
#2
import random

def grade(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"
for x in range(20):
    score = random.random()*100
    print(score, grade(score))
	
#3
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100:
        t.fillcolor("yellow")
    elif height < 100:
        t.fillcolor("green")
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def main():
    data = [48, 117, 200, 240, 160, 260, 220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()

#4
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100:
        t.fillcolor("yellow")
    elif height < 100:
        t.fillcolor("green")
    t.begin_fill()               # start filling this shape
    if height < 0:
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def main():
    data = [48, 117, -100, 200, 240, 160, 260, 220]
    max_height = max(data)
    min_height = min(data)
    num_bars = len(data)
    border = 10

    if min_height > 0:
        bottom = 0
    else:
        bottom = min_height - border
        
    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, bottom, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()






#5
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)


#6
from test import testEqual

def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)


#7
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_odd(n):
    return (not(is_even(n)))

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)


#8
def is_hot(temp):
    if temp >= 90:
        return True
    else: 
        return False

def is_wet(rain):
    if rain == "yes":
        return True
    else: 
        return False
    
def pick_activity(is_hot,is_wet):
    if is_hot and is_wet:        #hot and wet, watch Netflix.
        return "watch Netflix."
    elif is_hot and not(is_wet): #hot and dry, go swimming.
        return "go swimming."
    elif not(is_hot) and is_wet: #cold and wet, paint.
        return "paint."
    else:                        #cold and dry, go to a cafe and read.
        return "go to a cafe and read."

def main():
    temp = int(input("What is the temperature (F)?"))
    rain = input("Is it raining? (yes/no)")
    result = pick_activity( is_hot(temp), is_wet(rain) )
    print("Based on the current weather, you should", result)

if __name__ == "__main__":
    main()



#9
from test import testEqual

def is_rightangled(a, b, c):
    if abs( (a**2 + b**2) - (c**2) ) < 0.001:
        return True
    else:
        return False

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)


#10
from test import testEqual

def is_rightangled(a, b, c):
    sides = [a,b,c]
    sides.sort()
    if abs( (sides[0]**2 + sides[1]**2) - (sides[2]**2) ) < 0.001:
        return True
    else:
        return False

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(16.0, 4.0, 8.0), False)
testEqual(is_rightangled(4.1, 9.1678787077, 8.2), True)
testEqual(is_rightangled(9.16787, 4.1, 8.2), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.64031, 0.4), True)


#11
def date_of_easter(year):
    # Your code here
    if year < 1900 or year > 2099:
        return ("ERROR: Year is out of range")
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e
        # special_years =(1954, 1981, 2049, 2076)
        if year in (1954, 1981, 2049, 2076):
            date = date - 7
        
        if date > 31: 
            return "April " + str(date - 31)
        else:
            return "March " + str(date)

def main():
    # Your code here
    year = int(input("Please enter a year:"))
    print(date_of_easter(year))

if __name__ == "__main__":
    main()


#Weekly Graded Assignment
def is_leap(year):
    if year % 4 != 0: # not divisible by 4
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

