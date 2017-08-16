# Imports
import turtle
import random

# Questions
players = 4 # int(input("How many players?"))
dice_quantity = 2 # int(input("How many dice?"))
dice_sides = 20 # int(input("How many sides per die?"))


# Functions
def rand_color():
    '''Generate random color'''
    if wn.colormode() == 255:
        return random.randint(0,255)
    elif wn.colormode() == 1:
        return random.random()

def dice_roll(q,s):
    '''Simulate roll of multiple dice'''
    total_roll = 0
    for i in range(q):
        total_roll += random.randint(1,s)
    return total_roll  

def get_player_info(player_number):
    player_name = input("Player", player_number, "Name?")
    return 


wn = turtle.Screen()
wn.title("Turtle Race 2.0")
wn.bgcolor('black')
wn.colormode(1.0)


'''
number_of_players = random.randint(2,12)
racers = [ i + 1 for i in range(randint(2,13))  ]
print(racers)
'''

racers = ['red','orange','yellow','green','blue','purple'] 
         
n = len(racers)
wn.setup(width=(max(75*n,800)), height=(max(75*n,600)))
screen_h = wn.window_height()-50
screen_w = wn.window_width()-75

start_x = screen_w//2 - screen_w
finish_x = screen_w//2
base_y = screen_h//2 - screen_h
lane_h = (screen_h // n)
lane_start = start_x + 75
lane_finish = finish_x - 100
# Create track
track = turtle.Turtle()
track.shape()
track.speed(10)
track.color('white')
track.pensize(n)
track.ht()
track.penup()
track.goto(lane_start,base_y)
track.pendown()
track.goto(lane_start,base_y+(lane_h*n))
track.write('Start')
for lane_num in range(n+1):
    track.pensize(1)
    track.penup()
    track.goto(lane_start,base_y+(lane_h*lane_num))
    track.pendown()
    track.goto(lane_finish,base_y+(lane_h*lane_num))
track.penup()
track.goto(lane_finish,base_y+(lane_h*n))
track.pendown()
track.pensize(n)
track.write('Finish')
track.goto(lane_finish,base_y)

    
racer_number = 0 
for racer in racers:
    
    racers[racer_number] = turtle.Turtle()
    #racers[racer_number].ht()
    racers[racer_number].shape('turtle')
    racers[racer_number].speed(10)
    racers[racer_number].color(racer)
    racers[racer_number].penup()
    racers[racer_number].goto(start_x+15,(base_y + ((screen_h // n) * (racer_number + 0.5))))
    racers[racer_number].write(racer.title())
    racers[racer_number].pencolor(rand_color(),rand_color(),rand_color())
    racers[racer_number].forward(50)
    #racers[racer_number].st()
    racers[racer_number].speed(1)
    racer_number += 1
    
for lap in range(n**42):
    turn = random.randrange(0,n)    # random player
    steps = dice_roll(dice_quantity,dice_sides)   # roll dice 
    
    racers[turn].forward(steps)
    
    if racers[turn].xcor() >= lane_finish:
        racers[turn].forward(15)
        racers[turn].write("Winner!!!",move=True,font=("Arial", 12, "normal"))
        racers[turn].forward(15)
        break
    
    
'''    
while (racers[0].xcor() < lane_finish) and (racers[1].xcor() < lane_finish):
    racers[0].forward(random.randrange(2,13))
    racers[1].forward(random.randrange(2,13))

if racers[0].xcor() > racers[1].xcor():
    print(racers[0])
elif racers[1].xcor() > racers[0].xcor():
    print(racers[1])
elif racers[0].xcor() == racers[1].xcor():
    print("Tie!")
'''
wn.exitonclick()
