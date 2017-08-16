import random

def roll(q,s):
    total_roll = 0
    for i in range(q):
        total_roll += random.randrange(1,s+1)
    return total_roll  

quantity = int(input("How many dice?"))
sides = int(input("How many sides per die?"))

print("You rolled:", roll(quantity,sides))
