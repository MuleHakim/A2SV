class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2:
            for i in range(n):
                nums1.pop(m)
                nums1.append(nums2[i])
            nums1.sort()