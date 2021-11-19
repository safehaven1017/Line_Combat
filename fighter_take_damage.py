def fighter_take_damage(victim, damage):
    if victim.health - damage > 0:
        victim.health = victim.health - damage
    else: 
        victim.health = 0
    
