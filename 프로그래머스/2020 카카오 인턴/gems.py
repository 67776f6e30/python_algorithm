from collections import defaultdict


def solution(gems):
    kind = set(gems)
    need = len(kind)
    df = defaultdict(int)
    left = right = start = end = 0
    result = []
    for g in gems:
        df[g] += 1
        need -= df[g] == 1
        right += 1
        while need <= 0 and left < right:
            df[gems[left]] -= 1
            need += df[gems[left]] <= 0
            start = left + 1
            end = right
            result.append((end - start, (start, end)))
            left += 1
    return sorted(result)[0][1]


print(solution(["AA", "AB", "AC", "AA", "AC"]))
