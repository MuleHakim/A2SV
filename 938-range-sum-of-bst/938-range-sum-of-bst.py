# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        r = root
        if low<=r.val<=high:
            return r.val + self.rangeSumBST(r.left,low,high) + self.rangeSumBST(r.right,low,high)
        else:
            return self.rangeSumBST(r.left,low,high) + self.rangeSumBST(r.right,low,high)
        