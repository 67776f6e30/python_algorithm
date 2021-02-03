def solution(tickets):
    visit = []
    result = []

    def dfs(next, tickets):
        visit.append(next)
        for t in tickets:
            if t[0] == next:
                tmp = tickets[:]
                tmp.remove(t)
                dfs(t[1], tmp)
        if not tickets:
            result.append(visit[:])

        visit.pop()

    dfs('ICN', tickets)

    result.sort()

    return result[0]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
