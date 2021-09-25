def prime(number):
    if number == 1 or number % 2 == 0 and number != 2 :
        return False
    loopVar=2
    while loopVar*loopVar <= number :
        if number % loopVar == 0:
            return False
        loopVar += 1
    return True
# Remove character from left side one by one from the number
def removeLeftList(number) :
    tempList = list(str(number))
    resultList = []
    while len(tempList) >= 1 :
        tempString = ""
        for k in range(len(tempList)) :
            tempString += tempList[k]
        resultList.append(int(tempString))
        tempList.pop(0)
    return resultList
# Remove character from right side one by one from the number
def removeRightList(number) :
	tempList = list(str(number))
	resultList = [number]
	while len(tempList) > 1 :
		try:
			tempList.pop(-1)
			tempString = ""
			for k in tempList :
				tempString += k
			resultList.append(int(tempString))
		finally :
			pass
	return resultList
# check if truncatable Prime
def checkTruncatable(set1,set2) :
    for i in set1 :
        if not prime(i) :
            return False
    for i in set2 :
        if not prime(i) :
            return False
    return True
# Main function
loopVar = 10
count = 0
loopCount = 0
truncatablePrime = []
while count < 11 :
    loopCount += 1
    if prime (loopVar) :
        set1 = removeLeftList(loopVar)
        set2 = removeRightList(loopVar)
        if checkTruncatable(set1,set2) :
            count += 1
            print (count,set1,set2)
            truncatablePrime.append(loopVar)
    loopVar += 1
print ("loopCount=",loopCount)
print ("Result=",truncatablePrime)
print ("sum=",sum(truncatablePrime))

# Completed


"""


The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""