# Solution1
def addBorder1(picture):
    l = len(picture[0])
    p = ["*"+i+"*" for i in picture]
    p.insert(0,"*"*(l+2))
    p.append("*"*(l+2))
    return p

# Solution2
def addBorder2(picture):
    l = len(picture[0]) + 2
    return ["*"*l] + [i.center(l,"*") for i in picture] + ["*"*l]
