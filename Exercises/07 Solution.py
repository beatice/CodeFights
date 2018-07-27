# Solution 1
def commonCharacterCount1(s1, s2):
    num = []
    for i in range(len(s1)):
        count1, count2 = s1.count(s1[i]), s2.count(s1[i])
        m = min(count1, count2)
        if count1 > 1 and i == s1.index(s1[i]):
            num.append(-m * (count1 - 2))
        else:
            num.append(m)
    return sum(num)
    
# Solution 2
def commonCharacterCount2(s1, s2):    
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))
