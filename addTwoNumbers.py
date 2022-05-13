# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode((l1.val + l2.val)%10)
        extra = (l1.val + l2.val)//10
        curNode = result
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            
            curNode.next = ListNode((extra + l1.val + l2.val)%10)
            extra = (extra + l1.val + l2.val)//10
            curNode = curNode.next
        while(l1.next):
            l1 = l1.next
            curNode.next = ListNode((extra + l1.val)%10)
            extra = (extra + l1.val)//10
            curNode = curNode.next
        while(l2.next):
            l2 = l2.next
            curNode.next = ListNode((extra + l2.val)%10)
            extra = (extra + l2.val)//10
            curNode = curNode.next
        if extra > 0:
            curNode.next = ListNode(1)
            
        return result
