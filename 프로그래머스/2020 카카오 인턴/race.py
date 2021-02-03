import heapq
from collections import deque


def solution(board):
    memo = [
        [[0, 0]] * len(board) for n in board
    ]
    q = deque([(0, 0)])
    while q:
        node = q.popleft()
    return


data = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
data = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(data))
