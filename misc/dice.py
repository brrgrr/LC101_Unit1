import random

def roll(q,s):
    total_roll = 0
    for i in range(q):
        roll = random.randint(1,s)
        print("d"+str(s), i+1, ":", roll)
        total_roll += roll
    return total_roll  

quantity = int(input("How many dice?"))
sides = int(input("How many sides per die?"))

print("Total score:", roll(quantity,sides))
