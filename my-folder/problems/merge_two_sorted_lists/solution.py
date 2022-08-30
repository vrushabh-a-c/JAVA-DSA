# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1==None:
            return list2
        if list2==None:
            return list1
    
        temp = dummy = ListNode(0)
        
        while list1 and list2:
            if list1.val<=list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            elif list1.val>list2.val:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
        
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return temp.next
        
        