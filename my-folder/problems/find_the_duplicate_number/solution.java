class Solution {
    public int findDuplicate(int[] nums) {
        for(int num:nums){
            int idx = Math.abs(num);
            if(nums[idx]<0)
                return idx;
            nums[idx] = -nums[idx];
        }
        return nums.length;
    }
}