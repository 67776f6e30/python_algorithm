def solution(a):
    MOD = 10000019

    def combine(row):
        nCr = [[0] * (row + 1) for _ in range(row + 1)]
        nCr[0][0] = 1
        for i in range(1, row + 1):
            for j in range(i + 1):
                if i == j:
                    nCr[i][j] = 1
                else:
                    nCr[i][j] = nCr[i-1][j-1] + nCr[i-1][j]
                nCr[i][j] %= MOD
        return nCr

    def get_one_cnt(row, col):
        one_cnt = [0] * (col + 1)
        for i in range(row):
            for j in range(col):
                one_cnt[j+1] += a[i][j]
        return one_cnt

    row = len(a)
    col = len(a[0])
    nCr = combine(row)
    one_cnt = get_one_cnt(row, col)
    DP = [[0] * (row + 1) for _ in range(col + 1)]
    DP[1][row - one_cnt[1]] = nCr[row][row - one_cnt[1]]

    for c in range(1, col):
        oc = one_cnt[c]
        for even_num in range(row + 1):
            if DP[c][even_num] == 0:
                continue
            for k in range(oc + 1):
                if even_num < k:
                    continue
                be_even_num = even_num + oc - (2 * k)
                if be_even_num > row:
                    continue
                result = (nCr[even_num][k] * nCr[row - even_num][oc - k]) % MOD
                DP[c + 1][be_even_num] = (DP[c + 1][be_even_num] + DP[c][even_num] * result) % MOD

    return DP[col][row]


data = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
print(solution(data))
