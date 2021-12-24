n = int(input("Enter The Value of N : "))

'''
*
**
***
****
*****
'''

print("First Pattern : ")
#Old Technique :
for x in range(1,n+1):       #We have 1,2,3 row. not 0 number row. that's why we start with 1, not 0.
    for y in range(x):
        print("*",end="")
    print()

print()
#New Technique :
for x in range(1,n+1):
    print(x*"*")



'''
*
***
*****
*******
*********

This is {(2*n)-1} patern. Where n is the number of line.
'''
print("\n\nSecond Pattern : ")
#Old Technique :
for x in range(1,n+1):
    for y in range((2*x)-1):
        print("*", end="")
    print()

print()
#New Technique :
for x in range(1,n+1):       #That's mean the line. there are how many line, that define there.
    print(((2*x)-1)*"*")     #that's how we can say how many time this "*" will come for print.




'''
    *
   **
  ***
 ****
*****

here n =5.
'''

print("\n\nThird Pattern : ")

#New Technique:
for x in range(1,n+1):
    print((n-x)*" "+x*"*")