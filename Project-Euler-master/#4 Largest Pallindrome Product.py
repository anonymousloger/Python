def reverse(s): 
    return s[::-1] 
def pal(num):
    if reverse(num)==num :
        return True
    return False
l=[]
a=999
b=900
for i in range(a,b,-1):
    for k in range(a,b,-1):
        l.append(i*k)
l.sort()
l.reverse()
for i in l:
    if pal(str(i)):
        print (i)
        break


#  The largest palindrome made from the product of two n-digit numbers 
# example : 99*91=9009