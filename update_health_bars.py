from create_health_bar import *
from fighter_classes import *

def update_health_bars(fighter_a, fighter_b):
    if isinstance(fighter_a, npcFighter) == True:
        create_health_bar_left(fighter_b.health, fighter_b.max_health)
        create_health_bar_right(fighter_a.health, fighter_a.max_health)
    else:
        create_health_bar_left(fighter_a.health, fighter_a.max_health)
        create_health_bar_right(fighter_b.health, fighter_b.max_health)
