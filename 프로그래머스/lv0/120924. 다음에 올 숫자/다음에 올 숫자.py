def solution(common):
    n = len(common)
    cd, cr = 0, 0
    cd = common[1] - common[0]
    if common[0] != 0 and common[1] % common[0] == 0:
        cr = common[1] // common[0]
    if common[0] * (cr ** (n - 1)) == common[-1]:
        return common[0] * (cr ** n)
    else:
        return common[0] + (cd * n)