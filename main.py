import random

while True:
    choices =["R", "P", "S"]
    
    CPU = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("R, P or S?: ")
    if player == CPU:
            print("CPU: ",CPU)
            print("player: ",player)
            print("Tie!")
            continue 
    elif player == "R":
        if CPU == "P":
            print("CPU: ",CPU)
            print("player: ",player)
            print("You lose!") 
        if CPU == "S":
            print("CPU: ",CPU)
            print("player: ",player)
            print("Winner!")
    elif player == "S":
        if CPU == "R":
            print("CPU: ",CPU)
            print("player: ",player)
            print("You lose!") 
        if CPU == "P":
            print("CPU: ",CPU)
            print("player: ",player)
            print("Winner!") 
    elif player == "P":
        if CPU == "S":
            print("CPU: ",CPU)
            print("player: ",player)
            print("You lose!") 
        if CPU == "R":
            print("CPU: ",CPU)
            print("player: ",player)
            print("Winner!") 
        break
print("Bye!")


             

