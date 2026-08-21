# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            # all trees have the empty tree as a subtree
            return True
        if not root:
            # empty tree can only have empty tree as a subtree (handled above)
            return False

        if self.sameTree(root, subRoot):
            # we do this intead of just returning the result of sameTree
            # so that a negative result doesnt make the whole problem false
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        elif root1 and root2 and root1.val == root2.val:
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

        return False
        