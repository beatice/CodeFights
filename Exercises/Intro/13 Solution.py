# Solution1
def areSimilar1(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if a.count(a[i]) != b.count(a[i]) or a.count(b[i]) != b.count(b[i]):
                return False
        if count > 2:
            return False
    return count != 1

# Solution2
def areSimilar2(A, B):
    count = 0
    for a,b in zip(A,B):
        if a != b:
            count += 1
            if A.count(a) != B.count(a) or A.count(b) != B.count(b):
                return False
        if count > 2:
            return False
    return count != 1

# Solution3
def areSimilar3(A, B):
    return sorted(A) == sorted(B) and sum([a!=b for a,b in zip(A,B)]) < 3

    """
    错误写法：
    return A.sort() == B.sort() and sum([a!=b for a,b in zip(A,B)]) < 3

    解释：
      sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
      list 的 sort 方法是对已经存在的列表进行操作，没有返回值，而内建函数 sorted 方法返回的是一个新的 list。
    """

# Solution4
from collections import Counter as C

def areSimilar4(A, B):
    return C(A) == C(B) and sum([a!=b for a,b in zip(A,B)]) < 3
