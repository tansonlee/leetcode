class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];

        int pre_curr = 1;
        for (int i = 0; i < nums.length; ++i) {
            pre_curr *= nums[i];
            pre[i] = pre_curr;
        }

        int post_curr = 1;
        for (int i = nums.length - 1; i >= 0; --i) {
            post_curr *= nums[i];
            post[i] = post_curr;
        }

        int[] result = new int[nums.length];
        result[0] = post[1];
        result[nums.length - 1] = pre[nums.length - 2];
        for (int i = 1; i < nums.length - 1; ++i) {
            result[i] = pre[i - 1] * post[i + 1];
        }

        return result;
        
    }
}
