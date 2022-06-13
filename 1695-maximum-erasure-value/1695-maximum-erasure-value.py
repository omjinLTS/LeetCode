class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        p, n = [0]+nums[:], len(nums)
        for i in range(n):
            p[i+1] = p[i] + nums[i]
        m = [-1]*10001
        s = 0
        ret = 0
        for i in range(n):
            s = max(s, m[nums[i]]+1)
            ret = max(ret, p[i+1] - p[s])
            m[nums[i]] = i
        return ret