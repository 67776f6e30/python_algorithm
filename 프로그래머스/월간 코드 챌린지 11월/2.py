def solution(s):
    result = [0, 0]

    def func(d: str):
        if not d or d == "1":
            return
        zero_cnt = d.count("0")
        result[0] += 1
        result[1] += zero_cnt
        return format(len(d) - zero_cnt, "b")

    _ = s
    while True:
        _ = func(_)
        if not _:
            break

    return result


data = "110010101001"
print(solution(data))
