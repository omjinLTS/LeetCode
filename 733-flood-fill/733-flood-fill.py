class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dx = 0, 1, 0, -1
        dy = 1, 0, -1, 0
        m, n = len(image), len(image[0]) # m rows, n columns
        sourceColor = image[sr][sc]
        if newColor == sourceColor:
            return image
        q = deque()
        q.append((sr, sc))
        image[sr][sc] = newColor
        while q:
            curR, curC = q.popleft()
            for i in range(4):
                nR, nC = curR + dx[i], curC + dy[i]
                if nR < 0 or nC < 0 or nR >= m or nC >= n:
                    continue
                if image[nR][nC] == sourceColor:
                    image[nR][nC] = newColor
                    q.append((nR, nC))
        return image
                