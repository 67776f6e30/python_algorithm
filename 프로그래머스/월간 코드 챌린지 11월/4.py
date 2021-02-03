from collections import defaultdict


"""
def solution(t):
    graph = defaultdict(list)
    memo = [[0] * (len(t) + 1) for _ in range(len(t) + 1)]
    for node, edge in t:
        graph[node]. append(edge)
        graph[edge].append(node)

    def dfs(root, n):
        stack = [n]
        visit = [root]
        while stack:
            node = stack.pop()
            for next in graph[node]:
                if next not in visit:
                    memo[root][n] += 1
                    stack.append(next)
                    visit.append(next)

    root_node = max(graph.items(), key=len)[0]
    for e in graph[root_node]:
        dfs(root_node, e)

    result = 0
    count_list = sorted(memo[root_node], reverse=True)
    for i in range(min(len(graph[root_node]), len(count_list), 3)):
        result += count_list[i] if count_list[i] > 0 else 1

    return result + 1



"""


def solution(t):
    graph = defaultdict(list)
    memo = [[0] * (len(t) + 1) for _ in range(len(t) + 1)]
    for node, edge in t:
        graph[node].append(edge)
        graph[edge].append(node)

    tmp = list(graph.items())
    c = 0
    for tt in tmp:
        if len(tt[1]) > 3:
            c += len(tt[1]) - 3
    return len(t) + 1 - c


data = [[2,5],[2,0],[3,2],[4,2],[2,1]]
print(solution(data))
