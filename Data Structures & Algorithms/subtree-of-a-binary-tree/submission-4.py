# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(don, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t: return True
        if not s: return False

        if don.sameTree(s,t):
            return True
        return (don.isSubtree(s.left,t) or don.isSubtree(s.right,t))

    def sameTree(don,s,t):
        if not s and not t: return True
        if s and t and s.val ==t.val:
            return (don.sameTree(s.left,t.left) and don.sameTree(s.right,t.right))
        return False