class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int number1 = -1;
        int number2 = -1;
        int count1 = 0;
        int count2 = 0;
        int n = nums.length;
        
        for(int i=0;i<n;i++){
            if(nums[i]==number1)
                count1++;
            else if(nums[i]==number2)
                count2++;
            else if(count1==0){
                number1 = nums[i];
                count1++;
            }
            else if(count2==0){
                number2 = nums[i];
                count2++;
            }
            else{
                count1--;
                count2--;
            }
        }
        List<Integer> list = new ArrayList<>();
        count1 = 0;
        count2 = 0;
        for(int i=0;i<n;i++){
            if(nums[i]==number1)
                count1++;
            else if(nums[i]==number2)
                count2++;
        }
        
        if(count1>(n/3))
            list.add(number1);
        if(count2>(n/3))
            list.add(number2);
        
        return list;
    }
}