def power(number,toPower) :
    result = 1
    loopVar = 0
    while loopVar < toPower :
        result *= number
        loopVar += 1
    return  result
def selfPowSum(number) :
    sum = 0
    for loopVar in range(1,number + 1) :
        sum += power(loopVar,loopVar)
    return sum
number = 1000
loopCount = 0
sum = selfPowSum(number)
#print (sum)
sum = str(sum)[::-1]
result = ""
for loopVar in range(10) :
    loopCount += 1
    result += sum[loopVar]
print ("loopCount=",loopCount)
print ("Result=(str)",result[::-1])
print ("Result=(int)",int(result[::-1]))
#print ("Sum=",sum)

# reprogram this if possible
# Completed
"""


The series, 1(1) + 2(2) + 3(3) + ... + 10(10) = 10405071317.

Find the last ten digits of the series, 1(1) + 2(2) + 3(3) + ... + 1000(1000).

"""