from update_health_bars import update_health_bars
from convert_choices import *
import os

clear = lambda: os.system('clear')

def player_choices(player, npc):

    if player.status == "Broken Knuckles":
        print("1. Low Kick\n2. Roundhouse Kick\n3. Takedown\n\n")
        print(f"{player.name}'s Status: {player.status}")
        print(f"{npc.name}'s Status: {npc.status}")
        attack_choice = int(input("choose your offensive move: "))
        convert_offense_choice(attack_choice, player)
        
        clear()

    elif player.status == "Broken Shin":

        print("1. Punch\n2. Takedown\n\n")
        print(f"{player.name}'s Status: {player.status}")
        print(f"{npc.name}'s Status: {npc.status}")
        attack_choice = int(input("choose your offensive move: "))
        convert_offense_choice(attack_choice, player)
        
        clear()

    else:

        print("1. Punch\n2. Low Kick\n3. Roundhouse Kick\n4. Takedown\n\n")
        print(f"{player.name}'s Status: {player.status}")
        print(f"{npc.name}'s Status: {npc.status}")
        attack_choice = int(input("choose your offensive move: "))
        convert_offense_choice(attack_choice, player)
        
        clear()