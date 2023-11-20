P = int(input())
li = ['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for _ in range(P):
    cnt = {c:0 for c in li}
    string = input()
    for i in range(len(string)-2):
        cnt[string[i:i+3]] += 1
    print(' '.join(map(str, cnt.values())))