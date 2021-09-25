"""
def prime(n):
    if n<=1:
        return False                #can be used to check whether prime or not
    if n<=3:
        return True
    if n%2 == 0 or n%3 == 0 :
        return False
    i=5
    while i*i <= a :
        if n%i == 0 or n%(i+2) == 0 :
            return False
        i+=6
    return True
"""
def prime(a):
    i=2
    while (i*i<=a):
        if a%i == 0:
            return False
        i+=1
    return True
end = 2000000
sum = 0
count = 0
for i in range(2,end):
    if prime(i):
        count+=1
        sum+=i
print (count,sum)

# edit this program , use new prime method
# count and sum of all prime numbers under n
"""


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""