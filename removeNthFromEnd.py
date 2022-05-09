# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return None
        
        result = ListNode()
        result.next = head
        right = result
        left = result
        
        for i in range(n):
            right = right.next
        while right.next != None:
            right = right.next
            left = left.next
        left.next = left.next.next

        return result.next
