def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    points = [0, 0, 0]
    result = []

    for j, n in enumerate(answers):
        for i in range(len(points)):
            if patterns[i][j % len(patterns[i])] == n:
                points[i] += 1

    max_score = max(points)
    for i in range(len(points)):
        if max_score == points[i]:
            result.append(i + 1)

    return result


print(solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
