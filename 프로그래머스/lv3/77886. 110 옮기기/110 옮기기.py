from collections import deque

def solution(s):
    answer = []   
    for b in s:
        q = deque(list(b))
        left, right = deque(b[:2]), deque(b[2:])
        cnt = 0
        while right:
            left.append(right.popleft())    
            if len(left) > 2 and left[-3] == '1' and left[-2] == '1' and left[-1] == '0':
                left.pop()
                left.pop()
                left.pop()
                cnt += 1 
        left = list(left)
        for i in range(len(left) - 1, -1, -1):
            if left[i] == '0':
                left= left[:i + 1] + (['110'] * cnt) + left[i + 1:]
                break
        else:
             left = ['110'] * cnt + left   
        answer.append(''.join(left))
    return answer