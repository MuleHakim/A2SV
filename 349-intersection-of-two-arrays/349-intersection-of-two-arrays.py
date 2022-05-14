class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myStack = []
        for i in range(len(nums2)):
            if nums2[i] in nums1 and nums2[i] not in myStack:
                myStack.append(nums2[i])
        return myStack