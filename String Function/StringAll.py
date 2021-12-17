txt1 = "Hello"
print(txt1+"\n")

txt2 = "My name is Sourav Dhali"
print(txt2+"\n")

txt3 = """"My name is Sourav Dhali.
I love my country and
My country name is Bangladesh"""
print(txt3+"\n")

txt4 = '''My name is Sourav Dhali.
I love my country and
My country name is Bangladesh'''
print(txt4+"\n")


#String's are array of character.
txt5 = "Bangladesh"   #Indexing start from 0.
print("Number 1 Index value is : ",txt5[1]+"\n")

#printing each character of string by iterator.
txt6 = "Bangladesh"
print("Here we go for iterator : ",end="")   #this end is define that,how the line will be end. By defult every print take a new line.
for x in txt6:
    print(x,end="\n\t\t\t\t\t\t  ")


#checking the length of the string.
print("\nThe length of the String is : ",len(txt6))  #every print function take a new line after it call.

#is any sub-string and character containing or not in the main string.(This is case sensative.)
txt7="The name of our country is Bangladesh."
print("\nIs Bangladesh Contain in \"txt7\" variable? ","Bangladesh" in txt7)
print("Is not USA Contain in \"txt7\" variable? ","USA" not in txt7)

#Slicing of string. Syntex : variableName[startingPositon : endingPosition]
print("\nSlicing String:")
print(txt6[2:5])  #indexing start from o. end_position is not included.
print(txt6[:5])   #start with begening. means postion 0.
print(txt6[2:])   #end to the last of string.
print(txt6[-5:-2])

#Some built in function.
print("\nMaking Uppercase : ",txt6.upper())
print("Making Lowercase : ",txt6.lower())
print("Replacing character or string : ",txt6.replace("B","K"))
print("Here we use spilt function(we can fixed a separator by this function) : ",txt7.split(" "))  #This is return a list.

#concat strings.
firstName ="Sourav"
lastName ="Dhali"
fullName = firstName+" "+lastName
print("\nThe name of a student is : "+fullName)   #we can use either + or , for string. but different data type we have string formation method. or we can simplay use ,.
print("The name of a student is : ",fullName)     #coma(,) take's an extra space.


#Formating String.
age =23
#print("\nMy age is : "+age)   #This is worng we can not combain a string and number by this way.
print("\nMy age is : ",age)    #This way we can do this.

#we can use format() function for this formationg any string.
print("My age is : {}".format(age))

txt8 = "My age is : {}"       #use via a variable.
print(txt8.format(age))

quantity = 3
itemNo = 567
price = 49.95
myOrder ="I want {} pieces of item {} for {} dollar's."
print(myOrder.format(quantity,itemNo,price))

myOrder ="I want to pay {2} dollars of {0} prices of item {1}."   #we can specify by giving index.
print(myOrder.format(quantity,itemNo,price))

print("I want to pay {2} dollars of {0} prices of item {1}.".format(quantity,itemNo,price))  #without using variable.

#we do this by not using format() function.
print(f"I want to pay {price} dollars of {quantity} prices of item {itemNo}.")  #here we use a f, before the double quotes.
#we can do some simple math also here.
num1 = 30
num2 = 20
print(f"Sum is : {num1}+{num2} = {num1+num2}")