#1+2+3+4+....+(n-1)+n
n = int(input("Enter the number : "))
startingNumber = 1
sum = 0
while startingNumber<=n:
    sum+=startingNumber
    startingNumber+=1
print(f"The sum is : {sum}")


#2+4+6+....+(n-2)+n
n = int(input("Enter the number : "))
startingNumber = 1
sum = 0
while startingNumber<=n:
    sum+=startingNumber
    startingNumber+=2
print(f"The sum is : {sum}")