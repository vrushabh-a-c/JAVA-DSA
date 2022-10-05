class Solution {
    public static void swap(int[] nums,int i,int j){
        int data = nums[j];
        nums[j] = nums[i];
        nums[i] = data;
    }
    public static void reverse(int[] nums,int low, int high)
    {
        for(int i=low,j=high;i<j;i++,j--)
            swap(nums,i,j);
    }
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        if(k>len)
            k = k%len;
        if(k<0)
            return;
        //reverse last k elements
        reverse(nums,len-k,len-1);
        //reverse first k elements
        reverse(nums,0,len-k-1);
        //reverse the entire array
        reverse(nums,0,len-1);
    }
}