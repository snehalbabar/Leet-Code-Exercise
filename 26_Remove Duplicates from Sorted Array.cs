public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int IndexCnt=1;
        int len = nums.Length;
        for(int i =1 ; i< len; i++)
        {
           if(nums[i] != nums[i-1])
           {
               nums[IndexCnt] =  nums[i];
               IndexCnt ++;
           }
        }
        return IndexCnt;
    }
}