# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(root1,root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is not None and root2 is not None and root1.val==root2.val:
                return isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
            
            return False
        
        return isMirror(root,root)