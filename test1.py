def function(string, flag) :
    if flag:
        return string[::2]
    else:
        return string[1::2]

print(function("TRACXN",0))
print(function("TRACXN",1))


'''

0 = False
1 = True

flag = 0
flag = 1

012345
TRACXN

[1:4:2]

array[start:end:skip]

string[start:end:skip]

'''
