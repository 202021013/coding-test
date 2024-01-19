def solution(num_list):
    answer = num_list.copy()
    if answer[-1] > answer[-2]:
        answer.append(answer[-1] - answer[-2])
    else:
        answer += [answer[-1] * 2]
    return answer
