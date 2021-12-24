#This function return a sequence of number.
#Syntax : range(start,stop,incrementStep)   #Stop point is not inclued in the range. by default start's with 0 and by default incrementStep is 1.

list1 = list(range(11))    #This is return a list which has 0-10.
print(list1)

list2 = list(range(10,21))
print(list2)

list3 = list(range(10,21,2))    #This is increment by 2.
print(list3)

#We cant store a sequence of number in to a variable. We must convert it into a list by list() method(not mandetory for loop) then we can print the list to show the output.
