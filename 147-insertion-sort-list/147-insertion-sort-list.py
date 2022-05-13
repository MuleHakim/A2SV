# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        curr = head
        while curr != None:
            temp = curr.next
            left = result
            right = result.next
            while right != None:
                if right.val > curr.val:
                    break
                left = right
                right = right.next
            curr.next = right
            left.next = curr
            curr = temp
        return result.next