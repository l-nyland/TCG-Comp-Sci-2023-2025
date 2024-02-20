mylist = [3, 7, 1, 9, 4, 6]

mylist.sort()

print(mylist)

length = len(mylist)
#This will be used to see how many items are in the list

#next step will be to check if there is an even or odd number in the list
#if it the number is divisible by 2 with no remainder, it is even
#if not, it must be odd

if length % 2 == 0: #checks if the remainder is 0
    #list has an even amount of numbers:
    middle_plus_one = length//2 #finds the posistion of the first of the middle numbers
    x = middle_plus_one #renames for easiness
    
    median = ( mylist[x-1] + mylist[x] )/ 2
    #takes our two middle numbers, and finds the mean of them
    
else:
    #list has an odd amount of numbers
    middle = length // 2 #finds the position of the middle
    median = mylist[middle]

print("the median is: ", median)
    
    
    

