from TreeNode import TreeNode, serialize


def build_tree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))

        node = TreeNode(inorder[index])
        node.left = build_tree(preorder, inorder[0:index])
        node.right = build_tree(preorder, inorder[index + 1:])

        return node


p = [1, 2, 4, 5, 3, 6, 7, 9, 8]
i = [4, 2, 5, 1, 7, 9, 6, 8, 3]
print(serialize(build_tree(p, i)))
