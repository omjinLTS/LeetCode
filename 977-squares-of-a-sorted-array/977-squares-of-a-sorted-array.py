from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q = deque()
        l, r = 0, len(nums)-1
        for _ in nums:
            nL, nR = nums[l]**2, nums[r]**2
            if nL > nR:
                q.appendleft(nL)
                l+=1
            else:
                q.appendleft(nR)
                r-=1
        return q