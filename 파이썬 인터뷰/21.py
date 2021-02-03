import collections


def remove_duplicate_letters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + remove_duplicate_letters(suffix.replace(char, ''))
    return ''


def remove_duplicate_letters(s):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)


print(remove_duplicate_letters('cbacdcbc'))
