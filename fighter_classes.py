from random import randrange
from create_health_bar import create_health_bar_left


# FIGHTER CLASS. HOLDS HEALTH AND STATUSES FOR PLAYER AND NPC
class fighter(object):
    def __init__(self, name, max_health = 50):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.status = "Normal"
        self.offense = "Punch"
        self.defense = "Parry"
        self.debuff_flag = 0

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health
   
    def get_max_health(self):
        return self.max_health
    
    def get_status(self):
        return self.status


# NPC CLASS. ITS THE SAME AS FIGHTER, BUT INCLUDES RANDOM ROLLS FOR ATTACK AND DEFENSE
class npcFighter(fighter):
    def __init__(self, name, max_health = 50):
        # super.__init__(self, name, max_health = 50)
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.status = "Normal"
        self.offense = "Punch"
        self.defense = "Parry"
        self.debuff_flag = 0
    
    def roll_offense(self):

        if self.status == "Broken Knuckles":
            offensive_list = ["Low Kick", "Roundhouse Kick", "Takedown"]
            random_offense_int = randrange(3)
            self.offense = offensive_list[random_offense_int]
        elif self.status == "Broken Shin":
            offensive_list = ["Punch", "Takedown"]
            random_offense_int = randrange(2)
            self.offense = offensive_list[random_offense_int]
        else:
            offensive_list = ["Punch", "Low Kick", "Roundhouse Kick", "Takedown"]
            random_offense_int = randrange(4)
            self.offense = offensive_list[random_offense_int]
    
    def roll_defense(self):
        defensive_list = ["Parry", "Kick Check", "Leg Catch", "Judo Counter"]
        random_defense_int = randrange(4)
        self.defense = defensive_list[random_defense_int]
        
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health
   
    def get_max_health(self):
        return self.max_health
    
    def get_status(self):
        return self.status
    
    def get_difficulty(self):
        return self.difficulty
    
