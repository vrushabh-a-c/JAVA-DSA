class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_list = set()
        for _ in nums:
            set_list.add(_)
        
        if len(set_list)==len(nums):
            return False
        else:
            return True
        