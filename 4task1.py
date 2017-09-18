#Task 1: Create a function to modify a list (Do not return a list back)

my_list = [1,3,4,5]

def mod_list(some_list):
    """ This takes in a list and modifiys it in place"""
    if isinstance(some_list,list):
        #do something
    else:
        print ("Please give me a list")
        return None

#The function call
mod_list(my_list)
print(my_list)
