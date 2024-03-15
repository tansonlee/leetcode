class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int prev = 0;
        int result = 0;
        
        HashMap<Integer, Integer> found = new HashMap<>();
        found.put(0, 1);

        for (int i = 0; i < nums.length; ++i) {
            int curr = nums[i] + prev;
            prev = curr;

            if (found.containsKey(curr - goal)) {
                result += found.get(curr - goal);
            }
            found.put(curr, found.getOrDefault(curr, 0) + 1);
        }
        return result;
    }
}
