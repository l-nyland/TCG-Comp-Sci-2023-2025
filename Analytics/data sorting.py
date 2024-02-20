data = [1, -4, 10, 3, 6, -3]

data.sort()

print(data)

for item in data:
    if item < 0:
        data.remove(item)
        
print(data)

#why does this not remove the -3?
#can you edit it so that it does remove the -3?
