import re


def solution(new_id: str):
    char_filter = '1234567890abcdefghijklmnopqrstuvwxyz.-_'
    id_str = ''
    len_id = 0
    prev = ''

    for c in new_id.lower():
        if len_id == 15:
            break
        if (c in char_filter) and not prev == c == '.':
            if c == '.' and len_id == 0:
                continue
            id_str += c
            len_id += 1
            prev = c

    if len_id == 0:
        id_str = 'a'
        len_id = 1

    if id_str[-1] == '.':
        id_str = id_str[:-1]
        len_id -= 1

    if len_id <= 2:
        id_str += id_str[-1] * (3 - len_id)

    return id_str

data = "...!@BaT#*..y.abcdefghijklm"
print(solution("z-+.^."))
