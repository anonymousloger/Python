def generatePrimeList(number) :
    prime = [True for loopVar in range(number + 1)]
    loopVar = 2
    while loopVar * loopVar <= number :
        if prime[loopVar] :
            for loopVar2 in range(loopVar * 2,number + 1,loopVar) :
                prime[loopVar2] = False
        loopVar += 1
    prime[0] = False
    prime[1] = False
    primeList = []
    for loopVar in range(number + 1) :
        if prime[loopVar] :
            primeList.append(loopVar)
    return primeList
number = 100
print (generatePrimeList(number))
print (len(generatePrimeList(number)))


"""
using Sieve of Eratosthenes

"""