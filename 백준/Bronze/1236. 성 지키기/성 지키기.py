from sys import stdin
n, m = map(int, stdin.readline().strip().split(' '))

rows = {i: 0 for i in range(n)}
columns = {i: 0 for i in range(m)}

for row_n in range(n):
    row = stdin.readline().strip()
    for col_n, col_v in enumerate(row):
        if col_v == 'X':
            rows[row_n] = 1
            columns[col_n] = 1

r_answer = 0
for rv in rows.values():
    if rv == 0:
        r_answer += 1

c_answer = 0
for cv in columns.values():
    if cv == 0:
        c_answer += 1

if r_answer > c_answer:
    print(r_answer)
else:
    print(c_answer)