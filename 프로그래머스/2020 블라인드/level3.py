import heapq

"""
def solution(N, number):
    answer = 0
    if N == 1:
        return number

    if number >= 11:
        acc = number * N
        acc -= N * 10 + N
        if acc == N / N:
            return 3
        answer = 3 + (acc // N)
    elif N < number:
        acc = number * N
        acc -= N * N
        answer = 2 + acc
    else:
        acc = N - number
        answer = 1 + (acc * 2)
    return answer if answer < 8 + 1 else -1


#print(9, solution(5, 12))
for i in range(1, 30):
    for j in range(1, 30):
        print(i, j, solution(i, j))
"""

def solution(v):
    x = []
    y = []

    for e in v:
        x.append(e[0])
        y.append(e[1])

    max_x = max(x)
    max_y = max(y)
    width = max_x - min(x)
    height = max_y - min(y)

    vertex = [
        (max_x, max_y),
        (max_x, max_y - height),
        (max_x - width, max_y),
        (max_x - width, max_y - height)
    ]

    return (set(vertex) - set([(e[0], e[1]) for e in v]))[0]


data = [
    [0, 0],
    [0, 1],
    #[1, 0],
    [1, 1],
]
print(solution(data))