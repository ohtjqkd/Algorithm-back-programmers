for _ in range(int(input())):
    result = 0
    x, y = map(int, input().split())
    distance = y-x
    i = 0
    if distance == 1:
        print(1)
    elif distance == 2:
        print(2)
    else:
        while True:
            if (i+2)*(i+1) < distance:
                i += 1
            else:
                break
        if distance-(i+1)*i <= i+1:
            print((i+1)*2-1)
        else:
            print((i+1)*2)
