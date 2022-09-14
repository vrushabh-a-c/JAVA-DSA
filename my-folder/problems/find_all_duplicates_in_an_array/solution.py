class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            curr = abs(num)
            if nums[curr-1]<0:
                res.append(curr)
            else:
                nums[curr-1] = -nums[curr-1]
                
        return res