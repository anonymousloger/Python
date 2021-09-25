def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=100
fact=str(fact(n))
sum=0
for i in fact:
    sum+=int(i)
print (sum)



"""


n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""