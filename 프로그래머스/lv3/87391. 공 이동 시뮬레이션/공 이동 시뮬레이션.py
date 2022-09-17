def solution(n, m, x, y, queries):
    col_q, row_q = [], []
    for c, d in queries:
        div, mod = divmod(c, 2)
        if div == 0:
            if mod == 0:
                col_q.append(-d)
            else:
                col_q.append(d)
        else:
            if mod == 0:
                row_q.append(-d)
            else:
                row_q.append(d)

    def sub_f(axios_q: list, dest: int, wall: int):
        mn, mx = dest, dest
        while axios_q:
            dd = axios_q.pop()
            if dd < 0:
                if mn > 0:
                    mn = max(0, mn - dd)
                else:
                    if mx - dd < 0:
                        return 0
                mx = min(mx - dd, wall - 1)
            else:
                if mx < wall - 1:
                    mx = min(mx - dd, wall - 1)
                else:
                    if mn - dd > wall - 1:
                        return 0
                mn = max(0, mn - dd)
        return (mx - mn) + 1
    col = sub_f(col_q, y, m)
    row = sub_f(row_q, x, n)
    return col * row