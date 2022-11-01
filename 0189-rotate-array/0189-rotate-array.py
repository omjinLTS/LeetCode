class Solution(object):
    def rotate(self, nums, k):
        tmp = nums+nums
        N = len(nums)
        k%=N
        nums[:] = tmp[N-k:2*N-k]
        