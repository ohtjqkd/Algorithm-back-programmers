def solution(survey, choices):
    answer = []
    mbti = "RTCFJMAN"
    score = dict()
    for t in mbti:
        score[t] = 0
    for t, c in zip(survey, choices):
        score[t[c // 4]] += abs(c - 4)
    for i in range(0, 8, 2):
        f, s = mbti[i: i+2]
        if score[f] >= score[s]:
            answer.append(f)
        else:
            answer.append(s)
    return ''.join(answer)