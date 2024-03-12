/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        while (true) {
            // Find the cumulative sum of values in the list.
            ArrayList<Integer> cumulativeSums = new ArrayList<>();
            cumulativeSums.add(0); // Add zero because initial cumulative sum is 0.
            ListNode curr = head;
            while (curr != null) {
                cumulativeSums.add(cumulativeSums.get(cumulativeSums.size() - 1) + curr.val);
                curr = curr.next;
            }

            // Find 2 indicies whose cumulative sums match.
            int start = -2;
            int end = -2;
            HashMap<Integer, Integer> found = new HashMap<>();
            for (int i = 0; i < cumulativeSums.size(); ++i) {
                if (found.containsKey(cumulativeSums.get(i))) {
                    start = found.get(cumulativeSums.get(i)) - 1;
                    end = i - 1;
                    break;
                } else {
                    found.put(cumulativeSums.get(i), i);
                }
            }

            // None match so no more to delete.
            if (start == -2) {
                return head;
            }

            // Delete the nodes between start and end.
            if (start == -1) {
                for (int i = 0; i < end + 1; ++i) {
                    head = head.next;
                }
            } else {
                ListNode startNode = head;
                for (int i = 0; i < start; ++i) {
                    startNode = startNode.next;
                }

                ListNode endNode = head;
                for (int i = 0; i < end; ++i) {
                    endNode = endNode.next;
                }

                startNode.next = endNode.next;
            }
        }
    }
}
