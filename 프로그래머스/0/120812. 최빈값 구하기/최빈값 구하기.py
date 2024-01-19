from collections import Counter

def solution(array):
    # 배열의 각 원소의 빈도수를 계산
    counts = Counter(array)

    # 가장 빈도수가 높은 값 찾기
    max_count = max(counts.values())
    
    mode_values = []
    for key, value in counts.items():
        if value == max_count:
            mode_values.append(key)

    if len(mode_values) > 1:
        return -1
    else:
        return mode_values[0]