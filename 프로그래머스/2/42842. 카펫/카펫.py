def solution(brown, yellow):
    # a*b = brown + yellow, (a-2) * (b-2) = yellow
    total = brown + yellow
    
    # a * b = total 구하기
    for a in range(1, total + 1):
        if total % a == 0:
            b = total // a
            
            # (a-2) * (b-2) = yellow 조건 확인
            if (a - 2) * (b - 2) == yellow:
                return [max(a, b), min(a, b)]
    
    return []