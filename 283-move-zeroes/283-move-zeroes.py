class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ret = []
        zeros = 0
        for n in nums:
            if n:
                ret.append(n)
            else: 
                zeros += 1
        nums[:] = ret + [0]*zeros
        