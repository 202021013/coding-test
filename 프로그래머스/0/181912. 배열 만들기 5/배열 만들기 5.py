def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        j = i[s:s+l]
        if int(j) > k:
            answer.append(int(j))
    return answer