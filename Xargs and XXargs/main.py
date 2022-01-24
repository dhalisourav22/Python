#Xargs
#If the number of arguments is unknown, add a * before the parameter name. This paramenter behave line a tuple

def student(*details):
    print(details)          #This print like a tuple. because the details is a tuple with value 337,"Sourav",3.909.
student(337,"Sourav",3.909)

def my_student(*stuDetails):
    print("\nId is : ",stuDetails[0])
    print("Name is : ",stuDetails[1])
    print("CGPA is : ",stuDetails[2])
my_student(337,"Sourav",3.909)

#Sum of number.
def add(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum          #This is return the value of sum.

print("\nThe Sum is : ",add(10,20))
print("The Sum is : ",add(10,20,30))
print("The Sum is : ",add(10,20,30,40))


#XXargs
#If the number of keyword arguments is unknown, add a double ** before the parameter name. and this act like a dictionary.
def my_function(**kid):
    print("The las name of the kid is : ", kid["lastName"])
my_function(firstName = "Oly" , lastName = "Vera")


