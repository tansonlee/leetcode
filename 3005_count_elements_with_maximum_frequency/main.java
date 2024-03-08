import java.util.HashMap;

class Solution {
    public int maxFrequencyElements(int[] nums) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        int maxCount = 0;
        int result = 0;

        for (int num : nums) {
            int newCount = counts.getOrDefault(num, 0) + 1;
            counts.put(num, newCount);
            if (newCount > maxCount) {
                maxCount = newCount;
                result = 0;
            }
            if (newCount == maxCount) {
                result += counts.get(num);
            }
        }

        return result;
    }
}
