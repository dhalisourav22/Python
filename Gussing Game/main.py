# from random import randint
#
# print("Welcome...!")
# n = int(input("How Many Time You Want To Play : "))
# count = 0
#
# for x in range(1,n+1):
#     guessNumber = int(input("Enter The Guess Number between 1 to 5 : "))
#
#     if randomNumber == guessNumber :
#         print(f"\tYou Won..!\n")
#         count+=1
#     else:
#         print("\tYou Guess Wrong Number..!")
#         print(f"\tThe Right Number Is {randomNumber}.\n")
#
# print(f"\nYou Total Won {count} time in {n} time.")


from random import randint

print("Welcome...!")
n = int(input("How Many Time You Want To Play : "))
count = 0

i=0
while i<n:
    guessNumber = int(input("Enter The Guess Number between 1 to 5 : "))

    if guessNumber<1 or guessNumber>5:    #I can't do this by for loop.
        print("\tPlease Try to Keep Your Guess between 1 to 5.\n\tTry Again..!\n")
        continue                         #here we don't have to need decrease the i value. because the updation will happend in else.

    else:
        randomNumber = randint(1, 5)
        i += 1                           #here the increment will be happen. otherwise the same i value will be run again.
        if randomNumber == guessNumber :
            print(f"\tYou Won..!\n")
            count+=1
        else:
            print("\tYou Guess Wrong Number..!")
            print(f"\tThe Right Number Is {randomNumber}.\n")

print(f"\nYou Total Won {count} time in {n} time.")
