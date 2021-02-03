import collections


def can_finish(num_courses, prerequisites):
    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        if i in traced:
            return False
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True


print(can_finish(2, [[1, 0], [2, 1]]))
