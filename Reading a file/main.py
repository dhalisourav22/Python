file = open("NewText.txt","r")      #Here first parameter is the file location(If the file is not the same directiory), file name(if the file is same directory). But whatever we can do, we must need double quotes behaing and after the name or location.
                                    #Here Second parameter r means we can only read. w means we can only write. r+ means we can do both read and write.
print(file.readable())              #This is check the file readable or not!
print(file.writable())              #This is check the file writable or not!

#allText = file.read()               #This read() function take all text from the file variable means the file "NewText.txt". and put the text into allText variable.
#print(allText)                      #This is print the whole text of NewText.txt file.

#someText = file.read(11)            #The read(11) means that take only 11 character from file variable and put those 11 charecter into someText variable.
#print(someText)                     #This is print first 11 charecter of NewText.txt file.

#size = len(someText)                #This len function return how many character the variable have.
#print(size)                         #print the size or someText string.

# allLineTextAsList = file.readlines() #This is return a list by depends on line.
# print(allLineTextAsList)             #This is return a list of NewText.txt text lines.
#
# #we can print specific line by indexing this list. also throw a for loop.
# print("The second line is : ",allLineTextAsList[1])   #Because the allLineTextAsList is a list.
#
# print("Line one by one by using loop :")
# for x in allLineTextAsList:
#     print("\t\t\t\t\t\t\t\t",x,end="")                                   #The extra line come. because end of every item of list contain \n.


##We can print one by one line.
# firstLine = file.readline()                  #This mean the first line store in the firstLine variable.
# print(firstLine,end="")                      #when we print use readline() then an extra new line come.
# print(file.readline())                       #This means the second line directly printed.

file.close()                                 #It is a good practice to always close the file when you are done with it.


#opening file from different directory.
file1 = open("C:/Users/dhali/OneDrive/Desktop/xx.txt","r")

allTextOfFile1 = file1.read()
print(allTextOfFile1)