# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        
        self.res = []
        def dfs(node):
            if not node.left and not node.right:
                self.res.append(node.val)
                return
            
            

            dfs(node.left) if node.left else None
            
            if len(self.res) == k:
                return

            self.res.append(node.val)
            dfs(node.right) if node.right else None
        
        dfs(root)
        return self.res[k - 1]