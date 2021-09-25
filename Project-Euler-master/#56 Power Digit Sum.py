def power(number,toPower) :
    ans = 1
    loopVar = 1
    while loopVar <= toPower :
        ans *= number
        loopVar += 1
    return ans
start = 99
end = 1
loopCount = 0
sumList = []
for loopVar in range(start,end,-1) :
    for loopVar2 in range(start,80,-1) :
        loopCount += 1
        sumList.append(sum(list(map(int,list(str(power(loopVar,loopVar2)))))))
print (len(sumList),max(sumList),sumList.index(max(sumList)))
print ("loopCount=",loopCount)


# Completed

"""


A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""