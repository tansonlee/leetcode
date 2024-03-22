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
    public boolean isPalindrome(ListNode head) {
        int length = 0;
        ListNode p = head;
        while (p != null) {
            p = p.next;
            length++;
        }

        // Reverse the second half of the LL
        int half = (length + 1) / 2;
        ListNode prev = null;
        ListNode curr = head;
        for (int i = 0; i < half; ++i) {
            prev = curr;
            curr = curr.next;
        }

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        while (head != prev) {
            if (head.val != prev.val) {
                return false;
            }
            if (head.next == prev) {
                break; // even length
            }
            head = head.next;
            prev = prev.next;
        }

        return true;
    }
}
