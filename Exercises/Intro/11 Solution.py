# Solution1
def alternatingSums1(a):
    team1 = [a[i] for i in range(0,len(a),2)]
    team2 = [a[i] for i in range(1,len(a),2)]
    return [sum(team1), sum(team2)]
    
# Solution2
def alternatingSums2(a):
    return [sum(a[::2]),sum(a[1::2])]
