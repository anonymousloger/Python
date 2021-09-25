import math
def sumOfFactors(n):
    i=1
    factor=[]
    while i<= math.sqrt(n) :
        if n%i == 0:
            if n/i == i :
                factor.append(i)
            else:
                factor.append(i)
                factor.append(int(n/i))
        i+=1
    return (sum(factor)-n)
# creats the list of abundant numbers under a range
def abundantNos():
    start=1
    limit =16000
    nos=[]
    while start<limit :
        if sumOfFactors(start) > start :
            nos.append(start)
        start+=1
    return nos
# creates a list of condition matched numbers
def sumAbund() :
    nos = abundantNos()
    print (len(abundantNos()))
    lnos=[]
    loopcount=1
    for i in nos :
        for k in nos :
            print (loopcount)
            loopcount+=1
            if i+k >28123:
                break
            if i+k not in lnos :
                lnos.append(i+k)
        if i+k > 28123 :
          break
    return lnos

print(sumAbund())


# stuck...... lemme check it some other time










"""

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the 
sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""