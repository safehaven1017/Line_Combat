import os
from random import randint
from convert_choices import *
from update_health_bars import update_health_bars
from defense_check import defense_check
from attack_check import attack_check
from deal_attacks import deal_attacks
from takedown_round import takedown_round
from player_choices import player_choices
from validate import validate_menu_selection


def fight(p1, p2):    
    
    clear = lambda: os.system('clear')

    clear()
    clear()

    p1.health = p1.max_health
    p2.health = p2.max_health
    p1.status = "Normal"
    p2.status = "Normal"
    p1.debuff_flag = 0
    p2.debuff_flag = 0

    print(f"Time to fight!!! Your opponent will be {p2.get_name()}!")
    input("Press 'Enter' to continue...")

    update_health_bars(p1, p2)

    while p1.health > 0 and p2.health > 0:
        
        

        if p1.status == "Taken Down":

            takedown_round(p2, p1)
        
        elif p2.status == "Taken Down":

            takedown_round(p1, p2)
        
        if p1.debuff_flag == 1:
            p1.debuff_flag = 0
            p1.status = "Normal"
        if p2.debuff_flag == 1:
            p2.debuff_flag = 0
            p2.status = "Normal"

        else:
            
            clear()
            clear()

            update_health_bars(p1, p2)
            input("press 'Enter' to roll for defense checks. This will determine who goes first...")

            while True:
                fighter_a_roll = randint(1,100)
                fighter_b_roll = randint(1,100)

                if fighter_a_roll > fighter_b_roll:
                    p1.advantage = True
                    p2.advantage = False
                    clear()
                    clear()
                    update_health_bars(p1, p2)
                    print(f"{p1.name} has the advantage! Their defense check will go first!")
                    input("Press 'Enter' to continue...")
                    break
                elif fighter_b_roll > fighter_a_roll:
                    p2.advantage = True
                    p1.advantage = False
                    clear()
                    clear()
                    update_health_bars(p1, p2)
                    print(f"{p2.name} has the advantage! Their defense check will go first!")
                    input("Press 'Enter' to continue...")
                    break
                else:
                    continue

            player_choices(p1, p2)

            update_health_bars(p1, p2)
            
            print("1. Parry\n2. Kick Check\n3. Leg Catch\n4. Judo Counter\n\n")
            print(f"{p1.name}'s current attack: {p1.offense}")
            defense_choice = validate_menu_selection(1, 4)
            convert_defense_choice(defense_choice, p1)

            clear()
            clear()

            update_health_bars(p1, p2)

            print(f"{p1.name}'s current attack: {p1.offense}")
            print(f"{p1.name}'s current defense: {p1.defense}\n")
            input("Press 'Enter' to continue...")

            p2.roll_offense()
            p2.roll_defense()

            if p1.debuff_flag == 0 or p2.debuff_flag == 0:
                p1.debuff_flag = 1
                p2.debuff_flag = 1

            if p1.advantage == True:
                if defense_check(p1, p2) == False:
                    if defense_check(p2, p1) == False:
                        if attack_check(p1, p2) == False:
                            deal_attacks(p1, p2)
                            deal_attacks(p2, p1)
            else:
                if defense_check(p2, p1) == False:
                    if defense_check(p2, p1) == False:
                        if attack_check(p1, p2) == False:
                            deal_attacks(p1, p2)
                            deal_attacks(p2, p1)
    
    clear()
    clear()
    
    if p1.health == 0 and p2.health == 0:
        print("\nIT'S A DRAW!!!!!!!\n")
        input("Press 'Enter' to continue...")
    elif p2.health == 0:
        print("\nYOU WIN!!!!!!!\n")
        input("Press 'Enter' to continue...")
    else:
        print(f"\n{p2.get_name().upper()} WINS!!!!!!!\n")
        input("Press 'Enter' to continue...")