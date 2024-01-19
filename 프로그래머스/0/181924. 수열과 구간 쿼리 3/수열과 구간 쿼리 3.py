def solution(arr, queries):
    answer = arr.copy()
    for query in queries:
        i,j = query
        answer[i],answer[j] = answer[j],answer[i]
    return answer