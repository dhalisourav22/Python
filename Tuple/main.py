#When we need to multiple item to save in a single variable, this variable is called tuple.
#We can not direactly update any tuple.(We can only do this by using list.)
thisTuple = ("Apple","Banana","Cherry")
thisTuple1 = ("A","b",True,4)                                    #We can use different data type in tuple.
thisTuple2 = ("x",)                                              #Single item in a tuple, for that reason an extra coma use after this item.
thisTuple3 = tuple(("X","Y","Z"))                                #This tuple() method help to create a tuple.
thisTuple4 = (("Apple","Banana"),("Cherry","Mango"),5,(4,8,6))   #This is an 2D Tuple.


#Type of a tuple.
print("Type is :",type(thisTuple))

#length of a tuple.
print("Length is :",len(thisTuple))

#Printing tuple.
print(thisTuple)                                              #printing as a tuple.
print("The 1 index item is :",thisTuple[1])
print("The 2D tuple 1,1 index is :",thisTuple4[1][1])
print("printing tuple by negative indexing :",thisTuple[-1])
print("We can tell the range of print :",thisTuple[0:2])      #printing as a tuple.(We can use negative index and blank index also here).

#update in a tuple(this is only happend by help of list. Because tuple dose not support updation.)
x = ("Apple","Banana","Cherry")
y = list(x)
y[1]= "Mango"              #This is change the value of index 1.
x = tuple(y)
print("After updation of tuple :",x)


x = ("Apple","Banana","Cherry")
y = list(x)
y.append("Mango")           #add an item in the last of the list or we can say last of the tuple.
x = tuple(y)
print("After updation of tuple :",x)


x = ("Apple","Banana","Cherry")
y = list(x)
y.remove("Apple")              #This is remove the specific item.
x = tuple(y)
print("After updation of tuple :",x)


x1 = ("Apple","Banana","Cherry")
del x1
#print(x1)      #This is give error. because the x1 dose not exist.


#join tuple
x = ("Apple","Banana","Cherry")
y = ("Mango",)
x = x+y                        #This is exactly work like number 32 line. Because there y has only one item.
print("After joining two tuple :",x)

x =(1,2,3,4)
x = x*3                       #This is repeat the x tuple for 3 time.
print(x)

#For loop for traversing.
print("The Items : ")
for x in thisTuple3:
    print(x,end=" ")

print("\nThe Items : ")
for x in range(len(thisTuple3)):
    print(thisTuple3[x],end=" ")

print("\nThe Items : ")
i =0
while i<len(thisTuple3):
    print(thisTuple3[i])
    i+=1

