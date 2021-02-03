def pingpong(x: int):
    if x <= 7:
        return x
    if x <= 14:
        return 14 - x

    def multiple(n):
        return (n % 7) == 0

    def contain(n):
        if n < 7:
            return False
        return True if (n % 10) == 7 else contain(n // 10)

    def rec(i, d, a):
        if i == x:
            return a
        if multiple(i) or contain(i):
            return rec(i + 1, -d, a - d)
        return rec(i + 1, d, a + d)

    return rec(15, 1, 1)


for i in range(1, 100):
    print(f'{i:2}', end=' ')
print('')
for i in range(1, 100):
    print(f'{pingpong(i):2}', end=' ')
