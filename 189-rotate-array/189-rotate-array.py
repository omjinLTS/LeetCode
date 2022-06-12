class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums+nums
        N = len(nums)
        k=k%N
        nums[:] = tmp[N-k:2*N-k]