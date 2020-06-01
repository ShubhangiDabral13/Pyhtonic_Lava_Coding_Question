# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def mirror(node):
            if (node == None):
                return
            else:
                temp = node
            mirror(node.left)
            mirror(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

        mirror(root)

        return root
        
