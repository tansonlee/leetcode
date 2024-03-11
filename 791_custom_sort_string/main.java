class Solution {
    public String customSortString(String order, String s) {
        HashMap<Character, Integer> counts = new HashMap<>();

        for (char c : s.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }

        StringBuilder result = new StringBuilder();
        for (char c : order.toCharArray()) {
            if (counts.containsKey(c)) {
                for (int i = 0; i < counts.get(c); ++i) {
                    result.append(c);
                }
            }
            counts.remove(c);
        }

        for (char c : counts.keySet()) {
            for (int i = 0; i < counts.get(c); ++i) {
                result.append(c);
            }
        }

        return result.toString();
    }
}
