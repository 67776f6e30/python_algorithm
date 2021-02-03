def solution(progresses, speeds):
    stack = [i for i in range(len(progresses)-1, -1, -1)]
    result = []
    while stack:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            while stack and progresses[stack[-1]] >= 100:
                stack.pop()
                cnt += 1
        if cnt > 0:
            result.append(cnt)
    return result


p = [93, 30, 55]
s = [1, 30, 5]
print(solution(p, s))
