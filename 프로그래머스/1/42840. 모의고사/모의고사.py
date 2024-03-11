def solution(answers):
    result = []
    count = [0, 0, 0]
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i, answer in enumerate(answers):
        for j in range(3):
            if answer == patterns[j][i % len(patterns[j])]:   # answers가 patterns보다 길때
                count[j] += 1
    
    max_count = max(count)
    result = [i+1 for i,c in enumerate(count) if c == max_count] # 가장 큰 값의 index값의 +1
    
    return result