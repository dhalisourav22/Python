#This lambda function is a kind of a anonymous function. Lambda function always work with single expression.
#Lambda function always return a value.

'''
#This is the traditional function.
def myFun(x):
    return x*x

#This is the lambda or anonymous function of the traditional function.
lambda x : x*x
'''

#One way to call lambda function.

#Print via a variable.
x = (lambda x : x*x)(5)      #The value we pass in the lambda function is 5
print("The value of the function is :",x)

#Direct print.
print("The value of the function is :",(lambda x : x*x)(6))


#Another way to call lambda function.
y = lambda x: x+10
print(y(2))         #That's mean the value we pass into y variable or the lambda function is 2.

#The lambda function under the traditional function.
def myFunc(n):
    return lambda a: a+n

var = myFunc(10)        #This is the value of n. and that is 10
print(var(5))           #Here we intialized the value of a variable. we can set this way.