from random import randint
from update_health_bars import update_health_bars
from fighter_take_damage import fighter_take_damage
import os
from animate_health_bar import animate_health_bar

clear = lambda: os.system('clear')

def takedown_round(attacker, defender):
    
    clear()
    clear()

    update_health_bars(attacker, defender)
    print(f"{attacker.get_name()} has {defender.get_name()} on the ground! {attacker.get_name()}")
    print(f"has a 50% chance of performing a successful lock on {defender.get_name()}.")
    print(f"If {attacker.get_name()} has the advantage, they'll have a better chance of winning!")
    print(f"{attacker.get_name()} will do 10 extra damage to {defender.get_name()} if they are successful!")
    input("Press 'enter' to see the results...")

    if attacker.advantage == True:
        dice_roll = randint(25, 100)
    else:
        dice_roll = randint(1, 75)

    clear()
    clear()

    

    if dice_roll < 50:
        clear()
        clear()
        update_health_bars(attacker, defender)
        print(f"{defender.get_name()} was able to flawlessly escape from {attacker.get_name()}'s hold!")
        print(f"{defender.get_name()} receives no damage.")
        attacker.debuff_flag = 0
        defender.debuff_flag = 0
        attacker.status = "Normal"
        defender.status = "Normal"
        input("Press 'enter' to continue...")
    else:
        
        animate_health_bar(attacker, 0, defender, 10) 
        fighter_take_damage(defender, 10)
        clear()
        clear()
        update_health_bars(attacker, defender)
        print(f"{attacker.get_name()} hurt {defender.get_name()} while in an arm bar!")
        print(f"{defender.get_name()} receives 10 damage!")
        attacker.debuff_flag = 0
        defender.debuff_flag = 0
        attacker.status = "Normal"
        defender.status = "Normal"
        input("Press 'enter' to continue...")
