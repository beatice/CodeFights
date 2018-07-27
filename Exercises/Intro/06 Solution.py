def allLongestStrings(inputArray):
    m = max(len(i) for i in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r
