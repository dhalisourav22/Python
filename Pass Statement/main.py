#This is avoid the error. when any if/elif/else block are empty. we can't use any of thoes block as empty.
a=30
b=30
if a>b:
    pass             #this is avoid the error of empty.
elif (a==b):         #We can use bracket here.
    print("They are equal.")