def solution(emergency):
    answer = emergency.copy()
    sort_answer = sorted(answer , reverse = True)
    for i, value in enumerate(sort_answer):
        idx = emergency.index(value)
        answer[idx] = i+1
        
    return answer