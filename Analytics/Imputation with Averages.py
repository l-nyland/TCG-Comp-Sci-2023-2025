#Replacing with averages
data = [1, -4, 10, 3, 6, -3]

total_correct =  0
count_correct = 0

print('OG Data:', data)

#find the average of the non-faulty data:
for i in data:
    if i >= 0:
        total_correct = total_correct + i
        count_correct = count_correct + 1
        
print(total_correct)
print(count_correct)
average = total_correct / count_correct
print(average)
    
#replace the faulty data with the average

i = 0

for x in data:
    if data[i] < 0:
        data[i] = average
    i = i + 1
    
print('Cleaned data:', data)
    


        





