def solution(p):
    def bracket_check(string):
        if len(string) == 0 or len(string) % 2 == 1 or string[0] == ')' or string[-1] == '(':
            return False
        stack = []
        for c in string:
            if c == '(':
                stack.append(c)
            else:
                try:
                    stack.pop()
                except IndexError:
                    return False
        if len(stack):
            return False
        return True

    def rec(string):
        len_s = len(string)
        count = 0
        u = v = ''

        if len_s == 0:
            return ''

        for i in range(len_s):
            count += 1 if string[i] == '(' else -1
            if count == 0:
                u = string[:i+1]
                v = string[i+1:]
                break

        if u in ('()', ')(') and v == '':
            return '()'

        v = rec(v)
        if bracket_check(u):
            return u + v
        else:
            rev = ''
            for i in range(1, len(u) - 1):
                rev += '(' if u[i] == ')' else ')'
            return '(' + v + ')' + rev

    if bracket_check(p):
        return p

    return rec(p)


print(solution("()))((()"))

