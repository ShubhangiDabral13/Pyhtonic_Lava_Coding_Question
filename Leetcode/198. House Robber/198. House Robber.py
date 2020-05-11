class Solution:
    def rob(self, nums: List[int]) -> int:
    
    	a, b, L = 0, 0, len(nums)
    	for i in range(L):
            b, a = max(a + nums[i], b), b

    	return 0 if L == 0 else max(nums) if L <= 2 else b
