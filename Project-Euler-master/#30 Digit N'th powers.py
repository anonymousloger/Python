import math
power = 5
start  = 100
end = 1000000
loopCount = 0
numberList = []
while start < end :
    i = 0
    sumpow = 0
    while i < len(str(start)) :
        loopCount += 1
        sumpow += int(math.pow(int(str(start)[i]), power))
        i += 1
    #print (start,sum)
    if int(start) == sumpow :
        #print (start)
        numberList.append(int(start))
    start += 1
print ("Loopcount=",loopCount)
print ("Numbers=",numberList)
print ("Sum=",sum(numberList))

# completed

""""


Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""