def calculate(input_v):
    result = 0
    cnt = 5 - len(set(input_v))
    if cnt == 4:
        result = input_v[0]*5000+50000
    
    elif cnt == 3:
        if input_v[1] != input_v[2]: ## 겹치는 눈이 3개인 경우
            result = sum(set(input_v))*500+2000
        else: ## 겹치는 눈이 2개씩 2쌍인 경우
            result = input_v[1]*1000+10000
    elif cnt == 2:
        if input_v[0] == input_v[1]:
            result =input_v[0]*100+1000
        elif input_v[1] == input_v[2]:
            result =input_v[1]*100+1000
        else:
            result = input_v[2]*100+1000


        
    else:
        result = input_v[3] * 100
    return result
n = int(input())
sums = []
for _ in range(n):
    dice = sorted(list(map(int, input().split())))
    sums.append(calculate(dice))
print(max(sums))