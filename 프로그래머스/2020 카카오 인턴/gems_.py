from collections import defaultdict


def solution(gems):
    kind = set(gems)
    left = start = end = 0
    result = []
    for right, g in enumerate(gems, 1):
        while set(gems[left:right+1]) == kind:
            start = left + 1
            end = right + 1
            result.append((end - start, (start, end)))
            left += 1

    return list(sorted(result)[0][1])


print(solution(["AA", "AB", "AC", "AA", "AC"]))
