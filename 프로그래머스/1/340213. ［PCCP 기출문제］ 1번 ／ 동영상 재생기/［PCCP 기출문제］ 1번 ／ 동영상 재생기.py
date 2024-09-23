def convert2sec(time: str) -> int:
    m, s = map(int, time.split(':'))
    return 60 * m + s

def convert2timestamp(time: int) -> str:    
    return str(time // 60).zfill(2) + ':' + str(time % 60).zfill(2)

def rewind(curr: int) -> int:
    return max(0, curr - 10)

def fastforward(video_len: int, curr: int) -> int:
    return min(video_len, curr + 10)

def skip_op(op_s: int, op_e: int, curr: int) -> int:
    if op_s <= curr <= op_e:
        return op_e
    return curr

def solution(video_len, pos, op_start, op_end, commands):
    op_s = convert2sec(op_start)
    op_e = convert2sec(op_end)
    curr = convert2sec(pos)
    total_len = convert2sec(video_len)
    for cmd in commands:
        curr = skip_op(op_s, op_e, curr)
        if cmd == 'prev':
            curr = rewind(curr)
        else:
            curr = fastforward(total_len, curr)
    curr = skip_op(op_s, op_e, curr)
    
    return convert2timestamp(curr)
