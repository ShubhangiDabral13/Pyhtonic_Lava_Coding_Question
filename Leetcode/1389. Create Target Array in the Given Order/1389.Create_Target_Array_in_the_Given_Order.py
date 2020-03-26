class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if len(nums) != len(index):
            return
        else:
            target = []
            for i in range(len(index)):
                target.insert(index[i],nums[i])
            return target

        
