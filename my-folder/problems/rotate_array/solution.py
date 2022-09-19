class Solution(object):
    def reverse(self,nums,i,j):
        left = i
        right = j
        while left<right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            
            left+=1
            right-=1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        if k<0:
            k +=n
        
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)