def final_amount(principal, interest, years):
    f = principal*((1+interest))**years
    return f


test = final_amount(1000, 0.04, 10)
print(test)

test2 = final_amount(2000, 0.04, 10)
print(test2)