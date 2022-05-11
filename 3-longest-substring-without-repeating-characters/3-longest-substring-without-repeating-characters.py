class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        st = [0] * 128
        l = r = 0

        res = 0
        while r < len(s):
            rc = s[r]
            st[ord(rc)] += 1
            while st[ord(rc)] > 1:
                lc = s[l]
                st[ord(lc)] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return res