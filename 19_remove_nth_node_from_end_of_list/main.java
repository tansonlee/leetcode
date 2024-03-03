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
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode fast = head;
        for (int i = 0; i < n; ++i) {
            fast = fast.next;
        }

        ListNode slow = head;
        ListNode prev = null;

        while (fast != null) {
            fast = fast.next;
            prev = slow;
            slow = slow.next;
        }

        if (prev == null) {
            if (slow.next == null) {
                return null;
            } else {
                return slow.next;
            }
        }
        prev.next = slow.next;
        return head;
    }
}
