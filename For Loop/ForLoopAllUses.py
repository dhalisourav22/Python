#Printing a list by loop.
num=[10,20,45,32,58,45,12,30]
for x in num:                #we can use list, range(not converted list) and string. Which we can iterat.
    print(x,end=", ")        #This loop will run, until the list all item are executed.
print("\b\b.")

#Printing a string by loop. this is iterat depend's on letter.
num1="Sourav"
print("Iterat the string : ",end="")
for y in num1:               #we can directly assign a value in the loop on the place of num1.
    print(y,end=", ")
print("\b\b.")

#We can use range() function to tell how many time the loop will run.
#we write a program, which show the number 0-100
#Technique 1:
num2=list(range(101))        #This is return a list.
for z in num2:               #This num2 is a list of 0-100.
    print(z,end=", ")
print("\b\b.")

#Technique 2:
for m in range(101):         #we can use directly a range function. this is return a sequens or number. That's why we can do this.
    print(m, end=", ")
print("\b\b.")

#Writing a program for : sum of 0-100 number's
sum = 0
for x in range(101):
    sum += x
print("The Sum Of those value is : ",sum)

#writing a program for : 2+4+6+8+....+(n-2)+n
sum = 0
n = int(input("Enter The Last Number Of Your series : "))
for y in range(2,n+1,2):             #range(start,stop,increment)
    sum = sum+y
print("The 2+4+6+8+....+(n-2)+n is : ",sum)

#We can use else statement with loop.
for x in range(6):
    if x==3:
        break             #For this break statement, the else never gone be read.
    print(x,end=", ")
else:
    print("Normally Finished.")

#Pass statement. when we have an empty loop. to skip the error, we can use pass statement.
for x in [0,1,2]:         #We can use direct list for loop.
    pass

#nested Loop.
adj = ["red","bog","green"]
fruits = ["apple","banana","cherry"]

print("\nNested Loop Part1: ")
for x in adj:
    for y in fruits:
        print("\t\t\t\t  ",x,y)


print("\nNested Loop part2: ",end="")
for x in range(len(adj)):
    for y in range(len(fruits)):
        if x==0 and y==0:                 #using this if for designing.
            print(adj[x],fruits[y])
        else:
            print("\t\t\t\t  ",adj[x],fruits[y])