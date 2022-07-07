# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        nums = []
        while(start):
            nums.append(start.val)
            start = start.next
        
        left, right = 0, len(nums) - 1
        newnums = []
        while(left <= right):
            if left == right:
                newnums.append(nums[left])
                break
            else:
                newnums.append(nums[left])
                newnums.append(nums[right])
            left += 1
            right -= 1
        
        start = head
        
        for i in newnums:
            start.val = i
            start = start.next