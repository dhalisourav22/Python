def thisFunction():
    print("This is a no parameter function")

thisFunction()     #Here We Call The Function.

def add(num1, num2):
    sum = num1 + num2
    print("Sum is :", sum)
add(10, 20)
add(50, 50)
#add(10)                #given error because the function expect 2 argument.
#add(10,20,30)          #given error because the function expect 2 argument.

def studentInfo(name, id, cgpa):
    print("\nSTUDENT INFO : ")
    print("\tName is :", name)
    print("\tId is   :", id)
    print("\tCGPA is :", cgpa)

studentInfo("Sourav", 337, 3.90)               #We should maintain this order.
studentInfo(id=340, name="Xrin", cgpa=4.00)    #Here we break the order. but we say whick parameter value is whick.

#Dafult parameter value.
def myfun(country = "Norway"):
    print("I am from", country)
myfun("USA")
myfun()              #here the deafult value of parameter will be use.

def myfun(name, country = "Norway"):
    print("I am "+name+" from", country)
myfun("Sourav", "USA")
myfun("Shuvo")              #here the deafult value of parameter will be use.

#we can use a list, dictionary etc as a argument.
def thisFun1(food):               #in this function or scope the food variable trat like a list.
    print("\nFood's are :",end=" ")
    for x in food:
        print(x,end=" ,")
fruits = ["Apple","Banana","Cherry"]
thisFun1(fruits)                 #here we use a list as a value

#We can return any value by any function by using return key word.
def add1(num1, num2):
    return num1+num2
sumResult = add1(10,30)          #This function return the sum of those value.
print("\nThe result is :", sumResult)

#We can not creat a function as a empty. that's give error. this error can be ignored by using pass statment.
def thisEmpty():
    pass