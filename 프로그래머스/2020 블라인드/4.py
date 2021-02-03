from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.len = 0
        self.wild = False
        self.reverse = False


class QueryTrie:
    def __init__(self, s):
        self.root = TrieNode()
        self.insert(s)

    def insert(self, s=''):
        node = self.root
        node.len = len(s)
        if s[0] == '?':
            node.reverse = True
            s = reversed(s)
        for c in s:
            if c == '?':
                node.wild = True
            node = node.child[c]
            node.val = c

    def match(self, s):
        node = self.root
        if node.len != len(s):
            return False
        if node.reverse:
            s = reversed(s)
        for c in s:
            if node.wild:
                return True
            if c not in node.child:
                return False
            node = node.child[c]


def solution(words, queries):
    answer = [0] * len(queries)
    for i, q in enumerate(queries):
        trie = QueryTrie(q)
        for w in words:
            answer[i] += trie.match(w)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
