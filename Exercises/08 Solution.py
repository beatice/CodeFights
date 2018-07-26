# Solution 1
def isLucky1(n):
    s = str(n)
    l = len(s)
    sum1 = sum([int(s[i]) for i in range(l//2)])
    sum2 = sum([int(s[j]) for j in range(l//2, l)])
    return sum1 == sum2
    
# Solution 2
def isLucky2(n):
    s = str(n)
    pivot = s//2
    s1, s2 = s[:pivot], s[pivot:]
    return sum(map(int, s1)) == sum(map(int, s2))
