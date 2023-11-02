##problem 1439
s = input()

change = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        change+=1

if change%2 == 0:
    result = change//2
else:
    result = change//2 + 1
    
print(result)