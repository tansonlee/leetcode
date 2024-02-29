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
import java.util.function.BiFunction;

class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int depth = 0;

        while (queue.size() > 0) {
            int level_size = queue.size();
            if (!check_level(queue.toArray(new TreeNode[0]), depth)) {
                return false;
            }
            for (int i = 0; i < level_size; ++i) {
                TreeNode n = queue.poll();
                if (n.left != null) {
                    queue.add(n.left);
                }
                if (n.right != null) {
                    queue.add(n.right);
                }
            }
            ++depth;
        }

        return true;
    }

    private boolean check_level(TreeNode[] level, int depth) {
        BiFunction<Integer, Integer, Boolean> cmp = (a, b) -> (depth % 2 == 0 ? a < b : b < a);

        for (TreeNode n : level) {
            if (n.val % 2 == depth % 2) {
                return false;
            }
        }

        for (int i = 0; i < level.length - 1; ++i) {
            if (!cmp.apply(level[i].val, level[i + 1].val)) {
                return false;
            }
        }

        return true;
    }
}
