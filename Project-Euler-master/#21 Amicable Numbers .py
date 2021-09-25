import math
def factors(number):
    start = 1
    factor = []
    loopCount = 0
    while start <= math.sqrt(number) :
        if number%start == 0:
            if number/start == start :
                factor.append(start)
            else:
                factor.append(start)
                factor.append(int(number/start))
        start += 1
        loopCount += 1
    return sorted(factor)
number = 2
amicableNumberList = []
limit = 10000
loopCount = 0
while number <= limit :
    loopCount += 1
    factorList = factors(number)
    factorList.pop(len(factorList) - 1)
    if sum(factorList) == number :
        number += 1
        continue
    #print (number,factorList,sum(factorList))
    tempNumber = sum(factorList)
    factorList = factors(tempNumber)
    factorList.pop(len(factorList) - 1)
    #print (tempNumber,factorList,sum(factorList))
    if sum(factorList) == number :
        amicableNumberList.append(number)
    number += 1
print ("loopCount=",loopCount)
print (amicableNumberList)
print ("sum=",sum(amicableNumberList))


# completed


"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""