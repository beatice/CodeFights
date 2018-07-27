def arrayChange(inputArray):
    sum = 0
    for i in range(0,len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            sum += int(inputArray[i]) - int(inputArray[i+1]) + 1
            inputArray[i+1] = inputArray[i] + 1
    return sum
