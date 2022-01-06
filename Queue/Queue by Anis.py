from collections import deque                #this deque class is under a module called collections.

thisQueue = deque(["a","b","c","d","e"])     #this deque object gives the list some extra featuer. like, pop item by left side of the list by using popLeft() function.

#Adding item into the list or queue.
thisQueue.append("f")
print("After adding 'f' into the list or queue :",thisQueue)

#We pop the item. That's mean the item of index 0 will be deleted.
thisQueue.popleft()
thisQueue.popleft()
thisQueue.popleft()
print("After Pop 3 time :",thisQueue)
print(f"We have : {len(thisQueue)} item's")      #this is return the number of item the queue have.

if not thisQueue:
    print("This Queue is empty!")