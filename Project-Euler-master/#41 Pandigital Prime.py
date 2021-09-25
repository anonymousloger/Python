import itertools
def prime(number) :
    if number == 1 or number % 2 == 0 and number != 2 :
        return False
    loopVar = 2
    while loopVar * loopVar <= number :
        if number % loopVar == 0 :
            return False
        loopVar += 1
    return True
def listPermutations(number) :
    tempList = list(itertools.permutations(map(int,list(str(number)))))
    ansList = []
    for loopVar in tempList :
        tempNumber = 0
        for loopVar2 in loopVar :
            tempNumber = tempNumber * 10 + loopVar2
        ansList.append(tempNumber)
    return sorted(ansList)[::-1]

digitCount = 9
loopCount = 0
flag = True
while flag :
    digitTest = 0
    permuteList = []
    #print (digitCount)
    for loopVar in range(1,digitCount + 1) :
        loopCount += 1
        digitTest = (digitTest * 10) + loopVar
    #print (digitTest)
    permuteList = listPermutations(int("".join(str(digitTest)[::-1])))
    primeListCheck = list(map(prime,permuteList))
    #print(primeListCheck)
    if True in primeListCheck :
        print (permuteList[primeListCheck.index(True)])
        flag = False
        break
    #print (loopCount)
    digitCount -= 1
#print (digitTest)
print ("loopCount=",loopCount)


# Completed

"""

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""