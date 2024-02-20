mylist = [3, 7, 1, 9, 4, 6, 10]

mylist.sort()

print(mylist)

length = len(mylist)

if length % 2 == 0:
    middle_plus_one = length//2
    x = middle_plus_one
    
    median = ( mylist[x-1] + mylist[x] )/ 2
    
else:
    middle = length // 2
    median = mylist[middle]

print("the median is: ", median)
    
    
    

