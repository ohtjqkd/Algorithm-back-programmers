def solution(num, total):
    start = -(num // 2) - (num % 2) + 1
    for i in range(start, 101):
        if (i + (i + num - 1)) * num // 2 == total:
            return [j for j in range(i, i + num)]
