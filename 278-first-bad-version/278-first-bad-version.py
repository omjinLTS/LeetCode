# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import bisect
class Solution:
    def __getitem__(self, n: int):
        return isBadVersion(n)
    
    def firstBadVersion(self, n: int) -> int:
        return bisect.bisect_left(self, True, 1, n)