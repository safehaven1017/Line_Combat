from random import randint
from update_health_bars import update_health_bars
from fighter_take_damage import fighter_take_damage
import os

clear = lambda: os.system('clear')

def takedown_round(attacker, defender):
    
    clear()

    update_health_bars(attacker, defender)
    print(f"{attacker.get_name()} has {defender.get_name()} on the ground! {attacker.get_name()}")
    print(f"has a 50% chance of performing a successful lock on {defender.get_name()}.")
    print(f"{attacker.get_name()} will do 10 extra damage to {defender.get_name()} if they are successful!")
    input("Press 'enter' to see the results...")

    dice_roll = randint(1, 100)

    clear()

    update_health_bars(attacker, defender)

    if dice_roll < 50:
        print(f"{defender.get_name()} was able to flawlessly escape from {attacker.get_name()}'s hold!")
        print(f"{defender.get_name()} receives no damage.")
        attacker.debuff_flag = 0
        defender.debuff_flag = 0
        attacker.status = "Normal"
        defender.status = "Normal"
        input("Press 'enter' to continue...")
    else:
        fighter_take_damage(defender, 10)
        update_health_bars(attacker, defender)
        print(f"{attacker.get_name()} hurt {defender.get_name()} while in an arm bar!")
        print(f"{defender.get_name()} receives 10 damage!")
        attacker.debuff_flag = 0
        defender.debuff_flag = 0
        attacker.status = "Normal"
        defender.status = "Normal"
        input("Press 'enter' to continue...")
