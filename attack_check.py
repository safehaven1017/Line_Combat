from fighter_take_damage import fighter_take_damage
from update_health_bars import update_health_bars

# THIS FUNCTION WILL RUN IF DEFENSE CHECKS FOR BOTH FIGHTERS RETURN FALSE. 
# WHEN BOTH FIGHTERS USE THE SAME ATTACK, THEY HAVE A SPECIAL INTERACTION.
# IF BOTH FIGHTERS USE THE SAME ATTACK, THE FUNCTION WILL RETURN TRUE.


def attack_check(attacker_a, attacker_b):
    if attacker_a.offense == attacker_b.offense and attacker_a.offense == "Punch":
        fighter_take_damage(attacker_a, 5)
        fighter_take_damage(attacker_b, 5)
        update_health_bars(attacker_a, attacker_b)
        print("Both fighters attempted to punch each other! They hit each others knuckles, ouch!") 
        print("They both take 5 damage and decide not to punch next round...")
        attacker_a.status = "Broken Knuckles"
        attacker_b.status = "Broken Knuckles"
        attacker_a.debuff_flag = 0
        attacker_b.debuff_flag = 0
        input("Press enter to continue...")
        return True
    
    elif attacker_a.offense == attacker_b.offense and attacker_a.offense == "Low Kick":
        fighter_take_damage(attacker_a, 7)
        fighter_take_damage(attacker_b, 7)
        update_health_bars(attacker_a, attacker_b)
        print("Both fighters threw low kicks and hit each others shins! Ouch!!!! Both fighters take 7 damage.")
        print("They also decide not to kick next round.")
        attacker_a.status = "Broken Shin"
        attacker_b.status = "Broken Shin"
        attacker_a.debuff_flag = 0
        attacker_b.debuff_flag = 0
        input("Press enter to continue...")
        return True
    
    elif attacker_a.offense == attacker_b.offense and attacker_a.offense == "Roundhouse Kick":
        update_health_bars(attacker_a, attacker_b)
        print("Both fighters threw roundhouse kicks! It looked really cool, but no one was hit...")
        input("Press enter to continue...")
        return True
    
    elif attacker_a.offense == attacker_b.offense and attacker_a.offense == "Takedown":
        fighter_take_damage(attacker_a, 10)
        fighter_take_damage(attacker_b, 10)
        update_health_bars(attacker_a, attacker_b)
        print("Both fighters decided to perform takedowns! Both fighters struggled each other to")
        print("the ground. They hurt each other a lot during the tussle. Both fighters take 10 damage!")
        input("Press enter to continue...")
        return True
    
    else:
        return False