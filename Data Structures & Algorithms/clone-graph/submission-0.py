"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}
        current = node
                
        def dfs(node):
            if not node:
                return

            if node not in old_to_new:
                old_to_new[node] = Node(node.val)
                for n in node.neighbors:
                    old_to_new[node].neighbors.append(dfs(n))

            if node in old_to_new:
                return old_to_new[node]

            
        
        return dfs(node)

            








        