#Creation a dictionary.(dictionar did not suport duplicate value. If there any duplicate value, then this will be overwrite.)
thisdict = {
    "Brand" : "Audi",
    "Model" : "Zx3",
    "Year"  :1965
}

#printing the dictionary.
print(thisdict)
print(thisdict["Brand"])
print(thisdict.get("Year"))
print(thisdict.get("Location","This is Not in the Dictionary."))

#Duplicate value.
thisdictDuplicate = {
    "Brand" : "Audi",
    "Model" : "Zx3",
    "Year"  :1965,
    "Year"  :2008,
    "Year"  :2022
}
print("This list after duplicate is : ",thisdictDuplicate)   #Here we only see the year with 2022 because this item overwrite older key with Year.

#printing all keys, values, items by built-in function.
allValues = thisdict.values()
print("The all Values are :",allValues)
allkeys = thisdict.keys()
print("The all Keys are :",allkeys)
allitems = thisdict.items()
print("The all items are :",allitems)

#Containity check of any key by in/not in .
if "Model" in thisdict:                #Return True, because model is in the dictionary.
    print("Yes..! this key is in the dictionary..!")

#adding new items. Items mean a key:value pair.
thisdict["Color"] = "Black"
thisdict.update({"Type":"SUV"})
print("After adding two new items, the Dictionary look's like :",thisdict)

#Changing any item's value of the dictionary.
thisdict["Color"] = "Deep Blue"
thisdict.update({"Brand":"BMW"})
print("After Changing two item of the dictionary, we get :",thisdict)

#length of a dictionary.
print("The length of this dictionary is :",len(thisdict))  #how many item has in the dictionary.

#Showing the type of a dictionary.
print("The type of a dictionary is :",type(thisdict))

#delete items
thisdict.popitem()       #This is delete the last item of the dictionary.
print("After deleting the last item of the dictionary :",thisdict)

thisdict.pop("Model")    #This is delete the specific item of the dictionary.
print("After deleting the 'Model' key from the dictionary :",thisdict )

del thisdict["Year"]     #This is delete the specific item of the dictionary by del keyword.
print("After deleting the 'Year' key from the dictionary :",thisdict )

del thisdict
#print("After Deleting the whole Dictionary :",thisdict)     #This is given error, because this dictionary not exist after delete.

thisdict1 = {            #We create new dictionary.
    "Brand" : "Audi",
    "Model" : "Zx3",
    "Year"  :1965
}
thisdict1.clear()       #This is clear the whole dictionary. this is make the dictionary empty.
print("After clearing the whole dectionary :",thisdict1)        #This is show empty dictionary.

#Copy a dictionary.
thisdict2 = {            #We create another new dictionary.
    "Brand" : "Audi",
    "Model" : "Zx3",
    "Year"  :1965
}
copyditionary1 = thisdict2.copy()         #By copy() method.
copyditionary2 = dict(thisdict2)          #By list() method.
print("Copy Dictionary is :",copyditionary1)
print("Copy andother Dictionary is :",copyditionary2)

#Traversing by loop.
print("The Keys are : ",end="")
for x in thisdict2:
    print(x,end=" ,")

print("\nThe values are : ",end="")
for x in thisdict2:
    print(thisdict2[x],end=" ,")

print("\nThe keys are : ",end="")
for x in thisdict2.keys():
    print(x,end=" ,")

print("\nThe values are : ",end="")
for x in thisdict2.values():
    print(x,end=" ,")

print("\nThe items are : ",end="")
for x,y in thisdict2.items():
    print(f"({x},{y})",end=" ,")

#Nested dictionary.
family = {                            #One way.
    "Child1" : {
        "Name" : "Liana",
        "Age" : 23
    },
    "Child2": {
        "Name": "Xerin",
        "Age": 25
    },
    "Child3": {
        "Name": "Alexa",
        "Age": 21
    }
}
print("\n\nThe nested list is : ",family)


firstChild = {                  #Another way to create nested dictionary.
    "Name": "Liana",
    "Age": 23
}
secondChild = {
    "Name": "Xerin",
    "Age": 25
}
thirdChild = {
    "Name": "Alexa",
    "Age": 21
}

family = {
    "child1" : firstChild,
    "child2" : secondChild,
    "child3" : thirdChild
}
print("The nested list is : ",family)