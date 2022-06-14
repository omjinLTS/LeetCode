class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        d = [[0]*(len(s2)+1) for n in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j],d[i][j-1])
        return len(s1)+len(s2)-2*d[-1][-1]