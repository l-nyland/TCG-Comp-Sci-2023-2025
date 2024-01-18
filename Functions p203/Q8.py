#Q8 page 203

def pet_cost(pet, food):
    
    cost = 0
    kg = (food * 21)/1000
    
    if pet == 'hamster':
        cost = 3 * kg
        
    elif pet == 'cat':
        cost = 5 * kg
    else:
        print('Invalid pet entered')
        
    return cost
    
petq = input('Do you have a hamster or a cat?')
foodq = int(input('How many grams of food do they eat per day?'))

print(pet_cost(petq, foodq))

