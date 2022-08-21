input_v = list(map(int, input().split()))

cnt = 4 - len(set(input_v))

if cnt == 3:
    print(input_v[0]*1000+10000)
elif cnt == 2:
    if input_v[0] == input_v[1] or input_v[0] == input_v[2]:
        print(input_v[0]*100 + 1000)
    else:
        print(input_v[1]*100 + 1000)
else:
    print(max(input_v) * 100)