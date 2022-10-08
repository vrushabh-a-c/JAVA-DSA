class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> list = new ArrayList<>();
        if(nums.length<4)
            return list;
        Arrays.sort(nums);
        int len = nums.length;
        
        for(int i=0;i<len-3;i++){
            if(i==0 || i>0 && nums[i]!=nums[i-1]){
                for(int j=i+1;j<len-2;j++){
                    if(j==i+1 || (j>i+1 && nums[j]!=nums[j-1])){
                        long sum = nums[i]+nums[j];
                        long new_target = ((long)target-sum);
                        int left = j+1;
                        int right = len-1;
                        while(left<right){
                            int curr_sum = nums[left]+nums[right];
                            if(curr_sum==new_target){
                                list.add(Arrays.asList(nums[i],nums[j],nums[left],nums[right]));
                                while(left<right && nums[left]==nums[left+1])
                                    left++;
                                while(left<right && nums[right]==nums[right-1])
                                    right--;
                                left++;
                                right--;
                            }
                            else if(curr_sum<new_target)
                                left++;
                            else
                                right--;
                        }
                    }
                }
            }
        }
        return list;
    }
}