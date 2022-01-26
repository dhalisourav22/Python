#Zip function basically combine two or more iterator as a tuple. And return zip object.
#zip(iterator1, iterator2, iterator3,...)

#The iterators have same number of item.
id = [337,342,350]
name = ["Sourav","Shihab","Juthi"]
x = zip(id, name)                 #This is return zip type object. We can directly use list here Instead of variable.
print(list(x))                    #The answer we want in to as a list of tuple.


#Whene the iterator have different number of items.
id = [337,345]
name = ["Sourav","Shihab","Juthi"]
x = zip(id , name)
y = zip([337,345],["Sourav","Shihab","Juthi"])   #We can use this way. by directly put list into the zip function.
z = list(zip(id,name))                           #That way. we can directly change the type of the zip function from zip object to list.

print(list(x))
print(list(y))
print(z)                                         #Because this z variable already converted into a list type from zip object


#String as a iterator.
id = [337,333,345]
name = ["Sourav","Nishad","Shihab"]
x = zip(id, name, "BAB")
print(tuple(x))                                  #Here we gate the zip object as a tuple.