# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good_count = 0

        def dfs(node, prev_max):
            if not node:
                return 

            if node.val >= prev_max:
                self.good_count += 1
            
            new_max = max(prev_max, node.val)

            dfs(node.left, new_max)
            dfs(node.right, new_max)


        dfs(root, -float("inf"))
        return self.good_count
