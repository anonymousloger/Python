

def TreeConstructor(strArr):
    parents = {}
    for node in strArr:
        p = int(node.split(",")[1][0])
        if p in parents.keys():
            parents[p] += 1
        else:
            parents[p] = 1
    
    if max(parents.values()) <= 2:
        return True
    return False

inp = ["(1,2)","(2,4)","(5,7)","(7,2)","(9,5)"]

print(TreeConstructor(inp))

inp = ["(1,2)","(3,2)","(2,12)","(5,2)"]

print(TreeConstructor(inp))
    