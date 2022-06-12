class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ret = [0]*N
        l, r = 0, N-1
        for i in range(1, N+1):
            nL, nR = abs(nums[l]), abs(nums[r])
            if nL > nR:
                ret[-i] = nL*nL
                l+=1
            else:
                ret[-i] = nR*nR
                r-=1
        return ret