n = int(input())
input_value = []
for _ in range(n):
    input_value.append(int(input()))


temp1 = list()
temp2 = list()
left_cnt, right_cnt = 1, 1
left_standard, right_standard = input_value[0], input_value[-1]

for i in range(1, len(input_value)):
    if left_standard < input_value[i]:
        left_standard = input_value[i]
        left_cnt += 1
    if right_standard < input_value[-(i+1)]:
        right_standard = input_value[-(i+1)]
        right_cnt += 1

print(left_cnt)
print(right_cnt)