def evens(numbers):
    
    new_list = []
    
    for x in numbers:
        if x % 2 == 0:
            new_list.append(x)
            
    return new_list

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(evens(array))