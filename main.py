import os
from fighter_classes import *
from fight import fight
from in_game_manual import in_game_manual
from player_choices import player_choices
from update_health_bars import update_health_bars
from validate import *

clear = lambda: os.system('clear')

def main():  
    
    while True:

        clear()

        while True:
            user_name = input("Enter your name. It must have 4 characters min, 10 characters max: ")
            if input_length_within_range(user_name, 4, 10) == True:
                break
            else:
                print("Either too little or too many characters!!!")

        my_fighter = fighter(user_name)
        npc_fighter = npcFighter("Robot Wrangler")
        npc_fighter.random_name()

        clear()
        clear()

        while True:
            clear()
            clear()
            print(f"Welcome to Line Combat, {my_fighter.get_name()}! The fighting game that requires lots of luck and a little skill.")
            print("\n\n\n\n")
            print(f"Your opponent will be: 'The {npc_fighter.get_name()}'")
            print("1. Start")
            print("2. View Manual")
            print("3. Change Your Name")
            print("Q. Quit")
            play_choice = validate_menu_selection(1, 3)
            if play_choice == 'q':
                    print("This will completely exit the game... are you sure?")
                    print("Press 'q' again to quit or '1' to continue.")
                    exit_choice = validate_menu_selection(1, 1)
                    if exit_choice == 'q':
                        quit()
                    else:
                        continue
            elif play_choice == 1:
                fight(my_fighter, npc_fighter)
                
                clear()
                clear()

                print("Would you like to fight again, but against a new bot???")
                print("Enter '1' to play again, and 'q' to quit to the main menu.")
                menu_choice = validate_menu_selection(1, 1)
                if menu_choice == 'q':
                    continue
                else:
                    npc_fighter.random_name()
                    fight(my_fighter, npc_fighter)
                
                clear()
            elif play_choice == 2:
                in_game_manual()
            elif play_choice == 3:
                while True:
                    clear()
                    my_fighter.name = input("Enter your name. It must have 4 characters min, 10 characters max: ")
                    if input_length_within_range(my_fighter.get_name(), 4, 10) == True:
                        break
                    else:
                        print("Either too little or too many characters!!!")

main()

