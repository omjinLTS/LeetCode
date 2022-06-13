class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1): return nums[0]
        dp1 = nums[:-1]+[0]*2
        dp2 = nums[1:]+[0]*2
        for i in range(2, len(nums) + 1):
            dp1[i] += max(dp1[i-2], dp1[i-3])
            dp2[i] += max(dp2[i-2], dp2[i-3])
        return max(dp1[-1], dp2[-1])