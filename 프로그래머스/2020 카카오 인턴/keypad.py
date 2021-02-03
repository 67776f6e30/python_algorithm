from collections import deque


def solution(numbers, hand):
    result = ''
    graph = {
        1: [2],
        2: [5],
        3: [2],
        4: [5],
        5: [2, 8],
        6: [5],
        7: [8],
        8: [0, 5],
        9: [8],
        0: [8],
        '#': [0],
        '*': [0]
    }

    def dfs(position, target, visit):
        distance = 0
        visit.append(position)
        if position == target:
            return 1
        for i in graph[position]:
            if i in visit:
                continue
            distance += dfs(i, target, visit)
        return distance + 1 if distance > 0 else 0

    right = ['#']
    left = ['*']
    for n in numbers:
        if n in [1, 4, 7]:
            left.append(n)
            result += 'L'
        elif n in [3, 6, 9]:
            right.append(n)
            result += 'R'
        else:
            right_distance = dfs(right[-1], n, [])
            left_distance = dfs(left[-1], n, [])
            if right_distance < left_distance:
                right.append(n)
                result += 'R'
            elif left_distance < right_distance:
                left.append(n)
                result += 'L'
            else:
                if hand == 'right':
                    right.append(n)
                    result += 'R'
                else:
                    left.append(n)
                    result += 'L'
    return result


data = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(data, 'right'))
