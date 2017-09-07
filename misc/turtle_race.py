import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

players = int(input("How many players?"))
racers = ["ben", "liz"]

for racer_number in range(len(racers)):
    x = racers[racer_number]
    racers[racer_number] = turtle.Turtle()    # 3. Create two turtles
    print(type(racers[racer_number]))
    racers[racer_number].ht()
    racers[racer_number].shape('turtle')
    racers[racer_number].speed(3)
    racers[racer_number].color('green')


racers[0].penup()                  # 4. Move the turtles to their starting point
#liz.penup()
racers[0].goto(-200,20)
#liz.goto(-200,-20)
racers[0].st()
#liz.st()

while (ben.xcor() < 200) and (liz.xcor() < 200):
    ben.forward(random.randrange(2,13))
    liz.forward(random.randrange(2,13))

if ben.xcor() > liz.xcor():
    print("Ben wins!")
elif liz.xcor() > ben.xcor():
    print("Liz wins!")
elif liz.xcor() == ben.xcor():
    print("Tie!")

wn.exitonclick()
