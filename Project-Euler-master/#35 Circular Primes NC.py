def prime(number):
    if number in [2,5] :
        return True
    if number == 1 or number % 2 == 0 or number % 5 == 0 :
        return False
    loopVar=2
    while loopVar*loopVar <= number :
        if number % loopVar == 0:
            return False
        loopVar += 1
    return True
def primeNumbers(start, end) :
    primeList = []
    if start < 3 :
        primeList.append(2)
    if start % 2 == 0 :
        start -= 1
    for loopVar in range(start,end,2) :
        if prime(loopVar) :
            primeList.append(loopVar)
    return primeList
def listCyclicRotation(number) :
    listDigit = list(map(int,list(str(number))))
    numberList = []
    loopVar = 0
    while loopVar < len(str(number)) :
        numberList.append(int("".join(list(map(str,listDigit)))))
        listDigit.append(listDigit[0])
        listDigit.pop(0)
        loopVar += 1
    return numberList
def checkCircular(number) :
    numberRotationList = listCyclicRotation(number)
    if sorted(numberRotationList)[0] in circularPrimeList :
        return True
    primeCheckList = list(map(prime,numberRotationList))
    if False in primeCheckList :
        return False
    print (numberRotationList)
    return True
def evenOrFiveFactor(number) :
    if number % 2 == 0 or number % 5 == 0 :
        return True
    return False
start = 1
end = 100
loopCount = 0
circularPrimeList = []
primeList = sorted(primeNumbers(start,end))
for loopVar in primeList :
    loopCount += 1
    if loopVar > 10 :
        evenFiveNoCheck = list(map(evenOrFiveFactor,list(map(int,list(str(loopVar))))))
        if True in evenFiveNoCheck :
            continue
    if int("".join(sorted(list(str(loopVar))))) in circularPrimeList :
        circularPrimeList.append(loopVar)
        continue
    if checkCircular(loopVar) :
        circularPrimeList.append(loopVar)
        #print (circularPrimeList)

print ("loopCount=",loopCount)
print ("Count=",len(circularPrimeList))

# not completed
"""


The number, 197, is called a circular prime because all cyclic rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

