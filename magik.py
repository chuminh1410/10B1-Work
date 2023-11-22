import random
mana = 100
magic_ball = 5
holy = 10
drain_life = 20 

def attack():
    print("Choose your skill: \n1 - Magic Ball \n2 - Holy \n3 - Drain Life\n")
    choice = input("")
    while choice >=1 and choice <= 3:
        succ = random.randint(0,100)
        if choice == 1:
            if succ > 85:



attack()
