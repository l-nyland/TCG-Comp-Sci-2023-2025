#Q6 page 203
def sale_price(RRP, discount):

    #discount = int(input('Enter percentage discount'))
    discount = discount / 100
    
    new_price = RRP - (RRP * discount)
    
    return new_price

prices = [10, 10, 15, 18, 25, 30]
discounts = [10, 20, 30, 40, 50, 60]

for i in range(6):
    print(sale_price(prices[i], discounts[i]))
    

