# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            if root is None:
                return 0
            return max(height(root.left),height(root.right))+1
        
        
        if root is None:
            return 0
        
        lheight = height(root.left)
        rheight = height(root.right)
        
        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)
        
        return max(lheight+rheight,max(ldia,rdia))
        