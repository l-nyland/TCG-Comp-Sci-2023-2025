#Q4 page 203

def divide_check(a, b):
    ans = a % b
    
    #print(ans)
    
    if ans == 0:
        return True
    else:
        return False

print(divide_check(9, 3))