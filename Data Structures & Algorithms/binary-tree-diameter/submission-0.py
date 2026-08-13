# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findHeight(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        if not root.right and not root.left :
            return 1
        if not root.left :
            return 1 + self.findHeight(root.right)
        if not root.right :
            return 1 + self.findHeight(root.left)
        return max(1 + self.findHeight(root.left), 1 + self.findHeight(root.right))
            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0

        # dfs
        stack = []
        stack.append(root)

        visited = set()

        while stack :
            n = stack.pop()
            visited.add(n)

            leftHeight = self.findHeight(n.left)
            rightHeight = self.findHeight(n.right)

            d = leftHeight + rightHeight

            if d > maxHeight :
                maxHeight = d

            if n.left and n.left not in visited :
                stack.append(n.left)
            if n.right and n.right not in visited :
                stack.append(n.right)

        return maxHeight

        
