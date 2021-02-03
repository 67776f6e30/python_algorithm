def solution(s):
    result = []
    len_s = len(s)
    if len_s < 2:
        return len_s

    for unit in range(1, (len_s // 2) + 1):
        string = ''
        prev = s[0:unit]
        count = 1
        for left in range(unit, len(s), unit):
            substr = s[left:left+unit]
            if prev == substr:
                count += 1
            else:
                string += str(count if count > 1 else '') + prev
                count = 1
            prev = substr
        string += str(count if count > 1 else '') + prev
        result.append(len(string))
    return min(result)


print(solution("a"))
