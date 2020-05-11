# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findpath(self,root :TreeNode):

        if root:

            leftpath = self.findpath(root.left)
            rightpath = self.findpath(root.right)
            path = leftpath + rightpath

            if path > self.diameter:
                self.diameter = path

            return max(leftpath,rightpath) + 1

        return 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.diameter = 0
        self.findpath(root)

        return self.diameter
        
