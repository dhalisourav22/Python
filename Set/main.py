#Set is a unordered collection of items. this is unorder, that's why we can't print any item of a set by it's index.
#Set dose not allow duplicated value or item.

thisSet = {"Apple","Banana","Cherry"}
thisSet1 = set(("Mango", "papaya", "Suger"))
thisSet2 = {1,2,3,4,5}
thisSet3 = {"Sourav",337,3.92,True}

#Showing Output. (as a set.)
print(thisSet)                               #this print like random. because a set has no order.
print(thisSet1)

#we can print item by using loop.
print("The set items are :",end=" ")
for x in thisSet:
    print(x,end=" ")

#We can see the type and length of a set like list or tuples.
print("\nThe length of the set is :",len(thisSet))
print("The type of the set is :",type(thisSet))

#Insert item in to a set.(Finaly the set will give items as a random. because set has no order.)
thisSet.add("Mango")
print("After adding a new item :",thisSet)   #the mango not addd last of the set. but the mango add in the set. this is not happenig for set. because there has no order.

#Adding a set with a set.
set1 = {"apple","bannana"}
set2 = {"cherry","mango"}
set1.update(set2)                 #set1 = set1 + set2 ; this type of work happen in here.
print("After adding set1 and set2 into set1 :",set1)

#We can add different type of collection with set by update function.
set3 = {"apple","bannana"}
list1 = ["cherry","mango"]
set3.update(list1)                #we put the sum value into the set called set3. thats why this result become set now.
print("After adding a list with set :",set3)
print("The Type of that :",type(set3))

#Remove spesific item from the set.
print("Before doing any work the set look's like :",thisSet2)
thisSet2.remove(2)                                   #This instruction remove 2 from the set.
print("After removing 2 from the set :",thisSet2)    #Note: If the item to remove does not exist, remove() will raise an error.
thisSet2.discard(3)                                  #This instruction remove 3 from the set.
print("After removing 3 from the set :",thisSet2)    #Note: If the item to remove does not exist, discard() will NOT raise an error.

#We can clear all item in the set by using clear() method.
thisSet2.clear()
print("After clearing the whole set :",thisSet2)     #This will return empty set of items.

#We can delete the whole set by using del key word.
del thisSet2    #now thisSet2 dose not exist in the total program. that's why next time if we want to print thisSet2 then it will give error.

#Unior, Intersection and Symetric differance.
num1 = {1,2,3,4,5}
num2 = {4,5,6,7}

print("The union by operator is :",num1 | num2)              #We can do this by built-in function. Which is given in W3 website( Python > Python Sets > Join Sets).
print("The intersection by operator is :",num1 & num2)
print("The differance by operator is :",num1 - num2)