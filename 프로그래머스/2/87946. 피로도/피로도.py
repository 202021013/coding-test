from itertools import permutations  # permutations 함수를 사용하기 위해 itertools 모듈을 import합니다.

def solution(k, dungeons):
    # 가능한 모든 던전 순열을 저장할 리스트를 초기화합니다.
    all_dungeons = []

    # 주어진 던전 리스트를 순열로 생성하고 all_dungeons 리스트에 저장합니다.
    for i in permutations(dungeons, len(dungeons)):
        all_dungeons.append(list(i))

    # 각 순열에 대해 가능한 통과할 수 있는 던전 수를 저장할 리스트를 초기화합니다.
    possible = []

    # 모든 던전 순열에 대해 탐색합니다.
    i = 0
    while i < len(all_dungeons):
        # 현재 체력을 초기화합니다.
        stamina = k
        # 현재 순열에서 통과한 던전 수를 초기화합니다.
        count = 0
        # 각 던전에 대해 체력을 확인하고 통과할 수 있는지 확인합니다.
        for j in all_dungeons[i]:
            if stamina >= j[0]:  # 만약 체력이 해당 던전을 통과하는 데에 충분하다면
                stamina -= j[1]  # 체력을 감소시키고
                count += 1       # 통과한 던전 수를 증가시킵니다.
            elif stamina < j[0]:  # 만약 체력이 부족하다면
                break            # 해당 던전을 통과할 수 없으므로 반복문을 종료합니다.
        # 현재 순열에서 통과한 던전 수를 possible 리스트에 추가합니다.
        possible.append(count)
        i += 1  # 다음 순열로 이동합니다.

    # 가능한 모든 순열 중에서 가장 많은 던전을 통과할 수 있는 경우를 찾아 반환합니다.
    answer = max(possible)
    return answer
