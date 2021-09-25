import math
def pythogon(a,b,c):
    if a*a+b*b == c*c :
        return True
    return False
# a=3
# loopCount=0
# for i in range(1,1000):
#     for k in range(1,1000):
#         loopCount+=1
#         b=a+k
#         c=int(math.sqrt(a*a+b*b))
#         if pythogon(a,b,c) :
#             # if int((math.sqrt(a*a+b*b))*10)%10 == 0 :
#                 #print (a,b,c)
#                 #print (pythogon(a,b,c))
#                 #print (a,a*a,b,b*b,c,c*c)
#             if a+b+c == 1000:
#                 print (a,b,c,"=",a*b*c)
#                 print(loopCount)
#                 exit()
#     a+=1



#   There n=1000
n=1000
loopCount=0
for a in range(1,int(n/3)):
    for b in range(1,int(n/2)):
        c=1000-a-b
        loopCount+=1
        if (c**2 == a**2+b**2):
            print(loopCount)                
            print(a,b,c,a+b+c)
