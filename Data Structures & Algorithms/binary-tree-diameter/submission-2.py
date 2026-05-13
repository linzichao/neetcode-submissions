# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.long = 0

        def dfs(r):
            if r:
                left, right = dfs(r.left), dfs(r.right)
                self.long = max(self.long, left + right)
                return max(left, right) + 1
            return 0
        
        dfs(root)
        return self.long