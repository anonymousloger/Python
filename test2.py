


for num in range(1,101):
    if num % 15 == 0:
        print('BizzFizz', end=' ')
    elif num % 3 == 0:
        print('Fizz', end=' ')
    elif num % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(num, end=' ')



'''

range(start,end,skip)


range(10)
 - start = 0
 - end = 10
 - skip = 1

range(2, 10)
 - start = 2
 - end = 10
 - skip = 1

range(2, 10, 3)
 - start = 2
 - end = 10
 - skip = 3

'''