# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        if not head:
            return head
        while left.next!=None:
            if left.val == left.next.val:
                nextNode = left.next
                left.val = nextNode.val
                left.next = nextNode.next
            else:
                left = left.next
        return head
        
