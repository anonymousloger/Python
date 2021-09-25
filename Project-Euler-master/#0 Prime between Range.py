def prime(number):
    if number == 1 or number % 2 == 0 and number != 2 or number != 5 and number % 5 == 0 :
        return False
    loopVar=2   
    while loopVar*loopVar <= number :
        if number % loopVar == 0:
            return False
        loopVar += 1
    return True
start = 1
end = 10
loopCount = 0
primeList = [2]
for loopVar in range(start,end,2) :
    loopCount += 1
    if prime(loopVar) :
        primeList.append(loopVar)
print ("loopCount=",loopCount)
print (primeList)
