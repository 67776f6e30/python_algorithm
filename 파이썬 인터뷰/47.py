from TreeNode import TreeNode
import collections


def deserialize(string):
    index = 1
    root = TreeNode(string[0])
    q = collections.deque([root])

    while q:
        if index >= len(string):
            break
        node = q.popleft()
        if string[index] != '#':
            node.left = TreeNode(int(string[index]))
            q.append(node.left)
        index += 1

        if string[index] != '#':
            node.right = TreeNode(int(string[index]))
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
    s = ''.join(result)
    n = i = 0
    while n < length:
        n += 2 ** i
        i += 1
    return s[:n]


#print(serialize(make_tree([1, 2, 3, 4, 5, 6, 7])))
print(serialize(deserialize('12345##')))
