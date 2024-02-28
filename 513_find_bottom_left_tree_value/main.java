/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int findBottomLeftValue(TreeNode root) {
        int result = root.val;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (queue.size() > 0) {
            int current_size = queue.size();
            for (int i = 0; i < current_size; ++i) {
                TreeNode n = queue.poll();
                if (n.left != null) {
                    queue.add(n.left);
                }
                if (n.right != null) {
                    queue.add(n.right);
                }
            }
            if (queue.size() > 0) {
                result = queue.peek().val;
            }
        }

        return result;
    }
}
