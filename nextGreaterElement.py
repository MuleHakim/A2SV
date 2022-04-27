class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        index = {}
        for i,n in enumerate(nums2):
            index[n] = i
        for n in nums1:
            idx = index[n]
            for j in nums2[idx+1:]:
                if j > n:
                    output.append(j)
                    break
            else:
                output.append(-1)
        return output
