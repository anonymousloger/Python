def fact(number) :
    ans = 1
    loopCount = 0
    for item in range(1,number + 1) :
        loopCount += 1
        ans *= item
    print (f'loopCount = {loopCount}')
    return ans


for item in range(1,100) :
    print (f'{item}! = {fact(item)}')