import math
import random
#from random import randint

x = random.randint(5,10)  #This will give 5-10 random number.
#x = randint(5,10)        #Whene We only import randint not the entire module.
print("The Random Number Is :",x)





y = random.random()
print("This Will Give Float Random Number Between 0-1 Except 0 and 1 :",y)

z= random.random()*100
print("This Will Give Float Random Number Between 0-100 Except 0 and 100 :",z)

zz= random.random()*100+10
print("This Will Give Float Random Number Between 10-110 Except 10 and 110 :",zz)

xx= random.random()*100+10       #Here 100 is intervel and 10 is the starting point(10 is not included)
xx= math.ceil(z)
print("This Will Give Integer Random Number Between 11-110 with 11 and 110 :",xx)