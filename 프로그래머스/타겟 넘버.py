def solution(numbers, target):
    length = len(numbers)
    result = [0]

    def dfs(s, i):
        if i == length:
            if s == target:
                result[0] += 1
            return
        dfs(s + numbers[i], i + 1)
        dfs(s - numbers[i], i + 1)

    dfs(0, 0)
    return result[0]


print(solution([1, 1, 1, 1, 1], 3))
