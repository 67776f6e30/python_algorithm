import collections
from TreeNode import make_tree, print_tree


def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root


def invert_tree(root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root


data = make_tree([4, 2, 7, 1, 3, 6, 9])
print_tree(invert_tree(data))
