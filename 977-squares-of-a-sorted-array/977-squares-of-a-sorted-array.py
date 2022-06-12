class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = [n*n for n in nums]
        ret.sort()
        return ret