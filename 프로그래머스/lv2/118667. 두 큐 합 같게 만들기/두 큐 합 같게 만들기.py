def solution(queue1, queue2):
    answer = 0
    q1_end, q1_sum = len(queue1), sum(queue1)
    q2_end, q2_sum = 0, sum(queue2)
    target_sum = q1_sum + q2_sum
    if target_sum % 2 == 1:
        return -1
    else:
        target_sum //= 2
    new_queue = queue1 + queue2
    total_len = len(new_queue)
    start = q1_end - 1
    while q1_end != q2_end and q1_end % total_len != start:
        if q1_sum == target_sum:
            return answer
        elif q1_sum > target_sum:
            q1_sum -= new_queue[q2_end % total_len]
            q2_sum += new_queue[q2_end % total_len]
            q2_end += 1
        else:
            q2_sum -= new_queue[q1_end % total_len]
            q1_sum += new_queue[q1_end % total_len]
            q1_end += 1
        answer += 1
            
    return -1