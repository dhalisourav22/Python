#List comprehension is the syntex where we create a new list by existing list depends on conditions.
#[expresion for item in list if condition]
#We can use this List comprehension as a filter function or map function.

number = [1,2,3,4,5,6,7,8]
result = [x for x in number if x%2==0]       #This is kind of a filter function work
print("The result is :",result)

#If we want then we can ignore the condition part from the list comprehension.
result = [x+x for x in number]
print(result)