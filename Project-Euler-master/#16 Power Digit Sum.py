import math
number = 1000
num = int(math.pow(2,number))
num = str(num)
sum = 0
loopCount = 0
for i in num:
    loopCount += 1
    sum += int(i)
    #print (i)
print (sum)
print ("loopCount=",loopCount)

# completed

"""


215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""