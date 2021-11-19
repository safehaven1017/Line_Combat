from fighter_classes import *
from create_health_bar import *
import time
import os

clear = lambda: os.system('clear')

testFighter = npcFighter("NPC")
testFighter2 = fighter("Rick")

def animate_health_bar(object_a, damage_a, object_b, damage_b):
    sleep_time = 0.2
    flashing_index_min_a = object_a.health - damage_a
    flashing_index_max_a = object_a.health
    flashing_index_min_b = object_b.health - damage_b
    flashing_index_max_b = object_b.health
    
    for i in range(4):
        if isinstance(object_a, npcFighter) == True:
            clear()
            create_health_bar_left(flashing_index_min_b, flashing_index_max_b)
            create_health_bar_right(flashing_index_min_a, flashing_index_max_a)
    
            time.sleep(sleep_time)
            clear()
        else:     
            clear()
            create_health_bar_left(flashing_index_min_a, flashing_index_max_a)
            create_health_bar_right(flashing_index_min_b, flashing_index_max_b)
            
            time.sleep(sleep_time)
            clear()
        if isinstance(object_a, npcFighter) == True:
            create_health_bar_left(object_b.health, object_b.health)
            create_health_bar_right(object_a.health, object_a.health)
    
            time.sleep(sleep_time)

            
        else:     
            create_health_bar_left(object_a.health, object_a.health)
            create_health_bar_right(object_b.health, object_b.health)
            
            time.sleep(sleep_time)
        

