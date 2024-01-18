def biggest(a, b):
    if a > b:
        print(a, 'is bigger than', b)
        return a
    else:
        print(b, 'is bigger than', a)
        return b
    
def max_value(a, b, c):
    return biggest(c, biggest(a, b))

print(max_value(8, 2, 10))
    