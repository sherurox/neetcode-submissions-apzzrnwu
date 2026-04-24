class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0  # this will store the best (max) diameter found so far

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0  # height of empty tree

            left = dfs(node.left)     # height of left subtree
            right = dfs(node.right)   # height of right subtree

            # diameter passing THROUGH this node = left height + right height
            diameter = max(diameter, left + right)

            # return height of this subtree
            return 1 + max(left, right)

        dfs(root)          # fills 'diameter' while computing heights
        return diameter    # final answer