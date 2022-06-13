class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums + [0]*2
        for i in range(2, len(nums) + 2):
            dp[i] += max(dp[i-2], dp[i-3])
        return dp[-1]