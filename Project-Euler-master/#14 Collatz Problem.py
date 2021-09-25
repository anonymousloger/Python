def nextnum(n):
    if n%2 == 0:
        return int(n/2)
    return (3*n+1)
number = 1000000
limit = 100000
loopCount = 0
count = []
numberList = []
while number != limit :
    elementList = []
    numberList.append(number)
    #print (n)
    tempNumber = number
    while tempNumber > 0:
        loopCount += 1
        elementList.append(tempNumber)
        tempNumber = nextnum(tempNumber)
        if tempNumber == 1 :
            elementList.append(tempNumber)
            break
    count.append(len(elementList))
    number -= 1
#print (count)
print ("loopCount=",loopCount)
print ("Max count=",max(count))
#print (count.index(max(count)))
print ("Starting Number=",numberList[count.index(max(count))])


# try reducing loopcount if possible...
# Completed



"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
 Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""