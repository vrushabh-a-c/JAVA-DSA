class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = sys.maxint
        ans = 0
        for left in range(len(nums)-2):
            mid = left+1
            right = len(nums)-1
            while mid<right:
                curr_sum = nums[left]+nums[mid]+nums[right]
                if(curr_sum==target):
                    return curr_sum
                elif(curr_sum<target):
                    if(abs(curr_sum-target)<min_diff):
                        min_diff = abs(curr_sum-target)
                        ans = curr_sum
                    mid = mid+1
                elif(curr_sum>target):
                    if(abs(curr_sum-target)<min_diff):
                        min_diff = abs(curr_sum-target)
                        ans = curr_sum
                    right = right-1
        return ans