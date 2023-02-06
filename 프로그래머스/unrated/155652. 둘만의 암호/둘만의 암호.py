def solution(s, skip, index):
    alph = []
    _mapping = {}
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in skip:
            alph.append(chr(i))
    for i, a in enumerate(alph):
        _mapping[a] = i
    answer = []
    for c in s:
        answer.append(alph[(_mapping[c] + index) % len(alph)])
    return ''.join(answer)