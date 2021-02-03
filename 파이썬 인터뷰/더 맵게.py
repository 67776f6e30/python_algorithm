import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    while scoville:
        food = heapq.heappop(scoville)
        if food >= K:
            return result
        elif scoville:
            new_food = food + (2 * heapq.heappop(scoville))
            heapq.heappush(scoville, new_food)
            result += 1
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
