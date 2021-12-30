userInput = input("Enter The String : ")
noOfWords = 0
noOfLetter = 0
noOfNumber = 0

for x in userInput:        #This
    x.lower()
    if x>="a" and x<="z":
        noOfLetter+=1
    elif x>="0" and x<="9":  #Here we use quotes because the 0 to 9 also string in userInput.
        noOfNumber+=1
    elif x == " ":
        noOfWords+=1
print("The number of letter :",noOfLetter)
print("The number of Number :",noOfNumber)
print("The number of Word :",noOfWords+1)
