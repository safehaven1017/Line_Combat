import os
from fighter_classes import *
from fight import fight
from update_health_bars import update_health_bars

clear = lambda: os.system('clear')

def main():  
    
    clear()

    my_fighter = fighter("Rick")
    npc_fighter = npcFighter("Robot")

    fight(my_fighter, npc_fighter)

    clear()
    
    if my_fighter.health == 0 and npc_fighter.health == 0:
        print("\nIT'S A DRAW!!!!!!!\n")
    elif npc_fighter.health == 0:
        print("\nYOU WIN!!!!!!!\n")
    else:
        print(f"\n{npc_fighter.name.upper} WINS!!!!!!!\n")
    input("Press 'Enter' to end...")

main()

clear()