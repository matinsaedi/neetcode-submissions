"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        arr = []
        current = head

        while current:
            arr.append(current.val)
            current = current.next

        node = None
        for val in arr[::-1]:
            node = Node(val, next=node)

        new_head = node

        hash_map = {}

        p1, p2 = head, new_head

        while p1 and p2:
            hash_map[p1] = p2
            p1 = p1.next
            p2 = p2.next

        for node in hash_map:
            current = hash_map[node]
            if node.random != None:
                current.random = hash_map[node.random]

        return new_head
        


        



        








        