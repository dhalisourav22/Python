#There are Four type's of collection in python. 1.List  2.Tuple  3.Set  4.Dictionary

myList = ["Sourav", "Sumi","Shuvo","Sumon"]
myList1 = [10,20,15,25,30,12]
myList2 = ["Sourav",337,3.909,23,True]    #We can add different data type in a list.
myList3 = ["Sourav", "Sumi","Shuvo","Sumon","Sourav","Juthi"]  #List can contain duplicate item's also.

#Printing Full List.
print("This list is : ",myList)
print("This list of duplicate item's is : ",myList3)

#Printing By Specified index.
print("The first Index value of myList is :",myList[0])
print("The negative Index value of myList is :",myList[-1])
#Printing By Range.
print("The value of 1 and 2 index of the list : ",myList[1:3])  #This is return as a list.
print("The value of 0,1 and 2 index of the list : ",myList[:3])
print("The value of 1,2 and 3 index of the list : ",myList[1:])
print("The value of -3 and -2 index of the list : ",myList[-3:-1])

#printing any specified item's index:
print("The index of Sumi is : ",myList.index("Sumi"))

#Item Exist or not.
print("\nExam Result : ",end="")
if "Sumi" in myList:                 #Return's True.
    print("Sumi, pass the exam.")
if "Juthi" not in myList:            #Return's True.
    print("\t\t\t  Juthi, is not pass in the exam.")

#Checking the type of list.
print("\nThe Type Of myList is : ",type(myList))

#Geting Length of any list.
print("The Number of Item's in the list is : ",len(myList))

#replaceing item's in the list.
myList[1] = "Supti"  #Supti replace Sumi from the list.
print("After replacing Sumi by Supti : ",myList)

myList[1:3]=["Sweet","Rafshan"]   #we replace two item Supti and Shuvo by Sweet and Rafshan.
print("After replacing Supti and Shuvo : ",myList)

myList[1:3]=["Mehedi"]   #we replace two item Sweet and Rafshan by Mehedi.
print("After replacing Sweet and Rafshan : ",myList)  #This is decrease The list size.

myList[1:2]=["Suhana","Maumita"]   #we replace one item Mehedi by Suhana and Maumita.
print("After replacing Mehedi : ",myList)  #This is Increase The list size.


#inserting item by insert() method.
myList.insert(0,"Akash")              #without replacing.
print("After inserting Akash in the O index of list : ",myList)

#Insert item in the last of the list.
myList.append("Niloy")
print("After inserting Niloy in the list by append method : ",myList)

#Joining two list.
myList4 = myList+myList3
print("After Joining two List by '+' operator : ",myList4)

myList.extend(myList3)
print("After Joining two List by built in function called extend : ",myList)

#Remove Specified item's:
myList.remove("Sourav")
print("After removing Sourav from the list : ",myList)      #This remove Function remove only one time Sourav. Not all Sourav from the list.

#Removed specified index item.
myList.pop(0)
print("After Removing the 0 indexed item : ",myList)

del myList[1]
print("After Removing the 1 indexed item : ",myList)

#Remove the top item from the List.
myList.pop()
print("After Removing the Top item from the list : ",myList)

#Delating Full List.
del myList
print("myList is deleted, if we use farther this myList then this give us error.")

#Clear Full List. make a list empty.
myList4.clear()
print("After Clearing a list it's look like : ",myList4)

#We can travers a list by a loop.
print("A list traversing looks like : ",end="")
i=0
while i<len(myList3):
    print(myList3[i],end=", ")
    i+=1

#Sort a list.
myList3.sort()
print("\nAfter Sorting(Ascending) The myList3 : ",myList3)

myList1.sort(reverse=True)
print("The reverse sort looks like : ",myList1)

#Copying a list.
myList5 = myList1.copy()
print("After Copy we see myList5 as : ",myList5)

myList6 = list(myList3)
print("After Copy we see myList6 as : ",myList6)

#counting item. That how many this item the list have.
print("The number of Sourav in the class is : ",myList3.count("Sourav"))