class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> hash = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int diff = target-nums[i];
            if(hash.containsKey(diff)){
                int ans[] = {hash.get(diff),i};
                return ans;
            }
            hash.put(nums[i],i);
        }
        return null;
    }
}