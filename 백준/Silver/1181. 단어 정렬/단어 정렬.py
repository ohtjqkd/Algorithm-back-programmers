import sys

input = sys.stdin.readline

print(*sorted(list(set([input().rstrip() for _ in range(int(input()))])), key=lambda x: (len(x), x)), sep='\n')