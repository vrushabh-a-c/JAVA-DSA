class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int low = 0;
        int high = n-1;
        if(n==1)
            return nums[0];
        if(n==2)
            return Math.min(nums[0],nums[1]);
        
        while(low<=high){
            if(nums[low]<nums[high])
                return nums[low];
            int mid = low+(high-low)/2;
            if(nums[mid]>nums[mid+1])
                return nums[mid+1];
            if(nums[mid]<nums[mid-1])
                return nums[mid];
            if(nums[mid]<nums[high])
                high = mid-1;
            else
                low = mid+1;
        }
        return 0;
    }
}