# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            l = []

            for i in range(level_size):
                node = queue.popleft()
                l.append(node.val)

                for child in (node.left, node.right):
                    if child:
                        queue.append(child)
            res.append(l)

        return [l[-1] for l in res]
