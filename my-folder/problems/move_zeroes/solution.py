class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        end = len(nums)
        
        while i<end:
            if nums[i]==0:
                nums.append(0)
                del nums[i]
                end-=1
            else:
                i+=1
            
        