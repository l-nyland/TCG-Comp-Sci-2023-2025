#Deciding Whether To Give a Loan or Not


request = 40000
time = 1
wages = 3500
    
def lender():
    term = time * 12 #calculates how many months the loan will run for
    
    i = 0.0032 #this is the banks current interest rate
    
    save = wages * 0.4
    
    #apply LC Amortisation Formula
    
    monthly_repay = round((request*i*((1+i)**term))/(((1+i)**term)-1))
    
    print('Monthly payments would be', monthly_repay)
    
    if monthly_repay > save:
    
        return 'We cannot give you a loan'
    else:
        
        return 'yes you can have the loan'
    
while time < 7:
    print(lender())
    time+=1
    
    