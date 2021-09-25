def prime(number):
    if number == 1 or number % 2 == 0 and number != 2 :
        return False
    loopVar=2
    while loopVar*loopVar <= number :
        if number % loopVar == 0:
            return False
        loopVar += 1
    return True

position = 10001
number = 2
loopCount = 0
count = 0
while True :
    loopCount += 1
    if prime(number) :
        count += 1
    if count == position:
        print (number)
        break
    number += 1
print ("loopCount=",loopCount)
# prints the n'th prime number