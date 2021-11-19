# THIS FUNCTION WILL CREATE AND RETURN A LIST FILLED WITH A 
# DESIGNATED STRING, 'STRING'. THE LENGTH OF THE STRING IS 
# DETERMINED BY 'NUM'.
def populate_list_with_char(string, num):
    populated_list = []
    for index in range(num):
        populated_list.append(string)

    return populated_list