from collections import defaultdict, deque
import heapq


def solution(sales, links):
    result = 0
    graph = defaultdict(list)
    cost = defaultdict(list)
    for index, dest in links:
        graph[index].append(dest)

    for c in range(len(sales)):
        cost[c+1] = sales[c]

    q = deque([1])
    visit = [1]
    prev = 0
    while q:
        heap = []
        node = q.popleft()
        heapq.heappush(heap, (cost[node], node))
        for n in graph[node]:
            q.append(n)
            heapq.heappush(heap, (cost[n], n))
            visit.append(n)
        while heap:
            c, i = heapq.heappop(heap)
            if graph[i]:
                prev = i
                result += c
                break

    return result


s = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
l = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(s, l))