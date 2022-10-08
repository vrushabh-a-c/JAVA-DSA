class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        if(nums.length<3)
            return list;
        int n = nums.length;
        for(int i=0;i<n-2;i++){
            if(i>0 && nums[i]==nums[i-1])
                continue;
            int left = i+1;
            int right = n-1;
            while(left<right){
                int currSum = nums[i]+nums[left]+nums[right];
                if(currSum==0){
                    list.add(Arrays.asList(nums[i],nums[left],nums[right]));
                    
                    while(left<right && nums[left]==nums[left+1])
                        left++;
                    while(left<right && nums[right]==nums[right-1])
                        right--;
                    left++;
                    right--;
                }
                else if(currSum>0)
                    right--;
                else
                    left++;
            }
        }
        return list;
    }
}