from update_health_bars import update_health_bars
from convert_choices import *
from validate import validate_menu_selection
import os

clear = lambda: os.system('clear')

def player_choices(player, npc):
    
    while True:
        
        clear()
        clear()
        update_health_bars(player, npc)
        
        if player.status == "Broken Knuckles":
            print("1. Low Kick\n2. Roundhouse Kick\n3. Takedown\n")
            print(f"{player.name}'s Status: {player.status}")
            print(f"{npc.name}'s Status: {npc.status}")
            attack_choice = validate_menu_selection(1, 3)
            if attack_choice == 'q':
                print("This will completely exit the game... are you sure?")
                print("Press 'q' again to quit or '1' to continue.")
                exit_choice = validate_menu_selection(1, 1)
                if exit_choice == 'q':
                    quit()
                else:
                    continue
            convert_offense_choice(attack_choice, player)
            
            clear()
            clear()
            break

        elif player.status == "Broken Shin":

            print("1. Punch\n2. Takedown\n")
            print(f"{player.name}'s Status: {player.status}")
            print(f"{npc.name}'s Status: {npc.status}")
            attack_choice = validate_menu_selection(1, 2)
            if attack_choice == 'q':
                print("This will completely exit the game... are you sure?")
                print("Press 'q' again to quit or '1' to continue.")
                exit_choice = validate_menu_selection(1, 1)
                if exit_choice == 'q':
                    quit()
                else:
                    continue
            convert_offense_choice(attack_choice, player)
            clear()
            clear()
            break

        else:

            print("1. Punch\n2. Low Kick\n3. Roundhouse Kick\n4. Takedown\n")
            print(f"{player.name}'s Status: {player.status}")
            print(f"{npc.name}'s Status: {npc.status}")
            attack_choice = validate_menu_selection(1, 4)
            if attack_choice == 'q':
                print("This will completely exit the game... are you sure?")
                print("Press 'q' again to quit or '1' to continue.")
                exit_choice = validate_menu_selection(1, 1)
                if exit_choice == 'q':
                    quit()
                else:
                    continue
            convert_offense_choice(attack_choice, player)
            clear()
            clear()
            break
        