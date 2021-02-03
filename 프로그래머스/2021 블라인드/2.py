from collections import defaultdict, Counter
from itertools import combinations


def solution(orders, course):
    candidate = [defaultdict(int) for _ in course]
    result = []

    for o in orders:
        for i in range(2, len(o) + 1):
            if i not in course:
                break
            comb = combinations(o, i)
            for c in comb:
                len_c = len(c)
                if len_c in course:
                    candidate[course.index(len_c)][tuple(sorted(c))] += 1

    for c in candidate:
        counter = Counter(c)
        menu_list = counter.most_common()

        if len(menu_list) == 0:
            break

        prev_count = menu_list[0][1]

        for menu in menu_list:
            if menu[1] < 2:
                break

            if menu[1] != prev_count:
                break

            prev_count = menu[1]
            result.append(''.join(menu[0]))

    return sorted(result)


print(solution(['ABC', 'AB', 'AC'], [2,3,4]))
