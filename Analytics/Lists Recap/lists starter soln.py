values = [3, 7, 1, 8, 2, 10, 6]


values.append(4)
print(values)

values.sort()

print(values)

print(values[1])
print(values[4])
print(values[5])

newlist = []

for x in values:
   sq = x**2
   newlist.append(sq)
    
print(newlist)
    



