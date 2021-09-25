  
   def BitmapHoles(strArr):
    bitmap = {}
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            bitmap[(i,j)] = int(strArr[i][j])
    
    hole_count = 0
    hole = set()
    checked = set()
    flag = True
    
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            stack = [(i,j)]
            while stack:
                crd = stack.pop()
                if crd not in checked:
                    checked.add(crd)
                    if bitmap[crd] == 0 and crd not in hole:
                        hole.add(crd)
                        if flag == True:
                            hole_count += 1
                            flag = False
                        if crd[0] - 1 >= 0 and (crd[0]-1,crd[1]) not in checked:
                            stack.append((crd[0]-1,crd[1]))
                        if crd[0] + 1 < len(strArr) and (crd[0]+1,crd[1]) not in checked:
                            stack.append((crd[0]+1,crd[1]))
                        if crd[1] - 1 >= 0 and (crd[0],crd[1]-1) not in checked:
                            stack.append((crd[0],crd[1]-1))
                        if crd[1] + 1 < len(strArr[crd[0]]) and (crd[0],crd[1]+1) not in checked:
                            stack.append((crd[0],crd[1]+1))
            flag = True
            
    return hole_count

strArr = ['01111','01101','00011','11110']
print(BitmapHoles(strArr))

strArr = ['1011','0010']
print(BitmapHoles(strArr))