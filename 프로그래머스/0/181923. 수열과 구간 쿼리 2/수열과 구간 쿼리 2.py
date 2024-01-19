def solution(arr, queries):
    answer = []

    for query in queries:
        s, e, k = query
        valid_elements = [arr[i] for i in range(s, e + 1) if arr[i] > k]

        if not valid_elements:
            answer.append(-1)
        else:
            min_value = min(valid_elements)
            answer.append(min_value)

    return answer