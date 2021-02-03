def solution(begin, target, words):
    if target not in words:
        return 0

    result = []

    def check(left, right):
        diff = 0
        for index, c in enumerate(right):
            if left[index] != c:
                diff += 1
            if diff > 1:
                return False
        return True

    def dfs(b, t, w, n):
        if b == t:
            result.append(n)
            return

        if b in w:
            w.remove(b)

        if not w:
            return

        for word in w:
            if check(b, word):
                dfs(word, t, w[:], n + 1)

    dfs(begin, target, words, 0)

    return min(result)


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
