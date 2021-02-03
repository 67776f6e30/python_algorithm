def solution(key, lock):
    def rotate_left():
        len_k = len(key)
        k = [
            [0] * len_k for _ in range(len_k)
        ]
        for i in range(len_k):
            for j in range(len_k):
                k[j][i] = key[i][len_k-1-j]
        return k

    for _ in range(4):
        key = rotate_left()


key_ = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_ = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key_, lock_)
