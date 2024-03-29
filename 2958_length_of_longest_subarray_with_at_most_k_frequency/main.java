class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();

        int front = 0;
        int result = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; ++i) {
            counts.put(nums[i], counts.getOrDefault(nums[i], 0) + 1);
            while (counts.get(nums[i]) > k) {
                counts.put(nums[front], counts.get(nums[front]) - 1);
                ++front;
            }

            result = Math.max(result, (i - front + 1));
        }

        return result;
    }
}
