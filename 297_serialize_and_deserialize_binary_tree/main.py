# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # DFS traversal.
        def helper(node):
            if node is None:
                return "#"
            
            return str(node.val) + " " + helper(node.left) + " " + helper(node.right)

        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        tokens = data.split()
        ptr = 0

        def helper():
            nonlocal ptr
            if tokens[ptr] == "#":
                ptr += 1
                return None
            val = tokens[ptr]
            ptr += 1
            left = helper()
            right = helper()
            return TreeNode(int(val), left, right)
        
        return helper()



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
