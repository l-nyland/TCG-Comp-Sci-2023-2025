#how to read information from a CSV file

file = open('Primes.csv', 'r' ) 

values = file.read()

file.close()

print(values)

myList = values.split(",")
print(myList)

new_list = [int(x) for x in myList]

print(new_list)





