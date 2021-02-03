import collections
import re


def solution(str1: str, str2: str) -> int:
    str1s = [
        str1[i:i + 2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i:i + 2].lower())
    ]
    str2s = [
        str2[i:i + 2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i + 2].lower())
    ]

    intersection = sum((collections.Counter(str1s) &
                        collections.Counter(str2s)).values())
    union = sum((collections.Counter(str1s) |
                        collections.Counter(str2s)).values())

    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)


print(solution('aa1+aa2', 'AAAA12'))
