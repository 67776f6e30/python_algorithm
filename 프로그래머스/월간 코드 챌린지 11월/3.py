from collections import defaultdict


def solution(a):
    result = []
    memo = defaultdict(bool)
    len_a = len(a)
    if len_a == 0:
        return 0
    if len_a == 2:
        return 2

    path = []

    def dfs(start, end):
        if start >= len_a or end >= len_a:
            return
        try:
            path.append(str(a[start]) + str(a[end]))
        except:
            return
        path_s = "".join(path)
        if len(path) % 2 == 0 and not memo[path_s]:
            result.append(path_s)
            memo[path_s] = True
        dfs(end + 1, end + 2)
        dfs(end + 1, end + 3)
        path.pop()
        return

    def check(arr):
        s = set(arr[:2])
        for i in range(len(arr) // 2):
            tmp = set(arr[2*i:2*i+2])
            s &= tmp
            if len(s) == 0:
                return False
        return True

    dfs(0, 1)
    print(result)
    max_size = 0
    for r in result:
        if check(r):
            max_size = max(max_size, len(r))

    return max_size


data = [0,3,3,0,7,2,0,2,2,0]
print(solution(data))
