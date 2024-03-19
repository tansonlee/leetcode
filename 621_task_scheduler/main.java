class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> frequencyMap = new HashMap<>();
        
        for (char c : tasks) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Character, Integer>> heap = new PriorityQueue<>(new Comparator<Map.Entry<Character, Integer>>() {
            @Override
            public int compare(Map.Entry<Character, Integer> entry1, Map.Entry<Character, Integer> entry2) {
                return entry2.getValue() - entry1.getValue(); // Sort in descending order of frequencies
            }
        });
        
        heap.addAll(frequencyMap.entrySet());

        int result = 0;
        while (!heap.isEmpty()) {
            Map<Character, Integer> putBack = new HashMap<>();
            result += n + 1;
            for (int i = 0; i < n + 1; ++i) {
                if (heap.isEmpty() && putBack.isEmpty()) {
                    result -= (n - i + 1);
                    break;
                }
                if (heap.isEmpty()) {
                    break;
                }
                Map.Entry<Character, Integer> next = heap.peek();
                if (putBack.containsKey(next.getKey())) {
                    break;
                }

                heap.poll();
                if (next.getValue() > 1) {
                    putBack.put(next.getKey(), next.getValue() - 1);
                }
            }
            for (Map.Entry<Character, Integer> x : putBack.entrySet()) {
                heap.offer(x);
            }
        }

        return result;
    }
}
