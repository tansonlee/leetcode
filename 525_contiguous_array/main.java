class Solution {
    public int findMaxLength(int[] nums) {
        int[] cumulative = new int[nums.length + 1];
        cumulative[0] = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == 1) {
                cumulative[i+1] = cumulative[i] + 1;
            } else {
                cumulative[i+1] = cumulative[i] - 1;
            }
        }

        HashMap<Integer, Integer> found = new HashMap<>();
        int result = 0;
        for (int i = 0; i < cumulative.length; ++i) {
            if (found.containsKey(cumulative[i])) {
                result = Math.max(result, i - found.get(cumulative[i]));
            } else {
                found.put(cumulative[i], i);
            }
        }
        
        return result;
    }
}
