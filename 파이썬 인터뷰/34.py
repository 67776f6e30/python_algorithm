import itertools

data = [1, 2, 3]


def permute(nums):
    return itertools.permutations(nums)
    result = []
    stack = []

    def dfs(lst):
        if len(lst) == 0:
            result.append(stack[:])
            return

        for n in lst:
            tmp = lst[:]
            tmp.remove(n)
            stack.append(n)
            dfs(tmp)
            stack.pop()

    dfs(nums)

    return result


print(list(map(list, permute(data))))
