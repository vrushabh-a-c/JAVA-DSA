class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        int low = 0;
        int high = n-1;
        int first = -1;
        int last = -1;
        while(low<=high){
            int mid = low+(high-low)/2;
            if(nums[mid]==target){
                first = mid;
                last = mid;
                while(first>=0 && nums[first]==target)
                    first--;
                while(last<n && nums[last]==target)
                    last++;
                return new int[]{first+1,last-1};
            }
            else if(nums[mid]<target)
                low = mid+1;
            else
                high = mid-1;
        }
        return new int[]{-1,-1};
    }
}