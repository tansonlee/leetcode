class Solution {
    public long countSubarrays(int[] nums, int k) {
        int maxElement = Integer.MIN_VALUE;
        for (int n : nums) {
            maxElement = Math.max(maxElement, n);
        }

        int[] cumulativeMaxCount = new int[nums.length + 1];
        cumulativeMaxCount[0] = 0;
        for (int i = 0; i < nums.length; ++i) {
            cumulativeMaxCount[i + 1] = cumulativeMaxCount[i] + (nums[i] == maxElement ? 1 : 0);
        }

        Map<Integer, Integer> countNOrLower = new HashMap<>();
        for (int i = 0; i < cumulativeMaxCount.length; ++i) {
            countNOrLower.put(cumulativeMaxCount[i], i + 1);
        }

        long result = 0;

        for (int i = 0; i < cumulativeMaxCount.length; ++i) {
            int underN = cumulativeMaxCount[i] - k;
            while (underN > 0 && !countNOrLower.containsKey(underN)) {
                underN--;
            }

            int r = countNOrLower.getOrDefault(underN, 0);
            result += r;
        }

        return result;
    }
}
