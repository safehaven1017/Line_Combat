import os

clear = lambda: os.system('clear')

def in_game_manual():
    clear()
    clear()
    print("""Game is turn based.
Each turn, both players pick an offensive and defensive maneuver. The attack you choose determines the potential damage output, 
and the defense determines the potential damage mitigation. Defenses can also inflict damage, or even inflict special debuffs.

Maneuver manual:
Punching - a simple attack that does little damage (5), but you are punished the least if the opponent picks 
the right defensive maneuver, which is parry. Parry simply removes all damage done by an incoming punch

Low Kicking - an attack that does moderate damage (8). Low Kick is punished by kick check. If someone kick checks successfully, 
they take a reduced amount of only 2 damage, but the opponent gets fractured shin. This means they take 5 extra damage and 
can’t roundhouse kick or low kick on the next turn. If the defender has 2 or less health, they won’t lose health from a 
successful kick check.

Roundhouse Kick - an attack that does high damage (12) but is punished harshly. It is countered by kick catch, which makes the 
opponent immobile on the next turn. The person who catches the kick can get a free leg sweep on the next turn. This does 5 damage, 
and puts the opponent in takedown mode.

Takedown - an attempt to bring your opponent to the ground that has a special affect. If you successfully takedown an opponent they 
receive 5 damage and have to guess between an arm bar or choke hold on the next round. If they guess wrong, they take another 10 damage. 
If they guess right, they won’t receive additional damage. Takedown is countered by judo counter. 
If someone falls victim to a judo counter, they receive 7 damage and are put in takedown mode themself.
""")
    input("Press 'Enter' to go back to the main menu...")
    clear()
    clear()    

