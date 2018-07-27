def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i] - inputArray[i+1]) for i in range(0,len(inputArray)-1)])
