# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        
        queue = []
        return_list = []
        queue.append(root)
        
        while len(queue)>0:
            ans = []
            l = len(queue)
            
            for i in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
                
            return_list.append(ans)
            
        return return_list
    
        
        