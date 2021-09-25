import math
def factors(n):
    factor=[]
    i=1
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

a=1
b=10
n=b*b
while True:
    count=0
    print (factors(n))
    for i in range(a,b+1) :
        if i in factors(n) :
            count+=1
    if count == (b-a+1) :
        print (sum(factors(n)))
        print (n)
        break
    n+=1


    # progaram not completed....
    # infinte loop
    # need to reduce loop count

"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""