#1
def print_triangular_numbers(n):
    sum=0
    for i in range(n):
        sum += (i+1)
        print(sum)

def main():
    print_triangular_numbers(5)

if __name__ == "__main__":
    main()

#2
import random
import turtle

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def main():
    julia = turtle.Turtle()
    screen = turtle.Screen()

    julia.shape('turtle')
    while is_in_screen(screen, julia):
        julia.seth(random.randrange(0,360, 30))
        julia.forward(50)

    screen.exitonclick()

if __name__ == "__main__":
    main()

#3
import random
import turtle

wn = turtle.Screen()
left_bound = -wn.window_width() / 2
right_bound = wn.window_width() / 2
top_bound = wn.window_height() / 2
bottom_bound = -wn.window_height() / 2

def random_start(t):
    t.ht()
    t.up()
    t.goto(random.randrange(left_bound, right_bound),
           random.randrange(bottom_bound, top_bound))
    t.seth(random.randrange(0,360,90))
    t.down()
    t.st()

def walk(t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)

def is_in_screen(t):
    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def main():
    ben = turtle.Turtle()
    liz = turtle.Turtle()

    random_start(ben)
    random_start(liz)

    ben.color('green')
    liz.color('yellow')

    while is_in_screen(ben) and is_in_screen(liz):
        walk(ben)
        walk(liz)

    wn.exitonclick()

if __name__ == "__main__":
    main()


#4
import random
import turtle
import math

wn = turtle.Screen()
left_bound = -wn.window_width() / 2
right_bound = wn.window_width() / 2
top_bound = wn.window_height() / 2
bottom_bound = -wn.window_height() / 2

def random_start(t):
    t.speed(0)
    t.ht()
    t.up()
    t.goto(random.randrange(left_bound, right_bound),
           random.randrange(bottom_bound, top_bound))
    t.seth(random.randrange(0,360,90))
    t.down()
    t.st()

def walk(t1, t2):

    for t in [t1,t2]:
        t.left(random.choice([-90,90]))

        for i in range(50):
            t.forward(2)
            if is_bounce(t1,t2):
                t.seth(t.heading()+180)





def is_in_screen(t):
    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def is_bounce(t1, t2):
    bounce = False
    for t in [t1,t2]:
        turtle_x = t.xcor()
        turtle_y = t.ycor()

        if min( abs(turtle_x - right_bound), abs(turtle_x - left_bound),
           abs(turtle_y - top_bound), abs(turtle_y - bottom_bound)) < 5:
            bounce = True

    if t1.distance(t2) < 5:
        bounce = True

    return bounce


def main():
    ben = turtle.Turtle()
    liz = turtle.Turtle()

    random_start(ben)
    random_start(liz)

    ben.color('green')
    liz.color('yellow')

    while is_in_screen(ben) and is_in_screen(liz):
        walk(ben,liz)
    else:
        ben.home()
        liz.home()


    wn.exitonclick()

if __name__ == "__main__":
    main()

#5
import sys

def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! You got this!")

def main():
    sys.setExecutionLimit(120000) # keep program from timing out
    lifts = ["squat", "bench", "deadlift"]
    # Your code here
    for lift_name in lifts:
        wt = 10
        input_prompt = "Keep doing the " + lift_name + "? Enter yes for the next set."
        keep_going = 'yes'
        while keep_going == 'yes':
            workout_coach(lift_name, wt)
            keep_going =input(input_prompt)
            wt +=10
            if lift_name == 'bench' and wt > 200:
                break
            elif keep_going != 'yes':
                break
            else:
                continue



if __name__ == "__main__":
    main()

#6
import image

def remove_red(p):
    new_red = 0
    green = p.getGreen()
    blue = p.getBlue()
    new_pixel = image.Pixel(new_red, green, blue)
    return new_pixel

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        new_img.setPixel(col, row, remove_red(p))

new_img.draw(win)
win.exitonclick()

#7
import image

def grayscale(p):
    red = p.getRed()
    green = p.getGreen()
    blue = p.getBlue()
    gray = (red + green + blue) / 3
    new_pixel = image.Pixel(gray, gray, gray)
    return new_pixel

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        new_img.setPixel(col, row, grayscale(p))

new_img.draw(win)
win.exitonclick()

#8
import image

def grayscale(p):
    red = p.getRed()
    green = p.getGreen()
    blue = p.getBlue()
    gray = (red + green + blue) /3
    new_pixel = image.Pixel(gray, gray, gray)
    return new_pixel

def black_white(p):
    grayscale(p)
    if p.getRed() <  128:
        bw = 0
    else:
        bw = 255
    new_pixel = image.Pixel(bw, bw, bw)
    return new_pixel

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        new_img.setPixel(col, row, black_white(p))

new_img.draw(win)
win.exitonclick()


#9
import image

def sepia(p):
    R = p.getRed()
    G = p.getGreen()
    B = p.getBlue()
    new_r = min(int(R * 0.393 + G * 0.769 + B * 0.189),255)
    new_g = min(int(R * 0.349 + G * 0.686 + B * 0.168),255)
    new_b = min(int(R * 0.272 + G * 0.534 + B * 0.131),255)

    new_pixel = image.Pixel(new_r, new_g, new_b)
    return new_pixel


img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        new_img.setPixel(col, row, sepia(p))

new_img.draw(win)
win.exitonclick()

#10
import image

def double(old_image):
    old_w = old_image.getWidth()
    old_h = old_image.getHeight()

    new_img = image.EmptyImage(old_w * 2, old_h * 2)
    for row in range(old_h):
        for col in range(old_w):
            old_pixel = old_image.getPixel(col, row)

            new_img.setPixel(2*col, 2*row, old_pixel)
            new_img.setPixel(2*col+1, 2*row, old_pixel)
            new_img.setPixel(2*col, 2*row+1, old_pixel)
            new_img.setPixel(2*col+1, 2*row+1, old_pixel)

    return new_img

def main():
    img = image.Image("luther.jpg")
    win = image.ImageWin(img.getWidth() * 2, img.getHeight() * 2)

    big_img = double(img)
    big_img.draw(win)

    win.exitonclick()

if __name__ == "__main__":
     main()

#Weekly Graded Assignment
def course_grader(test_scores):
    '''
    sum_scores=0
    for i in test_scores:
        sum_scores += i
    '''
    avg_score = sum(test_scores) / len(test_scores)
    if avg_score < 70 or min(test_scores) < 50:
        message = 'fail'
    elif avg_score >= 70 and min(test_scores) > 50:
        message = 'pass'
    return message


def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
















