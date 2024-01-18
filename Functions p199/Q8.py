#Q8 page 199

def email_check(string):
    
    if len(string) > 8:
    
        if '@' and '.' in string:
            print('This is valid')
        else:
            print('Invalid email address given')
    else:
        print('Invalid email address given')
        
email = input("enter your email")

email_check(email)
        