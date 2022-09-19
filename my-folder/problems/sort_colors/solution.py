class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        i = 0
        count = 0
        while count<len(nums):
            if nums[i]==0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[right],nums[i] = nums[i],nums[right]
                right-=1
            count+=1
        return nums