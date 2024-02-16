def solution(n, lost, reserve):
    # 체육복을 도난당한 학생 중 여벌 체육복을 가진 학생은 빌려줄 수 없으므로 제외
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    # 여벌 체육복을 가진 학생이 도난당한 학생에게 빌려줄 수 있는지 확인
    for student in real_reserve:
        if student - 1 in real_lost:
            real_lost.remove(student - 1)
        elif student + 1 in real_lost:
            real_lost.remove(student + 1)
    
    # 체육수업을 들을 수 있는 학생 수 계산
    answer = n - len(real_lost)
    
    return answer