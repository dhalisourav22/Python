#creating a stack by using list. We can use all list operation here. because this is a list. 
thisStack = ["Sourav","Juthi","Sumi","Shuvo","Mehedi"]

#push an item.
thisStack.append("Kamal")
print("After adding an item into the stack :",thisStack)

#pop an item.
thisStack.pop()
print("After pop :",thisStack)
print("The top item is :",thisStack[-1])
print("We have :",len(thisStack),"item's.")         #this is show the number of item the stack have.
thisStack.pop()
thisStack.pop()
thisStack.pop()
thisStack.pop()
thisStack.pop()
print("After pop 5 time :",thisStack)

if not thisStack:                   #if the collection is empty then it will return True.
    print("The stack is empty.!")
