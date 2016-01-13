#xor

#import random
from random import randrange

print(1^1, 1^0)
print(1^0^1, 1^1^0)
print(1^0^1^0^1, 1^1^1^0^0)

print("0 or 1", randrange(2))

#gernerate random array
arr = [0] * 10
for i in range(len(arr)):
    arr[i] = randrange(2)

#xor of each array element, sequentially
for i in range(len(arr)):
    if(i==0):
        res = arr[i]
    else:
        res ^= arr[i]
print(arr, "res1", res)

#xor of each array element, in random order
accessd = [0]*10
for i in range(len(arr)):
    if(i==0):
        res = arr[0]
        accessd[0] = 1
    else:
        j = randrange(10)        
        while(accessd[j]==1) or (j==0):
            j = randrange(10)
        accessd[j] = 1    
        res ^= arr[i]

print(arr, "res2", res)
'''
summery:
res1 = res2 shows, order doesnt matter
'''

