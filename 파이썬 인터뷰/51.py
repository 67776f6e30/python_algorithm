from TreeNode import TreeNode, deserialize, serialize


class Solution:
    val: int = 0

    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bst_to_gst(root.right)
            self.val += root.val
            root.val = self.val
            self.bst_to_gst(root.left)
        return root


s = Solution()
data = s.bst_to_gst(deserialize('4 1 6 0 2 5 7 # # # 3 # # # 8'))
print(serialize(data))
