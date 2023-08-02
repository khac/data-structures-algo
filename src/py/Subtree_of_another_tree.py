# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def checkMatch(root, subRoot):
            if (not root) ^ (not subRoot):
                return False
            if not root and not subRoot:
                return True
            if root.val != subRoot.val:
                return False
            return checkMatch(root.left, subRoot.left) and checkMatch(root.right, subRoot.right)
        
        if root.val == subRoot.val and checkMatch(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)
