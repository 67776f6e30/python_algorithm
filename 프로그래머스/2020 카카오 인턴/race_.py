import heapq


def solution(board):
    len_board = len(board) - 1
    result = []
    path = []
    black_list = []

    def get_pos(direction, x, y):
        if direction == 'E':
            return x + 1, y
        if direction == 'S':
            return x, y + 1
        if direction == 'W':
            return x - 1, y
        if direction == 'N':
            return x, y - 1

    def dfs(x, y, prev_dir=None, cur_dir=None, n=0):
        if 0 <= x <= len_board and 0 <= y <= len_board:
            if board[y][x] == 1:
                return 0
            if (x, y) in black_list or (x, y) in path:
                return 0
            path.append((x, y))

            n += 1
            if prev_dir and prev_dir != cur_dir:
                n += 5

            if x == len_board and y == len_board:
                result.append(n - 1)
                path.pop()
                return 2
            dirs = [
                (0 if cur_dir == 'E' else 1, 'E'),
                (0 if cur_dir == 'S' else 1, 'S'),
                (0 if cur_dir == 'W' else 1, 'W'),
                (0 if cur_dir == 'N' else 1, 'N'),
            ]
            heapq.heapify(dirs)
            black_check = 0
            while dirs:
                d = heapq.heappop(dirs)[1]
                tmp = dfs(*get_pos(d, x, y), cur_dir, d, n)
                black_check += tmp
                if tmp == 2:
                    break

            path.pop()
            if black_check == 0:
                black_list.append((x, y))
        return 1
    dfs(0, 0, [])
    return min(result) * 100


data = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
data = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(data))
