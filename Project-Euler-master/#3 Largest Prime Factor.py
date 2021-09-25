import math
def prime(number):
    if number == 1 :
        return False
    loop=2
    while loop*loop <= number :
        if number%loop == 0:
            return False
        loop += 1
    return True

number = 12
numberList=[]
loop=1
while loop<= math.sqrt(number) :
    if number%loop == 0:
        if number/loop == loop :
            if(prime(loop)):
                numberList.append(loop)
        else:
            if(prime(loop)):
                numberList.append(loop)
            if(prime(int(number/loop))):
                numberList.append(int(number/loop))
    loop += 1
print (f'LoopCount = {loop}')
print (numberList)
print (max(numberList))


# completed


# largest prime factor of a number