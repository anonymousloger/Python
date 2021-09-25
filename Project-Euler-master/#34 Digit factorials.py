def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
start = 10
end = 100000
loopCount = 0
numberList = []
while start < end :
    factSum = 0
    for i in str(start) :
        loopCount += 1
        factSum += factorial(int(i))
    if factSum == start :
        numberList.append(start)
    start += 1
print ("Numbers=",numberList)
print ("Sum=",sum(numberList))
print ("loopCount=",loopCount)

# completed


"""

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""