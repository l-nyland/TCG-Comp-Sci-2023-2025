def unique(numbers):
    new_list = []
    
    for x in numbers:
        
        if x not in new_list:
            new_list.append(x)
           
    return new_list

array = [1, 2, 3, 3, 3, 3, 4, 5]

print(unique(array))