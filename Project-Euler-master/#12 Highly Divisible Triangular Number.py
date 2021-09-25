import math
def factors(n):
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
    factor.sort()
    return factor

TriangleNumberSet=[]
i=0
n=10
sum=0
while True:
    i+=1
    sum+=i
    TriangleNumberSet.append(sum)
    #print (TriangleNumberSet)
    #print ("fact",factors(sum))
    if len(factors(sum)) > n :
        print (sum)
        break


# value of the first triangle number to have over n divisors
# 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
# first 10 triangular nos: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55