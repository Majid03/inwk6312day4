# This is a histogram 

def hist(my_string,char_count):
    """ This takes a string and goes through each char and counts it in a dict"""
    #check if string
    if not isinstance(my_string,str):
        print ("Gimme a str")
        return None
    #Go through the string
    for my_char in my_string:
        if my_char in char_count:
            char_count[my_char] +=1
        else:
            char_count[my_char] = 1
    return char_count

def print_hist(my_hist):
    """ This prints the hist """
    if not isinstance(my_hist,dict):
        print ("Gimme a dict")
        return None 
    else: 
        for key in my_hist:
            print ( str(key) + " -> " + str(my_hist[key]))

        
