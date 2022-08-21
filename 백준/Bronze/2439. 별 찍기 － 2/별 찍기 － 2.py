n=int(input())
for i in range(n):
    string = ''
    for j in range(n):
        if j >= n-i-1:
            string+='*'
        else:
            string+=' '
    print(string)