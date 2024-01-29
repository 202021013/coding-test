def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            cur = numbers[i]*numbers[j]
            answer = max(cur,answer)
    return answer