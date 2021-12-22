#We convert data into one type to another type by using some built-in function.

#int()     - Use for converting into integer data type.
#float()   - Use for converting into float data type.
#str()     - Use for converting into string data type.
#bool()    - Use for converting into boolean data type.

numInt = 10
print(numInt)
print(str(numInt))                 #10 become "10" now.
print(float(numInt),end="\n\n")    #10 become 10.0 now.

numFloat = 10.5
print(numFloat)
print(str(numFloat))               #10.5 become "10.5" now.
print(int(numFloat),end="\n\n")    #10.5 become 10 now

numStr = "100.55"
print(numStr)
print(float(numStr),end="\n\n\n")    #"100.55" become 100.55 now
#print(int(numStr),end="\n\n\n")     #This is not possible. because The string has float value. which can not convert in to a integer.


#We try now bool(). This either return True or False.(First character must be upper case.)
'''None
   False
   Zero number of any numeric data type
   Empty - list, tuple, dictionary, string, bytes, set, renge.
   
Only those are return False in boolean. All other case those will return True. 
'''
#False's :
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}),end="\n\n")

#True's :
print(bool(True))
print(bool(15))
print(bool("Sourav Dhali"))
x="Hello"
y=15
print(bool(x))
print(bool(y))
