from collections import defaultdict
from typing import List


class User:
    def __init__(self, s=0):
        self.score = s


def solution(info: List[str], query: List[str]):
    user_dict = [defaultdict(list) for _ in range(4)]
    result = []
    cache = defaultdict(int)

    for row in info:
        sp = row.split()
        user = User(int(sp[4]))
        for index in range(4):
            user_dict[index][sp[index]].append(user)
            user_dict[index]['-'].append(user)

    for q in query:
        if cache[q]:
            result.append(cache[q])
            continue
        result_set = set()
        sp = q.split()
        index = 0

        for w in sp:
            if w == 'and':
                continue
            if index == 0:
                result_set = set(user_dict[index][w])
                index += 1
            elif index < 4:
                tmp_set = set(user_dict[index][w])
                result_set = result_set & tmp_set
                index += 1
            else:
                w = int(w)
                ft = list(filter(lambda x: x.score >= w, result_set))
                result.append(len(ft))
                cache[q] = len(ft)
                break
    return result


data = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(data, query))
