import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(lst):
    lst = collections.deque(lst)
    root = TreeNode(lst.popleft())
    q = collections.deque([root])

    while q:
        node = q.popleft()
        try:
            node.left, node.right = TreeNode(lst.popleft()), TreeNode(lst.popleft())
            q.append(node.left)
            q.append(node.right)
        except IndexError:
            break
    return root


def print_tree(root: TreeNode):
    q = collections.deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def deserialize(string):
    lst = string.split()
    index = 1
    root = TreeNode(int(lst[0]))
    q = collections.deque([root])

    while q:
        if index >= len(lst):
            break
        node = q.popleft()
        if lst[index] != '#':
            node.left = TreeNode(int(lst[index]))
            q.append(node.left)
        index += 1

        if lst[index] != '#':
            node.right = TreeNode(int(lst[index]))
            q.append(node.right)
        index += 1

    return root


def serialize(root: TreeNode):
    result = []
    length = 0
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(str(node.val))
            length += 1
            q.append(node.left)
            q.append(node.right)
        else:
            result.append('#')
    n = i = 0
    while n < length:
        n += 2 ** i
        i += 1
    s = ' '.join(result[:n])
    return s
