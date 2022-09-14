# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def recursive(node,num):
            num ^= pow(2,node.val-1)
            if node.left == None and node.right == None:
                bs = bin(num)[2:]
                if bs.count('1') <= 1:
                    self.res += 1
                return
            if node.left != None:
                recursive(node.left,num)
            if node.right != None:
                recursive(node.right,num)
        self.res = 0
        recursive(root,0)
        return self.res