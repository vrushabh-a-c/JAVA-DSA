class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictionary = {}
        dictionary[0] = 1
        curr_sum = 0
        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum-k in dictionary:
                count+=dictionary[curr_sum-k]
            if curr_sum in dictionary:
                dictionary[curr_sum]+=1
            else:
                dictionary[curr_sum]=1
        
        return count