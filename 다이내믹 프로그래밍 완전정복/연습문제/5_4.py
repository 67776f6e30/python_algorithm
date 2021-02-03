from sys import maxsize


def solution(origin, destination):
    height = abs(origin[0] - destination[0]) + 1
    width = abs(origin[1] - destination[1]) + 1
    memo = [[maxsize] * width for _ in range(height)]
    memo[0][0] = 0

    def check_knight(row, col):
        if row + 1 < height and col + 2 < width:
            memo[row + 1][col + 2] = min(memo[row + 1][col + 2], memo[row][col] + 1)
        if row + 2 < height and col + 1 < width:
            memo[row + 2][col + 1] = min(memo[row + 2][col + 1], memo[row][col] + 1)

    def check_king(row, col):
        if col + 1 < width:
            memo[row][col + 1] = min(memo[row][col + 1], memo[row][col] + 1)
        if row + 1 < height:
            memo[row + 1][col] = min(memo[row + 1][col], memo[row][col] + 1)
        if row + 1 < height and col + 1 < width:
            memo[row + 1][col + 1] = min(memo[row + 1][col + 1], memo[row][col] + 1)

    for i in range(height):
        for j in range(width):
            check_king(i, j)
            check_knight(i, j)

    return memo[height-1][width-1]


print(solution((7, 15), (0, 0)))
