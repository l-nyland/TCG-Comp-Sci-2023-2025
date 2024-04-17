#Deciding Whether To Give a Loan or Not

def lender():
    request = int(input('How much do you want to borrow?'))
    time = int(input('How long do you want to take the loan out for (in years)?'))
    wages = int(input('How much is your net monthly salary?'))
    
    term = time * 12 #calculates how many months the 
    
    i = 0.00325 #this is the banks current interest rate
    
    save = wages * 0.4
    
    #apply LC Amortisation Formula
    
    monthly_repay = (request*i*((1+i)**term))/(((1+i)**term)-1)
    
    print('Monthly payments would be', monthly_repay)
    
    if monthly_repay > save:
    
        return 'We cannot give you a loan'
    else:
        
        return 'yes you can have the loan'
    
print(lender())
    
    