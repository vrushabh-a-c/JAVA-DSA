class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = -1
        votes = 0
        
        for i in range(len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes+=1
            else:
                if nums[i]==candidate:
                    votes+=1
                else:
                    votes-=1
                    
        count = 0
        
        for i in range(len(nums)):
            if nums[i]==candidate:
                count+=1
            
        if count>(len(nums))//2:
            return candidate
    
        return -1