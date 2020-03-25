class Solution:
    def countPrimes(self, n: int) -> int:
        p = [True for i in range(n)]
        m = 2
        while(m*m <= n):
            if p[m] == True:
                for i in range(m*2,n,m):
                    p[i] = False
            m += 1
        result = p[2:n].count(True)
        return result
                
