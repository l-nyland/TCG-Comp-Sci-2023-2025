#Imputation Example

file = open('Random.csv', 'r')

data = file.read()

file.close()

print(data)

new_list = []

for x in data:
    x = int(x)
    new_list.append(x)

print(new_list)
    
print('Numerical list:', list_one)

index = 0

for num in data_list:
    if num < 0:
        data[index] = 'Removed negative value'
    index = index + 1
    
print("New List:", data)

