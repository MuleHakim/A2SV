# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        p = collections.defaultdict(list) 
        queue = [(root,0)]
        while queue:
            new = []
            dict_ = collections.defaultdict(list)
            for node, s in queue:
                dict_[s].append(node.val) 
                if node.left:
                    new += (node.left, s-1), 
                if node.right:
                    new += (node.right,s+1),  
            for i in dict_:
                p[i].extend(sorted(dict_[i]))
            queue = new
        output = []
        for i in sorted(p):
            output.append(p[i])
        return output