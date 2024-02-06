def solution(progresses, speeds):
    answer = []
    days = []

    # 각 기능의 개발 완료까지 필요한 날짜 계산
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) // speed
        if (100 - progress) % speed != 0:
            day += 1
        days.append(day)

    # 배포되는 기능 개수 계산
    count = 1
    max_day = days[0]
    for i in range(1, len(days)):
        if days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days[i]

    answer.append(count)

    return answer