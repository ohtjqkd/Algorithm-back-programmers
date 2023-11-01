from collections import defaultdict
import sys

dictionary = defaultdict(int)
i = 0
string = sys.stdin.read().replace('\n', '')
for char in string:
    if char != ' ':
        dictionary[char] += 1
char_li = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
result = ''.join([char_li[i][0] for i in range(len(char_li)) if char_li[i][1] == char_li[0][1]])
print(result)