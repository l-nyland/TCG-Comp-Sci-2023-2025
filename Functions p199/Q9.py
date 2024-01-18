#Q9 page 199

def freq(letter, sentence):
    
    ans = 0
    
    for i in sentence:
        if i == letter :
            ans = ans + 1
        
    print(letter, 'appears', ans, 'times in', sentence)
    
letter = input('Enter a letter')
sentence = input('Enter a sentence')

freq(letter, sentence)
        