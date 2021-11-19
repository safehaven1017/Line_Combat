# VALIDATE USER INPUT WHEN SELECTING NUMERICAL OPTIONS FROM A MENU

def validate_menu_selection(min, max):
    while True:
        
        # GIVES USER THE OPTION TO CHOOSE A MENU ITEM OR QUIT OUT OF LOOP
        menu_input = input("Enter your choice here: ")
        # DETECTS WHETHER OR NOT USER ENTERS "Q" FOR QUIT OR CHOOSES A NUMBER
        if menu_input.isnumeric() == True or menu_input.lower() == "q":
            
            # FOR NUMERICAL INPUTS
            if menu_input.lower() != 'q':
                
                # RETURNS INPUT IF NUMERICAL INPUT IS WITHIN RANGE
                if int(min) <= int(menu_input) <= int(max):
                    return int(menu_input)
                
                # ERROR HANDLING FOR USER CHOOSING NUMBER OUTSIDE OF RANGE
                else:
                    if min == max:
                        print(f"\nInvalid number. Number must be {min}.")
                    else:
                        print(f"\nInvalid number. Choose options between {min} and {max}.\n")
            
            # RETURNS INPUT WHEN USER TYPES "Q" OR "BACK" KEY, OR WHEN SELECTING AVAILABLE OPTION
            else:
                return menu_input.lower()
        else:
            print("\nInvalid entry. Try again...\n")

def input_length_within_range(string, min, max):
    if min <= len(string) <= max:
        return True

