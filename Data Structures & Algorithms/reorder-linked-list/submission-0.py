# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        p1 = head
        p2 = prev

        while p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2
            p2.next = tmp1

            p1 = p1.next.next
            p2 = tmp2



            