# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSubtree = False
        isSameTree = True

        if not subRoot :
            return True
        if not root : # (and subroot exists)
            return False

        def sameTree(r1, r2) :
            nonlocal isSameTree
            nonlocal isSubtree

            if not r1 and not r2 :
                print("a")
                print(isSameTree)
                return
            if not r1 or not r2 :
                print("b")
                isSameTree = False
                print(isSameTree)
                return
            
            if r1.val != r2.val :
                print("c")
                isSameTree = False
                print(isSameTree)
                return 
            print("d")
            sameTree(r1.left, r2.left)
            sameTree(r1.right, r2.right)
            
            print(isSameTree)
            return

        def dfs(r) :
            nonlocal isSubtree
            nonlocal isSameTree

            if not r :
                return

            print("r: " + str(r.val))

            # for each node, check if identical to subtree
            sameTree(r, subRoot)
            print(isSameTree)
            if isSameTree :
                isSubtree = True
                print("hallo!")
                return
            isSameTree = True # reset
            
            dfs(r.left)
            dfs(r.right)

            return 

        dfs(root)
        '''
        sameTree(root, subRoot)
        print(isSubtree)
        print(isSameTree)
        '''
        return isSubtree