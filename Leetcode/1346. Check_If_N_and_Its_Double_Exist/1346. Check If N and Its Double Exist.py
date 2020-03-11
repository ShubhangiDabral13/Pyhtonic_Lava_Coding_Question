class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        if arr.count(0)>1:
            return True
        for i in arr:
            if i*2 in arr and i != 0:
                return True
        else:
            return False
