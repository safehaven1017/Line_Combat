# CREATE HEALTH BAR USING CHARACTERS.
def create_health_bar_left(current_health, max_health):
    # HEALTH REPRESENTED BY THE "l" CHARACTER
    health_string = "l"
    # MISSING HEALTH REPRESENTED BY A SPACE
    missing_health_string = " "
    # WE WILL APPEND CHARACTERS TO THIS STRING
    health_bar_string = ""

    # FOR LOOP THAT APPENDS CHARACTERS TO STRING. ADDED TWO TO RANGE TO FACTOR FOR BRACKETS
    for index in range(max_health + 2):
        # PRINT FIRST BRACKET AT BEGINNING OF LOOP
        if index == 0:
            health_bar_string = health_bar_string + "{"
        # PRINT CURRENT HEALTH
        elif 0 < index < current_health + 1:
            health_bar_string = health_bar_string + health_string
        # PRINT BRACKET AT END OF HEALTH BAR, INDICATED BY "MAX HEALTH + 1" BECAUSE BRACKET TAKES UP FIRST INDEX
        elif index == max_health + 1:
            health_bar_string = health_bar_string + "}"
        # PRINT EMPTY SPACE FOR MIXING HEALTH
        else:
            health_bar_string = health_bar_string + missing_health_string
    
    print()
    print()
    print()
    print(health_bar_string, end = "")


# THE HEALTH BAR ON THE RIGHT USES THE SAME CONCEPT, EXCEPT IT HAS THE "EMPTY SPACE" 
# VARIABLES TO PUSH THE HEALTH BAR TO THE RIGHT. WHEN DESIGNING THE FOR LOOP, PRETEND
# THAT THE NUMBER "EMPTY SPACE" MARKS THE BEGINNING INDEX OF THE LOOP FOR THE BAR.

def create_health_bar_right(current_health, max_health):
    health_string = "l"
    missing_health_string = " "
    empty_space_string = " "
    health_bar_string = ""

    missing_health = max_health - current_health
    empty_space_amount = 41

    for index in range(empty_space_amount + max_health + 2):
        if index < empty_space_amount:
            health_bar_string = health_bar_string + empty_space_string
        elif index == empty_space_amount:
            health_bar_string = health_bar_string + "{"
        elif empty_space_amount < index < empty_space_amount + current_health + 1:
            health_bar_string = health_bar_string + health_string
        elif index == max_health + empty_space_amount + 1:
            health_bar_string = health_bar_string + "}"
        else:
            health_bar_string = health_bar_string + missing_health_string
    
    print(health_bar_string, end = "")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


