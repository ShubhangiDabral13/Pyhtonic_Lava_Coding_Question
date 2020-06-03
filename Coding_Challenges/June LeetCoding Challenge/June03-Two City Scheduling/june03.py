class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        res = 0

        costs = sorted(costs , key = lambda x : x[0] - x[1])

        for i in range(len(costs)):
            if i < len(costs)//2:
                res += costs[i][0]
            else:
                res += costs[i][1]

        return res
