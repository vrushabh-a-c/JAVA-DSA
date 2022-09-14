class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            curr = abs(num)-1
            if nums[curr]>0:
                nums[curr]*=-1
            
        return [i+1 for i in range(len(nums)) if nums[i]>0]