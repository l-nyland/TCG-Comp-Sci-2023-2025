def multiply(numbers):
    
    ans = 1
    
    for x in numbers:
        ans = ans * x
    
    print(ans)
    return ans

array = [8, 2, 3, -1, 7]

multiply(array)