#Q7 page 203

def temp_converter(temp, scale):
    
    if scale == 'F':
        new_temp = (temp - 32) * 0.5666
    elif scale == 'C':
        new_temp = (temp * 1.8) + 32
    else:
        print('Invalid scale given')
        
    return new_temp

print(temp_converter(50, 'C'))
print(temp_converter(102, 'F'))
print(temp_converter(37, 'C'))
print(temp_converter(20, 'F'))