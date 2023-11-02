N = int(input())
seq = [int(input()) for _ in range(N)]
same_diff  = (seq[1] - seq[0] == seq[2] - seq[1])
if same_diff:
    print(seq[-1] + seq[1] - seq[0])
else:
    print(seq[-1] * (seq[1] // seq[0]))