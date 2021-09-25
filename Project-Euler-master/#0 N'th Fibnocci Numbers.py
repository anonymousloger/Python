def fib(position) :
    a = -1
    b = 1
    fibList = []
    while len(fibList) <= position :
        c = a + b
        a = b
        b = c 
        fibList.append(c)
    return fibList

position = 10
print (fib(position)[-1])



'''
Find the n'th Fibnocci number .
'''