def solution(numbers):
    answer = [n for n in numbers]
    stack = [0]
    for i in range(1, len(numbers)):
        while stack:
            if numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            else:
                break
        stack.append(i)
    for i in stack:
        answer[i] = -1
    return answer