n = int(input())
i = 0
while True:
    i+=1
    if 3*(i-1)*i>=(n-1) and (n-1)>3*(i-1)*i-6*i:
        break
print(i)
