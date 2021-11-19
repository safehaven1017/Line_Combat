def convert_offense_choice(number_choice, fighter):

    if fighter.status == "Broken Knuckles":
       
        if number_choice == 1:
            fighter.offense = "Low Kick"
        elif number_choice == 2:
            fighter.offense = "Roundhouse Kick"
        else:
            fighter.offense = "Takedown"

    elif fighter.status == "Broken Shin":
       
        if number_choice == 1:
            fighter.offense = "Punch"
        else:
            fighter.offense = "Takedown"

    else:
        if number_choice == 1:
            fighter.offense = "Punch"
        elif number_choice == 2:
            fighter.offense = "Low Kick"
        elif number_choice == 3:
            fighter.offense = "Roundhouse Kick"
        else:
            fighter.offense = "Takedown"

def convert_defense_choice(number_choice, fighter):
    if number_choice == 1:
        fighter.defense = "Parry"
    elif number_choice == 2:
        fighter.defense = "Kick Check"
    elif number_choice == 3:
        fighter.defense = "Leg Catch"
    else:
        fighter.defense = "Judo Counter"