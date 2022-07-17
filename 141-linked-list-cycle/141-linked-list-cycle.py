# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        left = head
        right = head.next
        while left!=right:
            if right==None or right.next==None:
                return False
            left = left.next
            right = right.next.next
        return True