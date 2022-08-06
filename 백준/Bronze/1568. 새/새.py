totalbird = int(input())
answer = 0
i = 1
while totalbird > 0:
    totalbird -= i
    answer += 1
    i += 1
    if totalbird - i < 0:
        i = 1
    

print(answer)
