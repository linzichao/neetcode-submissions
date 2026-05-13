# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(r, sub_r):
            if not r and not sub_r:
                return True
            elif (r and not sub_r) or (not r and sub_r):
                return False
            else:
                if r.val == sub_r.val:
                    return is_same(r.left, sub_r.left) and is_same(r.right, sub_r.right)
                return False
            
        
        def dfs(r, sub_r):
            if not r and not sub_r:
                return True
            elif r and sub_r:
                if is_same(r, sub_r):
                    return True
                return dfs(r.left, sub_r) or dfs(r.right, sub_r)
            
            return False

        return dfs(root, subRoot)

