#We habe basically 3 step. 1. Select line from where we want to start debugging.  2. Start debugging by (Run >> Debug'fileName') / (shift+F9)  3. Change line by one by one by which we debug the segment of code step by spep. for this we have to click (step into) / F7.
def add(*numbers):
    sum=0
    for num in numbers:
        sum += num
        return sum

print(add(10,20))
