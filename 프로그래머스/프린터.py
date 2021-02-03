from collections import Counter, deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    priorities.sort()

    answer = 0
    while q:
        data = q.popleft()
        if data[0] < priorities[-1]:
            q.append(data)
            continue
        priorities.pop()
        answer += 1
        if data[1] == location:
            break
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
