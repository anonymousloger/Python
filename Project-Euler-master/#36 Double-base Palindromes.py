def pallindrome(number):
    if number == int(str(number)[::-1]) :
        return True
    return False
def binary(number) :
    tempList = list(str(bin(number)))
    #print (tempList)
    tempList.pop(0)
    tempList.pop(0)
    tempString = ""
    for i in tempList :
        tempString += i
    return int(tempString)
start = 1
loopCount = 0
end = 1000000
doubleBasePalList = [0]
for i in range(start,end,2) :
    loopCount += 1
    if pallindrome(i) & pallindrome(binary(i)) :
        doubleBasePalList.append(i)
        #print (i,bin(i))
print ("loopCount=",loopCount)
print(doubleBasePalList)
print (sum(doubleBasePalList))

# completed

"""


The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""