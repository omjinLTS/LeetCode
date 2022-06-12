class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ret = [0]*N
        l, r = 0, N-1
        for i in range(1, N+1):
            nL, nR = nums[l]*nums[l], nums[r]*nums[r]
            if nL > nR:
                ret[-i] = nL
                l+=1
            else:
                ret[-i] = nR
                r-=1
        return ret