def check(array, num):
    
    count = 0
    
    for i in array:
        if i == num:
            count = count + 1
    
    return count

numbers = [1, 5, 7, 3, 7, 8]

print(check(numbers, 5))
print(check(numbers, 7))
print(check(numbers, 10))