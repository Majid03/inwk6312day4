#Task 1: Create a function to modify a list (Do not return a list back)
my_number = 5

def mod_list(my_number):
    """ This takes in a list and modifiys it in place"""
    if isinstance(my_number,int):
        return my_number * 2
    else:
        print ("Please give me a list")
        return None

#The function call
my_number = mod_list(my_number)

