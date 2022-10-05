class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int currCount = 0;
        int maxCount = 0;
        for(int n:nums){
            if(n==1){
                currCount++;
                maxCount = Math.max(maxCount,currCount);
            }
            else
                currCount = 0;
        }
        return maxCount;
    }
}