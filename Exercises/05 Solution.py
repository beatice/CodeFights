# Solution 1
def matrixElementsSum1(matrix):
    l = len(matrix[0])
    ix = list(range(l))
    sum = 0
    for i in range(len(matrix)):
        jj = ix.copy()
        for j in jj:
            sum += matrix[i][j]
            if matrix[i][j] == 0:
                del ix[ix.index(j)]
    return sum

# Solution 2
def matrixElementsSum2(matrix):
    r = len(matrix)
    c = len(matrix[0])
    sum = 0
    for j in c:
        for i in r:
            sum += matrix[i][j]
            if matrix[i][j]==0:
                break
    return sum
    
