# Solution1
def isIPv4Address(inputString):
    address = inputString.split('.')
    if len(address) != 4:
        return False
    if "" in address:
        return False
    if all([i.isdigit() for i in address]):
        return all([int(i)>=0 and int(i)<=255 for i in address])
    else:
        return False

# Solution2
def isIPv4Address(inputString):
    address = inputString.split('.')
    return len(address) == 4 and all([i.isdigit() and 0 <= int(i) <= 255 for i in address])
