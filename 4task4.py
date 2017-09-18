# This is a histogram 

def hist(my_string):
    """ This takes a string and goes through each char and counts it in a dict"""
    #check if string
    if not isinstance(my_string,str):
        print ("Gimme a str")
        return None
    #Create an empty dict
    char_count = {}
    #Go through the string
    for my_char in my_string:
        if my_char in char_count:
            char_count[my_char] +=1
        else:
            char_count[my_char] = 1
    return char_count

my_char_count = hist("INWK63122"))

