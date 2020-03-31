class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target == 0 and numbers is None:
            return
        d = dict()
        for index,i in enumerate(numbers):
            if target - i in d:
                return(d[target - i]+1,index+1)
            else:
                d[i] = index
