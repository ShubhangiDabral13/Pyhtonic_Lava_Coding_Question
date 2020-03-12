class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1
        while n >= 1:
            prev,cur = cur,(prev+cur)
            n = n-1
        return prev
        
