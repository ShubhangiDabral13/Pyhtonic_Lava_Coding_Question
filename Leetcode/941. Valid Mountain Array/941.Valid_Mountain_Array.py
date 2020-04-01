class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if A== []:
            return False
        a = max(A)
        p = A.index(a)
        if len(A) < 3:
            return False
        if not(0 < p < len(A) -1):
            return False

        for i in range(1,p+1):
            if A[i] <= A[i-1]:
                return False

        for i in range(p,len(A)-1):
            if  A[i] <= A[i+1]:
                return False

        return True
