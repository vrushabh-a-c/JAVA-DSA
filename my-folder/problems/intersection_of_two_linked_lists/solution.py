# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = len2 = 0
        tempA,tempB = headA,headB
        
        while tempA:
            len1+=1
            tempA = tempA.next
            
        while tempB:
            len2+=1
            tempB = tempB.next
            
        tempA,tempB = headA,headB
        
        if len1>len2:
            for i in range(len1-len2):
                tempA = tempA.next
                
        elif len2>len1:
            for i in range(len2-len1):
                tempB = tempB.next
                
        
        while tempA!=tempB:
            tempA = tempA.next
            tempB = tempB.next
            
        
        return tempA