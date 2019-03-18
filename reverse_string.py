#PROGRAM TO REVERSE A GIVEN STRING
def reverse_string(string):
    str_list = string.split()
    reverse_string = []

    while len(str_list) != 0:
        
        last_element = str_list.pop()
        reverse_string.append(last_element)
    
        

    return(" ".join(reverse_string))

print(reverse_string("type any string over here to be reversed"))

