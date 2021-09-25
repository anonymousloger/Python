#program is correct for the inputs i give, but site says, incoorect answer

def sums(a,sum):
    n=10000
    i=1
    while(True):
        if i*a >= n:
            break
        sum+=(i*a)
        print (i,a,i*a,sum)
        i+=1
    return sum
sum=0
print(sum)
sum=sums(3,sum)
print(sum)
sum=sums(5,sum)
print (sum)