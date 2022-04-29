class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        Area = 0
        while i<j:
            Area = max(Area,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return Area
   
        
#         i = 0
#         j = len(height)-1
#         Area = 0
#         while i<len(height) and j<len(height):
#             currArea = min(height[i],height[j])*(j-i)
#             if currArea > Area:
#                 Area = currArea
#             j -= 1
#             if i==j:
#                 i += 1
#                 j = len(height)-1
#             if i==j==len(height)-1:
#                 break
#         return Area
