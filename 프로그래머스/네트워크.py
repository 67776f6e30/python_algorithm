def solution(n, computers):
    result = 0
    visit = []

    def dfs(i):
        if i in visit:
            return 0
        visit.append(i)
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] and j not in visit:
                dfs(j)
        return 1

    for i in range(n):
        result += dfs(i)

    return result


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
