class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:] = [n for n in nums if n] + [0]*nums.count(0)
        