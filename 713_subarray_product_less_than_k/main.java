class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int front = 0;
        int back = 0;
        int product = nums[0];
        int result = 0;

        while (back < nums.length) {
            if (product < k) {
                result += (back - front + 1);
            }
            if (product < k || back <= front) {
                ++back;
                if (back >= nums.length) break;
                product *= nums[back];
            } else {
                product /= nums[front];
                ++front;
            }
        }

        return result;
    }
}
