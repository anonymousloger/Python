def toPower(number, power):
    ans = 1
    loopVar = 1
    while loopVar <= power:
        ans *= number
        loopVar += 1
    return ans


answerList = []
loopCount = 0
digitCount = 1
loopVar = 1
while digitCount < 100:
    loopCount += 1
    if len(list(str(toPower(loopVar, digitCount)))) == digitCount:
        answerList.append([digitCount, loopVar, toPower(loopVar, digitCount)])
    elif len(list(str(toPower(loopVar, digitCount)))) > digitCount:
        loopVar = 0
        digitCount += 1
    loopVar += 1
print("loopCount=", loopCount)
print("Count=", len(answerList))
print(answerList)

# Completed
"""


The 5-digit number, 16807=7(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8(9), is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

