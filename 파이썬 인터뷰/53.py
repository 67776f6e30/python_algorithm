from TreeNode import TreeNode, deserialize
import sys


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def min_diff_in_bst(self, root: TreeNode) -> int:
        if root.left:
            self.min_diff_in_bst(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.min_diff_in_bst(root.right)
        return self.result


s = Solution()
data = s.min_diff_in_bst(deserialize('8 4 12 2 6 # # 1 3 5 7 # # # #'))
print(data)
