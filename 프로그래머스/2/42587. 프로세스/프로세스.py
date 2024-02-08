def solution(priorities, location):
    answer = 0
    while True:
        # 가장 높은 우선순위를 가진 프로세스를 꺼냄
        max_priority = max(priorities)
        front = priorities.pop(0)
        if front == max_priority:
            # 가장 높은 우선순위를 가진 프로세스인 경우
            answer += 1
            if location == 0:
                # 찾고자 하는 프로세스인 경우
                break
            else:
                # 다음 프로세스로 이동
                location -= 1
        else:
            # 우선순위가 더 높은 프로세스가 있으면 다시 큐의 맨 뒤에 추가
            priorities.append(front)
            if location == 0:
                # 찾고자 하는 프로세스가 맨 앞으로 이동한 경우
                location = len(priorities) - 1
            else:
                # 찾고자 하는 프로세스가 이동한 위치를 조정
                location -= 1
    return answer