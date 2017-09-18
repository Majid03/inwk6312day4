#Changing a list

my_list = [1,2,3,4,5]

def list_mul(my_list):
    """ This muls the list elements my 5"""
    new_list = []
    if isinstance(my_list,list):
        for index in range(len(my_list)):
            new_list.append(my_list[index] * 5) 
            # I can write that as my_list[index] *= 5
    else:
        print ("gimme a list!!!!")
    return new_list

print(my_list)
my_new_list = list_mul(my_list)
print(my_new_list)
