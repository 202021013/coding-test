from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = deque([])  # 건너는 트럭 리스트
    passed_trucks = []  # 지난 트럭 리스트

    while truck_weights or on_bridge:
        time += 1

        if on_bridge and time - on_bridge[0][1] == bridge_length:
            passed_trucks.append(on_bridge.popleft()[0])

        if truck_weights and sum(t[0] for t in on_bridge) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            on_bridge.append((truck, time))

    return time