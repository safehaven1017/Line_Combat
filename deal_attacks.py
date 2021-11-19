# THIS FUNCTION WILL RUN OF BOTH DEFENSE AND ATTACK CHECKS RETURN FALSE.
# IT WILL PRODUCE A SUCCESSFUL ATTACK FROM ONE FIGHTER TO THE OTHER.

from fighter_classes import fighter
from fighter_take_damage import fighter_take_damage
from update_health_bars import update_health_bars


def deal_attacks(attacker, defender):
    
    # ATTACKER ARGUMENT GOES FIRST
    if attacker.offense == "Punch":
        fighter_take_damage(defender, 5)
        update_health_bars(attacker, defender)
        print(f"{attacker.name} punched {defender.name}! {defender.name} takes 5 damage.")
        input("Press enter to continue...")

    elif attacker.offense == "Low Kick":
        fighter_take_damage(defender, 8)
        update_health_bars(attacker, defender)
        print(f"{attacker.name} low kicked {defender.name}! {defender.name} takes 8 damage.")
        input("Press enter to continue...")

    elif attacker.offense == "Roundhouse Kick":
        fighter_take_damage(defender, 12)
        update_health_bars(attacker, defender)
        print(f"{attacker.name} roundhouse kicked {defender.name}! {defender.name} takes 12 damage.")

        input("Press enter to continue...")

    elif attacker.offense == "Takedown":
        fighter_take_damage(defender, 5)
        update_health_bars(attacker, defender)
        print(f"""{attacker.name} performed a takedown on {defender.name}! 
        {defender.name} takes 5 damage, and must properly defend themselves on the ground next round!""")
        defender.status = "Taken Down"
        input("Press enter to continue...")