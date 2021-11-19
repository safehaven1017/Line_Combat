from deal_attacks import deal_attacks
from fighter_classes import fighter
from fighter_take_damage import fighter_take_damage
from update_health_bars import update_health_bars
import os

# THIS FUNCTION WILL COMPARE BOTH FIGHTER'S OFFENSE AND DEFENSE. IT WILL RETURN TRUE IF THE FIGHTER PASSES A DEFENSE CHECK

clear = lambda: os.system('clear')

def defense_check(defender, attacker):
    
    clear()
    clear()
    
    # IF FIGHTER_1 PICKS "PARRY" IN THE RIGHT OCCASION, DAMAGE IS MITIGATED
    if defender.defense == "Parry" and attacker.offense == "Punch":
        update_health_bars(attacker, defender)
        print(f"{defender.get_name()} parried {attacker.get_name()}'s punch! {defender.get_name()} takes no damage!")
        input("Press enter to continue...")
        deal_attacks(defender, attacker)
        return True
    
    # IF FIGHTER 1 PICKS "KICK CHECK" IN THE RIGHT OCCASION, MOST DAMAGE IS MITIGATED AND APPLIES "FRACTURED SHIN" ON THE ATTACKER
    elif defender.defense == "Kick Check" and attacker.offense == "Low Kick":
        if defender.health > 3:
            fighter_take_damage(defender, 3)
        else:
            defender.health = 1
        fighter_take_damage(attacker, 5)
        attacker.debuff_flag = 0
        update_health_bars(attacker, defender)
        print(f"{defender.get_name()} checked {attacker.get_name()}'s low kick with a kick check!") 
        print(f"{defender.get_name()} takes a little damage, but {attacker.get_name()} took 5 damage and fractured their shin!") 
        print(f"{attacker.get_name()} has reduced mobility next round...\n\n")
        attacker.status = "Broken Shin"
        input("Press enter to continue...")
        deal_attacks(defender, attacker)
        return True

    # IF FIGHTER_1 PICKS "LEG CATCH" IN THE RIGHT OCCASION, DAMAGE IS MITIGATED AND GETS A "LEG SWEEP"
    elif defender.defense == "Leg Catch" and attacker.offense == "Roundhouse Kick":
        fighter_take_damage(attacker, 7)
        attacker.debuff_flag = 0
        update_health_bars(attacker, defender)
        print(f"{defender.get_name()} caught {attacker.get_name()}'s kick! {defender.get_name()} takes no damage,")
        print(f"and swept {attacker.get_name()} for 7 damage! {attacker.get_name()} will be taken down next round.")
        attacker.status = "Taken Down"
        input("Press enter to continue...")
        return True

    # IF FIGHTER_1 PICKS "JUDO COUNTER" IN THE RIGHT OCCASION, DAMAGE IS MITIGATED AND GETS A TAKEDOWN
    elif defender.defense == "Judo Counter" and attacker.offense == "Takedown":
        fighter_take_damage(attacker, 7)
        attacker.debuff_flag = 0
        update_health_bars(attacker, defender)
        print(f"{defender.get_name()} performed a judo counter on {attacker.get_name()}'s takedown attempt!")
        print(f"{defender.get_name()} takes no damage, and {attacker.get_name()} takes 10 damage! {attacker.get_name()} is taken down next round instead!")
        attacker.status = "Taken Down"
        input("Press enter to continue...")
        return True

    else:
        return False
    


        
    

            
