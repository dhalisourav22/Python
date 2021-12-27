#input = 10 20 30 40
#output = Sum of those number is : 100

userString = input("Enter The String Of Number : ")    #taking input as a string.
userString = userString.split(" ")                     #distributed those string. Here the userString is become a list.
sum = 0         #Using For Addition.

for x in userString:
    sum = sum + int(x)             #because, here x is a string type of data.
print("Sum of those number is :",sum)