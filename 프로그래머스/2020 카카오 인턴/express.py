from itertools import permutations


def solution(expression: str):
    op = ['*', '-', '+']
    result = []
    exp_list = []
    start = 0
    for i, s in enumerate(expression):
        if s in op:
            exp_list.append(expression[start:i])
            exp_list.append(expression[i:i+1])
            start = i + 1
    exp_list.append(expression[start:])
    for priority in permutations(op):
        exp = exp_list[:]
        for o in priority:
            run = True
            while run:
                try:
                    index = exp.index(o)
                    val = eval(exp[index - 1] + exp[index] + exp[index + 1])
                    exp = exp[:index - 1] + [str(val)] + exp[index + 2:]
                except ValueError:
                    run = False
        result.append(abs(int(exp[0])))
    return max(result)


print(solution('50*6-3*2'))
