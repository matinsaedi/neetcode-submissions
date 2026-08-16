# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque([root])
        visited = {root}

        while queue:
            level_size = len(queue)
            level_res = []

            for i in range(level_size):
                node = queue.popleft()
                level_res.append(node.val)

                for child in (node.left, node.right):
                    if child and child not in visited:
                        queue.append(child)
                        visited.add(child)
            res.append(level_res)
        
        return res





            

        