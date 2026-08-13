# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = True

        def dfs(r1, r2) :
            nonlocal isSame

            if r1 == None and r2 == None :
                return
            if r1 == None or r2 == None :
                isSame = False
                return
            
            if r1.val != r2.val :
                isSame = False
            
            # goleft
            dfs(r1.left, r2.left)

            # goright
            dfs(r1.right, r2.right)

            return
        
        dfs(p, q)

        return isSame