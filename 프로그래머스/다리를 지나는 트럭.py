from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    q = deque()
    w = 0
    time = 0
    while q or truck_weights:
        if q and q[0][1] >= bridge_length:
            w -= q.popleft()[0]

        if truck_weights and w + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            q.append([truck, 0])
            w += truck

        for t in q:
            t[1] += 1

        time += 1
    return time


print(solution(2, 10, [7, 4, 5, 6]))
