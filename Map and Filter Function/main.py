#By using map and filter function we can pass any iterator's item one by one into a function.
#map(function,iterables)
#filter(function,iterables)
#The function will either traditional function or lambda function.
#The work of map and filter function ar same. but the general use we use the map function. and the use of filtering any collection item we use filter function.

def myfun(n):
    return n*n
num =[1,2,3]                    #We can use variable to store the list or collection.
x= list(map(myfun,num))         #This is return 3 value. 1*1=1 2*2=4 and 3*3=9. thats come like map object. that's why we convert the value into a list type.
print(x)

def myfunc(n):
    return n*n
x= list(map(myfunc,[1,2,3]))    #Here We direct using collection.
print(x)

def myfunct(x,y):
    return x*y
x = list(map(myfunct,[1,2,3],[3,1,2]))
print(x)


def myfunction(x):
    if x<18:
        return x
z = list(filter(myfunction,[10,12,19]))    #We can do it by map function.
print(z)

number = [1,2,3,4,5,6,7,8]
result = list(filter(lambda b : b%2==0,number))     #Here we use lambda function as a function under filter function.
print(result)