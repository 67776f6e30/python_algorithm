from collections import defaultdict, deque
import sys


def solution(n, s, a, b, fares):
    result = []
    graph = defaultdict(list)

    for f in fares:
        graph[f[0]].append((f[1], f[2]))
        graph[f[1]].append((f[0], f[2]))

    path = []

    def dfs(node, cost, total_cost, cg):
        if node in path:
            return
        path.append(node)
        total_cost += cost
        cg[node] = min(cg[node], total_cost)

        for i, c in graph[node]:
            dfs(i, c, total_cost, cg)
        path.pop()
        return


    #dfs(4, 0, 0)
    #
    a_cost = defaultdict(lambda: sys.maxsize)
    dfs(a, 0, 0, a_cost)
    b_cost = defaultdict(lambda: sys.maxsize)
    dfs(b, 0, 0, b_cost)
    cost1 = a_cost[b]

    for n in a_cost:
        if n != a:
            if a_cost[n] + b_cost[n] == cost1:
                ex = n
                break

    s_cost = defaultdict(lambda: sys.maxsize)
    dfs(s, 0, 0, s_cost)

    cost1 += s_cost[n]
    cost2 = s_cost[a] + s_cost[b]

    return min(cost1, cost2)


f = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
print(solution(6, 4, 5, 6, f))
