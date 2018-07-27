# Solution1
def areEquallyStrong1(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft == friendsLeft and yourRight == friendsRight) or (yourLeft == friendsRight and yourRight == friendsLeft)

# Solution2
def areEquallyStrong2(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft, yourRight]) == sorted([friendsLeft, friendsRight])

# Solution3
def areEquallyStrong3(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}
