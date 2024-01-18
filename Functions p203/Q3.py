#Q3 page 203

def spaces(string):
    
    count = 0
    
    for i in string:
        if i == ' ':
            count = count + 1
    return count

text = input('Enter a sentence')

print(spaces(text))