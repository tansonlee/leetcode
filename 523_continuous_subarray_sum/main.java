class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int[] cumulative = new int[nums.length];
        cumulative[0] = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            cumulative[i] = cumulative[i - 1] + nums[i];
        }

        HashSet<Integer> mods = new HashSet<>();
        int addNext = 0; // delay adding b/c need at least 2 elements in subarray.
        for (int i = 0; i < cumulative.length; ++i) {
            if (i > 0 && cumulative[i] == 0)  {
                return true; // 0 is always a multiple of k
            }
            if (mods.contains(cumulative[i] % k)) {
                return true;
            }

            mods.add(addNext);
            addNext = cumulative[i] % k;
        }

        return false;
    }
}
