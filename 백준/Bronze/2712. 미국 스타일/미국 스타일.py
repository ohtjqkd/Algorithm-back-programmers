convertor = {
    "kg": ["lb", 2.2046],
    "lb": ["kg", 0.4536],
    "l": ["g", 0.2642],
    "g": ["l", 3.7854]
}
for _ in range(int(input())):
    v, u = input().split(" ")
    t, cv = convertor[u]
    print(f'{cv * float(v):.4f} {t}')