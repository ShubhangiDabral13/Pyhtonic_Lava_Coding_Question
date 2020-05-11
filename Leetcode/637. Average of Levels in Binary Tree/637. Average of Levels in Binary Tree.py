# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        while root == None:
            return []

        ques = [root]
        ans  = []
        while len(ques) > 0:
            values = []
            ques1 = []
            for i in ques:

                if i.val != None:
                    values.append(i.val)

                if i.left:
                    ques1.append(i.left)

                if i.right:
                    ques1.append(i.right)

            if len(values) > 0:
                ans.append(sum(values)*1.0/len(values))
            ques = ques1

        return ans 
