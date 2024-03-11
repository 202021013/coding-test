def solution(answers):
    result = []
    count = [0, 0, 0]
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i, answer in enumerate(answers):
        for j in range(3):
            if answer == patterns[j][i % len(patterns[j])]: # patterns보다 길 경우 반복되게
                count[j] += 1

    max_count = max(count)
    result = [i + 1 for i, c in enumerate(count) if c == max_count] # 가장 큰 값의 인덱스에 +1한 값

    return result