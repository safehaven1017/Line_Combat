import os
from random import randint
from convert_choices import *
from update_health_bars import update_health_bars
from defense_check import defense_check
from attack_check import attack_check
from deal_attacks import deal_attacks
from takedown_round import takedown_round
from player_choices import player_choices


def fight(p1, p2):    
    
    clear = lambda: os.system('clear')

    clear()

    update_health_bars(p1, p2)

    if p1.debuff_flag == 1:
        p1.debuff_flag = 0
        p1.status = "Normal"
    if p2.debuff_flag == 1:
        p2.debuff_flag = 0
        p2.status = "Normal"

    while p1.health > 0 and p2.health > 0:

        if p1.status == "Taken Down":

            takedown_round(p2, p1)
        
        elif p2.status == "Taken Down":

            takedown_round(p1, p2)

        else:
 
            player_choices(p1, p2)
            
            update_health_bars(p1, p2)
            
            print("1. Parry\n2. Kick Check\n3. Leg Catch\n4. Judo Counter\n\n")
            print(f"{p1.name}'s current attack: {p1.offense}")
            defense_choice = int(input("choose your defensive move: "))
            convert_defense_choice(defense_choice, p1)

            update_health_bars(p1, p2)

            print(f"{p1.name}'s current attack: {p1.offense}")
            print(f"{p1.name}'s current defense: {p1.defense}\n\n")
            input("Press 'Enter' to continue...")

            p2.roll_offense()
            p2.roll_defense()

            if p1.debuff_flag == 0 or p2.debuff_flag == 0:
                p1.debuff_flag = 1
                p2.debuff_flag = 1

            if defense_check(p1, p2) == False:
                if defense_check(p2, p1) == False:
                    if attack_check(p1, p2) == False:
                        deal_attacks(p1, p2)
                        deal_attacks(p2, p1)